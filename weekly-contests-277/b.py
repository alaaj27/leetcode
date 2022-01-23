#5991. Rearrange Array Elements by Sign

class Solution(object):
    def rearrangeArray(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        pos = []
        neg = []

        l =[]
        for i in nums:
            if i<0 :
                neg.append(i)
            else:
                pos.append(i)

        countn = 0
        countp = 0
        for i in range (len (nums) ):
            if i% 2 == 0:
                l.append(pos[countp])
                countp +=1
            else:
                l.append(neg[countn])
                countn +=1

        return l
