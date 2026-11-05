class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        dict = {}
        for i, num in enumerate(nums):
            if num in dict:
                return True 
            else:
                dict[num] = i
        return False



        