# Rich feature hierarchies for accurate object detection and semantic segmentation
## 用于目标检测和语义分割的多特征层次
## abstract
基于标准PASCAL VOC数据集的目标检测算法在最近几十年里发展趋于平缓. 最好的方法是一个复杂系统的糅合，简单的将低层次的图片特征和高级的语义特征相结合。  
本文提出一种简单可扩展的检测算法，将mAP值提高了超过30%，达到了53.3%  
本文的方法主要包括2个方面：  
1. 采用高饱和的CNN网络自上而下的提出建议区域进行定位和分割；  
2. 由于具有标签的数据集稀少，利用预训练监督算法来辅助虚训练，能达到不错的加速效果。  

由于将建议的区域和CNN结合，所以本文提出的方法命名为：R-CNN。  
## R-CNN model
R-CNN模型包括3个部分：  
1. **generate category-independent region proposals** 第一步生成和物体种类无关的候选框  
2. **extract features** 第二步提取每一个候选框中的特征  
3. **linear SVMs** 第三步进行分类，输出每个候选框中的结果  
     
更多细节参考我的博客：[目标检测系列(1):R-CNN](https://blog.csdn.net/alfred_torres/article/details/82844747),代码实现部分会在github里分析。    
