# TensorFlow安装教程
由于想运行facenet的模型，安装了tensorflow，根据原作者的要求，需要tensorflow1.7.0版本(或以上)，建议和原作版本保持一致，但是不能低。
## 环境配置
Win10，64位，python3.5
## 1 tensorflow
**注意:区分gpu版和cpu版**之前装的是cpu版的，结果来跑模型就不行了，cpu也会out of system memeory。   
可以用简单的语句来测试装的是gpu版还是cpu版  
  ``` 
  import tensorflow as tf
  a = tf.constant('hello')
  Sess = tf.Session()
  Sess.run(a)
  ```
会显示你电脑上的gpu信息，就说明是gpu版。   
用conda或者pip都能安装   
`pip install tensorflow-gpu==1.7.0`   
因为太慢，我选择去[Pypi](https://pypi.org/project/tensorflow-gpu/1.7.0/)自己下载.whl文件，然后pip install。  
tensorflow安装成功的标志是可以import，然后用上面的代码检测安装的是gpu还是cpu版本。
## 2 cuda9.0
安装好tensorflow后，要安装cuda和cudnn，这两个的版本要和tensorflow对应，不然运行不了。具体的可以去tensorflow的官网看，每个版本的.md文件都有写。
我给出我的配置，tensorflow-gpu1.7，对应的
* cuda9.0[官网下载地址](https://developer.nvidia.com/cuda-90-download-archive?target_os=Windows&target_arch=x86_64&target_version=10&target_type=exelocal)，
* cudnn7.0[官网下载，要注册!](https://developer.nvidia.com/rdp/cudnn-archive),选**Download cuDNN v7.0.5 (Dec 5, 2017), for CUDA 9.0**
然后cuda9.0，一步一步安装就行了。
装完要重启后才能生效，不放心的话去系统的环境变量里看一下有没有
```
CUDA_PATH C:\Program Files\NVIDIA GPU Computing Toolkit\CUDA\v9.0
CUDA_PATH_V9_0 C:\Program Files\NVIDIA GPU Computing Toolkit\CUDA\v9.0
```
## 3 cudnn7.0
在上面链接给出的cudnn下载解压后，将cudnn三个文件分别放到cuda9.0就行。
具体的
```
cuda\bin\cudnn64_7.dll → C:\Program Files\NVIDIA GPU Computing Toolkit\CUDA\v9.0\bin
cuda\include\cudnn.h → C:\Program Files\NVIDIA GPU Computing Toolkit\CUDA\v9.0\include
cuda\lib\x64\cudnn → C:\Program Files\NVIDIA GPU Computing Toolkit\CUDA\v9.0\lib\x64
```
## 吐血
装完找个程序试试.....吐血
