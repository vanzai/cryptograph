def dv(Z):
  h = 0
  while h<len(Z):
    c = -1
    FFF = []
    GG = 0
    if Z[h]>0:
      GG = 1
      while Z[h] != 1:
        FFF.append(Z[h]%2)
        Z[h] = int(Z[h] / 2)
        c+=1
      while c >= 0:
        GG*=10
        GG+=FFF[c]
        c-=1
    Z[h] = GG
    h+=1
  return Z

def last(Z):
  G = ""
  h = 0
  while h<len(Z):
    Z[h] = str(Z[h])
    while len(Z[h]) != 3:
      Z[h] = "0" + Z[h]
    G+=Z[h]
    h+=1
  return G
print("RC4")
n = 3
S = [0,1,2,3,4,5,6,7]
i = 0
K = [2,5]
L = 2
j = 0
while i<2**n:
    j = (j+S[i]+K[i%L])%2**n
    kol=S[j]
    S[j]=S[i]
    S[i]=kol
    i+=1

Z=[]
i=0
j=0
kol=0
h = 0
while h<2**n:
  i=(h+1)%2**n
  j=(j+S[i])%2**n
  kol=S[j]
  S[j]=S[i]
  S[i]=kol
  t=(S[i]+S[j])%2**n
  Z.append(S[t])
  h+=1

Z = dv(Z)
print(last(Z))
x = input()