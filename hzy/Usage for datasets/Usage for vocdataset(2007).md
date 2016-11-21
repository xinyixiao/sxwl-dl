### 一般voc解压出来后都包括
```
Annotations,ImageSets,JPEFImages,SegmentationClass ,SegmentationObject
```
#### Annotations
Annotations中是放着所有图片的标记信息，以xml为后缀名.

#### ImageSets
以分类检测的数据为例，打开ImageSets中的layout，会有train，trainval，val三个txt格式数据。

txtname | info
---|---
train.txt | 训练数据
val.txt | 验证数据
trainval | 所有训练和验证数据
test | 测试数据

ImageSets中的Main文件夹中保存的是各类数据出现的统计，以areoplane为例，有三个相关文件aeroplane_train.txt,areoplane_val,areoplane_trainval.txt,以areoplain_train.txt为例，分为两列，第一列为图像名如00012（注意没有后缀），第二列为-1和1，-1表示目标在对应的图像没有出现，1则表示出现。

#### JPEGImages
JPEGImages文件夹种存放的是所有的文件信息

#### segmentationclass和segmentationobject
segmentationclass和segmentationobject中均为分割后的结果

存储路径
```
/Users/mac/github/sxwl-dl/hzy/logo_detection/Voc2007
```