# CNN1 - 经典卷积神经网络AlexNet
### 引言
AlexNet由Hinton的学生Alex在2012年的imagenet比赛中提出，获得了当年的imagenet的冠军，top-5的错误率为16.4%，比第二名的26.2%领先10%。
同时，alexnet的参数量不到第二名的1/2，充分说明了卷积神经网络在图像识别、计算机视觉领域的强大，自2012年开始，CNN开始席卷计算机视觉领域。  
AlexNet论文[ImageNet Classification with Deep Convolutional Neural Networks](http://xanadu.cs.sjsu.edu/~drtylin/classes/cs267_old/ImageNet%20DNN%20NIPS2012(2).pdf)
### AlexNet
#### 特点
对于AlexNet这篇文章的解读已经很多了，我就不详细写了，写了也没别人好。  
简单概况一下文章提出的几个break through：
1. 提出用Relu激活函数，代替之前的sigmoid，计算速度快，在深度卷积网络里优势大；
2. 提出LRN层，在神经元层面上创建了一种竞争机制，使得模型的泛化能力更强；
3. Dropout技术，加快训练速度，避免过拟合
4. 数据增强，data augmentation，也是避免过拟合，数据量越大，模型的泛化能力越好
#### 网络结构
![AlexNet](https://github.com/alfredtorres/Reading-notebook/blob/master/MyImage/AlexNet.png)    
    <table border="0.5" align="center">
        <tr>
            <th>layer name</th>
            <th>output size</th>
            <th>details</th>
        </tr>
        <tr>
            <th>input</th>
            <th>227x227x3</th>
            <th>-</th>
        </tr>
        <tr>
            <th>conv1</th>
            <th>55x55x96</th>
            <th>kernel_size:11x11,  
                filtes:96,  
                strides=4,  
                paddings=0</th>
        </tr>
        <tr>
            <th>maxpool1</th>
            <th>27x27x96</th>
            <th>kernel_size:3x3,  
                strides=2</th>
        </tr>
        <tr>
            <th>conv2</th>
            <th>27x27x256</th>
            <th>kernel_size:5x5,  
                filtes:256,  
                strides=1,  
                paddings=2</th>
        </tr>
        <tr>
            <th>maxpool2</th>
            <th>13x13x256</th>
            <th>kernel_size:3x3,  
                strides=2</th>
        </tr>
        <tr>
            <th>conv3</th>
            <th>13x13x384</th>
            <th>kernel_size:3x3,  
                filtes:384,  
                strides=1,  
                paddings=1</th>
        </tr>
        <tr>
            <th>conv4</th>
            <th>13x13x384</th>
            <th>kernel_size:3x3,  
                filtes:384,  
                strides=1,  
                paddings=1</th>
        </tr>
        <tr>
            <th>conv5</th>
            <th>13x13x256</th>
            <th>kernel_size:3x3,  
                filtes:256,  
                strides=1,  
                paddings=1</th>
        </tr>
        <tr>
            <th>maxpool3</th>
            <th>6x6x256</th>
            <th>kernel_size:3x3,  
                strides=2</th>
        </tr>
        <tr>
            <th>fc1</th>
            <th>4096</th>
            <th>-</th>
        </tr>
        <tr>
            <th>fc2</th>
            <th>4096</th>
            <th>-</th>
        </tr>
        <tr>
            <th>classifier</th>
            <th>1000</th>
            <th>-</th>
        </tr>
    </table>
### AlexNet在Tensorflow里的实现
#### MNIST数据集
```
import tensorflow as tf
#tf.enable_eager_execution()
import numpy as np
from tensorflow.examples.tutorials.mnist import input_data

file = "D:/dataset/MNIST"
# 读取MNIST数据集
class DataLoader():
    def __init__(self):
         # mnist = tf.contrib.learn.datasets.load_dataset("mnist")
        mnist = input_data.read_data_sets(file)
        self.train_data = mnist.train.images    # np.array[55000,784]
        self.train_label = np.asarray(mnist.train.labels, dtype=np.int32)   # # np.array[55000]
        self.eval_data = mnist.test.images      # np.array[10000,784]
        self.eval_label = np.asarray(mnist.test.labels, dtype=np.int32)   # # np.array[10000]
        
    def get_batch(self, batch_size):
        index = np.random.randint(0, np.shape(self.train_data)[0], batch_size)
        return self.train_data[index, :], self.train_label[index]
    
    def get_eval_batch(self, test_step, batch_size):
        index = np.arange(batch_size) + test_step * batch_size
        return self.eval_data[index, :], self.eval_label[index]
 # 定义CNN
 ## conv1 pool1 conv2 pool2 flat dense1 dense2
class AlexNet(tf.keras.Model):
    def __init__(self):
        super().__init__()
        self.conv1 = tf.keras.layers.Conv2D(
                filters=64,
                kernel_size=[3,3],
                padding="same",
                activation=tf.nn.relu)
        self.pool1 = tf.keras.layers.MaxPool2D(pool_size=[2,2], strides=2)
        self.conv2 = tf.keras.layers.Conv2D(
                filters=64,
                kernel_size=[3,3],
                padding="same",
                activation=tf.nn.relu)
        self.pool2 = tf.keras.layers.MaxPool2D(pool_size=[2,2], strides=2)
        self.conv3 = tf.keras.layers.Conv2D(
                filters=128,
                kernel_size=[3,3],
                padding="same",
                activation=tf.nn.relu)
        self.conv4 = tf.keras.layers.Conv2D(
                filters=128,
                kernel_size=[3,3],
                padding="same",
                activation=tf.nn.relu)
        self.conv5 = tf.keras.layers.Conv2D(
                filters=256,
                kernel_size=[3,3],
                padding="same",
                activation=tf.nn.relu)
        self.pool3 = tf.keras.layers.MaxPool2D(pool_size=[3,3], strides=2)
        self.flatten = tf.keras.layers.Reshape(target_shape=(3*3*256,))
        self.dense1 = tf.keras.layers.Dense(units=1024, activation=tf.nn.relu)
        self.dense2 = tf.keras.layers.Dense(units=10)
        
    def call(self, inputs):
        input = tf.reshape(inputs, [-1, 28, 28, 1])
        x = self.conv1(input)
        x = self.pool1(x)
        x = self.conv2(x)
        x = self.pool2(x)
        x = self.conv3(x)
        x = self.conv4(x)
        x = self.conv5(x)
        x = self.pool3(x)
        x = self.flatten(x)
        x = self.dense1(x)
        x = self.dense2(x)
        return x
    
    def predict(self, inputs):
        logits = self(inputs)
        return tf.argmax(logits, axis=-1)

 
# hyperparameters
num_batches = 10000
batch_size = 128
learing_rate = 0.001
data_loader = DataLoader()
mode = 'test'
# 训练阶段
def train():   
    # 实例化模型，数据读取类，优化器
    model = AlexNet()    
    optimizer = tf.train.AdamOptimizer(learning_rate=learing_rate)
    checkpoint = tf.train.Checkpoint(myAwesomeModel=model)
    # start train
    # sess = tf.InteractiveSession()
    #summary_writer = tf.contrib.summary.create_file_writer('./tensorboard')
    #with summary_writer.as_default(), tf.contrib.summary.always_record_summaries():   
    for batch_index in range(num_batches):
        X, y = data_loader.get_batch(batch_size)
        with tf.GradientTape() as tape:
            y_logit_pred = model(tf.convert_to_tensor(X))
            # y_logit_pred = model(X)
            loss = tf.losses.sparse_softmax_cross_entropy(labels=y, logits=y_logit_pred)
            # tf.contrib.summary.scalar("loss", loss, step=batch_index)
            print('batch %d: loss %f'%(batch_index, loss.numpy()))
        grads = tape.gradient(loss, model.variables)
        optimizer.apply_gradients(grads_and_vars=zip(grads, model.variables))
        if (batch_index + 1) % 10 ==0:
            checkpoint.save('./save_alexnetmnist/model.ckpt')
   
# eval
def test():
    model_to_be_resored = AlexNet()
    checkpoint = tf.train.Checkpoint(myAwesomeModel=model_to_be_resored)
    checkpoint.restore(tf.train.latest_checkpoint('./save_alexnetmnist'))
    acc = 0
    num_eval_samples = np.shape(data_loader.eval_label)[0]
    batch_size = 101
    test_step = num_eval_samples / batch_size
    step_left = num_eval_samples % batch_size
    # y_pred = np.zeros([num_eval_samples])
    for i in range(np.int(test_step)):
        X, y = data_loader.get_eval_batch(i, batch_size)
        y_pred = model_to_be_resored.predict(X).numpy()
        acc = acc + (y_pred == y).sum()
    if step_left > 0:        
        X, y = data_loader.get_eval_batch(i + 1, step_left)
        y_pred = model_to_be_resored.predict(X).numpy()
        acc = acc + (y_pred == y).sum()
    # y_pred = model.predict(data_loader.eval_data).numpy()
    print('test acc: %f'%(acc / num_eval_samples))
    ## test acc: 0.992318
    
if __name__ == '__main__':
    if mode == 'train':
        train()
    if mode == 'test':
        test()
```
#### CIFAR-10数据集
```
import tensorflow as tf
tf.enable_eager_execution()
import numpy as np

# 读取cifar10数据集
class DataLoader():
    def __init__(self):
        cifar = tf.keras.datasets.cifar10
        (train_data,train_label),(eval_data, eval_label) = cifar.load_data()
        self.train_data = train_data / 255.0
        self.eval_data = eval_data / 255.0
        self.train_label = np.asarray(train_label, dtype=np.int32)
        self.eval_label = np.asarray(eval_label, dtype=np.int32)
        
    def get_batch(self, batch_size):
        index = np.random.randint(0, np.shape(self.train_data)[0], batch_size)
        return self.train_data[index, :], self.train_label[index]
    
    def get_eval_batch(self, batch_size):
        index = np.random.randint(0, np.shape(self.eval_data)[0], batch_size)
        return self.eval_data[index, :], self.eval_label[index]
    
# 定义CNN
 ## conv1 pool1 conv2 pool2 flat dense1 dense2
class CNN(tf.keras.Model):
    def __init__(self):
        super().__init__()
        self.conv1 = tf.keras.layers.Conv2D(
                filters=64,
                kernel_size=[3,3],
                padding="same",
                activation=tf.nn.relu)
        self.pool1 = tf.keras.layers.MaxPool2D(pool_size=[2,2], strides=2)
        self.conv2 = tf.keras.layers.Conv2D(
                filters=64,
                kernel_size=[3,3],
                padding="same",
                activation=tf.nn.relu)
        self.pool2 = tf.keras.layers.MaxPool2D(pool_size=[2,2], strides=2)
        self.conv3 = tf.keras.layers.Conv2D(
                filters=128,
                kernel_size=[3,3],
                padding="same",
                activation=tf.nn.relu)
        self.conv4 = tf.keras.layers.Conv2D(
                filters=128,
                kernel_size=[3,3],
                padding="same",
                activation=tf.nn.relu)
        self.conv5 = tf.keras.layers.Conv2D(
                filters=256,
                kernel_size=[3,3],
                padding="same",
                activation=tf.nn.relu)
        self.pool3 = tf.keras.layers.MaxPool2D(pool_size=[2,2], strides=2)
        self.flatten = tf.keras.layers.Reshape(target_shape=(4*4*256,))
        self.dense1 = tf.keras.layers.Dense(units=1024, activation=tf.nn.relu)
        self.dense2 = tf.keras.layers.Dense(units=10)
        
    def call(self, inputs):
        # input = tf.reshape(inputs, [-1, 32, 32, 3])
        x = self.conv1(inputs)
        x = self.pool1(x)
        x = self.conv2(x)
        x = self.pool2(x)
        x = self.conv3(x)
        x = self.conv4(x)
        x = self.conv5(x)
        x = self.pool3(x)
        x = self.flatten(x)
        x = self.dense1(x)
        x = self.dense2(x)
        return x
    
    def predict(self, inputs):
        logits = self(inputs)
        return tf.argmax(logits, axis=-1)

 
# hyperparameters
num_batches = 10
batch_size = 128
learing_rate = 0.001
# 实例化模型，数据读取类，优化器
model = CNN()
data_loader = DataLoader()
optimizer = tf.train.AdamOptimizer(learning_rate=learing_rate)
# start train
# sess = tf.InteractiveSession()
#summary_writer = tf.contrib.summary.create_file_writer('./tensorboard')
#with summary_writer.as_default(), tf.contrib.summary.always_record_summaries():   
for batch_index in range(num_batches):
    X, y = data_loader.get_batch(batch_size)
    with tf.GradientTape() as tape:
        y_logit_pred = model(tf.convert_to_tensor(X))
        loss = tf.losses.sparse_softmax_cross_entropy(labels=y, logits=y_logit_pred)
        # tf.contrib.summary.scalar("loss", loss, step=batch_index)
        if batch_index % 50 == 0:            
            print('batch %d: loss %f'%(batch_index, loss.numpy()))
    grads = tape.gradient(loss, model.variables)
    optimizer.apply_gradients(grads_and_vars=zip(grads, model.variables))
        
   
# eval

num_eval_samples = np.shape(data_loader.eval_label)[0]
acc = 0
test_nums = 80
# y_pred = np.zeros([num_eval_samples])
for i in range(test_nums):
    X, y = data_loader.get_eval_batch(batch_size)
    y = np.reshape(y, [batch_size,])
    y_pred = model.predict(X).numpy()
    acc = acc + (y_pred == y).sum()
# y_pred = model.predict(data_loader.eval_data).numpy()
print('test acc: %f'%(acc / (test_nums * batch_size)))
## test acc: 0.689000   num_batches = 5000  batch_size = 50
## test acc: 0.746777   num_batches = 10000  batch_size = 128
```
