with open('numere.txt','r') as f :
    a=f.readline()
    b=f.readline()
if int(a)>int(b):
    c=int(b)
if int(b)>int(a):
    c=int(a)
if int(a)==int(b):
    c='egale'
with open ('minim.txt', 'w') as f:
    f.write(str(c))