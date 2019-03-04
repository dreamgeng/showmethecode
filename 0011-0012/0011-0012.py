"""
第 0011 题：
敏感词文本文件 filtered_words.txt，里面的内容为以下内容，
当用户输入敏感词语时，则打印出 Freedom，否则打印出 Human Rights。
北京
程序员
公务员
领导
牛比
牛逼
你娘
你妈
love
sex
jiangge
第0012题：
当用户输入敏感词语，则用 星号 * 替换，例如当用户输入「北京是个好城市」，则变成「**是个好城市」。
"""
# set() 函数创建一个无序不重复元素集
word_filter = set()
with open ('/home/dreamgeng/Documents/dreamgeng/showmethecode/0011/filtered_words.txt') as f:
	for w in f.readlines():
		# strip() 方法用于移除字符串头尾指定的字符（默认为空格）或字符序列
		word_filter.add(w.strip())

while True:
	s=input("please input s: ")
	if s == 'exit':
		break
# 0012
	for w in word_filter:
		if w in s:
			s=s.replace(w, '*'*len(w))
			print(s)
"""
    # 0011
	if s in word_filter:
		print('Freedom')
	else:
		print('Human Rights')
"""

	

