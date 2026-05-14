# 注意以下导包会报错,错误内容中有获取数据的代码
# from sklearn.datasets import load_boston  # 此行注释
# 以下代码,从错误信息中复制
import pandas as pd
import numpy as np

data_url = "http://lib.stat.cmu.edu/datasets/boston"
raw_df = pd.read_csv(data_url, sep="\s+", skiprows=22, header=None)
data = np.hstack([raw_df.values[::2, :], raw_df.values[1::2, :2]])
target = raw_df.values[1::2, 2]
# 自己打印
print(f"特征:{data[0]}")
print(f"标签:{target}")