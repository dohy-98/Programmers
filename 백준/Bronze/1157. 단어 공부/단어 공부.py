word = input().upper()       # 대문자로 입력
word_list = list(set(word))  # 단어들을 세트로 중복제거하고 리스트로 만듬

cnt = []                     # 리스트 생성
for i in word_list:          # word list에 있는 단어들 하나하나
  count = word.count         # word 에 있는지 카운트 하는 count정의
  cnt.append(count(i))       # count(i) 가 있는지 카운트해서 cnt에 추가

# print(cnt)                 # mississipi 입력할때 [1,1,4,4] 나옴
if cnt.count(max(cnt)) > 1:  # cnt에서 최댓값 4가 몇개인지 카운트하고 그게 1보다 크다면 
  print("?")                 # ? 출력

else:                         
  print(word_list[(cnt.index(max(cnt)))])  # 아