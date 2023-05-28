def check_armstrong_number(num):
    s1 = num
    s = 0
    num_len = len(str(num))
    while num != 0:
        res = num % 10
        s = s + res ** num_len
        # print(s)
        num = num // 10
    if s == s1:
        print(f"{s1} is an armstrong number")
    else:
        print(f"{s1} is not an armstrong number")


"""Here we are converting the number into string and traverse through each element and doing power"""


def check_armstrong_number2(num):
    s = num
    s1 = 0
    b = len(str(num))
    for i in str(s):
        s1 = s1 + int(i) ** b
    if s1 == s:
        print(f"{s} is an armstrong number")
    else:
        print(f"{s} is not an armstrong number")


check_armstrong_number(153)
check_armstrong_number(3456)

check_armstrong_number2(153)
check_armstrong_number2(3456)
