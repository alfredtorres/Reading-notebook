# 人脸识别API：SkyBiometry、sightengine、baidu-aip
我原本的任务是检测人脸是否戴了眼镜eyeglassed not sunglasses，发现了三个可调用的api
先说一下结果，三个都存在问题，不太符合我的要求，所以后面决定自己训练网络，但是显然没有这些大公司拥有的数据集多。
## skybiometry
这个是效果最好的，但是有个缺点是好像不能使用本地的图片，需要网络图片  
GitHub上有个python版介绍[skybiometry](https://github.com/SkyBiometry/python-face-client)    
而且，因为调用的是api，还有每日 每月 每小时的次数限制，这个倒是其次。  
不能处理本地上传的图片，和反应时间长无法接收，我把我想处理的图片上传到git，然后用url形式处理，一张图片的处理速度在2-3秒。  
## sightengine
这个的主要问题是检测的是sunglass 不是 eyeglass。。    
这个API能处理本地上传的图片，检测一张图片的速度也在2-3秒左右。  
## baidu-aip
百度的人脸识别最让人蛋疼了，，不知道是我不会用还是咋地，用了半天没能自己测。。
