整理一下CVPR 2017里的论文，给出摘要然后选择有用再详细阅读  
## [Face Normals "In-The-Wild" Using Fully Convolutional Networks](http://openaccess.thecvf.com/content_cvpr_2017/html/Trigeorgis_Face_Normals_In-The-Wild_CVPR_2017_paper.html)
In this work we pursue a data-driven approach to the problem of estimating surface normals from a single intensity image, 
focusing in particular on human faces. We introduce new methods to exploit the currently available facial databases for
dataset construction and tailor a deep convolutional neural network to the task of estimating facial surface normals `in-the-wild'. 
We train a fully convolutional network that can accurately recover facial normals from images including a challenging variety of 
expressions and facial poses. We compare against state-of-the-art face Shape-from-Shading and 3D reconstruction techniques and 
show that the proposed network can recover substantially more accurate and realistic normals. 
Furthermore, in contrast to other existing face-specific surface recovery methods, we do not require the solving of 
an explicit alignment step due to the fully convolutional nature of our network.  
针对从单一强度图像估计表面标准模型(estimating surface normals from a single intensity image)问题，提出一种数据驱动方法。
训练了一个FCN可以从具有表情、姿态的人脸图片中恢复出面部标准模型，与现在有的face Shape-from-Shading and 3D重构技术对比，证明本文提出的方法能更精确。
与现有的face-specific surface recovery方法对比，由于FCN的特点不需要alignment步骤。
