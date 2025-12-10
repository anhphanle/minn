from typing import List

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        """
        PROBLEM: Maximize profit by choosing a single day to buy and a different day in the future to sell.
        METHOD: O(n) Time, O(1) Space. Sliding Window (Two Pointers). 
        Left pointer `l` is buy day, Right `r` is sell day. If `price[l] < price[r]`, calculate profit. If `price[r]` is lower, update `l` to `r` (new low found).
        """
        l, r = 0, 1 # l = buy, r = sell
        maxP = 0
        
        while r < len(prices):
            # Is this a profitable transaction?
            if prices[l] < prices[r]:
                profit = prices[r] - prices[l]
                maxP = max(maxP, profit)
            else:
                # We found a new lower price, so shift buy pointer to current sell pointer
                l = r
            r += 1
            
        return maxP

# --- Main Execution ---
if __name__ == "__main__":
    sol = Solution()
    
    # Test Case 1: Standard case (Buy at 1, Sell at 6)
    prices1 = [7, 1, 5, 3, 6, 4]
    print(f"Test 1: {sol.maxProfit(prices1)}") # Expected: 5

    # Test Case 2: Prices only go down (No profit possible)
    prices2 = [7, 6, 4, 3, 1]
    print(f"Test 2: {sol.maxProfit(prices2)}") # Expected: 0

    # Test Case 3: Small variation
    prices3 = [2, 4, 1]
    print(f"Test 3: {sol.maxProfit(prices3)}") # Expected: 2 (Buy at 2, Sell at 4)