# 前序知识
# print('你好', end='')
# print('python', end='')

# for循环实现九九乘法表
for row in range(1, 10):
    for item in range(1, row + 1):
        print(f'{item}*{row}={row * item}', end='\t')
    print()
