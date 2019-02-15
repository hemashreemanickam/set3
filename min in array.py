N=int(input())
x=list(map(int,input().split()))
temp=x[1]
for i in range(0,len(x)):
    if temp>x[i]:
        temp=x[i]
print(temp)
