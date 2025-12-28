# 增
# add方法：向集合中添加元素
# s1 = {10,20,30,40,50}
# s1.add(60)
# print(s1)

# update方法：向集合中添加元素（必須傳遞可迭代對象，例如：列表、元組、集合等）
# s1 = {1,2,3,4,5,6,7,8,9,10}
# s1.update([60,70])
# s1.update([70,80])
# s1.update([80,90])
# s1.update(range(300,308))
# print(s1)

# remove方法
# s1 = {10,20,30,40,50}
# s1.remove(10)
# print(s1)

# s1 = {10,20,30,40,50}
# s1.discard(90)
# print(s1)

# s1 = {10,20,30,40,50,60,70,80,90,100,'你好','不好'}
# res = s1.pop()
# print(res)

# s1 = {10,20,30,40,50}
# s1.clear()
# print(s1)

# s1 = {10,20,30,40,50}
# s1.remove(10)
# s1.add(66)
# print(s1)

# s1 = {10,20,30,40,50}
# res = 20 in s1
# print(res)

s1 = {10, 20, 30, 40, 50}
res = 10 not in s1
print(res)
