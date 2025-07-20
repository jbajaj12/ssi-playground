from fastapi import FastAPI, HTTPException, Request
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse, JSONResponse
import asyncio
import httpx
from logger import log_message

# Try to import ddtrace tracer - make it optional
try:
    from ddtrace import tracer
    TRACING_AVAILABLE = True
except ImportError:
    TRACING_AVAILABLE = False
    # Create a dummy tracer for compatibility
    class DummyTracer:
        def trace(self, operation_name):
            class DummyContext:
                def __enter__(self):
                    return self
                def __exit__(self, *args):
                    pass
            return DummyContext()
    tracer = DummyTracer()

app = FastAPI(title="Datadog APM Demo", version="1.0.0")

# Create directories if they don't exist
import os
os.makedirs("static", exist_ok=True)
os.makedirs("templates", exist_ok=True)

# Mount static files
app.mount("/static", StaticFiles(directory="static"), name="static")

# Templates
templates = Jinja2Templates(directory="templates")

@app.get("/", response_class=HTMLResponse)
async def home(request: Request):
    """Serve the main page."""
    return templates.TemplateResponse("index.html", {"request": request})

@app.get("/api/slow")
async def slow_api():
    """Simulate a slow API response."""
    with tracer.trace("slow_api"):
        log_message('This request will take some time as you hit the /api/slow endpoint')
        await asyncio.sleep(1)  # Simulate delay
        log_message('Congrats!! You just sent a request to /api/slow')
        return JSONResponse({"message": "Slow response completed"})

@app.get("/api/chain")
async def chain_api():
    """Make a chained API call to the slow endpoint."""
    with tracer.trace("chain_api"):
        log_message('Received request: /api/chain')
        
        try:
            async with httpx.AsyncClient() as client:
                response = await client.get("http://localhost:8000/api/slow")
                data = response.json()
                
            log_message('Chained call completed: /api/chain -> /api/slow')
            return JSONResponse({"message": "Chain complete", "data": data})
        except Exception as e:
            log_message(f'Error in chained call: {str(e)}')
            raise HTTPException(status_code=500, detail="Chained call failed")

@app.get("/api/error")
async def error_api():
    """Intentionally throw an error for APM testing."""
    with tracer.trace("error_api"):
        log_message('Ohh!! this request failed because you just hit the /api/error endpoint')
        log_message('About to throw intentional error')
        raise HTTPException(status_code=500, detail="Intentional error for APM trace")

if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True) 