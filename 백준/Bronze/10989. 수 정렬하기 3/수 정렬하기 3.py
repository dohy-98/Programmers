import sys       # sys 모듈 가져오기 

# sys.stdin.readline() -> 한줄 입력받기 , stdin -> standardinput줄임말
N  = int(sys.stdin.readline())   

# 배열을 0으로초기화 범위가 1~10000까지이므로 
arr = [0]*10001

# 처음에 설정한 숫자만큼 입력받음 , num이 들어간 갯수 카운트
for _ in range(N):
    num = int(sys.stdin.readline())
    arr[num] += 1 # arr[num]에 num이 들어온 개수 count 

for i in range(10001): 
	# arr[i]에 숫자가 들어왔다면 
    if arr[i] != 0 :
    	# arr[num]에 num이 들어온 개수 만큼 출력 
        for j in range(arr[i]): 
            print(i)