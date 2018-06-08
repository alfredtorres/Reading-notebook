# MTCNN:Joint Face Detection and Alignment using Multi-task Cascaded Convolutional Networks  
# 利用多任务级联CNN联合实现脸部识别和脸部校准

## MTCNN的亮点在于：将face detection和face alignment两个任务一起实现，本片文章中的face alignmen是指人脸关键点检测，和alignment还是有点不同的。

### 摘要  
在非受限制环境下，因为不同的姿势、光照和遮挡等因素影响，脸部检测和校准具有一定的挑战性。最近的一些研究表明，利用深度学习方法这两个任务可以取得显著的效果。
本文在研究这两个任务内在联系的前提下，提出一种深度级联的多任务框架提升效果。在我们的框架中包括3个CNN网络，利用coarse-to-fine的方式预测脸部和关键点位置。
此外，在学习阶段，提出了一种在线的困难采样最小化策略而不是人为选择。本方法在FDDB和WIDER FACE人脸检测数据集上取得了不错的结果。在AFLW人脸校准数据集上也
取得了不错的结果，并且保持了实时性。
### introduct
本文提出了一种新的用联合级联CNN结构将face detection和face alignment两个任务综合实现。
级联CNN结构包括三个步骤：  
stage 1：通过一个shallow CNN产生候选框；  
stage 2：用一个稍复杂的CNN来去除大部分无人脸的背景区域；  
stage 3：用一个更有力的CNN细调结果，输出人脸特征点位置。  
### Approach
#### Overall Framework
![pipeline figure](https://github.com/alfredtorres/Reading-notebook/blob/master/MyImage/MTCNN_fig1.jpg)  

首先，对图片进行尺度缩放，建立图像金字塔。  
* Stage1：建立一个全连接FCN，叫P-Net(Proposal Network)，获取候选窗口和bonding box回归向量，参考的是[Multi-view Face Detection Using Deep Convolutional Neural Networks](https://arxiv.org/pdf/1502.02766.pdf)。然后用估计的bounding box回归向量正定候选窗口，最后用NMS来消除重叠的窗口。  
* Stage2:将stage1中得到候选窗口送到下一个R-Net(Refined Network)中,进一步的去除错误的无人脸的候选窗口，还是利用NMS和bounding box regression.  
* Stage3:这一部分和上一部差不多，但是这个阶段要输出人脸边框和关键点。
