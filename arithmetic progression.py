N,A,D=map(int,input().split())
i=1
ap=0
while i<=N:
    ap=ap+A
    A=A+D
    i+=1
print(ap)
