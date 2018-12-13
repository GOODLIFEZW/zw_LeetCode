class Solution:
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        max = 2 ** 31 -1
        min = -1 * 2 ** 31
        res = 0
        if x >= 0:
            res = int(str(x)[::-1])
        else:
            res = -1 * int(str(0 - x)[::-1])
        if res < min or res > max:
            return 0
        
        return res