N = int(input())
X = map(int,input().strip().split())
cnt = 0 
for i in X :
    if i == 1 :
        continue
    j_rep = []
    for j in range(1, i+1) :
        if i%j == 0 :
            j_rep.append(j)
    if len(j_rep) == 2 :
        cnt += 1
print(cnt)