#Count Elements With Strictly Smaller and Greater Elements:

#Given an integer array nums, return the number of elements that have
#both a strictly smaller and a strictly greater element appear in nums.



def findL (nums , n):
    for i in nums:
        if i < n:
            return True
    return False


def findG (nums , n ):
    for i in nums:
        if i > n:
            return True
    return False


class Solution(object):
    def countElements(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        count = 0

        for n in range (len (nums)) :
            if  findL(nums, nums[n]) and  findG(nums, nums[n]) :
                count +=1


        return count
