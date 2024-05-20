# coding=utf-8
import numpy as np
import matplotlib.pyplot as plt


# 用于正常显示中文
plt.rcParams['font.sans-serif'] = 'SimHei'
#用于正常显示符号
plt.rcParams['axes.unicode_minus'] = False
name=["英语","Java技术","线性代数","马克思主义","计算机导论","体育","Python程序设计","网页设计"]
val=[[78,90,78,90,48,79,82,93],
     [83,85,65,82,75,85,78,85],
     [88,85,71,83,86,87,89,56],
     [90,80,67,76,86,90,76,92],
     [72,73,80,71,74,71,82,84],
     [70,86,86,72,67,81,66,77]]

#results = [{"大学英语": 87, "高等数学": 79, "体育": 95, "计算机基础": 92, "程序设计": 85},
#           {"大学英语": 80, "高等数学": 90, "体育": 91, "计算机基础": 85, "程序设计": 88}]
data_length = len(name)
# 将极坐标根据数据长度进行等分
angles = np.linspace(0, 2*np.pi, data_length, endpoint=False)
labels = name

# 使雷达图数据封闭
score_a = np.concatenate((val[0], [val[0][0]]))
score_b = np.concatenate((val[1], [val[1][0]]))
score_c = np.concatenate((val[2], [val[2][0]]))
score_d = np.concatenate((val[3], [val[3][0]]))
score_e = np.concatenate((val[4], [val[4][0]]))
score_f = np.concatenate((val[5], [val[5][0]]))
angles = np.concatenate((angles, [angles[0]]))
labels = np.concatenate((labels, [labels[0]]))
# 设置图形的大小
fig = plt.figure(figsize=(8, 6), dpi=100)
# 新建一个子图
ax = plt.subplot(111, polar=True)
# 绘制雷达图
ax.plot(angles, score_a, color='g')
ax.plot(angles, score_b, color='b')
ax.plot(angles, score_c, color='r')
ax.plot(angles, score_d, color='y')
ax.plot(angles, score_e, color='pink')
ax.plot(angles, score_f, color='k')
# 设置雷达图中每一项的标签显示
ax.set_thetagrids(angles*180/np.pi, labels)
# 设置雷达图的0度起始位置
ax.set_theta_zero_location('N')
# 设置雷达图的坐标刻度范围
ax.set_rlim(0, 100)
# 设置雷达图的坐标值显示角度，相对于起始角度的偏移量
ax.set_rlabel_position(270)
ax.set_title("某组学生课程成绩")
plt.legend(["王芳", "李普","颜美","李壮","韩晓","杨乐"], loc='best')
plt.show()