def find_miss(lis):
    cummulative_sum = 0
    n = 0
    for i in lis:
        n = (i * (i + 1))//2
        cummulative_sum += i

        if n != cummulative_sum:
            return n - cummulative_sum

print(find_miss([1,2,3,4,6]))