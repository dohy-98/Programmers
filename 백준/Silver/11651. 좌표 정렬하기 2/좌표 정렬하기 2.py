N = int(input())
A = [list(map(int,input().split())) for _ in range(N)]
A.sort(key = lambda x: (x[1] , x[0]))
for i in A :
    print(i[0],i[1])
