import statistics
rep = []
for _ in range(5) :
    X = int(input())
    rep.append(X)

print(statistics.mean(rep))
print(statistics.median(rep))