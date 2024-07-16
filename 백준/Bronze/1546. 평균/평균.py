N = int(input().strip())
L = list(map(int,input().split()))
su = 0
for i in L :
    su += (i/max(L))*100
print(su/N)