import numpy as np
import matplotlib.pyplot as plt

# 用于正常显示中文
plt.rcParams['font.sans-serif'] = 'SimHei'
#用于正常显示符号
plt.rcParams['axes.unicode_minus'] = False

category_names = ['01','02','03','04','05','06','07','08','09','10','11','12']
results = {
    '2020年': [5.2,2.7,5.8,5.7,7.3,9.2,8.7,15.6,10.5,11.0,7.8,3.9],
    '2021年': [3.6,4.6,2.1,3.8,8.9,5.8,6.5,27.8,13.9,6.2,10.3,3.7]
}


def survey(results, category_names):
    labels = list(results.keys())
    # 获取标签
    data = np.array(list(results.values()))
    # 获取具体数值
    data_cum = data.cumsum(axis=1)
    # 逐项加和
    category_colors= plt.cm.Set3(np.linspace(0, 1, 12))

    # 常见颜色序列， 在cmap中取色
    fig, ax = plt.subplots(figsize=(5, 10))
    # 绘图
    # ax.invert_xaxis()
    # 使其更符合视觉习惯，index本身从下到上
    ax.yaxis.set_visible(False)
    ax.set_xticklabels(labels=labels, rotation=90)
    # 不需要可见
    ax.set_ylim(0, np.sum(data, axis=1).max())

    for i, (colname, color) in enumerate(zip(category_names, category_colors)):
        heights = data[:, i]
        # 取第一列数值
        starts = data_cum[:, i] - heights
        # 取每段的起始点
        ax.bar(labels, heights, bottom=starts, width=0.5,
               label=colname, color=color)
        xcenters = starts + heights / 2
        r, g, b, _ = color
        text_color = 'white' if r * g * b < 0.5 else 'darkgrey'
        for y, (x, c) in enumerate(zip(xcenters, heights)):
            ax.text(y, x, str(c), ha='center', va='center',
                    color=text_color, rotation=90)
    ax.legend()
    return fig, ax


survey(results, category_names)
plt.show()

