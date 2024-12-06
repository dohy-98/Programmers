N = int(input()) # 학생 수
x = [list(input()) for _ in range(N)]  # 학생들 학번
cnt = 0

for i in range(1,len(x[0])+1) :    # 뒤에 자리 갯수 하나씩 추가
    y = []              
    for j in x :                   # 학생들 학번 하나씩
        a = j[-i:]                 # 앞에 정해진 자릿수 만큼 파싱
        
        if len(a) == 0 :           # 첫번째 친구는 당연히 같은 사람없으니까
            y.append(a)            # y에 a를 추가 
        
        else :                     # 두번쨰 친구부터는 
            if a in y :            # 파싱한 값이 앞에 친구랑 같으면 
                break              # 자릿수 더 늘려야됨 
        
            else :                 # 앞에 친구랑 같지 않으면 
                y.append(a)        # 파싱한 값도 넣고 다음 친구로 넘어감

    if len(y) == N :               # break 한 경우는 y 갯수가 N이랑 다르겠지
        print(len(y[0]))           # 끝까지 다 돌렸다 == 같은 사람이 없다. => 이대로 하면된다.
        break                      # 그러니까 파싱한 자릿수 y[0] 프린트 하고 끝
        