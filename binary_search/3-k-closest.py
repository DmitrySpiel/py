arr = [1,2,3,4,5]
k = 4
x = 3

if k >= len(arr):
    print(arr)
left = 0
right = len(arr) - 1
while left + 1 < right:
    mid = (left + right) // 2
    if arr[mid] == x:
        res = [x]
        for i in range(1, k):
            print("ind:" + str(mid + i))
            if(mid+i >= len(arr)-1 or mid-i < 0):
                print(abs(arr[mid-i]))
                print(abs(arr[mid+i]))
                if abs(arr[mid-i]) != abs(arr[mid+i]):
                    s = min(abs(arr[mid-i] - x), abs(arr[mid+i]- x))
                    res.append(s)
                else:
                    s = min(abs(arr[mid-i]),abs(arr[mid+i]))
                    res.append(s)
                left = mid
    elif arr[mid] < x:
        left = mid
    else:
        right = mid
print(res)