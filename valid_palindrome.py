class Solution:
    def isPalindrome(self, s : str) -> bool:
        res = ''
        s = s.lower()
        for c in s:
            if (c.isalnum()):
                res += c

        if (res == ''):
            return True

        for i in range(len(res) // 2):
            if (res[i] != res[len(res) - i - 1]):
                return False
        return True
