# Exploring Disentangled Feature Representation Beyond Face Identification
超越人脸识别的特征表示研究
## abstract
本文旨在在最少的监督的前提下，学习*disentangled but complementary*(解开但互补的特征)人脸特征来完成人脸识别。
提出一种特征提取(distill)和分散(dispell)的自动编码框架，对抗地学习用于人脸识别的身份特征提取和用于误导人脸识别系统的身份特征分散。
由于设计了两条特征流路线，学习到的有用特征不仅可以表示身份或者属性，而且可以用来表示输入图片的全部信息。
进一步的研究表明，提取的特征不仅在人脸识别上取得了目前一流水平(在LFW数据集上)，而且对于人脸属性识别也有非常竞争力的表现(在celebA和LFWA)。
此外，本文提出的系统可以在语义上控制脸部延伸和编辑
## experiment
作者从face identification、Face Attribute Recognition、Face Editing三个方面对提出的模型进行了验证。说明本文模型的三个应用方向，face editing是个不错的方向，用对抗网络可以编辑生成自己想要的图片。
## my opine
![the distilling and dispelling autoencoder model](https://github.com/alfredtorres/Reading-notebook/blob/master/MyImage/exploring%20disentangled%20feature%20repren-fig2.jpg)   
文中提出了两种特征：与**id信息有关**的特征fT，与**id信息无关**的特征fP.  
实验部分中有一个我感兴趣的部分：**face attribute recognition**  
作者在CelebA和LFWA两个数据集上进行了验证，每个图片包括40个属性标签。**由于模型训练的时候没有使用属性作为监督信号，所以作者
提取了图片的特征fc(fc应该是ft和fp的联合）然后训练了一个SVM进行测试**   
说明这个作者用的也是SVM，那么我用SVM去进行glass detect应该是没错的。   
作者在附录中补充说了一点，D2AE-T特征在与ID相关的属性上表现的好，而D2AE-P特征在与ID无关的属性上表型的好。但是没有具体说那些是和ID相关的属性，哪些是和ID无关的属性呢？
