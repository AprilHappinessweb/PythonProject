# 从小到大
def welcome(n):
    if n > 1:
        welcome(n-1)
    print(
        f'你好呀{n}'
    )
welcome(5)

# 从大到小
def welcome(n):
    print(
        f'你好呀{n}'
    )
    if n > 1:
        welcome(n-1)
welcome(5)