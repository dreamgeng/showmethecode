# 将你的 QQ 头像（或者微博头像）右上角加上红色的数字，类似于微信未读信息数量那种提示效果。
# 0000
from PIL import Image, ImageFont, ImageDraw


def add_num(img):
    im = Image.open(img)
    w, h = im.size
    # 字体
    font = ImageFont.truetype('Arial.ttf', 50)
    # 颜色，红
    fillcolor = "#ff0000"
    draw = ImageDraw.Draw(im)
    draw.text((w-30, 0), '6', font=font, fill=fillcolor)
    im.save('r.jpg', 'jpeg')


if __name__ == '__main__':
    add_num('test.jpg')
