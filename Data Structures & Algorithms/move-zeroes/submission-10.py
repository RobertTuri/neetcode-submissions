class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        write = 0 
        for read in range(len(nums)):
            if nums[read] != 0:
                # non-0 present so we must swap + shift right to left
                # Here we can do bitwise left operation
                nums[write], nums[read] = nums[read], nums[write]
                write += 1





        

        