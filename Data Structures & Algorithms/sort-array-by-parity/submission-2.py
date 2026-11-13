class Solution:
    def sortArrayByParity(self, nums: List[int]) -> List[int]:
        # Any array means asc/desc order NOT required.
        # 2 possible options, mod(x) = 0 or 1 (even or odd)

        read, write = 0, len(nums)-1 # Classic start/end pointer logic

        while read < write:
            # Even first 
            if nums[read] % 2 == 1:
                # read is pointing at even number swap with 
                nums[read], nums[write] = nums[write], nums[read]
                write -= 1 

            else:
                # read is pointing at an odd number
                read += 1

        return nums
                

        