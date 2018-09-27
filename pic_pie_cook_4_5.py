# -*- coding: utf-8 -*-
from matplotlib import pyplot as plt
import pandas as pd

from matplotlib import font_manager

# 文件路径
path = "files/testday.csv"

# 导入输入
df = pd.read_csv(path)

# 设置字体
my_font = font_manager.FontProperties(fname="C:\Windows\Fonts\msyh.ttc")

cook = []
for i in range(len(df)):
    # cook_0 = df.iat[i, 2]
    # cook_1 = df.iat[i, 3]
    cook_2 = df.iat[i, 4]
    cook_3 = df.iat[i, 5]
    cook_4 = df.iat[i, 6]
    cook_5 = df.iat[i, 7]
    cook.append(cook_2 + cook_3 + cook_4 + cook_5)

# print(cook)

cook_0 = []
cook_1 = []

for i in range(len(df)):
    if cook[i] != 0:
        if df.iat[i, 25] == 0:
            cook_0.append(cook[i])
        else:
            cook_1.append(cook[i])

# 调节图形大小，宽，高
plt.figure(figsize=(7, 8))

# 定义饼状图的标签，标签是列表
labels = ['normal', 'abnormal']

# 每个标签占多大，会自动去算百分比
sizes = [len(cook_0), len(cook_1)]
colors = ['red', 'green']

# 将某部分爆炸出来， 使用括号，将第一块分割出来，数值的大小是分割出来的与其他两块的间隙
explode = (0, 0.2)

patches, l_text, p_text = plt.pie(sizes, explode=explode, labels=labels, colors=colors,
                                  labeldistance=1.1, autopct='%3.1f%%', shadow=False,
                                  startangle=90, pctdistance=0.6)

# 设置x，y轴刻度一致，这样饼图才能是圆的
plt.axis('equal')
plt.title("cook", fontproperties=my_font)
plt.legend(prop=my_font)
plt.show()
