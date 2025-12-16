# 06开头表示二进制
num1 = 0b11001
# 0o开头表示八进制
num2 = 0o1034
# 0x开头表示十六进制
num3 = 0x1cf

# print(num1, num2, num3)
#
# print(num1 + 1)
# print(str(num2))
# print(num3 > 400)

# 使用bin()将十进制转为二进制
result1 = bin(25)
# 使用otc()将十进制转为二进制
result2 = oct(25)
# 使用hex()将十进制转为二进制
result3 = hex(25)
# print(result1, result2, result3)
# # bin()、oct()、hex()返回的都是字符串
# print(type(result1), type(result2), type(result3))

# 使用int()将指定进制的数，转为十进制数字
value1 = int('0b11001', 2)
value2 = int('0o1034', 8)
value3 = int('0x1cf', 16)
print(value1, value2, value3)
print(type(value1), type(value2), type(value3))

