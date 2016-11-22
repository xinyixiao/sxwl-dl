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

<table>
  <tr>
    <th>logo</th>
    <th>count</th>
  </tr>
  <tr>
    <td>adidas</td>
    <td>70</td>
  </tr>
  <tr>
    <td>aldi</td>
    <td>70</td>
  </tr>
  <tr>
    <td>apple</td>
    <td>70</td>
  </tr>
  <tr>
    <td>becks</td>
    <td>70</td>
  </tr>
  <tr>
    <td>bmw</td>
    <td>70</td>
  </tr>
  <tr>
    <td>carlsberg</td>
    <td>70</td>
  </tr>
  <tr>
    <td>chimay</td>
    <td>70</td>
  </tr>
  <tr>
    <td>coccola</td>
    <td>70</td>
  </tr>
  <tr>
    <td>dhl</td>
    <td>70</td>
  </tr>
  <tr>
    <td>erdinger</td>
    <td>70</td>
  </tr>
  <tr>
    <td>corona</td>
    <td>70</td>
  </tr>
  <tr>
    <td>dhl</td>
    <td>70</td>
  </tr>
  <tr>
    <td>erdinger</td>
    <td>70</td>
  </tr>
  <tr>
    <td>esso</td>
    <td>70</td>
  </tr>
  <tr>
    <td>fedex</td>
    <td>70</td>
  </tr>
  <tr>
    <td>ferrari</td>
    <td>70</td>
  </tr>
  <tr>
    <td>ford</td>
    <td>70</td>
  </tr>
  <tr>
    <td>fosters</td>
    <td>70</td>
  </tr>
  <tr>
    <td>google</td>
    <td>70</td>
  </tr>
  <tr>
    <td>guiness</td>
    <td>70</td>
  </tr>
  <tr>
    <td>heineken</td>
    <td>70</td>
  </tr>
  <tr>
    <td>HP</td>
    <td>70</td>
  </tr>
  <tr>
    <td>mika</td>
    <td>70</td>
  </tr>
  <tr>
    <td>nvidia</td>
    <td>70</td>
  </tr>
  <tr>
    <td>paulaner</td>
    <td>70</td>
  </tr>
  <tr>
    <td>pepsi</td>
    <td>70</td>
  </tr>
  <tr>
    <td>rittersport</td>
    <td>70</td>
  </tr>
  <tr>
    <td>whell</td>
    <td>70</td>
  </tr>
  <tr>
    <td>single</td>
    <td>70</td>
  </tr>
  <tr>
    <td>starbucks</td>
    <td>70</td>
  </tr>
  <tr>
    <td>stellaartois</td>
    <td>70</td>
  </tr>
  <tr>
    <td>texaco</td>
    <td>70</td>
  </tr>
  <tr>
    <td>tsingtao</td>
    <td>70</td>
  </tr>
  <tr>
    <td>ups</td>
    <td>70</td>
  </tr>
</table>

存储路径
```
/home/sxwl1080/hzy/dl-data/sxwl_dataset/logo_detectionFlickrLogos-32
```

## FlickrLogos_pasted

### 目标检测数据集(仿照voc2007制作数据集)

文件夹路径
```
/home/sxwl1080/hzy/dl-data/sxwl_dataset/logo_detection/FlickrLogos_pasted
```
用于目标检测

#### logo图片(3404张)
截取每张图片中的logo图片保存在
```
/home/sxwl1080/hzy/dl-data/sxwl_dataset/FlickrLogos_pasted/logo_detection/my_logo
```
路径下。

#### 背景图片(6000张)
不包含logo的背景图片保存在
```
/home/sxwl1080/hzy/dl-data/sxwl_dataset/FlickrLogos-32/classes/no-logo
```
路径下。

#### 制作图片
上面的logo图片和背景图片随机组合生成新的图片存储在
```
/home/sxwl1080/hzy/dl-data/sxwl_dataset/FlickrLogos_pasted/logo_detection/JPEGImages
```
路径下,一共16032张图片，并且保存logo的位置信息于
```
/home/sxwl1080/hzy/dl-data/sxwl_dataset/FlickrLogos_pasted/logo_detection/position_info.txt
```
生成的xml文件:
```
/home/sxwl1080/hzy/dl-data/sxwl_dataset/FlickrLogos_pasted/logo_detection/Annotations
```
生成的txt文件:
```
/home/sxwl1080/hzy/dl-data/sxwl_dataset/FlickrLogos_pasted/logo_detection/ImageSets/Main
```

### logo识别数据集(仿照github上fb.resnet.torch工程制作数据集)

#### 训练集路径(32类13042张图片)
```
/home/sxwl1080/hzy/dl-data/sxwl_dataset/FlickrLogos_pasted/logo_recognize/dataset/train
```
#### 测试集路径(32类2990张图片)
```
/home/sxwl1080/hzy/dl-data/sxwl_dataset/FlickrLogos_pasted/logo_recognize/dataset/val
```

