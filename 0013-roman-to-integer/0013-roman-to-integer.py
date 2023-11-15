class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        assign_nums = {
            "I" : 1,
            "V" : 5,
            "X" : 10,
            "L" : 50,
            "C" : 100,
            "D" : 500,
            "M" : 1000
        }
        result = 0
        i = 0
        while i < (len(s) -1):
            if assign_nums[s[i]] < assign_nums[s[i+1]]:
                result += (assign_nums[s[i+1]] - assign_nums[s[i]])
                i += 2
            else:
                result += assign_nums[s[i]]
                i += 1
        if assign_nums[s[len(s)-1]] > assign_nums[s[len(s) -2]]:
            return result
        else:
            result += assign_nums[s[len(s)-1]]
        return result