class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # 3 numbers can be sorted into red, white, blue 0->2. Size=3

        red, white, blue = 0, 0, len(nums) - 1 # 0-indexed
        # These are also sometimes referred to as low, mid, high...

        # Double arrow-style methodology
        while white <= blue:
            if(nums[white]==0):
                nums[white], nums[red] = nums[red], nums[white]
                white += 1
                red += 1
            elif(nums[white]==1):
                white +=1

            else: # nums[white==2]
                nums[white], nums[blue] = nums[blue], nums[white]
                blue -= 1

        # Loop complete

        