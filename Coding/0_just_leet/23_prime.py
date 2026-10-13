def is_prime(num):
    for i in range(2, num):
        if num % i == 0:
            return False
    return True

def prime_generator():
    iterator = 2

    while True:
        if is_prime(iterator):
            yield iterator

        iterator += 1

prime = prime_generator()

for i in range(7):
    print(next(prime))
else:
    print("...")