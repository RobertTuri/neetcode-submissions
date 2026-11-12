class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dict = {}
        for i, num in enumerate(nums):
            compliment = target - num
            if compliment in dict:
                return [dict[compliment], i]
            else:
                dict[num] = i
            
            # It should return assuming there IS a pair which exists.

        