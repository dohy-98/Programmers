def az() :
    return [chr(char) for char in range(ord('a'),ord('z')+1)]

az_rep = az()   # a - z 리스트
lst_rep = []   
az_lst = []

txt = list(input())  # backjoon 입력
for i in range(len(txt)) : # txt backjoon의 길이만큼 반복
    lst_rep.append(az_rep.index(txt[i]))  # txt 문자의 0번째부터 마지막까지의 위치를 추가
for i in range(len(txt)) : # txt backjoon의 길이만큼 반복
    az_lst.append(txt.index(txt[i]))

new = [-1 for _ in az_rep]

for i in range(len(txt)) :
    new[lst_rep[i]] = az_lst[i]

result = ' '.join(map(str,new))
print(result)