import turtle


def dragon(c, height, n):
    if n == 0:
        return turtle.forward(height)
    turtle.left(45 * c)
    dragon(1, height, n - 1)
    turtle.right(90 * c)
    dragon(- 1, height, n - 1)
    turtle.left(45 * c)


def main():
    print("Добро пожаловать, вы рисуете Дракона! Введите следующие параметры:")
    height = int(input("Длину стороны ветки: "))
    n = int(input("Глубина рекурсии: "))
    turtle.color('pink')
    c = 1
    dragon(c, height, n)
    turtle.mainloop()


if __name__ == '__main__':
    main()
