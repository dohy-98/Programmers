M = int(input())
N = int(input())
rep= []
for i in range(M,N+1) :
    cnt = 0
    for j in range(2,i+1) :
        if i % j == 0 :
            cnt += 1
        elif cnt >= 2 :
            break
    if cnt == 1 :
        rep.append(i)
if rep == [] :
    print(-1)
else :
    print(sum(rep))
    print(min(rep))