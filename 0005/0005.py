# -*- coding: utf-8 -*-
"""
**第 0005 题：**
你有一个目录，装了很多照片，把它们的尺寸变成都不大于 iPhone5 分辨率的大小。
"""

from PIL import Image
import os

path = '/home/dreamgeng/Documents/dreamgeng/showmethecode/0005/pictures'
resultPath = '/home/dreamgeng/Documents/dreamgeng/showmethecode/0005/result'
if not os.path.isdir(resultPath):
	os.mkdir(resultPath)
for pic in os.listdir(path):
	picPath = os.path.join(path, pic) # 合并路径 join(path1, path2)
	# print(picPath)
	with Image.open(picPath) as im:
		w, h = im.size
		n = w/1366 if (w/1366) >= (h/640) else h/640
		im.thumbnail((w/n, h/n)) # 缩放
		# 以 jpeg 格式将图片示例保存为 resultPath+'/finish_' + pic.split('.')[0] + '.jpg'
		im.save(resultPath+'/finish_' + pic.split('.')[0] + '.jpg', 'jpeg') 