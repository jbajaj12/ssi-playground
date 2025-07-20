#!/usr/bin/env python3
"""
Datadog APM Demo - Python/FastAPI version
Clean version without manual tracing - ready for auto-instrumentation
"""

import uvicorn
import os

def main():
    print("🚀 Starting Datadog APM Demo (Python version)")
    print("📍 Application will be available at: http://localhost:8000")
    print("📊 API endpoints:")
    print("   - GET /api/slow   (simulates slow response)")
    print("   - GET /api/chain  (chained API call)")
    print("   - GET /api/error  (intentional error)")
    print()
    print("🔧 Tracing: Ready for auto-instrumentation")
    print("   To enable later: ddtrace-run python run.py")
    print("   Or set DD_TRACE_ENABLED=true environment variable")
    print("\n" + "="*50)

    uvicorn.run(
        "main:app",
        host="0.0.0.0",
        port=8000,
        reload=True,
        log_level="info"
    )

if __name__ == "__main__":
    main()
