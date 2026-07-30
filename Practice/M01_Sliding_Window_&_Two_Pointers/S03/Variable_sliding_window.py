from typing import List

def minSubArrayLen(target: int, nums: List[int]) -> int:
    left = 0
    curr_sum = 0
    min_length = float('inf')

    for right in range(len(nums)):
        curr_sum += nums[right]

        while curr_sum >= target:
            min_length = min(min_length, right - left + 1)
            curr_sum -= nums[left]
            left += 1

    return min_length if min_length != float('inf') else 0


# Input
target = 7
nums = [2, 3, 1, 2, 4, 3]

# Function call
result = minSubArrayLen(target, nums)
print(result)
        

class Solution:
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
        if k <= 1:
            return 0
        left = 0
        prod = 1
        count = 0
        for right in range(len(nums)):
            prod *= nums[right]
            while prod >= k:
                prod //= nums[left]
                left += 1
            count += right - left + 1
        return count