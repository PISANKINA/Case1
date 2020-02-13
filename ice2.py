import turtle


def ice2(n, size):
    if n == 0:
        turtle.forward(size)
    else:
        ice2(n - 1, size / 2)
        turtle.left(115)
        ice2(n - 1, size / 4)
        turtle.right(180)
        ice2(n - 1, size / 4)
        turtle.left(130)
        ice2(n - 1, size / 4)
        turtle.right(180)
        ice2(n - 1, size / 4)
        turtle.left(115)
        ice2(n - 1, size / 2)


def main():
    print("Добро пожаловать, вы рисуете ледяной фрактал! Введите следующие параметры:")
    n = int(input("Глубина рекурсии: "))
    size = int(input("Длину ледяного фрактала: "))
    turtle.up()
    turtle.goto(-100, 0)
    turtle.down()
    ice2(n, size)


if __name__ == '__main__':
    main()
