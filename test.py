from PIL import Image


im = Image.open('test.jpg')
w, h = im.size
print('Original image size: %s*%s' % (w, h))
# 缩放到50%:
im.thumbnail((w//2, h//2))
print('Resize image to: %s*%s' % (w//2, h//2))
im.save('thumbnail.jpg', 'jpeg')
