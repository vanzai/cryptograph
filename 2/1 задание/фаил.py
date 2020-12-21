import numpy as np
import binascii
def razd(x):
  ix = len(x)
  xmassive =[]
  i= 0
  while i<ix:
    xmassive.append(ord(x[i]))
    i+=1
  return xmassive

def vozvr(x):
  ix = len(x)
  xmassive =[]
  i= 0
  while i<ix:
    xmassive.append(chr(x[i]))
    i+=1
  return xmassive

def shiphr(sh1,sh2):
  n1 = 0
  n2 = 0
  X =[]
  while n1<len(sh1):
    if(n2 == len(sh2)):
      n2 = 0
    X.append(sh1[n1]^sh2[n2])
    n1+=1
    n2+=1
  return X


textr = open('text.txt', 'r')
keyr = open('key.txt', 'r')
text = textr.read()
key = keyr.read()
massive_key = razd(key)
massive = razd(text) 
 
if len(massive) >= len(massive_key):
  massive_itog = shiphr(massive,massive_key)
else:
  massive_itog = shiphr(massive_key,massive)

print(vozvr(massive_itog))

if len(massive_itog) >= len(massive_key):
  massive_itog = shiphr(massive_itog,massive_key)
else:
  massive_itog = shiphr(massive_key,massive_itog)

print(vozvr(massive_itog))

x = input()