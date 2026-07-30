from collections import defaultdict
from typing import List
class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        count = defaultdict(int)
        left = 0
        max_fruits = 0
        for right in range(len(fruits)):
            count[fruits[right]] += 1
            while len(count) > 2:
                count[fruits[left]] -= 1
                if count[fruits[left]] == 0:
                    del count[fruits[left]]
                left += 1
            max_fruits = max(max_fruits, right - left + 1)  
        return max_fruits

# Input
fruits = [1, 2, 1, 2, 3]                            
print(Solution().totalFruit(fruits))  # Output: 4