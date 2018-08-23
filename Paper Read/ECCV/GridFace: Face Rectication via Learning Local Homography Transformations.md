# GridFace: Face Rectification via Learning Local Homography Transformations
#### 人脸网格：通过学习局部Homography变换改进人脸
ECCV,2018
### abstract
本文提出一种减小脸部几何变形的方法，来提供识别的准确度。
本方法通过脸部改进网络学习局部Homography变换，利用局部Homography变换来改进脸部。  
为了得到canonical views，利用基于自然人脸分布的正则化处理。
rectification network和recognition network都是通过end-to-end的方法学习得到。
### 主要内容
<div align="center">
<img src="https://github.com/alfredtorres/Reading-notebook/blob/master/MyImage/gridface_fig2.jpg" width="640" height="480">  
</div>  

系统包括：**Recitification module纠正模块**、**Recognition module识别模块**
* Recitification Module：将输入图片进行纠正得到**canonical view正视图**
* Recognition Module：将纠正后的图片进行识别  
#### 文章亮点
本文的亮点在于**Recitificaiton Module**包括**Recitificaiton Netword**和**Regularization**
1. **Recitificaiton Netword**：输入图片I，得到n平方个残差矩阵H，变换矩阵H=H+单位矩阵，那么输出图片为HxI,即纠正后的图片。
2. **Regularization**正则化：

<div align="center">
<img src=https://github.com/alfredtorres/Reading-notebook/blob/master/MyImage/gridface_fig1.jpg" width="640" height="480">  
</div>  
