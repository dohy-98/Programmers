N = int(input())
rep = set(str(input()) for _ in range(N))
c = sorted(rep,key = lambda x : (len(x) , x.lower()))
for i in c :
    print(i)