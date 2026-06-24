from functools import wraps
import time

def trace(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        print(f"[TRACE] Entering {func.__name__}")
        start = time.perf_counter()

        try:
            result = func(*args, **kwargs)
            duration = time.perf_counter() - start
            print(f"[TRACE] {func.__name__} succeeded in {duration:.4f} seconds.")
            return result
        except Exception:
            duration = time.perf_counter() - start
            print(f"[TRACE] {func.__name__} failed after {duration:.4f} seconds.")
            raise
    return wrapper

@trace
def example_function(x, y):
    time.sleep(1)  # Simulate a delay
    return x + y

if __name__ == "__main__":
    try:
        result = example_function(5, 10)
        print(f"Result: {result}")
    except Exception as e:
        print(f"Error: {e}")