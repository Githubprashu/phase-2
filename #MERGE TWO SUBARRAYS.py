#MERGE TWO SUBARRAYS


def mergetwosubarrays(nums,left,mid,right):
    temp=[]
    index1=left
    index2=mid+1
    while index1<=mid and index2<=right:
        if nums[index1]<nums[index2]:
            temp.append(nums[index1])
            index1 += 1
        else:
            temp.append(nums[index2])
            index2 += 1
    
    while index1 <= mid:
        temp.append(nums[index1])
        index1 += 1

    while index2 <= right:
        temp.append(nums[index2])
        index2 += 1

    position=left
    for ele in temp:
        nums[position]=ele
        position += 1

def mergeanddivide(nums,left,right):
    print(left,right)
    if left>=right:
        return
    mid=(left+right)//2
    mergeanddivide(nums,left,mid)
    mergeanddivide(nums,mid+1,right)
    mergetwosubarrays(nums,left,mid,right)

def performmergesort(nums):
    n=len(nums)
    mergeanddivide(nums,0,n-1)

nums=[10,8,20,12,7,6,5,11,60]

print("before sorting:",nums)

performmergesort(nums)

print("after sorting:",nums)