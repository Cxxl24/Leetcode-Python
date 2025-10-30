from typing import List

class Solution:
    def longestCommonPrefix(self, strs : List[str]) -> str:
        result = ""
        strs.sort()
        for i in range(len(strs[0])):
            if (strs[len(strs) - 1][i] != None):
                if (strs[0][i] != strs[len(strs)-1][i]):
                    return result
                else:
                    result += strs[0][i]
            else:
                return result
        return result
