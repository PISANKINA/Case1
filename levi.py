import turtle


def levi(n, size):
    if n == 0:
        turtle.forward(size)
        return
    else:
        turtle.left(45)
        levi(n - 1, size)
        turtle.right(90 - 45 * (n - 1))
        levi(n - 1, size)


def main():
    print("Добро пожаловать, вы рисуете кривую Леви ! Введите следующие параметры:")
    n = int(input("Глубина рекурсии: "))
    size = int(input("Длину ледяного фрактала: "))
    return levi(n, size)


if __name__ == '__main__':
    main()
