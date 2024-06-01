import plotly.figure_factory as ff

# 甘特图数据
tasks = [
    dict(Task="任务1", Start='2024-06-01', Finish='2024-06-05'),
    dict(Task="任务2", Start='2024-06-03', Finish='2024-06-08'),
    dict(Task="任务3", Start='2024-06-06', Finish='2024-06-10')
]

# 创建甘特图
fig = ff.create_gantt(tasks)

# 显示甘特图
fig.show()
