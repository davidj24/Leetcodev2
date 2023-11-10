class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        y = list(reversed(str(x)))
        z = ""
        for i in range(len(y)):
            z += y[i]
        try:    
            (int(z))
        except ValueError:
            return False
        else:
            if (int(z) == x):
                return True
            else:
                return False
        

