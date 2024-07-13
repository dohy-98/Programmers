n = int(input().strip())
rps = []
for _ in range(n):
    A, B = map(int, input().strip().split())
    if 0 < A < 10 and 0 < B < 10 :
        rps.append(A + B)
for i in rps :
    print (i)