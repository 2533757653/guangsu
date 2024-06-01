import plotly.figure_factory as ff


def output(tasks):
    

    # 创建甘特图
    fig = ff.create_gantt(tasks)

    # 显示甘特图
    fig.show()
