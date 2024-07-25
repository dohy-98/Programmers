arr = []              # 저장소

for _ in range(5):    # 5번반복
    a = input()       # 입력
    arr.append(a)     # 저장

for i in range(max(len(w) for w in arr)): 
    for j in range(5):
        if i < len(arr[j]):
            print(arr[j][i], end="")