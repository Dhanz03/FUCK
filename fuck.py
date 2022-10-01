#!/bin/python
# program perulangan kata

# module
import os,sys,time
from time import sleep

# tampilan
os.system('clear')
os.system('figlet Dhanz 03')
sleep(1)
print('    (+) BY MR DHANZ SPM (+)')
print('=========================================')
print('    ')
print('Masukan Kata"mu Stah ')
kata = input('=> ')
print('Masukan Jumlah Perulangan')
jumlah = int(input('=> '))

# data
try:
   for i in range(jumlah):
       print('=> ' + kata)
       sleep(0.05)
       print('=> ' + kata)
       sleep(0.05)

except:
      print('berhasil')

