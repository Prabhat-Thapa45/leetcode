from typing import List


class Solution:
    def two_sum(self, nums: List[int], target: int) -> List[int]:
        number_of_elements = len(nums)
        for i in range(number_of_elements):
            for j in range(i+1, number_of_elements):
                if nums[i] + nums[j] == target:
                    return [i, j]


two_sum = Solution()
print(two_sum.two_sum([3, 3], 6))
