#coding=utf-8
import PIL
from PIL import Image,ImageDraw,ImageFont

font = ImageFont.truetype('/Library/Fonts/Chalkduster.ttf',200)
im01 = Image.open('test1.JPG')

draw = ImageDraw.Draw(im01)
draw.text((0,0),'4',fill=(255,0,0),font=font)

im01.show()
