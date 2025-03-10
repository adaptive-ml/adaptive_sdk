import functools
import logging

# Configure logging
logging.basicConfig(level=logging.INFO)


def log_function_name(func):
    """Decorator to log the function name when called."""

    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        logging.warning(f"Calling function: {func.__name__}")
        return func(*args, **kwargs)

    return wrapper
