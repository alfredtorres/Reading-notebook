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
  这个DNN用来分类，输入是经过3D人脸校准的RGB图像，输入输出、神经网络参数都可以在论文中查到，不多叙述。  
  网络的‘F7’层用来表示人脸特征的表征矢量，然后‘F7’后接一个softmax分类器。训练的目的就是使得正确分类的概率最大，利用最小化cross-entropy loss来实现。
  网络中使用了ReLU来使网络最大程度的非线性化，在第一个全连接层后加入dropout技术，使网络表示的稀疏性更强。  
  在网络训练好后，对于输入图像*I*,利用前向网络计算得到特征表示*G(I)*
## Verification Metric验证度量
face vertification是指对于两个图片，判断其是否属于同一个人，类似于相似性判断。对于在不同数据集上训练的模型，由于其样本不是随机均匀分布，所以对其他数据的泛化能力不同。例如，LFW数据集里男性占了75%，而且大多是工作照。本文的目的是学习一种非监督的度量可以适用于不同的数据集。
### X2距离
DeepFace里的特征矢量和LBP的特征矢量有很多相似点：
1. 没有负值
2. 具有稀疏性
3. 数据都在[0,1]之间  
采用X2距离相似性![X2 distance](https://github.com/alfredtorres/Reading-notebook/blob/master/MyImage/deepface_fig.png)  
权重wi通过一个线性SVM学习。  
### Siamese Network
此外，还测试了一个端到端的度量学习方法**Siamese Network**,采用的距离公式为![Siamses distance](https://github.com/alfredtorres/Reading-notebook/blob/master/MyImage/deepface_fig3.png)，参数可以通过cross-entropy 和BP训练得到。
### 总结
在得到图像的特征矢量后，如何进行人俩验证，选择合适的距离来计算相似性，这可能是一个研究的方向。也就是**mertic learing**，需要把本文提出的两种方法都复现一下，就在之前VGG-FACE网络的基础上  
我利用vgg-face的model提取4096维特征后similarity时遇到了问题   
1.用cosine距离的话没什么问题，用样本训练得到一个最优的阈值  
2.用论文提出的X2距离时，公式的分母会出现0，然后做除法后为Nan，所以这样的X2距离怎么计算？
## Experiment实验
