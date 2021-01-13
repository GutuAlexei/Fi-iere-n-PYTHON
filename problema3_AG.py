with open('globulet.txt','r') as f :
    a=f.readline()
r=int(a)+3
al=int(a)+r-2
with open ('bradut.txt', 'w') as f:
    f.write(str(int(a)+r+al))
