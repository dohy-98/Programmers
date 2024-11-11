
N = int(input())
num = 64
cnt = 0

if N == 64 :
    print(1)

else : 
    for i in range(1,7) :
        if N == 0 : 
            break
        a = num // (2**i)
        if N >= a :
            N -= a
            cnt += 1
        else : 
            continue
    print(cnt)
