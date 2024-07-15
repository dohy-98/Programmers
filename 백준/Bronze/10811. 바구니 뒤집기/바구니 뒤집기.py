N,M = map(int,input().strip().split())
rep = []
num = 0
if 1 <= N <= 100 and 1 <= M <= 100 :
    for i in range(1,1+N) :
        rep.append(str(i))

while True :
    i,j = map(int,input().strip().split())
    if 1 <= i <= j <= N :
        slice_part = rep[i-1:j]
        slice_part.reverse()
        rep[i-1:j] = slice_part
        num += 1
    if num == M:
        break
result = " ".join(rep)
print(result)