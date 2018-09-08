# 编译TensorFlow C/C++接口
因为项目需要，想要在vs平台下接入facenet，在尝试c++调用python无果后，决定直接用tensorflow的c/c++接口。 
## 准备工作
-------2018.8.28--------  
在自己的笔记本上编译出了13w+个errors，心态要崩了 
-------2018.8.30--------  
**不能**完全按照[TensorFlow官网](https://github.com/tensorflow/tensorflow/tree/master/tensorflow/contrib/cmake)给的推荐环境进行配置 
 * Microsoft Windows 10
 * VS 2015(Updata3,带skd10)
 * cuda 9.0
 * cudnn 7.0
 * swigwin 3.0.12
 * cmake 3.12.1
 * tensorflow 1.7.0  
 
 ------2018.9.3-----------  
 参考了多个链接，官方给的cuda和cudnn版本编译起来未成功，现在我连系统都重装了。  
 冷静，加油。  
 ------2018.9.7---------  
 终于编出dll和lib文件了，测试能用，回来写攻略。
## 参考链接
1. [TensorFlow github](https://github.com/tensorflow/tensorflow/tree/master/tensorflow/contrib/cmake)
2. [Windows下编译TensorFlow1.3 C++ library及创建一个简单的TensorFlow C++程序](https://blog.csdn.net/jacke121/article/details/80411437)
3. [Building a static Tensorflow C++ library on Windows](https://joe-antognini.github.io/machine-learning/build-windows-tf)
4. [如何在windows环境中使用vs2015编译tensorflow v1.5](https://blog.csdn.net/h8832077/article/details/78988488)
5. [在Windows 10 下用源码编译基于GPU的tensorflow.dll](https://zhuanlan.zhihu.com/p/29029860)
6. [TensorFlow GPU版本在Windows10下的编译](https://zhuanlan.zhihu.com/p/34942873)
