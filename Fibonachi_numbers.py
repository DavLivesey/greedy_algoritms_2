cache = {}


def fibon_student(num):
    if num not in cache:
        cache[num] = 1 if num <= 1 else fibon_student(num - 1) + fibon_student(num - 2)
    return cache[num]


if __name__ == '__main__':
    num = int(input())
    print(fibon_student(num))
