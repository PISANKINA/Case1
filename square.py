import turtle, random


def chooseRandomColor():
    red = random.random()
    green = random.random()
    blue = random.random()
    return red, green, blue


def squere(n, a):
    if n == 0:
        return n
    turtle.pendown()
    for i in range(4):
        turtle.forward(a)
        turtle.right(90)
    turtle.penup()
    turtle.right(10)
    turtle.forward(0.1 * a)
    squere(n - 1, 0.9 * a)


def main():
    print("Добро пожаловать, вы рисуете квадрат! Введите следующие параметры:")
    n = int(input("Глубина рекурсии: "))
    a = int(input("Длину стороны квадрата: "))
    turtle.color(chooseRandomColor())
    squere(n, a)


if __name__ == '__main__':
    main()
