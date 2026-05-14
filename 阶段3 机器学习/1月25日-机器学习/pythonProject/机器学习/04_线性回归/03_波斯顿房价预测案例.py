import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import SGDRegressor,LinearRegression
from sklearn.metrics import mean_absolute_error,mean_squared_error,root_mean_squared_error
# TODO 1.准备数据
# todo 1.1 获取原始数据
data_url = "http://lib.stat.cmu.edu/datasets/boston"
raw_df = pd.read_csv(data_url, sep="\s+", skiprows=22, header=None)
data = np.hstack([raw_df.values[::2, :], raw_df.values[1::2, :2]])
target = raw_df.values[1::2, 2]
# print(f"特征:{data}")
# print(f"标签:{target}")
# todo 1.2 数据切割
X_train, X_test, y_train, y_test = train_test_split(data, target, test_size=0.2, random_state=42)
# todo 1.3 特征的标准化数据
ss = StandardScaler()
new_x_train = ss.fit_transform(X_train) # 训练集用fit_transform()训练并转换
new_x_test = ss.transform(X_test) # 测试集只能用transform()转换,因为前面训练集已经训练了模型计算了相关内容
# TODO 2.准备模型(正规方程或者梯度下降)
# invscaling: 动态调整学习率    constant:固定学习率
# model = LinearRegression()
model = SGDRegressor(loss="squared_error",learning_rate="constant",eta0=0.01) # 梯度下降模型
# TODO 3.模型训练
model.fit(new_x_train,y_train)
print(f"训练后k权重参数:{model.coef_}")
print(f"训练后b偏置参数:{model.intercept_}")
# TODO 4.模型预测
y_pred = model.predict(new_x_test)
# TODO 5.模型评估
print(f"平均绝对误差:{mean_absolute_error(y_test,y_pred)}") # 平均绝对误差:3.157712560608428
print(f"均方误差:{mean_squared_error(y_test,y_pred)}") # 均方误差:23.00412271141051
print(f"均方根误差:{root_mean_squared_error(y_test,y_pred)}") # 均方根误差:4.796261326430255

