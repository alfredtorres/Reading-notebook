# 从零开始训练Light-CNN
## Light-CNN简介

## Light-CNN9网络结构
![Light-CNN 9layers](https://github.com/alfredtorres/Reading-notebook/blob/master/MyImage/lightCNN_9.png)  
Pytorch代码,借鉴[原作](https://github.com/AlfredXiangWu/face_verification_experiment)   
第一个9层模型完全按照最早的2015年的论文<Learning Robust Deep Face Representation>和原作在2018 TIFS上发的没有引入Inception模块
```
class network_simple9(nn.Module):
    def __init__(self, num_classes=10575):
        super(network_simple9, self).__init__()
        self.features = nn.Sequential(
                mfm(1, 48, 9, 1, 0),                   # 120*120*48
                nn.MaxPool2d(kernel_size=2, stride=2), # 60*60*48
                mfm(48, 96, 5, 1, 0),                  # 56*56*96
                nn.MaxPool2d(kernel_size=2, stride=2), # 28*28*96
                mfm(96, 128, 5, 1, 0),                 # 24*24*128
                nn.MaxPool2d(kernel_size=2, stride=2), # 12*12*128
                mfm(128, 192, 4, 1, 0),                # 9*9*192
                nn.MaxPool2d(kernel_size=2, stride=2, ceil_mode=True),
                )
        self.fc1 = nn.Linear(5*5*192, 256)
        self.fc2 = nn.Linear(256, num_classes)
    
    def forward(self, x):
        x = self.features(x)
        x = x.view(x.size(0), -1)
        x = self.fc1(x)
        x = F.dropout(x, training=self.training)
        out = self.fc2(x)
        return out, x
```
