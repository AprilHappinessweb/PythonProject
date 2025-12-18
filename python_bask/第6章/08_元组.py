# 定义元组、元组的下标
# t1 = (28,15,32,11,25)
# t2 = ('北京','超市','我在')
# t3 = (True,'北京',False,'超市','我在')
# t4 = (True,'北京',None,'超市','我在',t1)
# print(t1[-1])
# print(t2[2])
# print(t3[0])
# print(t4[-1])
# print(t4[2])

# 元组中的元素不可修改
# t1 = (28,15,32,11,25)
# t1[0] = 100

# 元组中如果存放了可变类型（列表），那可变类型中的内容仍然可以修改
# t2 = (True,'北京',None,'超市','我在',[100,200,300,('北京','超市','我在')])
# print(t2[5])
# t2[5][0] = 900
# print(t2[5])
# t2[5][3] = 888
# print(t2[5])

# 定义空元组
# t1 = ()
# t2 = tuple()
# print(t1)
# print(t2)
# 定义只有一个元素的元组
# t3 = (18,)
# t4 = ('我',)
# print(t3)
# print(t4)
# print(type(t3))
# t5 = ('你好'
#       '这个世界')
# print(t5)
# print(type(t5))

# 元组的常用方法
# t6 = (28,15,32,11,25)
# res6 = t6.index(25)
# print(res6)
# t7 = (28,25,15,32,11,25)
# res7 = t7.count(25)
# print(res7)
# t8 = (28,25,15,32,11,25)
# res8 = max(t8)
# print(res8)
# t9 = (28,25,15,32,11,25)
# res9= min(t9)
# print(res9)
# t10 = (28,25,15,32,11,25)
# res10 = len(t10)
# print(res10)
# t11 = (28,25,15,32,11,25)
# res11 = sorted(t11,reverse=True)
# print(res11)
# print(type(res11))
# res11 = tuple(res11)
# print(res11)
# print(type(res11))
# t12 = (28,25,15,32,11,25)
# res12 = sum(t12)
# print(res12)
# 实际开发中的元组，不一定是我们自己定义的，比如函数的可变参数
# def demo(*args):
#     print(args)
#     res = sum(args)
#     print(res)
# demo(1, 2, 3, 4, 5, 6)
# 元组的循环遍历
t13 = (28, 25, 15, 32, 11, 25)
# while循环遍历
# index = 0
# while index < len(t13):
#     print(t13[index])
#     index += 1
# for循环遍历
# for i in t13:
#     print(i)
for i in enumerate(t13, start=6):
    print(i)
