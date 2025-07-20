import logging
import sys
from datetime import datetime

# Try to import ddtrace - make it optional
try:
    from ddtrace import tracer
    DDTRACE_AVAILABLE = True
    print("✅ Datadog tracing libraries loaded")
except ImportError:
    DDTRACE_AVAILABLE = False
    print("⚠️  ddtrace not available - running without Datadog tracing")
    # Create a dummy tracer for compatibility
    class DummyTracer:
        def current_span(self):
            return None
    tracer = DummyTracer()

# Create a custom formatter that includes trace and span IDs
class DatadogFormatter(logging.Formatter):
    def format(self, record):
        if DDTRACE_AVAILABLE:
            try:
                span = tracer.current_span()
                if span:
                    trace_id = getattr(span, 'trace_id', 'N/A')
                    span_id = getattr(span, 'span_id', 'N/A')
                else:
                    trace_id = 'N/A'
                    span_id = 'N/A'
            except Exception:
                trace_id = 'N/A'
                span_id = 'N/A'
        else:
            trace_id = 'N/A'
            span_id = 'N/A'
        
        # Add trace info to the record
        record.dd_trace_id = trace_id
        record.dd_span_id = span_id
        
        return super().format(record)

# Configure logger
logger = logging.getLogger('apm_demo')
logger.setLevel(logging.INFO)

# File handler for app.log
file_handler = logging.FileHandler('app.log')
file_handler.setLevel(logging.INFO)

# Console handler
console_handler = logging.StreamHandler(sys.stdout)
console_handler.setLevel(logging.INFO)

# Formatter with trace information
formatter = DatadogFormatter(
    '[%(asctime)s] [%(levelname)s] [dd.trace_id=%(dd_trace_id)s dd.span_id=%(dd_span_id)s] %(message)s'
)

file_handler.setFormatter(formatter)
console_handler.setFormatter(formatter)

logger.addHandler(file_handler)
logger.addHandler(console_handler)

def log_message(message: str):
    """Log a message with optional trace context."""
    logger.info(message) 