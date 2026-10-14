nums=[9,8,7,6,5,4,3,2,1]
def bubble_sort(nums):
      n=len(nums)
      for i in range(n-2,-1,-1):
            for j in range(0,i+1):
                  if nums[j]>nums[j+1]:
                        nums[j],nums[j+1]=nums[j+1],nums[j]
      return nums
print(bubble_sort(nums))