# MTCNN:Joint Face Detection and Alignment using Multi-task Cascaded Convolutional Networks  
# 利用多任务级联CNN联合实现脸部识别和脸部校准

## MTCNN的亮点在于：将face detection和face alignment两个任务一起实现，本片文章中的face alignmen是指人脸关键点检测，和alignment还是有点不同的。

### 摘要  
在非受限制环境下，因为不同的姿势、光照和遮挡等因素影响，脸部检测和校准具有一定的挑战性。最近的一些研究表明，利用深度学习方法这两个任务可以取得显著的效果。
本文在研究这两个任务内在联系的前提下，提出一种深度级联的多任务框架提升效果。在我们的框架中包括3个CNN网络，利用coarse-to-fine的方式预测脸部和关键点位置。
此外，在学习阶段，提出了一种在线的困难采样最小化策略而不是人为选择。本方法在FDDB和WIDER FACE人脸检测数据集上取得了不错的结果。在AFLW人脸校准数据集上也
取得了不错的结果，并且保持了实时性。
