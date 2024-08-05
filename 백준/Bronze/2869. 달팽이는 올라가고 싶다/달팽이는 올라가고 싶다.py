import math
A,B,V = map(int,input().split())
print(math.ceil(float((V - A)/(A - B) + 1))) 