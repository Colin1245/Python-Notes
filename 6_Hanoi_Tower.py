"""Python的数据结构实现汉诺塔问题"""

def move(n ,a ,b ,c):
    if n == 1:
        print(a, '->', c)
    else:
        move(n - 1, a, c, b)
        print(a, '->', c)

        move(n - 1, b, a, c)

move(3, "A", "B", "C")