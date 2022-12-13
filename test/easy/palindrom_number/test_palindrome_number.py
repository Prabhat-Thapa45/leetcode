from easy.palindrom_number.palindrome_number import Solution

# data
nums = 121
expected_result = True


def test_solution():
    palindrome_number = Solution()
    result = palindrome_number.is_palindrome(nums)
    assert result == expected_result
