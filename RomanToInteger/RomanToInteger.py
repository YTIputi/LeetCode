class Solution:
    def romanToInt(self, s: str) -> int:
        result = 0
        flagI, flagX, flagC = False, False, False
        for latter in s:
            if flagI:
                if latter == 'V':
                    result += -2
                elif latter == 'X':
                    result += -2
                flagI = False
            elif flagX:
                if latter == 'L':
                    result += -20
                elif latter == 'C':
                    result += -20
                flagX = False
            elif flagC:
                if latter == 'D':
                    result += -200
                elif latter == 'M':
                    result += -200
                flagC = False
            
            if latter == 'I':
                result += 1
                flagI = True
            elif latter == 'X':
                result += 10
                flagX = True
            elif latter == 'C':
                result += 100
                flagC = True
            elif latter == 'V':
                result += 5
            elif latter == 'L':
                result += 50
            elif latter == 'D':
                result += 500
            elif latter == 'M':
                result += 1000
        return result


s = Solution()
print(s.romanToInt('LVIII'))