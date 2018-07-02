# Ring loss: Convex Feature Normalization for Face Recognition
Ring loss: 人脸识别的凸特征归一化
## abstract
本文提出一种Ring loss：一种特征归一化方法，用于增强深度网络中的损失函数。
我们认为，深度特征的归一化对于监督学习下的分类问题很重要，因为需要模型对不同类特征表示equally。  
特征归一化的直接方法是通过硬归一化，但是会导致非凸。  
本文提出的Ring loss通过一种软归一化的方式，保留了凸特性。 
## my opinion
![fig-4](https://github.com/alfredtorres/Reading-notebook/blob/master/MyImage/ring%20loss%20fig-4.jpg)  
上图中，左边为训练样本的特征分布情况，右边为测试样本中特征分布情况。  
从cosine角度上度量，训练集集中在一定的角度范围内，但是测试集分布的比较开，幅值越小时，偏离的角度越大。  
本文就提出了一个想法，把特征值归一化，但是，不是归一化到**1**，归一化到一个学习到的值**R**。 
其他的模型中也有做归一化的，但是是指定的归一化到几，本文的不同在于归一化到一个最优值。   
![fig-3](https://github.com/alfredtorres/Reading-notebook/blob/master/MyImage/ring%20loss%20fig-3.jpg)  
文中图3为不同R值，在softmax loss情况下，特征的分布情况
* 左图，R=0，即只有softmax时，是一坨点
* 中图，R=1时，比较集中
* 右图，R=20，一个环形
说明，R值不能太小，也不能太大，需要选取一个最合适的值。  
本文给出的结果是，在LFW数据集上，softmax最好的R=0.01
