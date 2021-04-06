class Solution(object):
    def numIdenticalPairs(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        cnt=0
        for i in range(0,len(nums)):
            j=i+1
            for j in range (j,len(nums)):
                if nums[i]==nums[j]:
                    cnt+=1
            i+=1
        return cnt