def priv(m1,m2):
  c1 = 0
  c2 = 1
  while m2 !=0:
    q = int(m1/m2)
    pr = m2
    m2 = m1%m2
    m1 =pr
    pr = c2
    c2 = c1-c2*q
    c1 = pr
    if c1<0:
      d = c2+c1
    else:
      d = c1
  return d
print("RSA")
p = 17
q = 29
print("Два простых числа: ",p,q)
mod = p*q
print("Их произведение (число, которое будем брать по модулю): ",mod)
f = (p-1)*(q-1)
print("Функция эйлера: ",f)
e = 11
print("Нужная нам экспонента (выбираем любое простое число меньшее полученного в функции эйлера и являющееся взаимнопростым с ним): ",e)
print("Открытый ключ: ", e, mod)
d = priv(f,e)
print("Приватный ключ: ", d, mod)
print("Введите число, меньшее ",mod," : ")
text = int(input())
shiphrtext = text**e%mod
print("Зашифрованный текст: ", shiphrtext)
print("Расшифрованный текст: ", shiphrtext**d%mod)
g = input()