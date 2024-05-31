#INSERTION SORTING

def performInsertionSort(nums):
    n=len(nums)
    lastEleInsortedArr=0
    for firstIndex in range(1,n):
        temp=nums[firstIndex]
        previous=lastEleInsortedArr

        while previous >= 0 and nums[previous]>temp:
            nums[previous+1]=nums[previous]
            previous -= 1
        nums[previous+1]=temp
        lastEleInsortedArr += 1

nums = [10, 8, 2, 14, 12, 7]

print("Before sorting:", nums)
 
performInsertionSort(nums)
 
print("After sorting:", nums)