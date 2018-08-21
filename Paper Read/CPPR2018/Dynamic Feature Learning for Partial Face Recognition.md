# Dynamic Feature Learning for Partial Face Recognition
部分人脸的动态特征学习
## abstract
This study combines Fully Convolutional Network (FCN)
with Sparse Representation Classification (SRC) to propose
a novel partial face recognition approach, called Dynamic
Feature Matching (DFM), to address partial face images re-
gardless of size. 
本文将全连接网络和稀疏表示分类相结合，提出一种新的部分人脸识别方法可以处理任意尺寸的部分人脸，叫做DFM。  
基于DFM，提出一种sliding loss来优化FCN。   
## 本文亮点
![1](https://github.com/alfredtorres/Reading-notebook/blob/master/MyImage/Dynamic%20feature%20learning%20for%20PFR%20fig-1.jpg)   
* setp 1：用FCN提取给定的特征图
* step 2：将gallery特征图按照probe特征图的尺寸进行滑动分解，得到若干个和probe特征图尺寸相同的gallery子特征图
* step 3：稀疏特征分类，将probe特征图用gallery子特征图线性表示。    
对于传统的类似VGG，facenet网络，只接收固定的图片输入，然后得到固定维度的特征向量。  
所以，对于任意尺寸的图片，不能直接送进网络。所以，将网络的的全连接层去掉，将卷积层的最后一个pool输出作为特征图feature maps。  
### 3.2 DFM
对于probe，经过FCN后得到的特征图p尺寸是w*h*d。 
对于gallery，按照probe特征图的尺寸进行滑窗分解，得到多个子特征图Gc={gc1,gc2,gc3...gck}，确保每个gc的尺寸都为w*h*d 
本文采用重构误差的方法，用Gc线性逼近p，p=Gc*wc。   
那么误差可以表示为
![2](https://github.com/alfredtorres/Reading-notebook/blob/master/MyImage/Dynamic%20feature%20learning%20for%20PFR%20fig-2.jpg)
但是，仅考虑误差是不够的，作者还提出两个约束项：
* 1 Sparse constraint稀疏约束：对wc进行L1-norm约束
* 2 Similarity-guided constrain:相似性约束，pTGcwc    
最终的约束可以表示为：![3](https://github.com/alfredtorres/Reading-notebook/blob/master/MyImage/Dynamic%20feature%20learning%20for%20PFR%20fig-3.jpg)
### 3.3 Sliding loss

### 4 实验部分
