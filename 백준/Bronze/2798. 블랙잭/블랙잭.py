N,M = map(int,input().split())
rep = list(map(int,input().split()))
sum_rep = []
for i in rep[:N-2] :
    for j in rep[rep.index(i)+1:N-1] :
        for k in rep[rep.index(j)+1:N] :
            a = i + j + k
            if a <= M :
                sum_rep.append(a)
print(max(sum_rep))