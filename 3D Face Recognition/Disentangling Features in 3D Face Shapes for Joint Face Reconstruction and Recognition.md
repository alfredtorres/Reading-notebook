# Disentangling Features in 3D Face Shapes for Joint Face Reconstruction and Recognition
## 探究3D人脸特征在人脸重建和识别中的作用
## abstract
本文提出一种编码-解码网络，用于从单个2D图像中重建精确的3D人脸模型，从而可以同时完成精确3D人脸重建和人脸识别两个任务。    
与现有的3D人脸重建方法不同，本文提出的方法直接从单个2D图像回归密集3D人脸形状，并且基于符合3D人脸模型明确的分别处理三维人脸新装中的身份和残差部分。   
针对提出的网络，训练时利用一种联合的loss函数，同时测量face id引起的loss和3D face shape重建引起的loss。   
为了构建训练数据，本文提出一种将3D形变模型拟合成2D多视图的方法。
