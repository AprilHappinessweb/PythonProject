# 定义有内容的【可变集合】
# s1 = {10, 20, 30, 40, 50, 60, 70, 80, 90, 100}
# s2 = {'你好', 'hello', '你好', '北京'}
# s3 = {10, '你好', 1, True, 12.4}
# s4 = {10, '你好', True, 1, 12.4}
# print(s1, type(s1))
# print(s2, type(s2))
# print(s3, type(s3))
# print(s4, type(s4))
# s2.add('今天天氣真好')
# print(s2)

# 定义有内容的【不可变集合】
# s1 = frozenset({10, 20, 30, 40, 50, 60, 70, 80, 90, 100})
# s2 = frozenset({'你好', 'hello', '你好', '北京'})
# s3 = frozenset({10, '你好', 1, True, 12.4})
# s4 = frozenset({10, '你好', True, 1, 12.4})
# print(s1, type(s1))
# print(s2, type(s2))
# print(s3, type(s3))
# print(s4, type(s4))
# print(s2)

# frozenset接收的參數，可以是任意可迭代對象，但最終返回的一定是【不可變集合】
# s1 = frozenset([10, 20, 30, 40, 50, 60])
# s2 = frozenset((10, 20, 30, 40, 50, 60))
# s3 = frozenset('hello')
# print(type(s1),s1)
# print(type(s2),s2)
# print(type(s3),s3)

# 定義空集合（可變集合和不可變集合和空字典）
# s1 = set()
# s2 = frozenset()
# s3 = {}
# print(type(s1),s1)
# print(type(s2),s2)
# print(type(s3),s3)

# 集合中不能嵌套【可變集合】，但可以嵌套【不可變集合】
# 通俗的理解：只有“不可變”的東西，才能安全的放進集合裏
s1 = {10, 20, 30, 40, 50}
s2 = [10, 20, 30, 40, 50]
s3 = (10, 20, 30, 40, 50)
s4 = frozenset({10, 20, 30, 40, 50})
s5 = {11, 22, 33, s3}
print(s5)
