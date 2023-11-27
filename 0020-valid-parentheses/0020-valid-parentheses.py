from collections import deque
class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        if len(s) % 2 != 0:
            return False
        stack = deque()
        for i in range(len(s)):
            if s[i] == "(" or s[i] == "[" or s[i] == "{":
                stack.append(s[i])
                continue
            if len(stack) == 0:
                return False
            if stack[-1] == "(" and s[i] == ")":
                stack.pop()
            elif stack[-1] == "[" and s[i] == "]":
                stack.pop()
            elif stack[-1] == "{" and s[i] == "}":
                stack.pop()
            elif s[i] == ")" or s[i] == "]" or s[i] == "}":
                return False
        if len(stack) != 0:
            return False
        else:
            return True