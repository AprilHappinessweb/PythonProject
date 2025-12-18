def calc_total(*nums):
    """
    计算总和
    :param nums: 可变参数
    :return: 返回和
    """
    return sum(nums)


def calc_avg(total, duration):
    """
    计算平均数
    :param total: 实际总和
    :param duration: 持续天数
    :return:
    """
    return total / duration


def check_success(total, goal):
    """
    判断是否挑战成功
    :param total: 实际总和
    :param goal: 目标
    :return: 返回挑战结果
    """
    if total >= goal:
        return '挑战成功！'
    else:
        return '挑战失败'


def main(title, duration, goal):
    """
    主函数，用于开始一场挑战赛
    :param title: 比赛标题
    :param duration: 比赛持续天数
    :param goal: 目标运动量
    :return: None
    """
    print(f'欢迎来到【{title}】【{duration}】天挑战赛')
    nums = []
    for i in range(duration):
        nums.append(int(input(f'请输入第{i + 1}的数据：')))

    total = calc_total(*nums)
    avg = calc_avg(total, duration)
    result = check_success(total, goal)
    print(result, f'在这【{duration}】天中，你总共记住了【{total}】个单词，平均每天记住{avg:.2f}个单词')


main('学习单词', 7, 30)
