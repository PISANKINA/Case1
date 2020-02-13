import turtle


def minkovskiy(n, size):
    if n == 0:
        turtle.forward(size)
        return n
    else:
        minkovskiy(n - 1, size)
        turtle.left(90)
        minkovskiy(n - 1, size)
        turtle.right(90)
        minkovskiy(n - 1, size)
        turtle.right(90)
        minkovskiy(n - 1, size)
        minkovskiy(n - 1, size)
        turtle.left(90)
        minkovskiy(n - 1, size)
        turtle.left(90)
        minkovskiy(n - 1, size)
        turtle.right(90)
        minkovskiy(n - 1, size)


def main():
    print("Добро пожаловать, вы рисуете кривую Минковского! Введите следующие параметры:")
    n = int(input("Глубина рекурсии: "))
    size = int(input("Длину кривой Минковского : "))
    return minkovskiy(n, size)


if __name__ == '__main__':
    main()
