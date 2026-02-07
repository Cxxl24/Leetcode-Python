class Solution:
    def lengthOfLastWord(self, s : str) -> int:
        s.strip()
        output = s.split()
        if not output:
            return 0

        return (len(output[len(output) - 1]))
