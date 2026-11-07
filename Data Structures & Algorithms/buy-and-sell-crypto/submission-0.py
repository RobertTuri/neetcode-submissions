class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        """
        Must remember to account for only going forward.
        Can do a simple keep or discard method...
        Outputting profit by finding their index in array.
        """
        # 'Brute Force' Approach.
        dict = {} # May not need
        bestProfit = 0
        lowest = 100 # Starting with 'worst-case'
        
        for i, num in enumerate(prices):
            if num < lowest:
                lowest = num
            else:
                bestProfit = max(num - lowest, bestProfit)

        return bestProfit 
            




        