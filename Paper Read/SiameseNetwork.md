# Learning a Similarity Metric Discriminatively, with Application to Face Verification（CVPR 2005）  
Yann LeCun是三作  
## 2 The general framework
在最简单的face verification任务中，先把注册过的人脸图片的特征全部计算出来，保存在X2中，然后对于一个输入图像x1，计算其特征X1，然后将min Ew(X1,X2)
和一个预先设置的阈值进行比较。  
face verification的目标是得到Ew()的权重w，对于同类的一对输入Ew()要最小，对于不同类的一对输入Ew()要最大。  
### 2.1 face verification with learned similarity metrics
衡量verification任务的两个标准：*false accepts*和*false rejects*，可以分别理解为误诊和漏诊，一个好的verification系统要同时使这两个量最小。  
本文的方法是建立一个可训练的系统，将输入的图片映射到一个低维可测量相似性的空间，对于同类输入的距离很小，而不同类输入的距离很大。
### 2.2  the energy function of the EBM
