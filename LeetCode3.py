class Solution:
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        d = {}
        head = L =  0
        for i, t in enumerate(s):
            if t in d:
                L = max(L, i - head)
                head = max(head, d[t] + 1)
            d[t] = i

        return max(L, len(s) - head)