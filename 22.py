a=int(input())
p=list(map(int,input().split()))
c=p[1:a:2]
d=p[0:a:2]
if(sum(c)>=sum(d)):
  print(sum(c))
else:
  print(sum(d))
