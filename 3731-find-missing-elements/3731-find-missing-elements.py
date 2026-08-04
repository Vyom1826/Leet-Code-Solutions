class Solution:
    def findMissingElements(self, nums):
        s = set(nums)
        ans = []

        start = min(nums)
        end = max(nums)

        for i in range(start, end + 1):
            if i not in s:
                ans.append(i)

        return ans