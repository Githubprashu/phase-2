#SELECTION SORTING

def performSelectionSort(nums):
    n=len(nums)
    fixThisIndex=n-1
    while fixThisIndex > 0:
        maxEleIndex=fixThisIndex

        for index in range(fixThisIndex):
            if nums[index]>nums[maxEleIndex]:
                maxEleIndex=index

        if maxEleIndex != fixThisIndex:
            temp=nums[maxEleIndex]
            nums[maxEleIndex]=nums[fixThisIndex]
            nums[fixThisIndex]=temp
        print(nums)

        fixThisIndex -= 1

nums=[10,20,15,55,40,30,15]
print("before sorting:",nums)

performSelectionSort(nums)
print("after sorting:",nums)