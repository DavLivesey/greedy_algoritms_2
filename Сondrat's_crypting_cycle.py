

def factorial(num):
    if num == 0 or num == 1:
        return 1
    factorial_num = 1
    for numeral in range(1, num + 1):
        factorial_num *= numeral
    return factorial_num


if __name__ == '__main__':
    n = int(input())
    print(factorial(n))