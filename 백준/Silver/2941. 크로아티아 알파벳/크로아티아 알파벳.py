txt = input().lower()
cro = ['dz=','c=','c-','d-','lj','nj','s=','z=']
num = 0

for i in cro :
    while i in txt :
        txt = txt.replace(i,'*',1)
print(len(txt))