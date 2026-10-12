class Solution(object):
    def runningSum(self, nums):
        sum = 0 
        arr = []
        for i in range(0,len(nums)):
            sum = sum + nums[i]
            arr.append(sum)
        return arr