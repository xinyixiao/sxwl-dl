#!/usr/bin/env python
# coding: utf-8
# 脚本传入三个参数：源目录，比例，目标目录
# 作用：将愿目录中的图片按照比例存入目标目录的train和val文件夹中

import argparse
import os
import random


parser = argparse.ArgumentParser()
parser.add_argument("source", help = "which source do u want to split")
parser.add_argument("ratio", help = "display a square of a given number",
                    type=float)
parser.add_argument("target", help = "where do u want to save")
args = parser.parse_args()

source = args.source
ratio = args.ratio
target = args.target

dirnames = []

# get img dir names
def getdir (args,dirname,filenames):
    """
    Callback Function

    @params:
    args : the parameter of os.path.walk(source, getdir, None)
    dirname : folder locations
    filename : filename in folder locations
    """
    
    dirnames.append(dirname)


# get img names
def getimg (args,dirname,filenames):
    """
    Callback Function

    @params:
    args : the parameter of os.path.walk(dirname, getimg, None)
    dirname : folder locations
    filename : filename in folder locations
    """

    if not filenames == '.DS_Store':
        file_paths.append(filenames)


# judge if dir train,val exists
if not os.path.exists(target + 'train'):
    os.system('mkdir ' + target + 'train')
if not os.path.exists(target + 'val'):
    os.system('mkdir ' + target + 'val')

# get img dir names
os.path.walk(source, getdir, None)

# mkdir train,val dir 
dirnames = dirnames[1:]
for dirname in dirnames:
    file_paths = []
    os.system('mkdir ' + target + 'train/' + dirname.split('/')[-1])
    os.system('mkdir ' + target + 'val/' + dirname.split('/')[-1])
    
# save img to train,val in ratio 4:1
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
    
