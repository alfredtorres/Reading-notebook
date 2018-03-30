上一篇论文DeepFace的提出的Verification Metric两种方法，X2距离和Siamese Network。  
Caffe里正巧有对Siamese网络的教程，数据是mnist数据集。就照着caffe里的Siamese 做了一遍，记录一下遇到的问题和结果。
# Siamese Network Training with Caffe
## 1 数据准备
数据用的还是mnist数据集，和LuNet的数据集是同一个。但是处理的方法是不一样，我一开始以为可以用LeNet的数据
** create_minist_siamese.h  **
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
