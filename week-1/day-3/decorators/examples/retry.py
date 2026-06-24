from functools import wraps
from random import random
import time

def retry(max_retries = 3, delay = 1, exceptions = (Exception,)):
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            for attempt in range(max_retries):
                try:
                    return func(*args, **kwargs)
                except exceptions as e:
                    print(f"Attempt {attempt + 1} failed with error: {e}. Retrying in {delay} seconds...")
                    time.sleep(delay)
            raise Exception(f"Function {func.__name__} failed after {max_retries} attempts.")
        return wrapper
    return decorator

@retry(max_retries = 2, delay = 1)
def unstable():
    if random.random() < 0.5:
        raise ValueError("Random failure!")
    return "Success!"

if __name__ == "__main__":
    try:
        result = unstable()
        print(result)
    except Exception as e:
        print(e)