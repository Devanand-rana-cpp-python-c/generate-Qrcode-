# -*- coding: utf-8 -*-
"""
Created on Wed Mar  9 15:45:02 2022

@author: devan
"""
#  Generate Qr Code .......
import pyqrcode
link="https://www.google.com/"
qr_code=pyqrcode.create(link)
qr_code.png(" this is Qr code for Google.png" ,scale=5)