# 导包
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score

# 1.读取文件获取数据
data = pd.read_csv('data/breast-cancer-wisconsin.csv', sep=',')
print(data.shape, data.ndim)  # 形状:(699, 11) 维度:2
# 2.数据预处理
# 2.0 注意: 数据中有"?"无效字符,需要先转换为numpy中的nan,然后使用dropna()删除或者fillna()填充
new_data = data.replace('?', np.nan).dropna()
print(new_data.shape, new_data.ndim)  # 形状:(683, 11) 维度:2
# 2.1 分别获取特征和标签
# 拓展:  iloc格式 : 数据.iloc[行索引,列索引]
x = new_data.iloc[:, 1:-1]
y = new_data.iloc[:, -1]
print(x.shape, x.ndim)  # 形状:(683, 9) 维度:2
print(y.shape, y.ndim)  # 形状:(683,) 维度:1
# 2.2 使用train_test_split()按比例切割成4部分
X_train, X_test, y_train, y_test = train_test_split(x, y, test_size=0.2,random_state=666)  # 同一个种子,同一份随机数据
# 3.特征处理(标准化)
ss = StandardScaler()  # 标准化模型对特征数据处理
new_x_train = ss.fit_transform(X_train)
new_x_test = ss.transform(X_test)
# 4.创建模型
lr_model = LogisticRegression()  # 逻辑回归模型真正预测结果
# 5.模型训练
lr_model.fit(new_x_train, y_train)
print('=======================================================')
# 6.模型预测和评估: 准确率
y_pred = lr_model.predict(new_x_test)  # 1.先预测
print(y_pred)
print(y_test.tolist())
print(f"准确率:{accuracy_score(y_test, y_pred)}")  # 2.再计算
print('---------------------------------------------------')
print(f"准确率:{lr_model.score(new_x_test, y_test)}")  # 底层也是先预测再计算
print('=======================================================')
