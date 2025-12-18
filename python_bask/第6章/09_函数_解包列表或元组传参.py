# 定义函数时，使用*args（变量不一定非要用args，比如写*data也可以），将收到的多个参数解包成元组
def test(*data):
    print(f'我接收到的参数是{data},参数的类型是{type(data)}')


list1 = [100, 200, 300, 400]
tuple1 = ('你好', 'hello', 'world')

# 函数调用时，正常传递:列表 或者 元组
# test(list1)
# test(tuple1)

# 函数调用时，使用*对：列表或元组进行解包后，再传递参数
test(*list1)
test(*tuple1)
