

def fibon_student(num):
    if num <= 0:
        return 1
    fb1, fb2 = 1, 1
    for _ in range(1, num):
        print(fb1, fb2)
        fb1, fb2 = fb2, (fb1+fb2) % 10
    return fb2


if __name__ == '__main__':
    num = int(input())
    print(fibon_student(num))
