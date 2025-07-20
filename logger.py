import logging
import sys

# Configure logger
logger = logging.getLogger('apm_demo')
logger.setLevel(logging.INFO)

# File handler for app.log
file_handler = logging.FileHandler('app.log')
file_handler.setLevel(logging.INFO)

# Console handler
console_handler = logging.StreamHandler(sys.stdout)
console_handler.setLevel(logging.INFO)

# Simple formatter (trace IDs will be automatically injected with auto-instrumentation)
formatter = logging.Formatter(
    '[%(asctime)s] [%(levelname)s] %(message)s'
)

file_handler.setFormatter(formatter)
console_handler.setFormatter(formatter)

logger.addHandler(file_handler)
logger.addHandler(console_handler)

def log_message(message: str):
    """Log a message. Trace IDs will be automatically injected when using ddtrace auto-instrumentation."""
    logger.info(message)
