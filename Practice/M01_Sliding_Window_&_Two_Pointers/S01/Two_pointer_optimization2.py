'''Remove Duplicates from Sorted Array
from typing import List

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if not nums:
            return 0

        k = 1

        for i in range(1, len(nums)):
            if nums[i] != nums[i - 1]:
                nums[k] = nums[i]
                k += 1

        return k
nums = [0,0,1,1,1,2,2,3,3,4]
print(removeDuplicates(nums))  # Output: 5


Remove Element
class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        k = 0
        for i in range(len(nums)):
            if nums[i] != val:
                nums[k] = nums[i]
                k += 1
        return k
nums = [3,2,2,3]
val = 3
print(removeElement(nums, val))  # Output: 2
'''