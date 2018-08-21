#!/usr/bin/env sh

# Create the imagenet lmdb inputs

# N.B. set the path to the imagenet train + val data dirs

set -e


EXAMPLE=D:/Software/caffe/caffe-master/examples/faceID/dataset/
DATA=D:/Software/caffe/caffe-master/data/CASIA-WebFace-cut144-simi1/
TOOLS=D:/Software/caffe/caffe-master/Build/x64/Release

TRAIN_DATA_ROOT=D:/Software/caffe/caffe-master/data/CASIA-WebFace-cut144-simi1/
VAL_DATA_ROOT=D:/Software/caffe/caffe-master/data/CASIA-WebFace-cut144-simi1/

# Set RESIZE=true to resize the images to 256x256. Leave as false if images have

# already been resized using another tool.

RESIZE=true
if $RESIZE; then

  RESIZE_HEIGHT=55

  RESIZE_WIDTH=55

else

  RESIZE_HEIGHT=0

  RESIZE_WIDTH=0

fi



if
 [ ! -d "$TRAIN_DATA_ROOT" ]; then

  echo "Error: TRAIN_DATA_ROOT is not a path to a directory: $TRAIN_DATA_ROOT"

  echo "Set the TRAIN_DATA_ROOT variable in create_imagenet.sh to the path" /
 
      "where the ImageNet training data is stored."

  exit 1

fi



if [ ! -d "$VAL_DATA_ROOT" ]; then

  echo "Error: VAL_DATA_ROOT is not a path to a directory: $VAL_DATA_ROOT"

  echo "Set the VAL_DATA_ROOT variable in create_imagenet.sh to the path" /

       "where the ImageNet validation data is stored."

  exit 1

fi



echo "Creating train lmdb..."



GLOG_logtostderr=1 $TOOLS/convert_imageset --resize_height=$RESIZE_HEIGHT  --resize_width=$RESIZE_WIDTH --shuffle $TRAIN_DATA_ROOT $EXAMPLE/deepId_train_lists.txt $EXAMPLE/faceNet_train_lmdb



echo "Creating val lmdb..."

GLOG_logtostderr=1 $TOOLS/convert_imageset --resize_height=$RESIZE_HEIGHT  --resize_width=$RESIZE_WIDTH --shuffle $VAL_DATA_ROOT $EXAMPLE/deepId_test_lists.txt $EXAMPLE/faceNet_val_lmdb



echo "Done."
