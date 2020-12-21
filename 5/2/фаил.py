import numpy as np
import math
from math import sqrt
y=int(input('y = '))
a=int(input('a = '))
p=int(input('p = '))

i = 0
while i < round(sqrt(p))+1:
    if i**2>p:
        k=i
        m=i
        break
    if i*(i+1)>p:
        k=i
        m=i+1
        break
    i+=1
print ("Шаг младенца")
x1=np.zeros(m)
i = 0
while i < m :
    x1[i]=(y*(a**i))%p
    i+=1
print(x1)

print ("Шаг великана")
x2=np.zeros(k)
i = 1
while i <k+1:
    x2[i-1]=(a**(m*i))%p
    i+=1
print(x2)
M = 0
while M < m:
    K = 0
    while K < k:
        if (x1[M]==x2[K]):
            j=M
            i=K+1
            break
        K+=1
    M+=1
x=i*m - j
print("x =",x)
d = input()