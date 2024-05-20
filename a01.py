import jieba
from wordcloud import WordCloud
from matplotlib import pyplot as plt
from imageio import imread

# 读取数据
text = open('郑州市第29场新冠肺炎疫情防控新闻发布会.txt', 'r', encoding='utf-8').read()
# 读取停用词，创建停用词表
stwlist = [line.strip() for line in open ('郑州市第29场新冠肺炎疫情防控新闻发布会.txt', encoding = 'utf-8').readlines()]

# 分词
words = jieba.cut(text, cut_all=False, HMM=True)

# 文本清洗
mytext_list = []
for seg in words:
    if seg not in stwlist and seg != " " and len(seg) != 1:
        mytext_list.append(seg.replace(" ", ""))
cloud_text = ",".join(mytext_list)

# 读取背景图片
jpg = imread('img_2.png')
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