import turtle


def vetka(n, size):
    if n == 0:
        turtle.left(180)
        return n
    x = size / (n + 1)
    for i in range(n):
        turtle.forward(x)
        turtle.left(45)
        vetka(n - i - 1, 0.5 * x * (n - i - 1))
        turtle.left(90)
        vetka(n - i - 1, 0.5 * x * (n - i - 1))
        turtle.right(135)
    turtle.forward(x)
    turtle.left(180)
    turtle.forward(size)


def main():
    print("Добро пожаловать, вы рисуете фрактал Ветка! Введите следующие параметры:")
    n = int(input("Глубина рекурсии: "))
    size = int(input("Длину стороны ветки: "))
    turtle.left(90)
    vetka(n, size)


if __name__ == '__main__':
    main()
