# HOG特征
## 1
## 2 opencv source code
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
    hog->compute(imageMat, descriptors, Size(2, 2), Size(0, 0));
    cout << "descriptors.size = " << descriptors.size() << endl;//输出hog特征描绘子的维度
输出是  
    
    descriptors.size = 54000
