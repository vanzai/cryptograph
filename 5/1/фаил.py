y=int(input('y = '))
a=int(input('a = '))
p=int(input('p = '))
x = 0
while x<p:
    x+=1
    if (a**x)%p==y:
        print("Ответ: ",x)
        break
e=input()