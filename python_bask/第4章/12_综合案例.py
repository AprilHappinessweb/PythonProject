print('🏆欢迎来到：答题闯关挑战赛（输入q可随时退出）\n', end='\n')

# 题目与答案
quese1, ans1 = '1+1=?', '2'
quese2, ans2 = '2+2=?', '4'
quese3, ans3 = '3+3=?', '6'

# 最多可尝试次数
max_tries = 3
# 总关卡数
total_levels = 3
# 是否处于游戏状态
is_playing = True

# 根据题目数量开始循环
for level in range(1, total_levels + 1):
    # 打印当前关卡所对应的题目和答案
    print(f'**********🎯第{level}关*********')
    # 取出当前关卡所对应的题目和答案
    if level == 1:
        question, answer = quese1, ans1
    elif level == 2:
        question, answer = quese2, ans2
    else:
        question, answer = quese3, ans3
    # 记录当前关卡的尝试次数
    tries = 1
    # 若已经尝试的次数，小于等于最大尝试次数，则进入循环
    while tries <= max_tries:
        # 向用户提问
        user_input = input(f'📢{question}')
        # 根据用户的输入来决定做什么
        if user_input == answer:
            print('✅回答正确！\n')
            break
        elif user_input == '':
            print('⚠️您的输入为空，请重新作答\n')
        elif user_input == 'q':
            is_playing = False
            print('👋您已经退出游戏！\n')
            break
        else:
            level = max_tries - tries
            if level > 0:
                print(f'❌回答错误，您还剩下{level}次机会\n')
                tries += 1
                continue
            else:
                print(f'😭挑战失败，本题的正确答案是：{answer},游戏结束！')
                is_playing = False
                break
    # 每次进入关卡之前，都要看一下is_playing，如果is_playing为False就要结束游戏
    if not is_playing:
        break
    if is_playing:
        print('🎉恭喜您，闯关成功！')
