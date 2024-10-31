class Solution:
    def isValid(self, s: str) -> bool:
        if len(s) == 1:
            return False
        stack = []
        for latter in s:
            if latter in "({[":
                stack.append(latter)
            elif stack:
                lastLatter = stack.pop()
                if lastLatter == '(' and latter == ')':
                    continue
                elif lastLatter == '{' and latter == '}':
                    continue
                elif lastLatter == '[' and latter == ']':
                    continue
                else:
                    return False
            else:
                return False
        return not stack

s = Solution()
print(s.isValid("()"))