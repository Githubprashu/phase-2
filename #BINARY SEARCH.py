#BINARY SEARCH

nums=[10,20,30,40,50]
target=20
nums=sorted(nums)

left=0
right=len(nums)-1
flag=-1

while left<=right:
    mid=(left+right)//2
    if nums[mid]==target:
        flag=mid
        break
    elif nums[mid]>target:
        right=mid-1
    else:
        left=mid+1

if flag==-1:
    print("target not found")
else:
    print("target found at index:",flag)