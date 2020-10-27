# 239. Sliding Window Maximum
## Hard
### Heap/Sliding Window
#
Relative: 76, [155](https://github.com/Yiyang-C/LeetCode/blob/master/0101~0200/0155_Min%20Stack.md), 159, 265
#

You are given an array of integers ```nums```, there is a sliding window of size ```k``` which is moving from the very left of the array to the very right. You can only see the ```k``` numbers in the window. Each time the sliding window moves right by one position.

Return *the max sliding window*.

Example1:
> Input: nums = [1,3,-1,-3,5,3,6,7], k = 3
> 
> Output: [3,3,5,5,6,7]
>
> Explanation: 
>
|Window position|Max|
|:---------------|:-----:|
|[1  3  -1] -3  5  3  6  7      |3|
|1 [3  -1  -3] 5  3  6  7       |3|
|1  3 [-1  -3  5] 3  6  7       |5|
|1  3  -1 [-3  5  3] 6  7       |5|
|1  3  -1  -3 [5  3  6] 7       |6|
|1  3  -1  -3  5 [3  6  7]      |7|

Example2:
> Input: nums = [1], k = 1
> 
> Output: [1]

Example3:
> Input: nums = [1,-1], k = 1
> 
> Output: [1,-1]

Example4:
> Input: nums = [9,11], k = 2
> 
> Output: [11]

Example5:
> Input: nums = [4,-2], k = 2
> 
> Output: [4]

**Constraints:** 
* ```1 <= nums.length <= 10^5```
* ```-10^4 <= nums[i] <= 10^4```
* ```1 <= k <= nums.length```

<details><summary>Hint1</summary>
How about using a data structure such as deque (double-ended queue)?</details>

<details><summary>Hint2</summary>
The queue size need not be the same as the window’s size.</details>

<details><summary>Hint3</summary>
Remove redundant elements and the queue should store only elements that need to be considered.</details>

**My Note:**
* Using deque to store the index of num
* Only store the index of the largest nums in deque
* Rember to popleft when window slides away
* Append the res when reach the size of k

Solution1:
*Time: O(n)*
*Space: O(k)*
```python
class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        res = []
        dq = collections.deque()
        for i, num in enumerate(nums):
            while dq and num > nums[dq[-1]]:
                dq.pop()
            dq.append(i)
            if i - dq[0] >= k:
                dq.popleft()
            if i >= k - 1:
                res.append(nums[dq[0]])
        return res
```
