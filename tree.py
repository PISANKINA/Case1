import turtle


def tree(hight, engle):
    if engle == 0:
        return engle
    turtle.forward(hight)
    turtle.right(30)
    tree(hight / 2, engle - 1)
    turtle.left(60)
    tree(hight / 2, engle - 1)
    turtle.right(30)
    turtle.backward(hight)


def main():
    print("Добро пожаловать, вы рисуете дерево! Введите следующие параметры:")
    hight = int(input('Пожалуйста, укажите высоту дерева: '))
    engle = int(input('Пожалуйста, укажите величину угла: '))
    turtle.left(90)
    turtle.color('green')
    tree(hight, engle)


if __name__ == '__main__':
    main()
