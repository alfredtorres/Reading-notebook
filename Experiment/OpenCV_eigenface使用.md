# 使用OpenCV:face模块eigenface
## 使用环境：python3.5  OpenCV3.4.2带extra modules
## EigenFace

## 代码
```
# -*- coding: utf-8 -*-
"""
Created on Thu Sep  6 19:56:58 2018

@author: ZhangZiyu
"""
import cv2
import numpy as np
import sys

def norm_0_255(src):
    dst = numpy.mat()
    if src.channels() == 1:
        cv2.normalize(src, dst, 0, 255, cv2.NORM_MINMAX, cv2.CV_8UC1)
    else:
        cv2.normalize(src, dst, 0, 255, cv2.NORM_MINMAX, cv2.CV_8UC3)
    return dst

def read_images(filename):
    file = open(filename)
    lines = file.readlines()
    lib_nums = len(lines)
    file.close()
    x = np.mat(np.zeros((int(lib_nums/2),112*92)))
    labels = np.zeros([int(lib_nums/2),1],dtype='int')
    y = np.mat(np.zeros((int(lib_nums/2),112*92)))
    labels2 = np.zeros([int(lib_nums/2),1],dtype='int')
    i = 0
    j = 0
    k = 0
    for line in lines:
        path = line.strip('\n').split(';')
        # read images
        img_path = path[0]
        img = cv2.imread(img_path, cv2.IMREAD_GRAYSCALE)
        # x[i,0,:] = img[:,:]
        # x[i,1,:] = img[:,:]
        if i % 2 == 0:
            x[j,:] = np.mat(img).flatten()
            # read labels:,
            labels[j] = (int(path[1]))
            j = j + 1
        else:
            y[k,:] = np.mat(img).flatten()
            # read labels:,
            labels2[k] = (int(path[1]))
            k = k + 1
        i = i + 1
    return x, labels, y ,labels2

if __name__ == '__main__':
    filename = 'D:\dataset\ORL\orl_csv.txt'
    lib_img, lib_label, test_img, test_label = read_images(filename)
    model = cv2.face.EigenFaceRecognizer_create()
    model.train(lib_img, lib_label)
    pred_label = np.zeros([len(test_label),1],dtype='int')
    for i in range(len(test_label)):
        pred_label[i] = model.predict(test_img[i])[0]
    # print(pred_label,test_label)
    count = 0
    for i in range(len(test_label)):
        if test_label[i] == pred_label[i]:
            count = count + 1
    print('acc:',count/len(test_label))

```
**准确率：acc=0.92**
