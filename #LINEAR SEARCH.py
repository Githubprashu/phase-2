#LINEAR SEARCH

nums=[0,10,20,30,40,50]
target=40
flag=-1
n=len(nums)
for index in range(n):
    if nums[index]==target:
        flag=index
        break
if flag==-1:
    print("not found")
else:
    print("target found at:",flag)