class Solution(object):
    def findDisappearedNumbers(self, nums):
        num = set(nums)
        x = []
        for i in range(1, len(nums) + 1):
            if i not in num:
                x.append(i)
        return x
