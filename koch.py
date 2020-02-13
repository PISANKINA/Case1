import turtle


def koch(n, size):
    if n == 0:
        turtle.forward(size)
    else:
        koch(n - 1, size / 3)
        turtle.left(60)
        koch(n - 1, size / 3)
        turtle.right(120)
        koch(n - 1, size / 3)
        turtle.left(60)
        koch(n - 1, size / 3)


def main():
    print("Добро пожаловать, вы рисуете кривую Коха! Введите следующие параметры:")
    n = int(input("Глубина рекурсии: "))
    size = int(input("Длину стороны кривой Кохи: "))
    return koch(n, size)


if __name__ == '__main__':
    main()
