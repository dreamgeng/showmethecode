# 第 0010 题：使用 Python 生成类似于下图中的字母验证码图片

from PIL import Image, ImageDraw, ImageFont, ImageFilter
import random

def rndChar():
	# chr():返回值是当前整数对应的ascii字符, 65-90对应A-Z
	return chr(random.randint(65, 90))

def rndColor():
	return (random.randint(64, 255), random.randint(64, 255), random.randint(64, 255))

def rndColor2():
	return (random.randint(32, 127), random.randint(32, 127), random.randint(32, 127))

width = 60*4
height = 60
# Image.new(mode, size, color) 
image = Image.new('RGB', (width, height), (255, 255, 255))
font = ImageFont.truetype('/usr/share/fonts/truetype/ubuntu-font-family/Ubuntu-RI.ttf', 36)
# 创建一个可以在给定图像上绘图的对象。
draw = ImageDraw.Draw(image)
for x in range(width):
	for y in range(height):
		draw.point((x, y), fill=rndColor())

for t in range(4):
	#第一个参数是加入字体的坐标
	#第二个参数是文字内容
	#第三个参数是字体格式
	#第四个参数是字体颜色
	draw.text((60*t + 10, 10), rndChar(), font=font, fill=rndColor2())

# 应用模糊滤镜
image = image.filter(ImageFilter.BLUR)
image.save('code.jpg', 'jpeg')