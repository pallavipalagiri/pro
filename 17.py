a,p=map(int,input().split())
c=list(map(int,input().split()))[:a]
d=0
for i in range(a):
  for j in range(a):
    if(j>i):
      if(c[i]+c[j]==p):
        d+=1
if(d>0):
  print("yes")
else:
  print("no")
