# 具体规则：/前边只能用位置参数，*后面只能用关键字参数
def greet(name,/, gender, age,*, height, weight):
    print(f'我是：{name}，我性别{gender}，我今年{age}岁啦，我的身高是{height}，体重是{weight}')


greet('jack', gender='man', age=8,height='89kg', weight='180cm')
