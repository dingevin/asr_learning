1. BN 与 LN  的 区别：
    BN 是取不同样本的同一帧， 然后对这一帧上的不同维度的每一个特征取均值；
    LN 是对同一个样本的不同帧， 然后对每一帧的不同维度的特征取均值；
    比如 [batch, time, 512] --> mean: [batch, time, 1] 是对这512个数取均值
    
    所以， BN的效果要优于LN , 但是在RNN中， 不能用BN
    
    https://zhuanlan.zhihu.com/p/54530247
