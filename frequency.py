l=[1,1,1,2,2,3,3,4,6,6,6,7,8,9,9,7,5,4,32,5,67,8,9]
d={}
n=len(l)
# for i in l:
#       if i in d:
#             d[i]+=1
#       else:
#             d[i]=1
# print(d)
for i in range(0,n):
      d[l[i]]=d.get(l[i],0)+1
print(d)