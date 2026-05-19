import pandas as pd
import torch
from torch import nn
from torch import optim
from sklearn.model_selection import train_test_split
from torch.utils.data import TensorDataset
from torch.utils.data import DataLoader
from torchsummary import summary
import numpy as np
from sklearn.preprocessing import StandardScaler

# 进度条工具： pip install tqdm -i https://mirrors.aliyun.com/pypi/simple/
from tqdm import tqdm

def create_dataset():
    # 文件->DataFrame->张量->Dataset->Dataloader
    # 1- 读取文件
    df = pd.read_csv("data/手机价格预测.csv", encoding="UTF-8")

    # 2- 拆分得到特征值和目标值
    x = df.iloc[:,:-1]
    y = df.iloc[:,-1]

    # 3- 划分得到训练集和测试集
    x_train,x_test,y_train,y_test = train_test_split(x,y,test_size=0.2,random_state=1018)

    # 标准化处理
    transformer = StandardScaler()
    x_train = transformer.fit_transform(x_train)
    x_test = transformer.transform(x_test)

    # 4- 将DataFrame封装为张量；再将张量封装为Dataset
    # 特征数据必须是小数
    x_train = torch.tensor(x_train,dtype=torch.float32)
    x_test = torch.tensor(x_test,dtype=torch.float32)
    # 目前该案例是分类案例，因此目标值必须是整数
    y_train = torch.tensor(y_train.values,dtype=torch.long)
    y_test = torch.tensor(y_test.values,dtype=torch.long)

    # 将特征数据和目标值按顺序拼接起来
    train_dataset = TensorDataset(x_train,y_train)
    test_dataset = TensorDataset(x_test,y_test)

    # 5- 获取特征个数和目标值种类个数
    feature_nums = x.shape[1] # 特征总个数
    target_nums = len(np.unique(y)) #目标值种类个数

    return train_dataset,test_dataset,feature_nums,target_nums

# 搭建神经网络结构
"""
    步骤：
        1- 定义一个类继承自torch.nn.Module
        2- 实现__init__（初始化父类、网络结构、w和b进行初始化）和forward（前向传播）
"""
class PhonePriceModel(nn.Module):
    def __init__(self,feature_nums,target_nums):
        # 1- 初始化父类
        super().__init__()

        # 2- 定义神经网络结构
        # 2.1- 第一层隐藏层
        self.linear1 = nn.Linear(in_features=feature_nums,out_features=512)

        # 2.2- 第二层隐藏层
        # 上下移动代码：shift+alt+上下键
        self.linear2 = nn.Linear(in_features=512,out_features=256)

        # 2.3- 第三层输出层
        self.out = nn.Linear(in_features=128,out_features=target_nums)

    def forward(self,x):
        # 1- 第一层隐藏层
        x = torch.relu(self.linear1(x))

        # 2- 第二层隐藏层
        x = torch.relu(self.linear2(x))

        # 3- 第三层输出层
        """
            为什么这里的输出层的外面不调用torch.softmax包含起来？
            原因：目前的需求是多分类问题，多分类问题的损失函数用的是交叉熵损失，
                 而交叉熵损失会自动的计算softmax，因此不能重复调用softmax激活函数
        """
        output = self.out(x)
        return output

def train_model(train_dataset,feature_nums,target_nums):
    # 1- 创建得到Dataloader
    torch.manual_seed(1018) # 为了让shuffle=True的时候，让数据的随机性固定下来
    dataloader = DataLoader(dataset=train_dataset,batch_size=8,shuffle=True)

    # 2- 创建神经网络结构对象
    model = PhonePriceModel(feature_nums,target_nums)

    # 3- 创建损失函数对象
    criterion = nn.CrossEntropyLoss()

    # 4- 创建优化器
    # optimizer = optim.SGD(params=model.parameters(),lr=1e-3)
    optimizer = optim.Adam(params=model.parameters(),lr=1e-4,betas=(0.9,0.99))

    # 5- 循环训练
    epochs = 50
    for epoch in tqdm(range(epochs)):
        # 每个轮次的总损失值
        total_loss_value = 0.0
        # 每个轮次训练的样本数据总条数
        total_sample_num = 0

        for x_train,y_train in dataloader:
            # 开启允许Dropout随机失活的开关
            model.train()

            # 训练
            y_pred = model(x_train)
            # print(f"y_pred-->{y_pred.shape}")
            # print(f"y_train-->{y_train.shape}")

            # 计算损失值
            # CrossEntropyLoss中不要求将y_train的形状修改，否则会报错：RuntimeError: 0D or 1D target tensor expected, multi-target not supported
            loss_value = criterion(y_pred,y_train)

            # 记录损失信息
            total_loss_value += loss_value.item()*len(x_train)
            total_sample_num += len(x_train)

            # 反向传播固定代码
            optimizer.zero_grad()   # 梯度清零
            loss_value.sum().backward() # 反向传播
            optimizer.step()        # 更新w权重和b偏置

        print(f"第{epoch+1}次，总的平均损失是：{total_loss_value/total_sample_num}")

    # 保存训练好的模型参数信息
    torch.save(model.state_dict(),"model/phone_price_model.pkl")


def predict_model(test_dataset,feature_nums,target_nums):
    # 1- 创建数据加载器
    dataloader = DataLoader(test_dataset,batch_size=3,shuffle=False)

    # 2- 创建神经网络算法实例对象
    model = PhonePriceModel(feature_nums,target_nums)

    # 3- 加载训练好的算法模型参数信息
    model.load_state_dict(torch.load("model/phone_price_model.pkl"))

    # 4- 对未知数据进行预测
    correct_count = 0 # 记录预测准确的数据条数

    for x_test,y_test in dataloader:
        # 关闭：允许Dropout随机失活的开关
        model.eval()

        # 预测
        y_pred = model(x_test)
        """
            为什么y_pred中输出的内容并不是四个类别的概率值，而且以行为单位，数值加起来结果也不是1？
            y_pred-->tensor([[ 6.2885,  6.0777, -3.8871, -9.3965],
                        [ 2.1558,  1.9666, -0.5807, -6.2001],
                        [-5.1727,  0.6991,  3.3093,  4.7401],
                        [-0.6344,  1.6007,  1.9306, -4.0238]], grad_fn=<AddmmBackward0>)
                        
            原因：输出层只是计算了线性求和结果，并没有调用softmax激活函数
            解决：如果想看到四个类别的概率值，手动调用softmax激活函数
        """
        # print(f"y_pred-->{y_pred}")
        # print(f"四个类别的概率值:{torch.softmax(y_pred, dim=1)}")
        # print(f"得到预测的类别ID:{torch.argmax(y_pred, dim=1)}")

        # 判断是否预测准确
        y_pred_ids = torch.argmax(y_pred, dim=1)
        # print((y_pred_ids == y_test))
        # print((y_pred_ids == y_test).sum())

        # correct_count = correct_count + (y_pred_ids == y_test).sum()
        correct_count += (y_pred_ids == y_test).sum()

    # 计算总的准确率
    acc_rate = correct_count.item()/len(test_dataset)
    print(f"预测准确率是：{acc_rate}")

if __name__ == '__main__':
    # 1- 准备数据集
    train_dataset,test_dataset,feature_nums,target_nums = create_dataset()
    print(feature_nums,target_nums)

    # 2- 搭建神经网络结构
    # model = PhonePriceModel(feature_nums,target_nums)
    # summary(model,(feature_nums,),1)

    # 3- 模型训练
    train_model(train_dataset,feature_nums,target_nums)

    # 4- 模型预测
    predict_model(test_dataset,feature_nums,target_nums)
