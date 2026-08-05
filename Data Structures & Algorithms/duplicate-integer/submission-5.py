class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        s=[]
        for i in range(len(nums)):
                if nums[i] in s:
                    return(True)
                else: 
                    s=s+[nums[i]]
        return (False)