import time

def function_logger(func):
    def wrapper(*args, **kwargs):
        start = time.perf_counter()

        result = None
        error = None

        try:
            result = func(*args, **kwargs)
            return result

        except Exception as e:
            error = type(e).__name__

        finally:
            end = time.perf_counter()

            print(
                f"LOG: Function={func.__name__} | "
                f"Args={args} | "
                f"Kwargs={kwargs} | "
                f"Time={round(end - start, 4)}s | "
                f"Return={result} | "
                f"Error={error}"
            )

    return wrapper

# Test 1: Addition
@function_logger
def add(a, b):
    return a + b

add(100, 200)


# Test 2: String concatenation
@function_logger
def join_words(a, b):
    return a + " " + b

join_words("Hello", "World")


# Test 3: Empty list
@function_logger
def list_length(data):
    return len(data)

list_length([])


# Test 4: List processing
@function_logger
def get_sum(numbers):
    return sum(numbers)

get_sum([10, 20, 30, 40])


# Test 5: ZeroDivisionError
@function_logger
def calculate_percentage(value, total):
    return (value / total) * 100

calculate_percentage(50, 0)


# Test 6: TypeError
@function_logger
def add_numbers(a, b):
    return a + b

add_numbers(10, "20")


# Test 7: Sleep and execution time
@function_logger
def wait_function():
    time.sleep(1)
    return "completed"

wait_function()


# Test 8: Dictionary access success
@function_logger
def get_name(user):
    return user["name"]

get_name({"name": "Alex", "age": 25})


# Test 9: KeyError
@function_logger
def get_missing_key(user):
    return user["email"]

get_missing_key({"name": "Alex"})


# Test 10: Custom exception
@function_logger
def check_age(age):
    if age < 18:
        raise Exception("Age not allowed")
    return "Allowed"

check_age(15)