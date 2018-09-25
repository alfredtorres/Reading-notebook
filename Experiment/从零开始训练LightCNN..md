# 从零开始训练Light-CNN
## Light-CNN简介
Light-CNN原作官方库[Light CNN for Deep Face Recognition, in pytorch](https://github.com/AlfredXiangWu/LightCNN)和[A Light CNN for Deep Face Representation with Noisy Labels](https://github.com/AlfredXiangWu/face_verification_experiment)   
Light-CNN是作者从2015年提出的一个轻量级的人脸识别网络，最小的网络为5层，最大的为29层，不过取得的效果缺很好，在减少参数量的同时保证了一定的识别精度。   
尤其是，提出了MFM结构(max feature-map)，而不是用ReLU，从另一个角度提高了特征图有用信息的利用率。

## 数据集预处理
### 透视变换
按照论文中的要求，训练的数据集为**CASIA-WebFace**，测试集为**LFW**和**YTF**。
训练集的预处理要求：
1. 检测人脸5个关键点，左眼、右眼、鼻尖、嘴巴左、嘴巴右。
2. 两眼水平
3. 两眼中间点和嘴巴中间点的y轴距离为48
4. 两眼的y轴坐标为48
5. 图像大小crop到144x144   

论文中给的图例  
![face normalized](https://github.com/alfredtorres/Reading-notebook/blob/master/MyImage/lightCNN_preprocess.png)  
文中没有给出具体的方法，我采用了opencv中的透视变换，透视变换只需要得到4个点变换前后的左边，然后得到透视变换矩阵。   
我的步骤：
1. 用MTCNN进行人脸检测，得到5个关键点
2. 计算变换后的四个点坐标
3. 计算透视变换矩阵，进行变换  

我的预处理算法得到的结果：  
![my method](https://github.com/alfredtorres/Reading-notebook/blob/master/MyImage/lightCNN_preprocess2.png)    
取得的效果能接受。  
### 预处理代码
借用了facenet中的mtcnn部分，一共耗时9个小时。。。得到图片475440，部分检测到多人脸和未检测到人脸的被舍弃
```
# -*- coding: utf-8 -*-
"""
Created on Wed Sep 19 09:31:15 2018
Light cnn 图像预处理
第一步：mtcnn检测关键点
第二步：用眼睛和嘴巴四个关键点进行透视变换
@author: ZhangZiyu
"""

from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

from scipy import misc
import sys
import os
import tensorflow as tf
import numpy as np
import facenet
import align.detect_face
import random
from time import sleep
import cv2
import time

time_start = time.time()

output_dir = 'D:/Experiments/mtcnn_perspective/dataset_align'
input_dir = 'D:/dataset/CASIA-WebFace'
gpu_memory_fraction = 0.5


sleep(random.random())
output_dir = os.path.expanduser(output_dir)
if not os.path.exists(output_dir):
    os.makedirs(output_dir)
# Store some git revision info in a text file in the log directory
src_path,_ = os.path.split(os.path.realpath(__file__))
facenet.store_revision_info(src_path, output_dir, ' '.join(sys.argv))
dataset = facenet.get_dataset(input_dir)

print('Creating networks and loading parameters')

with tf.Graph().as_default():
    gpu_options = tf.GPUOptions(per_process_gpu_memory_fraction=gpu_memory_fraction)
    sess = tf.Session(config=tf.ConfigProto(gpu_options=gpu_options, log_device_placement=False))
    with sess.as_default():
        pnet, rnet, onet = align.detect_face.create_mtcnn(sess, None)

minsize = 20 # minimum size of face
threshold = [ 0.6, 0.7, 0.7 ]  # three steps's threshold
factor = 0.709 # scale factor

# Add a random key to the filename to allow alignment using multiple processes
random_key = np.random.randint(0, high=99999)
bounding_boxes_filename = os.path.join(output_dir, 'bounding_boxes_%05d.txt' % random_key)

with open(bounding_boxes_filename, "w") as text_file:
    nrof_images_total = 0
    nrof_successfully_aligned = 0
    for cls in dataset:
        output_class_dir = os.path.join(output_dir, cls.name)
        if not os.path.exists(output_class_dir):
            os.makedirs(output_class_dir)
        for image_path in cls.image_paths:
            nrof_images_total += 1
            filename = os.path.splitext(os.path.split(image_path)[1])[0]
            output_filename = os.path.join(output_class_dir, filename+'.jpg')
            print(image_path)
            if not os.path.exists(output_filename):
                try:
                    img = misc.imread(image_path)
                except (IOError, ValueError, IndexError) as e:
                    errorMessage = '{}: {}'.format(image_path, e)
                    print(errorMessage)
                else:
                    if img.ndim<2:
                        print('Unable to align "%s"' % image_path)
                        text_file.write('%s\n' % (output_filename))
                        continue
                    if img.ndim == 2:
                        img = facenet.to_rgb(img)
                    img = img[:,:,0:3]

                    _, points = align.detect_face.detect_face(img, minsize, pnet, rnet, onet, threshold, factor)
                    if points.shape[0] == 10:
                        if points.shape[1] == 1:
                            # left eye(0,5) right eye(1,6) nose(2,7) left mouth(3,8) right mouth(4,9)
                            leye=np.array((points[0],points[5])).reshape(2,)
                            reye=np.array((points[1],points[6])).reshape(2,)
                            lmouth=np.array((points[3],points[8])).reshape(2,)
                            rmouth=np.array((points[4],points[9])).reshape(2,)
                            ## 两眼中心，嘴巴中心,距离
                            ceye = (leye+reye)/2
                            cmouth = (lmouth+rmouth)/2
                            dis_ce_cm = np.linalg.norm(ceye-cmouth)
                            ratio = 48 / dis_ce_cm
                            ## 变换后双眼和嘴巴的x坐标
                            dis_le_re = np.linalg.norm(leye-reye)
                            dis_lm_rm = np.linalg.norm(lmouth-rmouth)
                            l_eye = np.array((144 /2 - dis_le_re * ratio / 2 , 48)).reshape(2,)
                            r_eye = np.array((144 /2 + dis_le_re * ratio / 2 , 48)).reshape(2,)
                            l_mouth = np.array((144 /2 - dis_lm_rm * ratio / 2 , 48*2)).reshape(2,)
                            r_mouth = np.array((144 /2 + dis_lm_rm * ratio / 2 , 48*2)).reshape(2,)
                            ## 透视变换，获取变换矩阵
                            src = np.array((leye, reye, lmouth, rmouth))
                            dist = np.array((l_eye, r_eye, l_mouth, r_mouth), dtype=np.float32)
                            warpMatrix = cv2.getPerspectiveTransform(src, dist)
                            img_align = cv2.warpPerspective(img, warpMatrix, (144, 144))
                            misc.imsave(output_filename, img_align)
                            print('save' + output_filename)
                            print('time cost:',time.time() - time_start)
print('done')
print('time cost:',time.time() - time_start)                                                                                
```
### 制作数据集
之所以把这个写出来，是因为我遇到了一个大坑，原本可以很轻松的。。。   
**切记，图片分类编码从0开始**类似这样的
```
0000045\001.jpg    0
0000045\003.jpg    0
0000045\004.jpg    0
0000045\005.jpg    0
0000045\006.jpg    0
0000045\007.jpg    0
0000045\008.jpg    0
0000045\009.jpg    0
0000045\010.jpg    0
0000045\011.jpg    0
0000045\012.jpg    0
0000045\013.jpg    0
0000045\014.jpg    0
0000045\015.jpg    0
0000099\001.jpg    1
0000099\003.jpg    1
0000099\004.jpg    1
      ……
```
## Light-CNN9网络结构
![Light-CNN 9layers](https://github.com/alfredtorres/Reading-notebook/blob/master/MyImage/lightCNN_9.png)  
Pytorch代码,借鉴[原作](https://github.com/AlfredXiangWu/face_verification_experiment)   
第一个9层模型完全按照最早的2015年的论文《Learning Robust Deep Face Representation》和原作在2018 TIFS上发的没有引入Inception模块
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
