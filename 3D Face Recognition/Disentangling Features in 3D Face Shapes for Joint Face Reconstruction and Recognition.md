# Disentangling Features in 3D Face Shapes for Joint Face Reconstruction and Recognition
## 探究3D人脸特征在人脸重建和识别中的作用
## abstract
本文提出一种编码-解码网络，用于从单个2D图像中重建精确的3D人脸模型，从而可以同时完成精确3D人脸重建和人脸识别两个任务。    
与现有的3D人脸重建方法不同，本文提出的方法直接从单个2D图像回归密集3D人脸形状，并且基于符合3D人脸模型明确的分别处理三维人脸新装中的身份和残差部分。   
针对提出的网络，训练时利用一种联合的loss函数，同时测量face id引起的loss和3D face shape重建引起的loss。   
为了构建训练数据，本文提出一种将3D形变模型拟合成2D多视图的方法。
## 
![fig-1](https://github.com/alfredtorres/Reading-notebook/blob/master/MyImage/disentangle%20features%20in%203D%20face_fig-1.jpg)    
* (a) 现有的3D建模方法，只有一个reconstruct loss
* (b) 本文提出的方法，多了一个Identification loss，引入了参差的思想
* (c) LFW中的图片例子
* (d) 应用本文方法重建的3D shapes
* (e) 用于本文方法生成的Identity shapes    
![fig-2](https://github.com/alfredtorres/Reading-notebook/blob/master/MyImage/disentangle%20features%20in%203D%20face_fig-2.jpg)  
人脸模型S=平均人脸模型S_hat+ID相关S_idshapes+残差S_res    
利用2D图形重建3D模型：
* 1、编码器，获得维数较低的和ID、残差res相关的特征
* 2、解码器，把二维特征通过MLP变成三维模型
* 3、平均模型+Id_shape+残差得到最终的3D模型
