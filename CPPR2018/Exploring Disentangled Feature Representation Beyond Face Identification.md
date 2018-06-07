# Exploring Disentangled Feature Representation Beyond Face Identification
超越人脸识别的特征表示研究
### abstract
本文旨在在最少的监督的前提下，学习*disentangled but complementary*(解开但互补的特征)人脸特征来完成人脸识别。
提出一种特征提取(distill)和分散(dispell)的自动编码框架，对抗地学习用于人脸识别的身份特征提取和用于误导人脸识别系统的身份特征分散。
由于设计了两条特征流路线，学习到的有用特征不仅可以表示身份或者属性，而且可以用来表示输入图片的全部信息。
进一步的研究表明，提取的特征不仅在人脸识别上取得了目前一流水平(在LFW数据集上)，而且对于人脸属性识别也有非常竞争力的表现(在celebA和LFWA)。
此外，本文提出的系统可以在语义上控制脸部延伸和编辑
