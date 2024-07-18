txt = str(input())

x = txt[:len(txt)//2]
t = txt[len(txt)//2:]
t1 = txt[len(txt)//2+1:]
if len(txt)%2 == 0 :
    if x == t[::-1] :
        print("1")
    else :
        print("0")
elif len(txt)%2 == 1 :
    if x == t1[::-1] :
        print("1")
    else :
        print("0")