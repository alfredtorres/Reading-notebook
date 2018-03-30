上一篇论文DeepFace的提出的Verification Metric两种方法，X2距离和Siamese Network。  
Caffe里正巧有对Siamese网络的教程，数据是mnist数据集。就照着caffe里的Siamese 做了一遍，记录一下遇到的问题和结果。
# Siamese Network Training with Caffe
## 1 数据准备
数据用的还是mnist数据集，和LeNet的数据集是同一个。但是处理的方法是不一样，我一开始以为可以用LeNet的数据
**create_minist_siamese.h**   

    EXAMPLES=D:/Software/caffe/caffe-master/Build/x64/Release
    DATA=D:/Software/caffe/caffe-master/data/mnist
    echo "Creating leveldb..."
    rm -rf D:/Software/caffe/caffe-master/examples/mysiamese/mnist_siamese_train_leveldb
    rm -rf D:/Software/caffe/caffe-master/examples/mysiamese/mnist_siamese_test_leveldb
    $EXAMPLES/convert_mnist_siamese_data.exe \
        $DATA/train-images.idx3-ubyte \
        $DATA/train-labels.idx1-ubyte \
        D:/Software/caffe/caffe-master/examples/mysiamese/mnist_siamese_train_leveldb
    $EXAMPLES/convert_mnist_siamese_data.exe \
        $DATA/t10k-images.idx3-ubyte \
        $DATA/t10k-labels.idx1-ubyte \
        D:/Software/caffe/caffe-master/examples/mysiamese/mnist_siamese_test_leveldb  
     echo "Done."  
    
这和caffe/examples/siamese里的.sh文件有几点不同需要注意*convert_mnist_siamese_data.exe*不是*convert_mnist_siamese_data.bin*。数据文件格式中是.不是-。  
然后得到两个文件夹：*mnist_siamese_train_leveldb*和*mnist_siamese_test_leveldb*  
![test_fig](https://github.com/alfredtorres/Reading-notebook/blob/master/MyImage/Siamese_fig1.png)  
数据准备over，这个按照caffe教程走没什么问题。  
## 2 Siamese网络模型
*Siamese网络的模型caffe中都有，有几点需要注意的，但是不是自己写的，也就多说了。等研究Siamese的时候再分析*
网络模型：**mnist_siamese.prototxt**，**mnist_siamese_train_test.prototxt**  
求解器：**mnist_siamese_solver.prototxt**  
train：**train_mnist_siamese.sh**  
运行sh train_mnist_siamese.sh 后迭代50000次即可结束。
## 3 Plotting the results
可视化结果，  draw_net.sh和    mnist_siamese.ipynb  
这里都是问题，设计到其中的draw.py
需要  
pip install pydot
pip install graphviz  
下载graphviz安装（graphviz-2.38.msi），并添加环境变量
安装pygraphviz的时候，pip install pygraphviz --install-option="--include-path=D:\Software\graphviz\include" --install-option="--library-path==D:\Software\graphviz\lib\release\lib"  
然后下载 pygraphviz‑1.3.1‑cp27‑none‑win_amd64.whl  
pip install  pygraphviz‑1.3.1‑cp27‑none‑win_amd64.whl 
全搞完重新启动电脑。
**Draw_Net.sh**  

    TOOLS=D:/Software/caffe/caffe-master/Build/x64/Release/pycaffe
    EXAMPLES=D:/Software/caffe/caffe-master/examples/mysiamese
    $TOOLS/draw_net.py \
        D:/Software/caffe/caffe-master/examples/mysiamese/mnist_siamese.prototxt \
        D:/Software/caffe/caffe-master/examples/mysiamese/mnist_siamese.png
    $TOOLS/draw_net.py \
        D:/Software/caffe/caffe-master/examples/mysiamese/mnist_siamese_train_test.prototxt \
        D:/Software/caffe/caffe-master/examples/mysiamese/mnist_siamese_train_test.png  
    
得到两张图![Siamese Network](https://github.com/alfredtorres/Reading-notebook/blob/master/MyImage/mnist_siamese.png)  
SiameseNetwork网络图  
![Siamese Network_Train_Test](https://github.com/alfredtorres/Reading-notebook/blob/master/MyImage/mnist_siamese_train_test.png)  
Train Test网络图  
![Visualize the learned Siamese embedding](https://github.com/alfredtorres/Reading-notebook/blob/master/MyImage/Visualize%20the%20learned%20Siamese%20embedding.png)  
最终的Siamese网络的可视化图  
# 参考资料
[pygraphviz安装过程](https://www.cnblogs.com/AimeeKing/p/5021675.html)  
[如何在64位windows上安装pygraphviz](https://www.douban.com/note/618740837/)  
[caffe 使能python接口使用draw_net.py绘制网络结构图过程](https://blog.csdn.net/lemianli/article/details/53034432)  
[caffe中的siamese network（二）](https://blog.csdn.net/langb2014/article/details/53036758)  
[caffe中的siamese network（一）](https://blog.csdn.net/langb2014/article/details/53036216)
