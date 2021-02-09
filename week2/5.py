class Solution(object):
    def subtractProductAndSum(self, n):
        """
        :type n: int
        :rtype: int
        """
        n=str(n)
        prd=1
        sm=0
        for i in range(0, len(n)):
            
            prd*=int(n[i])
            sm+=int(n[i])
        return prd-sm