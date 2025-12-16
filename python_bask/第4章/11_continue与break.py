# for day in range(1, 7):
#     if day % 2 == 0:
#         continue
#     print(f'*********第{day}天*********')
#     print('学习')
#     print('健身')

for day in range(1, 5):
    if day % 2 == 0:
        break
    print(f'*********第{day}天*********')
    print('吃饭')
    for item in range(1, 3):
        print(f'豆奶{item}')
        continue
        print('牛奶')
    print('鸡蛋')