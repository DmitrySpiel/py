start = 0
end = x
while start <= end:
    mid = (start+end)//2
    if mid*mid == x:
        ans = mid
        print(ans)
    elif mid*mid < x:
        start = mid + 1
        ans = mid
    else:
        end = mid - 1
increment = 0.1
for i in range(0, 5):
    while (ans * ans <= x):
        ans += increment

    # loop terminates when ans * ans > number
    ans = ans - increment
    increment = increment / 10
    
print(int(ans))