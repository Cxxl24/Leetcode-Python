class Solution:
    def isValid(self, s : str) -> bool:
        if (len(s) % 2 != 0):
            return False

        stack = []
        for i in range(len(s)):
            stack[i] = s[i]

        for i in range(len(stack)):
            closing = stack.pop()
            if (closing == ']' and stack[i] != '['):
                return False
            elif (closing == '}' and stack[i] != '{'):
                  return False
            elif (closing == ')' and stack[i] != '('):
                return False
        return True
