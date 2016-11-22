## FlickrLogos-32(原数据集)
#### 32类logo图片数据总量为2240张可用于目标检测，边缘检测。

图片路径为

```
/FlickrLogos-32/classes/jpg
```

每张图片有对应的bboxs.txt文件在
```
/FlickrLogos-32/classes/mask
```
目录下，字段为x,y,width,height支持多目标检测。

logo | count
---|---
adidas | 70
aldi | 70
apple | 70
becks | 70
bmw | 70
carlsberg | 70
chimay | 70
coccola | 70
corona | 70
dhl | 70
erdinger | 70
esso | 70
fedex | 70
ferrari | 70
ford | 70
fosters | 70
google | 70
guiness | 70
heineken | 70
HP | 70
mika | 70
nvidia | 70
paulaner | 70
pepsi | 70
rittersport | 70
shell | 70
single | 70
starbucks | 70
stellaartois | 70
texaco | 70
tsingtao | 70
ups | 70

存储路径
```
/Users/mac/github/sxwl-dl/hzy/logo_detection/FlickrLogos-32
```

## FlickrLogos_pasted
### 目标检测数据集(仿照voc2007制作数据集)
#### 文件夹路径
```
/home/sxwl1080/hzy/sxwl_dataset/logo_detection/FlickrLogos_pasted
```
用于目标检测

#### logo图片(3404张)
截取每张图片中的logo图片保存在
```
/home/sxwl1080/hzy/sxwl_dataset/FlickrLogos_pasted/logo_detection/my_logo
```
路径下。

#### 背景图片(6000张)
不包含logo的背景图片保存在
```
/home/sxwl1080/hzy/sxwl_dataset/FlickrLogos-32/classes/no-logo
```
路径下。

#### 制作图片
上面的logo图片和背景图片随机组合生成新的图片存储在
```
/home/sxwl1080/hzy/sxwl_dataset/FlickrLogos_pasted/logo_detection/JPEGImages
```
路径下,一共16032张图片，并且保存logo的位置信息于
```
/home/sxwl1080/hzy/sxwl_dataset/FlickrLogos_pasted/logo_detection/position_info.txt
```
生成的xml文件:
```
/home/sxwl1080/hzy/sxwl_dataset/FlickrLogos_pasted/logo_detection/Annotations
```
生成的txt文件:
```
/home/sxwl1080/hzy/sxwl_dataset/FlickrLogos_pasted/logo_detection/ImageSets/Main
```

### logo识别数据集(仿照github上fb.resnet.torch工程制作数据集)

#### 训练集路径(32类13042张图片)
```
/home/sxwl1080/hzy/sxwl_dataset/FlickrLogos_pasted/logo_recognize/dataset/train
```
#### 测试集路径(32类2990张图片)
```
/home/sxwl1080/hzy/sxwl_dataset/FlickrLogos_pasted/logo_recognize/dataset/val
```

