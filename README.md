# Datadog APM Demo - Python Version

This is a **Python/FastAPI** conversion of the original Next.js Datadog APM demonstration application. It provides the same functionality for testing application performance monitoring and distributed tracing.

## 🎯 Features

- **Slow API Endpoint**: Simulates slow responses with 1-second delay
- **Chained API Calls**: Demonstrates distributed tracing across service calls
- **Error Generation**: Intentional error endpoint for APM testing
- **Datadog Integration**: Optional automatic trace and span injection into logs
- **Modern UI**: Clean, responsive interface with dark mode support
- **Python Compatibility**: Works with Python 3.8+ including Python 3.13

## 🚀 Quick Start

### 1. Install Dependencies

```bash
pip install -r requirements.txt
```

### 2. Run the Application

**Option A: Using the run script (recommended)**

```bash
python run.py
```

**Option B: Using uvicorn directly**

```bash
uvicorn main:app --host 0.0.0.0 --port 8000 --reload
```

### 3. Access the Application

Open your browser to: **http://localhost:8000**

## 🔧 Configuration

### Datadog Environment Variables (Optional)

```bash
export DD_SERVICE="apm-demo-python"
export DD_ENV="development"
export DD_VERSION="1.0.0"
export DD_TRACE_AGENT_URL="http://localhost:8126"
```

**Note**: The application uses the standard Datadog agent port **8126**. If your agent uses a different port, you can either:

- Update the `DD_TRACE_AGENT_URL` in `run.py`, or
- Set it as an environment variable: `export DD_TRACE_AGENT_URL="http://localhost:YOUR_PORT"`

### Without Datadog Agent

The application works perfectly fine without Datadog installed. It will:

- Show warnings about missing ddtrace
- Log without trace IDs
- Function normally for all API endpoints

## 📡 API Endpoints

| Endpoint     | Method | Description                       |
| ------------ | ------ | --------------------------------- |
| `/`          | GET    | Main application page             |
| `/api/slow`  | GET    | Slow response endpoint (1s delay) |
| `/api/chain` | GET    | Chained API call to slow endpoint |
| `/api/error` | GET    | Intentional error (HTTP 500)      |

## 🧪 Testing the Endpoints

1. **Trigger Slow API**: Tests performance monitoring of slow responses
2. **Trigger Chained API**: Tests distributed tracing across multiple services
3. **Trigger Error API**: Tests error tracking and exception handling

## 📊 Logging

All requests are logged to:

- **Console**: Real-time logging output
- **File**: `app.log` with timestamp and optional Datadog trace IDs

### Log Format

```
[2024-01-15 10:30:45,123] [INFO] [dd.trace_id=12345 dd.span_id=67890] Your log message
```

## 🏗️ Architecture

### Technology Stack

- **Backend**: FastAPI (Python async web framework)
- **Frontend**: HTML5 + Vanilla JavaScript
- **Styling**: Modern CSS with dark mode support
- **HTTP Client**: httpx for async requests
- **Logging**: Python logging with optional Datadog integration
- **Server**: Uvicorn ASGI server

### Key Differences from Node.js Version

| Component         | Node.js/Next.js    | Python/FastAPI    |
| ----------------- | ------------------ | ----------------- |
| **Web Framework** | Next.js API routes | FastAPI           |
| **Frontend**      | React components   | HTML + JavaScript |
| **Styling**       | TailwindCSS        | Custom CSS        |
| **Logging**       | Winston            | Python logging    |
| **HTTP Requests** | fetch API          | httpx             |
| **Templating**    | JSX                | Jinja2            |
| **Server**        | Node.js            | Uvicorn (ASGI)    |

## 🐳 Docker Support

You can containerize this application using the existing `dockerfile` pattern. Example:

```dockerfile
FROM python:3.11-slim

WORKDIR /app
COPY requirements.txt .
RUN pip install -r requirements.txt

COPY . .
EXPOSE 8000

CMD ["python", "run.py"]
```

## 🔄 Development

The application runs with **auto-reload** enabled by default. Any changes to Python files will automatically restart the server.

### Development Tips

- Use `python run.py` for development (includes auto-reload)
- Check `app.log` file for detailed logging
- Access FastAPI docs at `http://localhost:8000/docs`
- API schema available at `http://localhost:8000/redoc`

## 🐛 Troubleshooting

### Common Issues

**1. ddtrace Installation Errors**

```bash
# If ddtrace fails to install, you can run without it
pip install fastapi uvicorn jinja2 httpx python-multipart
```

**2. Port Already in Use**

```bash
# Change port in run.py or use:
uvicorn main:app --port 8001
```

**3. Template/Static Files Not Found**

- Ensure `templates/` and `static/` directories exist
- Check file permissions

## 📈 Performance Monitoring

When connected to Datadog:

- View traces in APM dashboard
- Monitor slow endpoint performance
- Track error rates and exceptions
- Analyze service dependencies via chain endpoint

## 🤝 Contributing

This is a demonstration application. Feel free to:

- Add new endpoints for testing
- Enhance error handling
- Improve UI/UX
- Add more comprehensive logging

---

**Original Node.js version** → **Python FastAPI version** ✅
