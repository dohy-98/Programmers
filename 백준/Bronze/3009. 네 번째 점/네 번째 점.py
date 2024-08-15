from collections import Counter
x_rep, y_rep = zip(*[map(int, input().strip().split()) for _ in range(3)])
xy_rep = []

count = Counter(x_rep)
result = [str(i) for i, cnt in count.items() if cnt == 1]
count = Counter(y_rep)
result += [str(i) for i, cnt in count.items() if cnt == 1]

print(" ".join(result))