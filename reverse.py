n=[1,2,3,4,5,6,7,8,9]
def reverse(n):
      l=0
      r=len(n)-1
      while l<=r:
            n[l],n[r]=n[r],n[l]
            l+=1
            r-=1
      return n
print(reverse(n))