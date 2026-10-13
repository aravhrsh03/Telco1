def recharge_decorator(func):
    def wrapper(n):
        print("Logging Started")
        func(n)
        print("Logging Finished")
    return wrapper


@recharge_decorator
def Recharge(n):
    print(f"Recharge Successful: {n}")


Recharge(399)