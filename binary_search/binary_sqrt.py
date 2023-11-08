def isPerfectSquare(num: int) -> bool:
        left = 0
        right = num
        if num == 0:
            return True
        while left < right:
            mid = (left + right) // 2
            if mid*mid == num:
                return True
            elif mid*mid < num:
                left = mid + 1
            else:
                right = mid
        return False
print(isPerfectSquare(16))