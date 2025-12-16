age = input('请输入你的年龄：')
age = int(age)
if age <= 12:
    print('你是儿童')
elif age <= 18:
    print('你是青少年')
elif age <= 30:
    print('你是青年')
else:
    print('你是成年人')
print('python的世界很精彩')