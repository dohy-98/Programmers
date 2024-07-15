N,M = map(int,input().strip().split())  

basket = [n for n in range(1,N+1)]   

for _ in range(M):          
    i, j = map(int, input().split()) 
    a = basket[i-1] 
    b = basket[j-1]
    basket[j-1] = a
    basket[i-1] = b
    
for i in range(N):   
    print(basket[i], end=" ")   