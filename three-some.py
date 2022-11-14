from itertools import combinations
class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        lst = []
        for i in combinations(nums, 3):
            if(sum(list(i))==0):
                lst.append(list(i))
        return lst
            
sol = Solution().threeSum([-1,0,1,2,-1,-4])
print(sol)