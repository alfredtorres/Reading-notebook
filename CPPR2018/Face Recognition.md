CVPR2018，人脸识别论文笔记  
# CosFace: Large margin cosine loss
face recognition的中心问题包括face verificaiton和face indentifification,两者都涉及face feature discrimination特征分辨能力。
但是，传统的softmax loss没有特征分辨能力，为了解决这个问题，最近的一些研究提出了center loss, large margin
softmax loss,angular softmax loss。所有这些改进loss的方法都有一个共同的思想：maximzing inter-class variance和
minimzing intra-class variance。本文提出一种新的loss函数：large margin cosine loss(LMCL).
通过引入一个余弦margin项来进一步的增加angular空间的决策边界，我们改写softmax loss函数变成一个cosine loss by 
L2 normalizing both features and weight vectors to remove radial variations.
最终，通过归一化和cosine decision margin maximizaiton取得了预期效果。
