import os
import sys
from PIL import Image, ImageOps, ImageDraw, ImageFont
import textwrap
import math
import csv
import datetime

trailer_name = "./Inception/66TuSJo4dZM"
myFont = ImageFont.truetype('OpenSans-Regular.ttf', 30)


def timecode_to_datetime(timecode):
    return datetime.datetime.strptime(timecode, "%H:%M:%S.%f")


# read srt file into a dictionary
file = open(trailer_name+".srt", "r")
lines = file.readlines()
lines = [i for i in lines if i[:-1]]
srt_dict = {}

i = 0
while i < len(lines):
    srt_dict.update({lines[i+1].split(' ')[0].replace(',', '.'): lines[i+2][:-1]})
    i += 3

print(srt_dict)


# read timecode list from XXXX-Scenes.csv
with open(trailer_name+"-Scenes.csv", newline='') as f:
    reader = csv.reader(f)
    timecode_list = next(reader)

timecode_list = timecode_list[1:]
print(timecode_list)


inpath = "./Inception/test_output"
img_list = sorted(os.listdir(inpath))

if len(img_list):
    if img_list[0] == '.DS_Store':
        del img_list[0]

    img_list = [inpath + '/' + im for im in img_list]

    images = map(Image.open, img_list)

    pages = math.ceil(len(img_list) / 12)
    total_width = (470*2 + 36) * pages + 9
    total_height = 470 * 6

    new_im = Image.new('RGB', (total_width, total_height), 'white')

    x_offset = 0
    y_offset = 0
    count = 1
    srt_idx = 0
    srt_dict_keys = list(srt_dict.keys())
    keys_len = len(srt_dict_keys)

    for im in images:
        if srt_idx < keys_len and count <= len(timecode_list) and timecode_to_datetime(srt_dict_keys[srt_idx]) <= timecode_to_datetime(timecode_list[count-1]):
            d = ImageDraw.Draw(im)
            text = textwrap.fill(srt_dict[srt_dict_keys[srt_idx]], 30)
            w, h = d.textsize(text, font=myFont)
            d.text(((470-w)/2, 430-h), text, font=myFont, fill='white')
            srt_idx += 1

        if count % 2 != 0:
            new_im.paste(ImageOps.expand(im, border=9, fill='white'), (x_offset, y_offset))
        else:
            new_im.paste(ImageOps.expand(im, border=9, fill='white'), (x_offset + 470, y_offset))
            y_offset += 470

        if count != 0 and count % 12 == 0:
            page_number = Image.new('RGB', (36, 470 * 6), 'white')
            draw = ImageDraw.Draw(page_number)
            draw.text((0, y_offset-45), str(int(count / 12)), font=myFont, fill='black')
            x_offset += 470 * 2
            y_offset = 0
            new_im.paste(page_number, (x_offset, 0))
            x_offset += 36

        count += 1

    if count % 12 != 1:
        page_number = Image.new('RGB', (36, 470 * 6), 'white')
        draw = ImageDraw.Draw(page_number)
        draw.text((0, 470 * 6 - 45), str(int(count / 12)+1), font=myFont,
                  fill='black')
        x_offset += 470 * 2
        new_im.paste(page_number, (x_offset, 0))


    new_im.save('result.jpg')
    # new_im.save('result_gray.jpg')

