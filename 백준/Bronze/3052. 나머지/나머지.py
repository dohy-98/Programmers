rep_a = []
rep_b = []
for _ in range(10) : 
    a = int(input())
    rep_a.append(a)
for i in rep_a :
    b = i%42
    rep_b.append(b)
print(len(set(rep_b)))