"""
第 0008 题：一个HTML文件，找出里面的正文。
"""
import requests, re
from bs4 import BeautifulSoup

url = 'https://dreamgeng.github.io'
data = requests.get(url)
# r = re.findall(r'<body>[\s\S]*<body>', data.text)
# print(data.text)

soup = BeautifulSoup(open('index.html')) # 本地 index.html 
# soup = BeautifulSoup(data.text, 'html.parser') # 网址

# 0008
print(soup.body.text)

# 0009
links = soup.find_all('a')

for link in links:
	print(link['href'])

