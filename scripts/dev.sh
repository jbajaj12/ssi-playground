#!/bin/bash

# Datadog APM Configuration
export DD_SERVICE="apm-demo-python"
export DD_ENV="development"
export DD_VERSION="1.0.0"

# Debug flags (optional - uncomment for debugging)
#export DD_TRACE_DEBUG=true
#export DD_TRACE_STARTUP_LOGS=true

# Additional Datadog settings
export DD_TRACE_AGENT_URL="http://localhost:8126"
export DD_LOGS_INJECTION=true

echo "🚀 Starting Python app with Datadog auto-instrumentation..."
echo "📊 Service: $DD_SERVICE"
echo "🏷️  Environment: $DD_ENV"
echo "📍 Version: $DD_VERSION"
echo ""

# Run with ddtrace auto-instrumentation
ddtrace-run python3 run.py
