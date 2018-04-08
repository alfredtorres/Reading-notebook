# 利用caffe复现DeepID
2014 CVPR论文《Deep Learning Face Representation from Predicting 10,000 Classes》
## 1 DeepID网络结构
论文中给出的网络结构为  
![DeepID structure in paper](https://github.com/alfredtorres/Reading-notebook/blob/master/DeepID/DeepId.png)  
caffe中显示  
![CNN in caffe](https://github.com/alfredtorres/Reading-notebook/blob/master/DeepID/deepId_train_test.png)  
网络配置文件[.prototxt](https://github.com/alfredtorres/Reading-notebook/blob/master/DeepID/deepId_train_test.prototxt)  
有一个在网上看到的注意点：fc160维之后不接ReLU,个人在这里吃了亏，因为拿fc160做特征时，用了ReLU就将负数信息删除了，而存在于这一层的负数特征可能对分类有帮助。  
## 2 训练数据
训练数据用的是*CASIA-WebFace*，我只下到了*CASIA-WebFace-cut144-simi1*共由5954个人，每个人的图片从几张到几百张不等。我用了网上一个推荐的选取训练数据的方法[prepare_deepID_data.py](https://github.com/alfredtorres/Reading-notebook/blob/master/DeepID/prepare_deepId_data.py)一共有974个类，每个类50张照片用来训练，剩下的用来test。
**没有进行人脸对齐**，仅仅把图片里的人进行了crop，输入的大小统一为55 * 55。  
利用[create_lmdb.sh](https://github.com/alfredtorres/Reading-notebook/blob/master/DeepID/create_deepId_data_lmdb.sh)生成训练用的lmdb文件夹，分别为train和val文件夹。

## 3 训练结果
分类训练过程中的loss曲线如下：  
![train loss iters](https://github.com/alfredtorres/Reading-notebook/blob/master/DeepID/train-loss-iters.png)  
分类训练过程中acc曲线如下:  

![test acc iters](https://github.com/alfredtorres/Reading-notebook/blob/master/DeepID/test-acc-iters.png)  

利用caffe里的tools工具和log文件直接画图时的一个坑为：需要先用parse_log.sh对.log进行解析，里面有个aux.txt文件不行，因为win10系统把aux当作是系统关键字不能创建，所以用换个其他名字就能解析了。

## 4 测试结果
在lfw数据集上，进行验证，使用cosine距离的roc曲线如下：  
![roc lfw cosine](https://github.com/alfredtorres/Reading-notebook/blob/master/DeepID/ROC%20curve%20lfw.png)   
在画ROC曲线时，也遇到了几个小问题，因为是第一次画ROC，所以记录一下  
ROC曲线的横坐标为fpr:false positive rate,纵坐标为tpr:true positive rate.  
python中有一个可以直接画roc曲线的函数     
    
    fpr,tpr,thresholds=sklearn.metrics.roc_curve(y_label, y_scores, pos_label=NONE)  
其中，y_label表示是真实值，y_scores表示预测值，pos_label=NONE表示是当y_scores>threshold时表示的是正例，相当于这个正例是自己规定的。  
对于人脸识别中还用到了距离  

    sklearn.metrics.pairwise.pairwise_distances(featureleft, featureright, metric='cosine')   
    
metric='euclidean'表示用欧式距离，即向量在空间里的绝对距离
metric='cosine'表示用余弦距离，但是pairwise里的余弦距离使用1-cos(a)的。
## 5 结果分析
从训练的loss和acc上看结果还行，因为人脸识别强调的是提取特征，而不是强调分类结果。  
从ROC曲线上看，这个结果与目前的结果差距较大，可能的原因为：
1. 训练图像和测试图像没有进行detect alignment
2. 训练量不够
