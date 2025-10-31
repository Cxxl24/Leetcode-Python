class Solution:
    def isValid(self, s : str) -> bool:
        stack = []
        opening_braces = ['{', '[', '(']
        for i in range(len(s)):
            if (s[i] in opening_braces):
                stack.append(s[i])
            else:
                if (not stack):
                    return False
                if (s[i] == '}'):
                    if (stack.pop() != '{'):
                        return False
                elif (s[i] == ']'):
                    if (stack.pop() != '['):
                        return False
                elif (s[i] == ')'):
                    if (stack.pop() != '('):
                        return False
        return len(stack) == 0
