class Solution:
    @staticmethod
    def is_palindrome(x: int) -> bool:
        if x < 0:
            return False
        if x < 10:
            return True
        if x % 10 == 0:
            return False
        final = 0
        original = x
        while x != 0:
            final = x % 10 + final * 10
            x = x // 10
        if final == original:
            return True
