#!/usr/bin/env python
# encoding: utf-8
"""
untitled.py

Created by Philip Plante on 2010-01-25.
Copyright (c) 2010 Endless Paths. All rights reserved.
"""

import sys
import os
import datetime
import hashlib
import random

import Image
import ImageFont, ImageDraw, ImageOps


def main():
    codes = []
    
    for x in xrange(100):
        code = hashlib.md5(''.join((str(datetime.datetime.now), str(random.random())))).hexdigest()
        code = '%s-%s-10' % (code[0:3], code[6:9])
        codes.append(code.upper())
    
    f = open('codes.txt', 'w')
    [f.write(code +'\n') for code in codes]
    f.close()
    
    for code in codes:
        im = Image.open('template.png')
        
        f = ImageFont.truetype('VERDANA.TTF', 32)
        d = ImageDraw.Draw(im)
        d.text((620, 290), code, font=f, fill=25)
        
        im.save('images/%s.png' % (code,))


if __name__ == '__main__':
	main()

