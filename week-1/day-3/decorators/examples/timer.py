import time
from functools import wraps

def timer(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        start = time.perf_counter()
        result = func(*args, **kwargs)
        print(f"Function {func.__name__} took {time.perf_counter() - start:.4f} seconds to complete.")
        return result
    return wrapper

@timer
def add(x, y):
    time.sleep(1)  # Simulate a delay
    return x + y

if __name__ == "__main__":
    add(5, 10)