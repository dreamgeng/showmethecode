# -*- coding: utf-8 -*-
# **第 0004 题：**任一个英文的纯文本文件，统计其中的单词出现的个数。
import re  # 正则表达式

file = open('0004.txt', 'r')
str = file.read()

reobj = re.compile('\b?(\w+)\b?')
words = reobj.findall(str)

wordDict = {}

for word in words:
	if word in wordDict:
		wordDict[word] += 1
	else:
		wordDict[word] = 1

for key,values in wordDict.items():
	print('%s: %s' % (key, values))