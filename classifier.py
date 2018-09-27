# coding=utf-8

import numpy as np
import pandas as pd
from sklearn import svm
from sklearn.model_selection import train_test_split
from sklearn.metrics import confusion_matrix
from sklearn.ensemble import RandomForestClassifier
from sklearn.ensemble import VotingClassifier
from sklearn.tree import DecisionTreeClassifier

# 文件路径
path = "files/day_three.csv"
# 导入文件
# data = np.loadtxt(path, dtype=float, delimiter=',')
data = pd.read_csv(path)
data = data[1:]
# 将数据的0到25列组成x，第26列得到y
x, y = np.split(data, (25,), axis=1)

# 交叉检验，将样本一分为二，样本中随机抽取40%作为测试集，剩余60%作为训练集合。
X_train, X_test, y_train, y_test = train_test_split(x, y, test_size=0.2, random_state=0)

# 建立非线性SVM分类器：
cls = svm.SVC(kernel='sigmoid')

# cls.fit(X_train, y_train)
# # 输出测试集的预测正确率
# print(cls.score(X_test, y_test))
# print(confusion_matrix(y_test, cls.predict(X_test)))
# print('Coefficients:%s,intercept %s' % (cls.coef_, cls.intercept_))

# 建立线性SVM分类器：
cls1 = svm.LinearSVC()
cls1.fit(X_train, y_train)
# 输出测试集的预测正确率
# print(cls1.score(X_test, y_test))
# print(confusion_matrix(y_test, cls1.predict(X_test)))

# 随机森林
clf2 = RandomForestClassifier(n_estimators=50, max_depth=1, min_samples_split=4, min_samples_leaf=54, oob_score=True)
clf2.fit(X_train, y_train)
# 输出测试集的预测正确率
# print(clf2.score(X_test, y_test))
# print(confusion_matrix(y_test, clf2.predict(X_test)))

print("*" * 100)

# 决策树
tre = DecisionTreeClassifier(criterion='gini', splitter='best')
tre.fit(X_train, y_train)
# 输出测试集的预测正确率
# print(tre.score(X_test, y_test))
# print(confusion_matrix(y_test, tre.predict(X_test)))

eclf = VotingClassifier(estimators=[('svcnl', tre), ('rf', clf2), ('svc', cls1)], voting='hard')
eclf.fit(X_train, y_train)
# 输出测试集的预测正确率
print("线性svm ",cls1.score(X_test, y_test))
print("非线性svm ",tre.score(X_test, y_test))
print("随机森林 ",clf2.score(X_test, y_test))
print("集成学习",eclf.score(X_test, y_test))
print(confusion_matrix(y_test, eclf.predict(X_test)))
