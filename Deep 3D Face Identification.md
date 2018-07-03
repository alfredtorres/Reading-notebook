# Deep 3D Face Identification
## abstract
本文提出一种利用深度CNN的3D人脸识别算法和一种3D增强技术。2D人脸识别技术由于深度学习和大规模数据集的发展得到了巨大的进步，3D人脸识别由于缺少大规模的3D
人脸模型数据，仍旧是一个难点。 
本文利用迁移学习从2D人脸到3D人脸识别，利用相对较小的3D人脸数据集fine tuing2D CNN模型。并且，本文提出一种3D人脸增强技术，用来生成不同面部表情的图像。
## 
![overview](https://github.com/alfredtorres/Reading-notebook/blob/master/MyImage/Deep%203D%20Face%20Recognition_fig-2.jpg)  
本文提出的3D人脸识别系统的流程。    
在训练阶段，将输入的3D点云通过利用增强技术和预处理生成丰富的3D点云，然后提出2D深度图像，送入VGG，后面的就和2D识别差不多了。    
在测试阶段，将输入的3D点云模型生成2D深度图，利用VGG提取特征，特征归一化，PCA降维，形成最终的人脸特征图。
