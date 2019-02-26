# -*- coding: utf-8 -*-
"""
**第 0006 题：**
你有一个目录，放了你一个月的日记，都是 txt，
为了避免分词的问题，假设内容都是英文，请统计出你认为每篇日记最重要的词。
"""
import os 
import re

def findWord(DicPath):
	if not os.path.isdir(DicPath):
	 	return 
	filelist = os.listdir(DicPath)
	reObj = re.compile('\b?(\w+)\b?')
	for file in filelist:
		filePath = os.path.join(DicPath, file)
		# 使用 and （与）时，表示只有两个条件同时成立的情况下，判断条件才成功。
		# isfile 判断路径是否为文件
		# splitext 分割路径，返回路径名和文件扩展名的元组
		if os.path.isfile(filePath) and os.path.splitext(filePath)[1] == '.txt':
			with open(filePath) as f:
				data = f.read()
				words = reObj.findall(data)
				wordDict = dict()
				for word in words:
					word = word.lower()
					if word in ['a', 'the', 'to']:
						continue # continue 语句用来告诉Python跳过当前循环的剩余语句，然后继续进行下一轮循环。
					if word in wordDict:
						wordDict[word] += 1
					else:
						wordDict[word] = 1
			
			# sorted(iterable, key=None, reverse=False)  
			# 参数说明：
			# iterable -- 可迭代对象。
			# key -- 主要是用来进行比较的元素，只有一个参数，具体的函数的参数就是取自于可迭代对象中，指定可迭代对象中的一个元素来进行排序。
			# reverse -- 排序规则，reverse = True 降序 ， reverse = False 升序（默认）。
			# 使用lambda来创建匿名函数,指定可迭代对象中的第二个元素来进行排序
			anslist = sorted(wordDict.items(),  key=lambda x: x[1], reverse=True)
			print(anslist)
			print('file: %s->the most word: %s ' % (file, anslist[0]))

if __name__ == '__main__':
	findWord('/home/dreamgeng/Documents/dreamgeng/showmethecode/0006')