N = int(input().strip())
numbers = list(map(int, input().strip().split()))
v = int(input().strip())
num = 0
for i in numbers :
    if i == v :
        num = num + 1
print(num)