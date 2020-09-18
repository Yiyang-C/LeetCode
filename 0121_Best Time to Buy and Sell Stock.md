# 121. Best Time to Buy and Sell Stock
## Easy
### Array/Dynamic Programming
#
Relative: 53, 122, 123, 188, 309
#

Say you have an array for which the ith element is the price of a given stock on day i.

If you were only permitted to complete at most one transaction (i.e., buy one and sell one share of the stock), design an algorithm to find the maximum profit.

Note that you cannot sell a stock before you buy one.

Example1:
> Input: [7,1,5,3,6,4]
> 
> Output: 5
>
> Explanation: Buy on day 2 (price = 1) and sell on day 5 (price = 6), profit = 6-1 = 5.
>
> Not 7-1 = 6, as selling price needs to be larger than buying price.

Example2:
> Input: [7,6,4,3,1]
> 
> Output: 0
>
> Explanation: In this case, no transaction is done, i.e. max profit = 0.

**My Note:**
* State Machine
* watch -> (buy) -> hold -> (sell) -> fin

Solution1:
*Time: O(n)*
*Space: O(1)*
```python
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        watch, hold, fin = 0, -float('inf'), 0
        for p in prices:
            pre_watch, pre_hold, pre_fin = watch, hold, fin
            watch = pre_watch
            hold = max(pre_hold, pre_watch - p)
            fin = max(pre_fin, pre_hold + p)
        return fin
```
