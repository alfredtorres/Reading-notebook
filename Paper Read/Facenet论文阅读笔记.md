# Facenet: a unified embedding for face recognition and clustering
一种用于人脸识别和人脸聚类的统一特征网络
本系列分为2篇blog，由于这篇文章是2015CVPR，已经比较旧，但是作者在github上更新了facenet的结构，开源了模型。  
第一篇关注论文，第二天关注实现。
## 摘要
facenet实现从image到embddings特征的一种映射关系，把图片映射到空间上的向量，然后两站图片的距离就是两个向量的欧式距离。 
## 本文主要亮点
### 1 Triplet Loss
图片通过facenet后得到一个d维的向量表示f(x),并且对f(x)进行归一化||f||=1    
triplet loss的原理如下：  
![1](https://github.com/alfredtorres/Reading-notebook/blob/master/MyImage/facenet_fig1.jpg)
![2](https://github.com/alfredtorres/Reading-notebook/blob/master/MyImage/facenet_fig2.jpg)
![3](https://github.com/alfredtorres/Reading-notebook/blob/master/MyImage/facenet_fig3.jpg)    
相比较两个样本，triplet需要三个样本，随机一个样本a，然后挑选一个相同的正样本p，负样本n，满足ap之间的距离比an之间的距离小。    
对于triplet样本的选择，3.2节专门写了，这对于实验很重要。 
理想的情况：对于随机样本a，挑选一个hard positive：和a同类但距离最远，hard negative：和a不同类距离最近。    
triplet的思想也满足:同类之间的最远距离要小于不同类之间的最小距离。
