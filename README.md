1.完成两个词云图（1）完成《中共中央关于党的百年奋斗重大成就和历史经验的决议》的词云，并解释词云体现的内涵意义。文本文档建文件“中共中央关于党的百年奋斗重大成就和历史经验的决议.txt”。决议总共七个部分，也可以只选择其中一部分或者几个部分形成新的.txt文件再做词云。（要求背景图片形状是一幅中国地图）。（2）完成“郑州市第29场新冠肺炎疫情防控新闻发布会”的词云图，文本文件见“郑州市第29场新冠肺炎疫情防控新闻发布会.txt”。（要求背景图片形状是一幅穿防护服的白衣天使背景图像）。

```
(1) import jieba
from wordcloud import WordCloud
from matplotlib import pyplot as plt
from imageio import imread

# 读取数据
text = open('中共中央关于党的百年奋斗重大成就和历史经验的决议.txt', 'r', encoding='utf-8').read()
# 读取停用词，创建停用词表
stwlist = [line.strip() for line in open ('中共中央关于党的百年奋斗重大成就和历史经验的决议.txt', encoding = 'utf-8').readlines()]

# 分词
words = jieba.cut(text, cut_all=False, HMM=True)

# 文本清洗
mytext_list = []
for seg in words:
    if seg not in stwlist and seg != " " and len(seg) != 1:
        mytext_list.append(seg.replace(" ", ""))
cloud_text = ",".join(mytext_list)

# 读取背景图片
jpg = imread('img.png')
# 生成词云
wordcloud = WordCloud(
    mask = jpg,
    background_color = "white",
    font_path = 'simhei.ttf',
    width = 2000,
    height = 1500,
    margin = 10
).generate(cloud_text)
# font_path='simhei.ttf' 这个参数为指定字体

# 绘制图片
plt.imshow(wordcloud)
# 去除坐标轴
plt.axis("off")
plt.show()
```

![image](https://github.com/liuxingjian/pythonTest/assets/69226327/eaee98ea-95af-4fb1-95fd-cf6a6c729a53)

从图中可以发现，我们国家特别重视发展和建设。

（2）

![image](https://github.com/liuxingjian/pythonTest/assets/69226327/a164331e-3d4a-4fa1-b590-aa3931c4c16f)

2.请设计程序，采用第三方库**numpy**和**matplotlib**用雷达图展示某一组学生成绩。假设某一组学生的8门课程成绩如下表二所示。

表二 某组学生课程成绩

| 课程 | 英语 | Java技术 | 线性代数 | 马克思主义 | 计算机导论 | 体育 | Python程序设计 | 网页设计 |
| ---- | ---- | -------- | -------- | ---------- | ---------- | ---- | -------------- | -------- |
| 王芳 | 78   | 90       | 78       | 90         | 48         | 79   | 82             | 93       |
| 李普 | 83   | 85       | 65       | 82         | 75         | 85   | 78             | 85       |
| 颜美 | 88   | 85       | 71       | 83         | 86         | 87   | 89             | 56       |
| 李壮 | 90   | 80       | 67       | 76         | 86         | 90   | 76             | 92       |
| 韩晓 | 72   | 73       | 80       | 71         | 74         | 71   | 82             | 84       |
| 杨乐 | 70   | 86       | 86       | 72         | 67         | 81   | 66             | 77       |

```
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
```

 
![image](https://github.com/liuxingjian/pythonTest/assets/69226327/1765450b-4fdf-48fb-9841-c7cea7f0ef91)

3.下面是2年服装店的营业数据（万元），请绘制堆积代码柱状图。

| **月份**                   | **1**   | **2**   | **3**   | **4**   | **5**   | **6**   | **7**   | **8**    | **9**    | **10**   | **11**   | **12**  |
| -------------------------- | ------- | ------- | ------- | ------- | ------- | ------- | ------- | -------- | -------- | -------- | -------- | ------- |
| **营业额（****2020****）** | **5.2** | **2.7** | **5.8** | **5.7** | **7.3** | **9.2** | **8.7** | **15.6** | **10.5** | **11.0** | **7.8**  | **3.9** |
| **营业额（****2021****）** | **3.6** | **4.6** | **2.1** | **3.8** | **8.9** | **5.8** | **6.5** | **27.8** | **13.9** | **6.2**  | **10.3** | **3.7** |

```
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
    fig, ax = plt.subplots(figsize=(10, 19))
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
```

![image](https://github.com/liuxingjian/pythonTest/assets/69226327/8a264e6a-fec5-495a-9266-53a52b27ad06)

\4. 自己设计数据和颜色，绘制倒影柱状图。*
\* import matplotlib.pyplot as plt
 
 
 num_list1 = [2.5, 0.6, 3.8, 6.6,1.2,9.5,4.2]
 num_list2 = [-6.6,-1.2,-3.5,-4.2,-2.5, -3.6, -10]
 
 
 name_list = ['Mon','Tue','Wed','Thu','Fri','Sat','Sun']
 
 plt.bar(range(len(num_list1)), num_list1,color='r',label='girl',tick_label=name_list)
 
 plt.bar(range(len(num_list2)), num_list2,color='y',label='boy',tick_label=name_list)
 
 plt.legend()
 
 plt.show()

![image](https://github.com/liuxingjian/pythonTest/assets/69226327/beb901f6-d352-4be2-be1a-a62ebaaa7c1a)

\5. 2022年1月11日,“郑州市新冠肺炎疫情防控”第29场新闻发布会在市政府新闻发布厅召开，通报郑州市新冠肺炎疫情防控工作最新进展情况。统计显示，截至1月10日24时，全市累计报告本土确诊病例103例（其中，二七区47例，中原区27例，管城区14例，高新区6例，航空港区4例，金水区4例，郑东新区1例）。请用饼状图表示上面这组数据。

```
import matplotlib.pyplot as plt
# 用于正常显示中文
plt.rcParams['font.sans-serif'] = 'SimHei'
#用于正常显示符号
plt.rcParams['axes.unicode_minus'] = False
# make the pie circular by setting the aspect ratio to 1
# plt.figure(figsize=plt.figaspect(1))
values = [47, 27, 14, 6,4,4,1]
labels = ['二七区', '中原区', '管城区', '高新区','航空港区','金水区','郑东新区']
def make_autopct(values):
    def my_autopct(pct):
        total = sum(values)
        val = int(round(pct*total/100.0))
# 同时显示数值和占比的饼图
        return '{p:.2f}%  ({v:d})'.format(p=pct,v=val)
    return my_autopct
plt.pie(values, labels=labels, autopct=make_autopct(values))
plt.title("全市累计报告本土确诊病例")
plt.show()
```

![image](https://github.com/liuxingjian/pythonTest/assets/69226327/dc0eca1a-c7b6-4569-9e5e-0cf7b8bafaa7)

\6. 绘制正线余弦图像，然后设置图例字体、标题、位置、阴影、背景色、边框颜色、分栏、符号位置等属性。

```
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
```

![image](https://github.com/liuxingjian/pythonTest/assets/69226327/a700ec92-ff4f-42a4-858b-b0e0315604cc)

7.自己设计图样和数据，绘制一幅三维图形。

```
# coding=utf-8
import numpy as np
import matplotlib.pyplot as plt
import mpl_toolkits.mplot3d
a,b = np.mgrid[-2:2:20j,-2:2:20j]
#测试数据
c=a*np.exp(-a**2-b**2)
#三维图形
ax = plt.subplot(111, projection='3d')
ax.set_title('My-3D');
ax.plot_surface(a,b,c,rstride=2, cstride=1, cmap=plt.cm.Spectral)
#设置坐标轴标签
ax.set_xlabel('A')
ax.set_ylabel('B')
ax.set_zlabel('C')
plt.show()
```
![image](https://github.com/liuxingjian/pythonTest/assets/69226327/ca20518d-5030-4e92-9ad6-c230f4c84b9b)

8.请使用递归函数设计和绘制一颗分形树。

```
## 绘制分型树,末梢的树枝的颜色不同

import turtle

def draw_brach(brach_length):

    if brach_length > 5:
        if brach_length < 40:
            turtle.color('green')
        else:
            turtle.color('red')
        # 绘制右侧的树枝
        turtle.forward(brach_length)
        turtle.right(25)
        draw_brach(brach_length-15)
        # 绘制左侧的树枝
        turtle.left(50)
        draw_brach(brach_length-15)
        if brach_length < 40:
            turtle.color('green')
        else:
            turtle.color('red')
        # 返回之前的树枝上
        turtle.right(25)
        turtle.backward(brach_length)  

def main():
    turtle.left(90)
    turtle.penup()
    turtle.backward(150)
    turtle.pendown()
    turtle.color('red')

    draw_brach(100)

    turtle.exitonclick()

if __name__ == '__main__':
    main()
```

 

9.请绘制能表现雪花形状的科赫曲线图。

```
from __future__ import print_function, division

import turtle


def koch(t, n):
    """Draws a koch curve with length n."""
    if n < 10:
        t.fd(n)
        return
    m = n/3
    koch(t, m)
    t.lt(60)
    koch(t, m)
    t.rt(120)
    koch(t, m)
    t.lt(60)
    koch(t, m)


def snowflake(t, n):
    """Draws a snowflake (a triangle with a Koch curve for each side)."""
    for i in range(3):
        koch(t, n)
        t.rt(120)


bob = turtle.Turtle()

bob.pu()
bob.goto(-150, 90)
bob.pd()
snowflake(bob, 300)

turtle.mainloop()
```

![image](https://github.com/liuxingjian/pythonTest/assets/69226327/2ddd30fd-6bce-4425-857f-ae470e08aab5)

10.这两个视频图特别有展现力。网上有一条视频（https://baike.baidu.com/item/%E5%8D%97%E4%B8%81%E6%A0%BC%E5%B0%94%E7%8E%AB%E7%91%B0%E5%9B%BE/19510516?fr=aladdin），用南丁格尔玫瑰图展示各个国家新冠疫情死亡人数变化的情况，记录和展现了历史，非常直观。

类似地，各个国家每年GDP数据的变化也可以这样展现。（https://view.inews.qq.com/a/20200615V0JQYT00全球GDP总量前10个国家排名）

请任意选择上面两种数据中的某一年中的部分国家数据，绘制出南丁格尔玫瑰图进行表示（即极坐标上画柱状图）。

```
import pandas as pd
# 读入数据
from pyecharts.charts import Pie
from pyecharts import options as opts
df = pd.read_excel("30.xlsx")
v = df['国家'].values.tolist()
d = df['经济'].values.tolist()
#设置颜色
color_series = ['#FAE927','#E9E416','#C9DA36','#9ECB3C','#6DBC49',
                '#37B44E','#3DBA78','#14ADCF','#209AC9','#1E91CA']
# 实例化Pie类
pie1 = Pie(init_opts=opts.InitOpts(width='1350px', height='750px'))
# 设置颜色
pie1.set_colors(color_series)
# 添加数据，设置饼图的半径，是否展示成南丁格尔图
pie1.add("", [list(z) for z in zip(v, d)],
        radius=["30%", "135%"],
        center=["50%", "65%"],
        rosetype="area"
        )
# 设置全局配置项
pie1.set_global_opts(title_opts=opts.TitleOpts(title='玫瑰图示例'),
                     legend_opts=opts.LegendOpts(is_show=False),
                     toolbox_opts=opts.ToolboxOpts())
# 设置系列配置项
pie1.set_series_opts(label_opts=opts.LabelOpts(is_show=True, position="inside", font_size=12,
                                               formatter="{b}:{c}例", font_style="italic",
                                               font_weight="bold", font_family="Microsoft YaHei"
                                               ),
                     )
# 生成html文档
pie1.render("南丁格尔玫瑰图.html")
```

![image](https://github.com/liuxingjian/pythonTest/assets/69226327/1d2f9d01-07b7-4d67-bffd-7b682c5ac305)
