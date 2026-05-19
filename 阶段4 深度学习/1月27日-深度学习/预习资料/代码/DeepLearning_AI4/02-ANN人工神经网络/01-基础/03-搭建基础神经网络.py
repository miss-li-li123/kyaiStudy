
"""
    步骤：
        1- 定义一个类，继承自torch.nn.Module
        2- 实现两个方法
            2.1- __init__
                定义网络结构，也就是隐藏层和输出层的层数、每层的神经元个数
                w、b参数初始化
            2.2- forward前向传播
                输入样本数据，经过各个网络层，得到预测结果
"""
import torch
from torch import nn
# 安装命令 pip install torchsummary -i https://mirrors.aliyun.com/pypi/simple/
from torchsummary import summary

class MyModel(nn.Module):
    def __init__(self):
        # 定义网络结构，也就是隐藏层和输出层的层数、每层的神经元个数

        # 1- 先初始化父类
        super().__init__()

        # 2- 定义网络结构
        # 第一层隐藏层
        self.linear1 = nn.Linear(in_features=3,out_features=3)

        # 第二层隐藏层
        self.linear2 = nn.Linear(in_features=3, out_features=2)

        # 输出层
        self.out = nn.Linear(in_features=2, out_features=2)

        # 3- w、b参数初始化
        # 第一层隐藏层
        nn.init.xavier_normal_(self.linear1.weight)
        nn.init.zeros_(self.linear1.bias)

        # 第二层隐藏层
        nn.init.kaiming_normal_(self.linear2.weight)
        nn.init.zeros_(self.linear2.bias)

        """
            为什么这里没有对输出层的w权重和b偏置进行初始化，也能够成功运行呢？
            因为nn.Linear底层源代码默认使用kaiming_uniform_对参数进行了初始化
        """

    def forward(self,x):
        # 神经元的运行步骤：先进行线性求和，再使用激活函数

        # 第一层隐藏层
        # 分开的版本
        # x = self.linear1(x) # 线性求和
        # x = torch.sigmoid(x) # 激活函数

        # 合并版
        x = torch.sigmoid(self.linear1(x))

        # 第二层隐藏层
        x = torch.relu(self.linear2(x))

        # 输出层
        # dim=-1的意思是：按照最后一层的数据计算多个类别的概率值
        result = torch.softmax(self.out(x),dim=-1)
        return result

def train_model():
    # 1- 准备训练数据：目前的需求中，每条样本必须有3个特征
    # 10：多少条样本；3：每条样本多少个特征
    data = torch.randn(10,3)

    # 2- 创建神经网络模型对象
    my_model = MyModel()

    # 3- 模型训练：将数据输入到神经网络中，进行前向传播
    # 内部自动调用forward方法
    output = my_model(data)
    print(f"预测结果是：{output}")
    print(f"预测结果形状：{output.shape}")

    print("-" * 30)

    # 4- 查看神经网络的概要信息
    """
        summary(参数1,参数2,参数3)：查看神经网络各层参数的信息
            参数1：神经网络算法实例对象
            参数2：输入的特征个数，类型必须是元组
            参数3：输入的每个批次样本条数，任意
    """
    summary(my_model,(3,),2)

    print("-"*30)

if __name__ == '__main__':
    train_model()