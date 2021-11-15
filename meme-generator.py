from random_word import RandomWords
from deep_translator import GoogleTranslator
from PIL import Image, ImageDraw, ImageFont
import textwrap


r = RandomWords()
words = str(r.get_random_word(hasDictionaryDef="true")) + " " + str(r.get_random_word(hasDictionaryDef="true"))
translated = GoogleTranslator(source='auto', target='ru').translate(words)
translated = translated.upper()
#print(translated)

im = Image.open("source.png")
draw = ImageDraw.Draw(im)
image_width, image_height = im.size

font = ImageFont.truetype(font="font/impact.ttf", size=int(image_height/10))

char_width, char_height = font.getsize('A')
chars_per_line = image_width // char_width
lines = textwrap.wrap(translated, width=chars_per_line)

y = 10

for line in lines:
	line_width, line_height = font.getsize(line)
	x = (image_width - line_width)/2
	draw.text((x-1, y-1), line, fill='black', font=font)
	draw.text((x+1, y-1), line, fill='black', font=font)
	draw.text((x-1, y+1), line, fill='black', font=font)
	draw.text((x+1, y+1), line, fill='black', font=font)
	draw.text((x,y), line, fill='white', font=font)
	y += line_height

im.save('output.png', "PNG")