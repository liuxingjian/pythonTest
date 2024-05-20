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