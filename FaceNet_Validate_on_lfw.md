# FaceNet人脸识别网络的应用
由于在自身库中准确率只有83%，所以运行一下官网配的validate_on_lfw，看看结果是否满足。
## 1 准备数据
已经下载了LFW的数据集，需要用MTCNN得到更小的人脸图片，facenet训练过程用的输入图片大小是160*160，在mtcnn检测到的
boundingbox基础上，每边加上一个margin=22.   
这一步需要align the lfw dataset使用官方提供的代码
```
python src/align/align_dataset_mtcnn.py 
D:\Software\caffe\caffe-master\data\30_Labeled_Faces_in_the_Wild_Home\lfw \
D:\Software\caffe\caffe-master\data\30_Labeled_Faces_in_the_Wild_Home\lfw_facenet \
--image_size 160 \
--margin 32 \
--random_order \
--gpu_memory_fraction 0.25 
``` 
运行的时候会有一些小错误，根据相应的改改就行，主要错误是import align.错误。
这样就得到可以直接用于facenet的160*160的lfw数据。
## 2 下载模型
直接去github上给的地址下载，幸好学校可以直接下载google driver的内容，如果有需求可以发给你们。  
我下载的是最新的模型[20180402-114759](https://github.com/davidsandberg/facenet)   
有如下4个文件
```
20180402-114759.pb
model-20180402-114759.ckpt-275.data-00000-of-00001
model-20180402-114759.ckpt-275.index
model-20180402-114759.meta
```
## 3 进行测试
### 3.1 按照官方给的完美配置运行
```
python src/validate_on_lfw.py \
D:\Software\caffe\caffe-master\data\30_Labeled_Faces_in_the_Wild_Home\lfw_facenet \
src/20180402-114759 \
--distance_metric 1 \
--use_flipped_images \
--subtract_mean \
--use_fixed_image_standardization
```
得到的结果
![1](https://github.com/alfredtorres/Reading-notebook/blob/master/MyImage/facenet_result1.png)  
### 3.2 不加预处理运行
只保留用余弦距离
```
python src/validate_on_lfw.py \
D:\Software\caffe\caffe-master\data\30_Labeled_Faces_in_the_Wild_Home\lfw_facenet \
src/20180402-114759 \
--distance_metric 1 \
```
得到的结果
![2](https://github.com/alfredtorres/Reading-notebook/blob/master/MyImage/facenet_result2.png)    
不加预处理得到的val准确率是0.87，比在我自己库上进行1：N匹配的83%高了4%，所以我的问题应该还是预处理的问题。
```
--use_flipped_images \
--subtract_mean \
--use_fixed_image_standardization
```
使用flipped_image、去特征平均值、图片标准化，三个步骤很重要，但是怎么加呢？
### 3.3 只加去均值
```
python src/validate_on_lfw.py \
D:\Software\caffe\caffe-master\data\30_Labeled_Faces_in_the_Wild_Home\lfw_facenet \
src/20180402-114759 \
--distance_metric 1 \
--subtract_mean
```
得到的结果
```
............
Accuracy: 0.98833+-0.00441
Validation rate: 0.89667+-0.02494 @ FAR=0.00067
Area Under Curve (AUC): 0.999
Equal Error Rate (EER): 0.012
```
说明特征去均值是有用的啊，但是为什么我在matlab里去均值后效果不变呢？
### 3.4 只加镜像flip
```
python src/validate_on_lfw.py \
D:\Software\caffe\caffe-master\data\30_Labeled_Faces_in_the_Wild_Home\lfw_facenet \
src/20180402-114759 \
--distance_metric 1 \
--use_flipped_images
```
得到的结果
```
........................
Accuracy: 0.98733+-0.00455
Validation rate: 0.91000+-0.02832 @ FAR=0.00100
Area Under Curve (AUC): 0.999
Equal Error Rate (EER): 0.013
```
我的库只加flip可以提高2%，说明确实有用
