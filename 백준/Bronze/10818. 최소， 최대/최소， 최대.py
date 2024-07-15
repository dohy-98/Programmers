N = int(input().strip())
rep = []
numbers = list(map(int, input().strip().split()))

rep.append(min(numbers))
rep.append(max(numbers))
for i in range(len(rep)) :
    print(rep[i], end=" ")