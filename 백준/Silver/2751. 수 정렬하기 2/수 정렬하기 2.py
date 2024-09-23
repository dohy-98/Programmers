import sys
N = int(sys.stdin.readline())
rep = list(int(sys.stdin.readline()) for _ in range(N))
rep.sort()
for i in rep :
    print(i)