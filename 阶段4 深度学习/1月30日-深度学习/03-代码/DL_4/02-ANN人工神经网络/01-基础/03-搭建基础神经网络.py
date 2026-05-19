
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