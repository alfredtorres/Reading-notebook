# -*- coding: UTF-8 -*-
import os
from random import shuffle
import cPickle


def check_parameter(param, param_type, create_new_if_missing=False):
    assert param_type == 'file' or param_type == 'directory'
    if param_type == 'file':
        assert os.path.exists(param)
        assert os.path.isfile(param)
    else:
        if create_new_if_missing is True:
            if not os.path.exists(param):
                os.makedirs(param)
            else:
                assert os.path.isdir(param)
        else:
            assert os.path.exists(param)
            assert os.path.isdir(param)


def listdir(top_dir, type='image'):
    # type_len = len(type)
    tmp_file_lists = os.listdir(top_dir)
    file_lists = []
    if type == 'image':
        for e in tmp_file_lists:
            if e.endswith('.jpg') or e.endswith('.png') or e.endswith('.bmp'):
                file_lists.append(e)
    elif type == 'dir':
        for e in tmp_file_lists:
            if os.path.isdir(top_dir + e):
                file_lists.append(e)
    else:
        raise Exception('Unknown type in listdir')
    return file_lists


def prepare_deepId_data_eq(src_dir, tgt_dir, num_threshold=50):
    check_parameter(src_dir, 'directory')
    check_parameter(tgt_dir, 'directory', True)
    if src_dir[-1] != '/':
        src_dir += '/'
    if tgt_dir[-1] != '/':
        tgt_dir += '/'
    class_lists = listdir(src_dir, 'dir')
    print '# class is : %d' % len(class_lists)
    class_table = {}

    num = 0

    for e in class_lists:
        assert e not in class_table
        class_table[e] = listdir(''.join([src_dir, e]), 'image')
        if len(class_table[e]) > num_threshold:
            num += 1
    print 'There are %d people whose number of images is greater than %d.' % (num, num_threshold)
    print 'Use %d num people to train the deepId net..' % num
    train_set = []
    test_set = []
    label = 0
    dirname2label = {}
    for k, v in class_table.iteritems():
        if len(v) >= num_threshold:
            shuffle(v)
            assert k not in dirname2label
            dirname2label[k] = label
            i = 0
            for i in xrange(num_threshold):
                train_set.append((k + '/' + v[i], label))
            i += 1
            num_test_images = min(num_threshold / 3, len(v) - num_threshold)
            for j in xrange(num_test_images):
                test_set.append((k + '/' + v[i + j], label))
            label += 1
    f = open(tgt_dir + 'dirname2label.pkl', 'wb')
    cPickle.dump(dirname2label, f, 0)
    f.close()
    f = open(tgt_dir + 'deepId_train_lists.txt', 'w')
    for e in train_set:
        print >> f, e[0], ' ', e[1]
    f.close()
    f = open(tgt_dir + 'deepId_test_lists.txt', 'w')
    for e in test_set:
        print >> f, e[0], ' ', e[1]
    f.close()


def prepare_deepId_data_dif(src_dir, tgt_dir, num_threshold=20, add_all=False):
    check_parameter(src_dir, 'directory')
    check_parameter(tgt_dir, 'directory', True)
    if src_dir[-1] != '/':
        src_dir += '/'
    if tgt_dir[-1] != '/':
        tgt_dir += '/'
    class_lists = listdir(src_dir, 'dir')
    print '# class is : %d' % len(class_lists)
    class_table = {}

    num = 0

    for e in class_lists:
        assert e not in class_table
        class_table[e] = listdir(''.join([src_dir, e]), 'image')
        if len(class_table[e]) > num_threshold:
            num += 1
    print 'There are %d people whose number of images is greater than %d.' % (num, num_threshold)
    print 'Use %d num people to train the deepId net, we do not care the validation set result...' % num
    train_set = []
    test_set = []
    label = 0
    dirname2label = {}
    for k, v in class_table.iteritems():
        if len(v) >= num_threshold:
            shuffle(v)
            assert k not in dirname2label
            dirname2label[k] = label
            i = 0
            for i in xrange(num_threshold):
                train_set.append((k + '/' + v[i], label))
            i += 1
            j = 0
            num_test_images = min(int(num_threshold / 3), len(v) - num_threshold)
            for j in xrange(num_test_images):
                test_set.append((k + '/' + v[i + j], label))

            if len(v) > num_threshold + num_test_images:
                offset = j + 1 + i
                if add_all is False:
                    # add the rest of all images or 3 times the num_threshold images to the training set....
                    num_left = len(v) - num_threshold - num_test_images
                    num_left = min(num_left, num_threshold)

                    for ii in xrange(num_left):
                        train_set.append((k + '/' + v[ii + offset], label))
                else:
                    # print 'Adding the rest of all data into training set.'
                    while offset < len(v):
                        train_set.append((k + '/' + v[offset], label))
                        offset += 1
            label += 1
    f = open(tgt_dir + 'dirname2label.pkl', 'wb')
    cPickle.dump(dirname2label, f, 0)
    f.close()
    f = open(tgt_dir + 'deepId_train_lists.txt', 'w')
    for e in train_set:
        print >> f, e[0], ' ', e[1]
    f.close()
    f = open(tgt_dir + 'deepId_test_lists.txt', 'w')
    for e in test_set:
        print >> f, e[0], ' ', e[1]
    f.close()


if __name__ == '__main__':
    prepare_deepId_data_eq('D:\Software\caffe\caffe-master\data\CASIA-WebFace-cut144-simi1/', 'dataset', 50)
    # prepare_deepId_data_dif('D:\Software\caffe\caffe-master\data\CASIA-WebFace-cut144-simi1/', 'dataset', 20, True)
    # 后缀eq表示每一类数目一样，50表示希望每一类都有50幅图片，dif每一类数目不一样。