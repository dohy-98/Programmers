N = int(input())
A = [list(map(int,input().split())) for _ in range(N)]
c = sorted(A)
for i in c :
    print(" ".join(map(str,i)))