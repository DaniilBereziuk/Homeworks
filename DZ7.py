import time

def timeit(func):
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        execution_time = end_time - start_time
        print(f"Function '{func.__name__}' executed in {execution_time:.8f} seconds")
        return result
    return wrapper
@timeit
def example_function(duration):
    time.sleep(duration)
    return "Function completed"
def test_example_function():
    assert example_function(1) == "Function completed"
    assert example_function(0.5) == "Function completed"
    assert example_function(0) == "Function completed"

if __name__ == "__main__":
    test_example_function()