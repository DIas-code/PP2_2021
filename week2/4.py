class Solution(object):
    def largestAltitude(self, gain):
        """
        :type gain: List[int]
        :rtype: int
        """
        mx=0
        al=0
        for i in range (0, len(gain)):
            al+=gain[i]
            if mx<al:
                mx=al
        return mx