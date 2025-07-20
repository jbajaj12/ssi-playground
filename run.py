#!/usr/bin/env python3
"""
Datadog APM Demo - Python/FastAPI version
Run script with optional Datadog tracing integration
"""

import uvicorn
import os

def main():
    # Try to initialize Datadog tracing if available
    try:
        from ddtrace import patch_all
        patch_all()
        print("✅ Datadog automatic instrumentation enabled")
    except ImportError:
        print("⚠️  ddtrace not installed - running without Datadog tracing")
        print("   To enable Datadog tracing: pip install ddtrace")
    except Exception as e:
        print(f"⚠️  Warning: Could not initialize ddtrace: {e}")

    # Set environment variables for Datadog (optional)
    os.environ.setdefault("DD_SERVICE", "apm-demo-python")
    os.environ.setdefault("DD_ENV", "development")
    os.environ.setdefault("DD_VERSION", "1.0.0")
    os.environ.setdefault("DD_TRACE_AGENT_URL", "http://localhost:8126")

    print("\n🚀 Starting Datadog APM Demo (Python version)")
    print("📍 Application will be available at: http://localhost:8000")
    print(f"🏷️  Datadog agent URL: {os.environ.get('DD_TRACE_AGENT_URL', 'default')}")
    print("📊 API endpoints:")
    print("   - GET /api/slow   (simulates slow response)")
    print("   - GET /api/chain  (chained API call)")
    print("   - GET /api/error  (intentional error)")
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