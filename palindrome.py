s=input('enter the string:')
l=0
r=len(s)-1
# def func(s,l,r):
      
#       while l<r:
#             if s[l]!=s[r]:
#                   return False
#             l+=1
#             r-=1
#       return True
# print(func(s,l,r))

def func(s,l,r):
      if l>=r:
            return True
      if s[l]!=s[r]:
            return False
      return func(s,l+1,r-1)
print(func(s,l,r))