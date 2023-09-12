n,m=map(int,input().split())
p=list(range(1,n+1))
while m:a,b=map(int,input().split());p[a-1:b]=reversed(p[a-1:b]);m-=1
print(*p)