# Mean-Variance Loss for Deep Age Estimation from a Face
## 人脸年龄估计的平均-方差损失
## abstract
年龄估计在视频监控、社交网络和人机交互中具有广泛的应用，但是目前的年龄估计方法将年龄估计看作回归问题，因此没有利用分布的
稳健性来表示模糊的标签。  
本文提出一种新的损失函数，mean-variance loss(平均-方差损失),利用分布学习进行准确的年龄估计。   
平均-方差损失由平均损失和方差损失两部分组成。   
平均损失：用来惩罚估计的年龄分布的平均值和真实值之间的差异；  
方差损失：用来惩罚年龄分布的方差以使部分更集中。  
将本文提出的平均-方差损失和softmax损失共同嵌入CNN网络中进行年龄估计。
## 本文亮点
![fig-1](https://github.com/alfredtorres/Reading-notebook/blob/master/MyImage/Mean-Variance%20loss%20for%20deep%20age%20eatimation%20fig-1.jpg)    
上图为使用平均-方差损失前后的效果，可以看出，平均损失使得估计的分布平均值与真实值相等，方差损失使得估计的分布方差变小。  
总体来说，针对年龄估计**分布**情况进行改进。  
![fig-2](https://github.com/alfredtorres/Reading-notebook/blob/master/MyImage/Mean-Variance%20loss%20for%20deep%20age%20eatimation%20fig-2.jpg)     
系统的流程图分布以上几个部分：图片输入、CNN提取特征、分类器输出年龄分布的概率、3种loss对网络进行优化。 
