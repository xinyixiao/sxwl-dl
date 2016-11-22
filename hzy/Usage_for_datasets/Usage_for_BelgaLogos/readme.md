## Image
BelgaLogos数据集由10000张图片组成，主题有:政治,经济，金融和社会事务，体育，文化和人物。所有图像都是JPEG格式，高度和宽度的最大值resize成800像素，保持长宽比。

## Annotations
BelgaLogos数据集的10,000张图片已手动注释。并提供两种groundtruth。

#### Global groundtruth
一共有26种logo，每张图像可能存在多个logo，每张图像针对每个logo有一条信息，和标志位，存在则标志位为1，否则为0。如果图像中的logo像素小于10*10，则不标注这个logo。

#### Local groundtruth
一共有37种logo，每个图像存在多个logo，并给出坐标，已有人肉眼标注，若肉眼不能识别则标注为‘垃圾’（0），否则为‘ok’（1）。

## Queries

#### qset3_internal_and_local.gt
字段信息：类别编号(增量)，类别名称，图片名称，logo，‘肉眼标注’信息，logo框的坐标
#### qset3_internal_and_local.qry
与qset3_internal_and_local.gt相似，但是只有通过‘肉眼标注’的字段信息。
#### qset3_internal_and_local.results
针对每张图片中的每个logo有一条信息，没有是否通过‘肉眼标准’的字段信息。

## 存储路径

```
/home/sxwl1080/hzy/dl-data/sxwl_dataset
```