import turtle


def ice(n, size):
    if n == 0:
        turtle.forward(size)
    else:
        ice(n - 1, size / 2)
        turtle.left(90)
        ice(n - 1, size / 3)
        turtle.right(180)
        ice(n - 1, size / 3)
        turtle.left(90)
        ice(n - 1, size / 2)


def main():
    print("Добро пожаловать, вы рисуете ледяной фрактал ! Введите следующие параметры:")
    n = int(input("Глубина рекурсии: "))
    size = int(input("Длину ледяного фрактала: "))
    turtle.up()
    turtle.goto(-100, 0)
    turtle.down()
    ice(n, size)


if __name__ == '__main__':
    main()
