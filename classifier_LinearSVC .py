# coding=utf-8

import numpy as np
import pandas as pd
from sklearn import svm
from sklearn.model_selection import train_test_split
from sklearn.metrics import confusion_matrix

# 文件路径
path = "files/testday.csv"

# 导入文件
data = pd.read_csv(path)
data = data[1:]

# 将数据的0到25列组成x，第26列得到y
x, y = np.split(data, (25,), axis=1)

# 交叉检验，将样本一分为二，样本中随机抽取20%作为测试集，剩余80%作为训练集合。
X_train, X_test, y_train, y_test = train_test_split(x, y, test_size=0.2, random_state=0)

# 建立线性SVM分类器：
cls1 = svm.LinearSVC()
cls1.fit(X_train, y_train)
# 输出测试集的预测正确率
print(cls1.score(X_test, y_test))
print(confusion_matrix(y_test, cls1.predict(X_test)))
