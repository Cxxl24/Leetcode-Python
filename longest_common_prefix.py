class Solution:
    def longestCommonPrefix(self, strs : List[str]) -> str:
        if not strs:
            return ""

        output = ""
        first = strs[0]

        for i in range(len(first)):
            for s in strs:
                if i >= len(s) or s[i] != first[i]:
                    return output
            output += first[i]

        return output
