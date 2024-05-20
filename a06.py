import numpy as np
from matplotlib import pyplot as plt
# 用于正常显示中文
plt.rcParams['font.sans-serif'] = 'SimHei'
#用于正常显示符号
plt.rcParams['axes.unicode_minus'] = False
plt.figure(figsize=(10, 6), dpi=80)
x = np.linspace(-np.pi, np.pi, 256, endpoint=True)
C, S = np.cos(x), np.sin(x)

# 设置线的颜色，粗细，和线型
plt.plot(x, C, color="blue", linewidth=2.5, linestyle="-", label=r'$sin(x)$')
plt.plot(x, S, color="red", linewidth=2.5, linestyle="-", label=r'$cos(x)$')

# 如果觉得线条离边界太近了，可以加大距离
plt.xlim(x.min() * 1.2, x.max() * 1.2)
plt.ylim(C.min() * 1.2, C.max() * 1.2)

# 当前的刻度并不清晰，需要重新设定,并加上更直观的标签
plt.xticks([-np.pi, -np.pi / 2, 0, np.pi / 2, np.pi],
           [r'$-\pi$', r'$-\pi/2$', r'$0$', r'$+\pi/2$', r'$+\pi$'])
plt.yticks([-1, 1],
           [r'$-1$', r'$1$'])

# 添加图例
plt.legend(loc='upper left')

# plt.gca()，全称是get current axis
ax = plt.gca()
ax.spines['right'].set_color('none')
ax.spines['top'].set_color('none')

# 由于我们移动的是左边和底部的轴，所以不用设置这两个也可以
ax.xaxis.set_ticks_position('bottom')
ax.yaxis.set_ticks_position('left')

# 指定data类型，就是移动到指定数值
# ax.spines['bottom'].set_position('zero')
ax.spines['bottom'].set_position(('data', 0))
ax.spines['left'].set_position(('data', 0))

t = 2 * np.pi / 3

# 利用plt.plot绘制向下的一条垂直的线，利用plt.scatter绘制一个点。
plt.plot([t, t], [0, np.cos(t)], color='blue', linewidth=2.5, linestyle="--")
plt.scatter([t, ], [np.cos(t), ], 50, color='blue')

plt.annotate(r'$sin(\frac{2\pi}{3})=\frac{\sqrt{3}}{2}$',
             xy=(t, np.sin(t)), xycoords='data',
             xytext=(+10, +30), textcoords='offset points', fontsize=16,
             arrowprops=dict(arrowstyle="->", connectionstyle="arc3,rad=.2"))

# 利用plt.plot绘制向上的一条垂直的线，利用plt.scatter绘制一个点。
plt.plot([t, t], [0, np.sin(t)], color='red', linewidth=2.5, linestyle="--")
plt.scatter([t, ], [np.sin(t), ], 50, color='red')

plt.annotate(r'$cos(\frac{2\pi}{3})=-\frac{1}{2}$',
             xy=(t, np.cos(t)), xycoords='data',
             xytext=(-90, -50), textcoords='offset points', fontsize=16,
             arrowprops=dict(arrowstyle="->", connectionstyle="arc3,rad=.2"))

plt.title("正余弦函数图像")
plt.show()
