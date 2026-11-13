class Solution:
    def sortColors(self, nums: List[int]) -> None:
        # We will use placeholders for red , white and blue
        # Pointers (penultimate will be dynamic)
        low, mid, high = 0, 0, len(nums) - 1

        # Not using built in sorting algorithms
        # Finite options of 0, 1, 2...
        while mid <= high: 
            if nums[mid] == 2:
                # Must be shifted to the top
                nums[mid], nums[high] = nums[high], nums[mid]
                high -= 1 

            elif nums[mid] == 0:
                # Must be swapped with low
                nums[low], nums[mid] = nums[mid], nums[low]
                low += 1
                mid += 1 # logically mid must shift also?

            else:  
                # its a 1
                mid += 1

        