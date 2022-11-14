class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        dick = {}
        for ind, val in enumerate(nums):
            if target-val in dick:
                return dick[target-val], ind
            dick.setdefault(val, ind)
obj = Solution().twoSum( [2,7,11,15], 9)
print(obj)