from src.easy.two_sum import Solution

# data
nums = [2, 7, 11, 15]
target = 9
expected_result = [0, 1]


def test_solution():
    two_sum = Solution()
    result = two_sum.two_sum(nums, target)
    assert result == expected_result
