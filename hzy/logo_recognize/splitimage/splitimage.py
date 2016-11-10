#!/usr/bin/env python
# coding: utf-8
# 脚本传入三个参数：源目录，比例，目标目录
# 作用：将愿目录中的图片按照比例存入目标目录的train和val文件夹中

import argparse
import os
import random


parser = argparse.ArgumentParser()
parser.add_argument("source", help="which source do u want to split")
parser.add_argument("ratio", help="display a square of a given number",
                    type=float)
parser.add_argument("target", help="where do u want to save")
args = parser.parse_args()

source = args.source
ratio = args.ratio
target = args.target

dirnames = []
#获取源目录下的图片文件夹名
def getdir (args,dirname,filenames):
    dirnames.append(dirname)
os.path.walk(source, getdir, None)

#获取源目录图片文件夹下的图片名
def getimg (args,dirname,filenames):
    if not filenames == '.DS_Store':
        file_paths.append(filenames)

#检测目标文件夹下是否存在train,val两个文件夹
if not os.path.exists(target + 'train'):
    os.system('mkdir ' + target + 'train')
if not os.path.exists(target + 'val'):
    os.system('mkdir ' + target + 'val')
    
#目标目录下创建相同文件夹
dirnames = dirnames[1:]
for dirname in dirnames:
    file_paths = []
    os.system('mkdir ' + target + 'train/' + dirname.split('/')[-1])
    os.system('mkdir ' + target + 'val/' + dirname.split('/')[-1])
#一次读取源文件夹下每个文件路径，并将图片复制到新的文件夹下，train和val的比例为ration
    os.path.walk(dirname, getimg, None)
    file_paths = file_paths[0]
    for file_path in file_paths:
        if random.randint(1,100) < ratio*100:
            order = 'scp ' + source[:-1] + '/' + dirname.split('/')[-1] + \
            '/' + file_path + ' ' + \
            target[:-1] + '/val/' + dirname.split('/')[-1] + '/' +  file_path
            os.system(order)
        else:
            order = 'scp ' + source[:-1] + '/' + dirname.split('/')[-1] + \
            '/' + file_path + ' ' + \
            target[:-1] + '/train/' + dirname.split('/')[-1] + '/' +  file_path
            os.system(order)
    
    