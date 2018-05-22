# Joint Training of Cascaded CNN for Face Detection
## 摘要
级联CNN因为低计算量的分类器可以在保持召回率的同时过滤大部分的背景，而被广泛应用在人脸检测中。
级联结构随着Viloa-Jones框架开始在检测任务中流行，之后在其他问题上应用，比如DPM和CNN。
但是，在目前的认知中，之前的检测方法中都是使用贪婪的方式，即在训练一个新阶段时，之前的阶段会被固定。
所以，对CNN的训练而言，每个CNN的调优是孤立的。
本文提出了一种联合的训练方式，来获得级联结构中端对端的最优解。CNN中使用的BP算法可以直接用于级联CNN结构。
本文呈现了如何联合的训练一个naive CNN cascade、更复杂的RPN和 fast R-CNN。
