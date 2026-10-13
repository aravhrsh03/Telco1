import time

def execution_timer(func):
    def wrapper(*args, **kwargs):
        start = time.time()
        func(*args, **kwargs)
        end = time.time()
        print()
        print(f"=== Execution Time : {end - start} ===")
    return wrapper

@execution_timer
def fun():
    for i in range(100000):
        continue

fun()