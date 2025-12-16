a = '你好a'
b = '你好b'


def my_fun():
    c = '你好c'
    d = '你好d'
    print('函数内：', a)
    print('函数内：', b)
    print('函数内：', c)
    print('函数内：', d)


# my_fun()
# print('函数外：',a)
# print('函数外：',b)
# print('函数外：',c)
# print('函数外：',d)

# 在 Python 中，global 是一个关键字，用于在函数内部声明某个变量是全局变量。它的主要作用是让函数内部能够修改在函数外部（即全局作用域中）定义的变量。
n, m = 100, 200


def test3():
    global n
    n += 1
    get_num = m
    print(n)
    print(m)
    print(get_num)

test3()
# print(n)
