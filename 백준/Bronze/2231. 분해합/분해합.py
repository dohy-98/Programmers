N = int(input())
rep = [] 
for i in range(N+1) : 
    cut = list(str(i))
    su = 0
    for j in cut :
        su += int(j)
    if  i + su == N :
        print(i)
        break
    elif i == N :
        print(0)