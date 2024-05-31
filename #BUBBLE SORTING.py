#BUBBLE SORTING

def performBubbleSort(nums):
    n=len(nums)
    fixThisIndex=n-1

    while fixThisIndex > 0:
        for index in range (fixThisIndex):
            if nums[index]>nums[index+1]:
                temp=nums[index]
                nums[index]=nums[index+1]
                nums[index+1]=temp
        print(nums)
        fixThisIndex -= 1

nums=[10,20,15,55,40,30,15]
print("before sorting:",nums)

performBubbleSort(nums)
print("after sorting:",nums)