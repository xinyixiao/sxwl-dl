GoogleOpenImage包含900w标注数据，存在两个images.csv文件中，分别用于train和validation。

#### /images.csv 格式
每条信息拥有如下字段:

name | what
---|---
ImageID | 图片ID
Subset| 图片作用(train/validation)
OriginalURL | 图片下载URL
OriginalLandingURL | 
License | 
AuthorProfileURL | 
Author | 
Title | 
OriginalSize | 
OriginalMD5 |

自己写了一个py文件解析并且能够下载含有特定关键字的图片
```
/home/sxwl1080/hzy/sxwl_dataset/google_open_img/download_google_image.py
```
csv文件路径
```
/home/sxwl1080/hzy/sxwl_dataset/google_open_img
```
