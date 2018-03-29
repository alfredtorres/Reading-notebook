# HOG特征
## 1
## 2 opencv source code
    HOGDescriptor(Size _winSize, Size _blockSize, Size _blockStride, Size _cellSize, int _nbins, [])//_nbins后面还有一堆参数
  Size _winSize：表示滑动窗口的大小，cvSize(int n,int m)  
  Size _blockSize:表示block大小，cvSize()  
  Size _blockStride:表示block的移动步长  
  Size _cellSize:cell的大小  
  int _nbins：bins的大小，一般为9
