"""
    本代码只实现反向传播
"""

import torch

if __name__ == '__main__':
    # 1- 初始化w权重值
    """
        requires_grad：允许对该数据进行梯度下降计算，必须为True
        dtype：因为更新梯度的过程中肯定会出现小数的情况，因此dtype必须是小数
    """
    # 多个权重
    # w = torch.tensor([10,20,30],requires_grad=True,dtype=torch.float32)
    # 一个权重
    w = torch.tensor(20,requires_grad=True,dtype=torch.float32)

    # 2- 定义Loss损失函数
    # 下面的公式因为目前没有学到深度学习的损失函数有哪些，因此下面的公式是自定义的，不用关心
    loss = 2*w**2

    # 3- 进行反向传播->让损失值越来越小
    loss.sum().backward()

    # 4- 更新w权重值
    # W1 = W0 - lr*grad
    """
        w.data = w.data - 0.1 * w.grad代码类似如下的过程
        a = 20
        a = a - 1
        
        w.data是从张量中将值取出来
    """
    w.data = w.data - 0.1 * w.grad

    print(f"更新后的权重值是{w}")



