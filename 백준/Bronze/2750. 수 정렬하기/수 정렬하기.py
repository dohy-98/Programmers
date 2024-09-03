N = int(input())
rep = []
for _ in range(N) :
    X = int(input())
    rep.append(X)
for i in sorted(tuple(rep)) :
    print(i)