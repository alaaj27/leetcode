#Find All Lonely Numbers in the Array


import collections


class Solution(object):
    def findLonely(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        lonely=[]
        freq = collections.Counter(nums)

        for n in nums:

            if freq[n] == 1 and freq[n-1]==0 and freq[n+1]==0:
                lonely.append(n)

        
        return lonely
