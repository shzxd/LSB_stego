#!/usr/bin/python
#coding:utf-8

import math
from PIL import Image 

cover = Image.open("./lena.bmp").convert("L")
cover.show()
stego = cover
secret = bin(18217652291)
sec_len = len(secret)
w ,h =cover.size

if sec_len > w*h:
    print 'Error!   There are too many secret!'
else:
    num = 2
    for i in range(0, w):
        for j in range(0, h):
            if num == sec_len:
                break
            ori_pix = cover.getpixel((i, j))
            ori_lsb = ori_pix & 1   #取原像素的最低有效位
            if ori_lsb == int(secret[num]):
                new_pix = ori_pix
            else:
                if ori_lsb == 0:
                    new_pix = ori_pix + 1
                else:
                    new_pix = ori_pix - 1
            stego.putpixel((i, j), new_pix)
            num=num+1

    stego.save("./stego.bmp")
    stego.show()
