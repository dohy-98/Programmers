a = list(map(int,input().split()))
rep = []

for i in range(1,min(a)+1) :
    if a[0] % i == 0 and a[1] % i == 0 :
        rep.append(i)

print(a[0]*a[1]//max(rep))