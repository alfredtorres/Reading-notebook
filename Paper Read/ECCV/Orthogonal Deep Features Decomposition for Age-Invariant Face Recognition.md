# Orthogonal Deep Features Decomposition for Age-Invariant Face Recognition
## 消除人脸识别中年龄影响的一种方法：深度特征正交分解
### 摘要
年龄在脸部的影响是人脸识别中类内差异的主要原因，年龄不变的人脸识别仍然是人脸识别领域的一个重要挑战。
为了减小年龄对类内的影响，本文提出了OE-CNNs【正交嵌入-卷积神经网络】来学习年龄不变的深度人脸特征。
其中，我们将深度人脸特征分解为2个正交部分：年龄相关的特征age-related features、身份相关的特征identity-related features。
利用identity-related features可以进行不受年龄影响的人脸识别。此外，为了更好的补充现有的跨年龄分布的人脸数据集，
我们创建了一个新的大型的跨年龄的人脸数据集CAF。
我们在MORPH、CACD-VS、FG-NET3个公共数据集上进行了大量的实验，证明了本文提出方法的有效性和CAF数据集的价值。
在LFW上进行实验说明了我们的方法的泛化能力。
### 本文方法
#### OE-CNN
AIFR:age-invariant face recognition的两个主要难点在于：  
1 由年龄差异引起的类内差异，可能包括形状、纹理上的变换；     
2 由CNN网络提取的特征，有额外的不可以避免的和身份无关的特征。   
对于1中由于年龄引起的类内差异，会导致原本是同一个人被判断为不同人，这是不应该的结果。由于年龄特征，和其他用于识别的身份特征融合在了一起，
这给跨年龄识别带来了干扰。  
所以，本文提出了一种特征正交分解方法，将CNN提取的特征向量x分解为两个x-age和x-identity。利用A-softmax特性，特征都在sphere空间里  
                                    x=x-age * x-identity           
在sphere空间里，x的角度：x-identity表示每个人唯一的特征，x的赋值：x-age表示人的年龄。

OE-CNN结构[亮点是汪峰？？]  
![OE-CNN 结构](https://github.com/alfredtorres/Reading-notebook/blob/master/MyImage/OE-CNN.png)  
主要的网络结构依托于Res-Net。
#### multi-task learning
由于把特征分别为两个age-related和identity-related，所以涉及到多任务训练。   
1 age-related    
学习年龄的loss可以看作回归问题，直接用2范数就行  
![age loss](https://github.com/alfredtorres/Reading-notebook/blob/master/MyImage/OE-CNN3.png)    
2 identity-related    
剩下的age-identity loss就可以A-softmax来实现，本文作者用的是A-softmax相似的一种   
![identity loss](https://github.com/alfredtorres/Reading-notebook/blob/master/MyImage/OE-CNN4.png)

![identity loss](https://github.com/alfredtorres/Reading-notebook/blob/master/MyImage/OE-CNN2.png)
