# 基于VGG face模型进行face verification
## 导言  
利用已经训练好的VGG face网络模型提取图像特征，然后计算两个图像之间的余弦相似度，判断是否为同一个人。  
## 重要的在于数据处理过程
VGG小组提供的VGG face模型，就当作是已经训练好的，在论文中也提到了用的训练数据和时间完全超过了我目前能训练的水平，所以我就不自己训练一个模型。一句话，
直接用它的模型，用来提取人脸特征。  
直接用LFW View1里的pairsDevTrain.txt来测试，但是lfw数据有多种，有最原始的lfw数据，lfw-funneled数据，或者自己将lfw数据进行detect、align、crop。  
直接用lfw数据进行测试的结果未记录，大概在89%左右  
用lfw-funneled数据得到的结果是91.09%，threshold=0.73，auc=0.9702  
### faceTools
利用faceTools进行检测对齐，能得到三个数据包detect、align、crop，但是这里有个问题，不是所有的lfw图片经过faceTools都能检测到，有一部分图片检测不到，
或者align失败，对于这些我用的是原始图片代替，相当于不做任何处理。  
用align数据进行测试，结果为95.68%，threshold=0.739，auc=0.9896(cosine)  
用crop数据进行测试，结果为75.18%，threshold=0.571，auc=0.8206(cosine)
### MTCNN
MTCNN是目前用来进行人脸检测和对齐最好的预处理算法，已经有开源的模块，但是仍未会使用，下一步的实验计划就是利用MTCNN对lfw数据进行人脸检测和对齐。  

## 实验结果讨论
vgg那篇论文里说用的是L2距离，但是我用L2距离测试的结果是80.32%，thershold=0.425，auc=0.8835(L2)
