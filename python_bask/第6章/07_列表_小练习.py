# 需求：实现一个成绩统计程序，可以对多名学生的成绩，进行统计和分析
# 备注：用户可以连续输入学生的成绩，知道用户输入“结束”字符串
# 总人数
# 最高分
# 最低分
# 合格人数
# 合格率
# 优秀人数
# 优秀率
# 平均分数
print('请输入学生成绩，输入“结束”停止录入')
score_list = []

# 持续循环，让用户输入学生成绩
while True:
    data = input('✍️请输入成绩：')
    if data == '结束':
        break
    else:
        score = int(data)
        score_list.append(score)

# 如果score_list中有数据，则开始统计
if score_list:
    # 统计平均分
    average = sum(score_list) / len(score_list)
    # 合格人数
    pass_count = 0
    # 优秀人数
    excellent_count = 0
    # 遍历列表开始统计
    for score in score_list:
        if score >= 60:
            pass_count += 1
        if score >= 90:
            excellent_count += 1
    # 合格率
    pass_rate = (pass_count / len(score_list)) * 100
    # 优秀率
    excellent_rate = (excellent_count / len(score_list)) * 100
    # 打印信息
    print('*************⬇️统计信息如下⬇️**************')
    print(f'🧑‍🤝‍🧑总人数为{len(score_list)}')
    print(f'🔺最高分为：{max(score_list)}')
    print(f'🔻最低分为：{min(score_list)}')
    print(f'✅合格的人数为：{pass_count}')
    print(f'📈合格率为：{pass_rate:.1f}%')
    print(f'🏆优秀的人数为：{excellent_count}')
    print(f'📈优秀率为：{excellent_rate:.1f}%')
    print(f'📊平均分数为：{average:0.2f}')
else:
    print('您没有输入任何成绩！')
