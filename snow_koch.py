import turtle


def snow_koch(n, size):
    if n == 0:
        turtle.forward(size)
    else:
        snow_koch(n - 1, size / 3)
        turtle.left(60)
        snow_koch(n - 1, size / 3)
        turtle.right(120)
        snow_koch(n - 1, size / 3)
        turtle.left(60)
        snow_koch(n - 1, size / 3)


def main():
    print("Добро пожаловать, вы рисуете cнежинку Коха! Введите следующие параметры:")
    n = int(input("Глубина рекурсии: "))
    size = int(input("Длину стороны cнежинки Кохи: "))
    for i in range(3):
        snow_koch(n, size)
        turtle.right(120)
    snow_koch(n, size)


if __name__ == '__main__':
    main()
