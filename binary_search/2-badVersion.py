#isBadVersion def is not defined here.this is an example to be used in the

class Solution:
    def firstBadVersion(self, n: int) -> int:

        left, right = 0, n
        while left < right:
            mid = (left + right) // 2
            if isBadVersion(mid):
                right = mid
            else:
                left = mid + 1

        # Post-processing:
        # End Condition: left == right
        if isBadVersion(left):
            return left
        return -1