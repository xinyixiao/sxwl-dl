#!/usr/bin/env python
# coding: utf-8
# 脚本传入参数：源目录
# 作用：将源目录中的文件夹改名，并生成‘文件夹路径，文件夹内图片类型’的映射文件


import argparse
import os

parser = argparse.ArgumentParser()
parser.add_argument("source",
        help="which source do u want to rename: example:/Users/mac/image/")
args = parser.parse_args()

source = args.source
#source = '/Users/mac/python_work/getlogo/logo_img2/'

dirnames = []
mapped = ''

#获取源目录下的图片文件夹名
def getdir (args,dirname,filenames):
    dirnames.append(dirname)
os.path.walk(source, getdir, None)
dirnames = dirnames[1:]

#修改文件夹名，并且存下映射信息
count = 1
mapped = mapped + 'return{'
for dirname in dirnames:
    first = ""+ dirname +""
    second = "" + source + '%05d'%count + ""
    os.rename(first,second)
    mapped = mapped + '\'' + source.split('/')[-1] + '%05d'%count + ',' + \
    dirname.split('/')[-1] + '\''
    mapped = mapped + ','
    mapped = mapped + '\n'
    count += 1
mapped = mapped[:-2] + '}'

#将mapped写出到lua文件
def writetolua(info):
    txt_path = 'path_imgtype_link.lua'
    with open(txt_path,"w") as f:
            f.write(info)
writetolua(mapped)
