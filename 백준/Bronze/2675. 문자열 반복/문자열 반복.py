T = int(input())
result = []
for _ in range(T) :
    rep = []
    R,S = map(str,input().strip().split())
    for i in range(len(S)) :           
        rep.append(S[i]*int(R))
    result.append(''.join(rep))
for i in result :
    print(i)