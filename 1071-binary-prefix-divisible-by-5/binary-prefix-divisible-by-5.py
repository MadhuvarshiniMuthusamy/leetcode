class Solution:
    def prefixesDivBy5(self, nums: List[int]) -> List[bool]:
        res=[]
        rem=0
        for i in nums:
            rem=(rem*2+i)%5
            res.append(rem==0)
        return res