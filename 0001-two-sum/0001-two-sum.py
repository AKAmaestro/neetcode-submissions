class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        len=0
        for i in nums:
            len = len+1
        
        for i in range(len-1):
            for j in range(i+1,len):
                # print(nums[i] +' , ' + nums[j]+" = "+ (nums[i]+nums[j]))
                if ((nums[j]+nums[i])==target):
                    return ([i,j])
        return[]
                