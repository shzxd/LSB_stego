#!/usr/bin/python
#coding:utf-8

from PIL import Image

stego = Image.open("./stego.bmp")
bin_sec = ''
w, h = stego.size
num = 0

for i in range(0, w):
    for j in range(0, h):
        if (num == 35):	#假设接收方已知秘密信息长度
            break
        bin_sec = bin_sec + str(stego.getpixel((i, j))&1)
        num = num+1

secret = int(bin_sec, 2)
print (secret)
