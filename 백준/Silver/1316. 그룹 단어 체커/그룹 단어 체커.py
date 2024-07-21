N = int(input().strip())  # 숫자입력
num = 0

for _ in range(N):                     # 입력한숫자만큼 반복
    txt = input().strip()              # 문자 입력
    is_group_word = True               # 식이 맞으면 True 
    seen_chars = set()                 # 봤던단어 set로 저장
    prev_char = ''                     # 이전에 본 단어 - 시작은 암것도없다

    for char in txt:                   # 입력한 단어 차례대로
        if char != prev_char:          # 그 단어가 직전 단어가 아니라면
            if char in seen_chars:     # 직전의 단어가 아닌데 본적있는 단어라면?
                is_group_word = False  # 이거 잘못된 친구다
                break                  # 파기
            seen_chars.add(char)       # 문제없으면 봤던단어에 현재 단어 추가
        prev_char = char               # 이제 현재단어는 직전단어가 되어 저장되고 다음단어 시작

    if is_group_word:                  # True면
        num += 1                       # +1  false면 0

print(num)