class Solution:
    def romanToInt(self, s : str) -> int:
        sum = 0
        romanMap = {'I' : 1, 'V' : 5, 'X' : 10, 'L' : 50, 'C' : 100, 'D' : 500, 'M' : 1000}
        for i in range(len(s) - 1):
            if (romanMap[s[i]] < romanMap[s[i+1]]):
                sum -= romanMap[s[i]]
            else:
                sum += romanMap[s[i]]
        sum += romanMap[s[len(s) - 1]]
        return sum
