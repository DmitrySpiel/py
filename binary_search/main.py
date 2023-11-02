nums = [-1,0,3,5,9,12]
target = 2

start = 0
end = len(nums) - 1

while start <= end:
    mid = (start+end)//2
    if nums[mid] < target:
        start = mid + 1
    elif nums[mid] > target:
        end = mid - 1
    else:
        print(mid)
        break
print(-1)