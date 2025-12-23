# 字符串的下标
# msg = 'welcome to python'
# print(msg)
# print(msg[3])
import numbers

# 字符串中的字符，不可修改
# msg1 = 'welcome to my world'
# msg1[1] = 'hello'
# print(msg1)

# 字符串不能嵌套
# msg2 = 'welcome to "yoyo" my world'
# print(msg2)

# 常用方法
#index 方法，获取指定字符串，在字符串中第一次出现的下标
# msg3 = 'welcome to my world'
# result3 = msg3.index('o')
# print(result3)

# split方法：将字符串按照指定字符进行分隔，并将分隔后的内容存入一个列表
# msg4 = '32342423 42312312 31231 234523534545345'
# result4 = msg4.split(' ')
# print(result4)

# replace方法：将字符串中的某个字符片段，替换成目标字符串（不修改原字符串，返回新字符串）
# msg5 = 'welcome to my world'
# result5 = msg5.replace('world', 'amusement park')
# print(result5)

# count方法：统计指定字符，在字符串中出现的次数
# msg6 = 'welcome to my world'
# result6 = msg6.count('w')
# print(result6)

# strip方法：从每个字符串中删除指定字符串中的任意字符
# 规则：从字符创两端开始删除，直到遇到第一个个不在指定字符串中的字符就停下
# msg7 = '666我家有6只猪6只狗666'
# result7 = msg7.strip('666')
# print(result7)
# msg8 = '1523我家有6只猪6只狗3521'
# result8 = msg8.strip('2351')
# print(result8)
# msg9 = '1523我家有6只猪6只狗5321'
# result9 = msg9.strip('1425')
# print(result9)

# 常用的内置函数
# msg8 = '我家有6只猪6只狗'
# result8 = len(msg8)
# print(result8)

# 字符串的遍历循环
msg9 = '我家有6只猪6只狗'
# index = 0
# while index < len(msg9):
#     print(msg9[index])
#     index += 1
# for item in msg9:
#     print(item)