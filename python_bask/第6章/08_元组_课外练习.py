## Python 元组练习题
### 基础练习
# 1. **创建元组**：创建一个包含 5 个城市名称的元组，并打印第 2 个和最后一个元素
cities = ('北京','上海','广州','深圳','长沙')
print(cities[1],cities[-1])
# 2. **元组解包**：创建元组 `(10, 20, 30)`，用解包的方式将三个值分别赋给变量 `a, b, c`
t = (10, 20, 30)
a, b, c = t
print(a, b, c)
# 3. **元组拼接**：将元组 `(1, 2, 3)` 和 `(4, 5, 6)` 合并成一个新元组
t1 = (1, 2, 3)
t2 = (4, 5, 6)
t3 = t1 + t2
print(t3)
# 4. **统计元素**：在元组 `(1, 2, 3, 2, 4, 2, 5)` 中统计数字 `2` 出现的次数
t4 = (1, 2, 3, 2, 4, 2, 5)
print(t.count(2))
# 5. **查找索引**：在元组 `('apple', 'banana', 'cherry')` 中查找 `'banana'` 的索引位置
t5 = ('apple', 'banana', 'cherry')
print(t5.index('banana'))
# ### 进阶练习
#
# 6. **元组遍历**：创建一个包含 5 个数字的元组，用 for 循环打印每个元素及其索引
t6 = (10, 20, 30, 40, 50)
for i in range(len(t6)):
    print(i,t6[i])
# 7. **嵌套元组**：创建一个表示学生信息的嵌套元组：`(("张三", 18, 90), ("李四", 19, 85))`，打印第一个学生的姓名和成绩
t7 = (("张三", 18, 90), ("李四", 19, 85))
print(t7[0][0],t7[0][2])
# 8. **元组转列表**：将元组 `(1, 2, 3)` 转换为列表，添加元素 `4`，再转回元组
t8 = (1, 2, 3)
l = list(t8)
l.append(4)
t8 = tuple(l)
print(t8)
# 9. **交换变量**：使用元组解包的方式交换两个变量 `x = 5` 和 `y = 10` 的值
x = 5
y = 10
x,y = y,x
print(x,y)
# 10. **返回多值**：编写一个函数，接收一个数字列表，返回一个元组包含 (最大值, 最小值, 平均值)
def demo(*data):
    resmax = max(data)
    resmin = min(data)
    resavg = sum(data)/len(data)
    return (resmax,resmin,resavg)

# --- AI 参考实现 ---
def get_stats(nums):
    """
    接收一个数字列表，返回 (最大值, 最小值, 平均值)
    """
    if not nums:
        return (None, None, 0)
    return (max(nums), min(nums), sum(nums) / len(nums))

# 验证我的代码
print("参考实现输出:", get_stats([1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]))

# 你的调用（注：由于 demo 定义使用了 *data，传入列表会报错，建议改为 demo(data) 或调用时拆包）
result = demo(*[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15])
print(result)

