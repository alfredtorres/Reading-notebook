# 编译TensorFlow C/C++接口
因为项目需要，想要在vs平台下接入facenet，在尝试c++调用python无果后，决定直接用tensorflow的c/c++接口。 
## 准备工作
-------2018.8.28--------  
在自己的笔记本上编译出了13w+个errors，心态要崩了 
-------2018.8.30--------  
完全按照[TensorFlow官网](https://github.com/tensorflow/tensorflow/tree/master/tensorflow/contrib/cmake)给的推荐环境进行配置 
 * Microsoft Windows 10
 * VS 2015
 * cuda 8.0
 * cudnn 5.1
 * swigwin 3.0.10
 * cmake 3.6
 * tensorflow 1.7.0
