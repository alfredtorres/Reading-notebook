# HOG特征
## 1  HOG算子介绍
Higtogram Of Gradient Orientations方向梯度直方图特征算子是传统计算机视觉领域里用来进行物体检测的特征描述子(fearture descriptor)，HOG是SIFT特征的一种变种。  
HOG的思想是**计算**和**统计**图像局部区域的梯度方向直方图来构成特征，要注意统计的思想。Delal在CVPR 2005中提出的利用HOG和SVM进行行人检测。  
## 2 HOG计算
*HOG的计算有很多文章都说了，暂时没看HOG的计算原理，先留着坑吧。*
## 3 维度计算
OpenCV里的HOG特征算子的源码是  

    HOGDescriptor(Size _winSize, Size _blockSize, Size _blockStride, Size _cellSize, int _nbins, [])//_nbins后面还有一堆参数
  Size _winSize：表示滑动窗口的大小，cvSize(int n,int m)  
  Size _blockSize:表示block大小，cvSize()  
  Size _blockStride:表示block的移动步长  
  Size _cellSize:cell的大小  
  int _nbins：bins的大小，一般为9  
简书上有个例子   

    imageMat = imread("Desktop/640_480.png", 1);//图像大小640 * 480  
    HOGDescriptor *hog = new HOGDescriptor(cvSize(64, 48), cvSize(32, 32), cvSize(8, 8), cvSize(16, 16), 9);
    vector<float> descriptors;
    hog->compute(imageMat, descriptors, Size(64, 48), Size(0, 0));
    cout << "descriptors.size = " << descriptors.size() << endl;//输出hog特征描绘子的维度  
输出是  
    
    descriptors.size = 54000  
  
这个54000是怎么得到的呢？  
1个cell是9个维度（指定的9还是3 * 3？这个不懂）；cell_size=16 * 16,block_size=32 * 32,所以一个block包括4个cell，
也就是一个block有4 * 9=36个维度。  
窗口的大小是64 * 48，block大小是32 * 32，block步长是8 * 8，所以在一个窗口内有（（64 - 32）/ 8 + 1） * （（48 - 32）/ 8 + 1）= 15 个block，
一个窗口的维度是15 * 36 = 540。  
图片大小是640 * 480，窗口滑动步长是  compute(imageMat, descriptors, Size(64, 48), Size(0, 0))    里的第三个参数，则共由
（（640 - 64）/ 64 + 1） * （（480 - 48）/ 48 + 1）= 100 个windows，所以总的维数是 100 * 540 = 54000  

为了验证维度计算的对不对，我换了一张自己图片，大小是324 * 223，其他参数不变，按照上述计算过程，只有最终的窗口数变化
（（324 - 64）/ 64 + 1） * （（223 - 48）/ 48 + 1）= 20 个windows，共20 * 540 = 10800维度  
输出是  
    
    descriptors.size = 10800  
说明维度计算没问题。
## 4 特征可视化
按照*Computer Vision: a modern approach*  P112 fig.5.15表示，HOG特征图是可以反应图像边缘信息的，但是我得到特征图后毫无效果，不懂。  

___  
未完待续  
## 5 参考资料  
[目标检测的图像特征提取之（一）HOG特征](https://blog.csdn.net/zouxy09/article/details/7929348)  
[简书：HOG特征提取OpenCV](https://www.jianshu.com/p/dc79d3f9ac7c)  
[OpenCV，配置](https://docs.opencv.org/3.3.0/d2/dca/group__xfeatures2d__nonfree.html)
