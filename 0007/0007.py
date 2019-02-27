# -*- coding: utf-8 -*-
"""
**第 0007 题：**
有个目录，里面是你自己写过的程序，统计一下你写过多少行代码。包括空行和注释，但是要分别列出来。
"""
import os
import re

def stat_code(dir_path):
	if not os.path.isdir(dir_path):
		return
	# 建议使用Python的r前缀，就不用考虑转义的问题了
	# '^' :匹配输入字符串开始的位置。
	exp_re = re.compile(r'^#.*')
	# os.listdir()列出指定目录的文件
	file_list = os.listdir(dir_path)
	print("%s\t%s\t%s\t%s" % ('file','all_lines', 'space_lines', 'exp_lines'))
	for file in file_list:
		file_path = os.path.join(dir_path, file)
		if os.path.isfile(file_path) and os.path.splitext(file_path)[1] == '.py':
			with open(file_path) as f:
				all_lines = 0
				space_lines = 0
				exp_lines = 0
				for line in f.readlines():
					all_lines += 1
					# strip() 方法用于移除字符串头尾指定的字符（默认为空格）或字符序列,不能删除中间部分的字符。
					if line.strip() == ' ':
						space_lines += 1
						continue
					exp = exp_re.findall(line.strip())
					if exp:
						exp_lines += 1

			print("%s\t%s\t%s\t%s" % (file, all_lines, space_lines, exp_lines))
		else:
			print('no py file')


if __name__ == '__main__':
	stat_code('.') # 任意路径