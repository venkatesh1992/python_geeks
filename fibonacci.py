import math

"""if we want to check n is a fibonacci number or not, 
if it is a fibonacci number then 5n^2 + 4 or 5n^2 - 4should be a perfect square"""


def check_fibonacci(num):
    res1 = 5 * num ** 2 - 4
    result = math.sqrt(res1)

    if result * result == res1:
        print(f"{num} is a fibonacci number")
    else:
        print(f"{num} is not a fibonacci number")


check_fibonacci(8)
check_fibonacci(34)


def print_nth_fibonacci(num):
    if num == 0:
        print("passed wrong number")
    elif num == 1:
        return 0
    elif num == 2:
        return 1
    else:
        return print_nth_fibonacci(num - 1) + print_nth_fibonacci(num - 2)


print(print_nth_fibonacci(10))


def print_all_fibonacci(num):
    res = [0, 1]
    if num > 2:
        for i in range(2, num):
            nextElement = res[i - 1] + res[i - 2]
            res.append(nextElement)
    print(res)


print_all_fibonacci(10)


def print_all_fibonacci2(num):
    res = []
    if num == 0:
        print("passed wrong number")
    elif num == 1:
        res = [0]
    elif num == 2:
        res = [1]
    else:
        res = [0, 1]
        for i in range(2, num):
            res.append(res[i - 1] + res[i - 2])
    print(res)


print_all_fibonacci2(10)
