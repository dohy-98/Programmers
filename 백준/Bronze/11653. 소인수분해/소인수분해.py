N = int(input())
rep = []
for i in range(2,N+1) :
    while True :
        if N % i == 0 :
            rep.append(i)
            N = N/i
        else :
            break
for i in rep :
    print(i)