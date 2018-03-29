# DeepFace(CVPR 2014, FAIR)
[DeepFace：Closing the Gap to Human-Level Performance in Face Verification](http://xueshu.baidu.com/s?wd=paperuri%3A%284f6ebc430416b52c9d52b5bad9b87083%29&filter=sc_long_sign&tn=SE_xueshusource_2kduw22v&sc_vurl=http%3A%2F%2Fieeexplore.ieee.org%2Fxpls%2Ficp.jsp%3Farnumber%3D6909616&ie=utf-8&sc_us=8790645633203158551)  
DeepFace是一个人脸验证系统(face verification)。传统的人脸识别技术由四个部分组成：**detect-align-represent-classify**.
这篇文章主要针对**align**和**represent**两个环节进行改进。  
align:利用3D模型的彷射变换进行人脸校准  
represent：利用一个9层的CNN提取人脸表征，9层的CNN参数量为120m。与标准的CNN不同的是，其中有几个不进行权值共享的本地连接层。用于训练的数据集为4000个人的4M张图片。  
效果：在LFW数据集上的准确率是97.35%。
## Alignment校准

## Representation特征提取  
  本文提出用于人脸分类的DNN结构如图所示  
  ![DNN结构](https://github.com/alfredtorres/Reading-notebook/blob/master/MyImage/deepface_fig2.png)
## Verification Metric验证度量

## Experiment实验
