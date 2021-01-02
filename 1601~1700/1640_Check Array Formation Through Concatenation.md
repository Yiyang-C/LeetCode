# 1640. Check Array Formation Through Concatenation
## Easy
### Array/Hash Table/Sort
#

You are given an array of **distinct** integers ```arr``` and an array of integer arrays ```pieces```, where the integers in ```pieces``` are **distinct**. Your goal is to form ```arr``` by concatenating the arrays in ```pieces``` **in any order**. However, you are **not** allowed to reorder the integers in each array ```pieces[i]```.

Return ```true``` *if it is possible to form the array ```arr``` from ```pieces```*. Otherwise, return ```false```.

Example1:
> Input: arr = [85], pieces = [[85]]
> 
> Output: true

Example2:
> Input: arr = [15,88], pieces = [[88],[15]]
> 
> Output: true
>
> Explanation: Concatenate [15] then [88]

Example3:
> Input: arr = [49,18,16], pieces = [[16,18,49]]
> 
> Output: false
>
> Explanation: Even though the numbers match, we cannot reorder pieces[0].

Example4:
> Input: arr = [91,4,64,78], pieces = [[78],[4,64],[91]]
> 
> Output: true
>
> Explanation: Concatenate [91] then [4,64] then [78]

Example5:
> Input: arr = [1,3,5,7], pieces = [[2,4,6,8]]
> 
> Output: false

**Constraints:** 
* ```1 <= pieces.length <= arr.length <= 100```
* ```sum(pieces[i].length) == arr.length```
* ```1 <= pieces[i].length <= arr.length```
* ```1 <= arr[i], pieces[i][j] <= 100```
* The integers in ```arr``` are **distinct**.
* The integers in ```pieces``` are **distinct** (i.e., If we flatten pieces in a 1D array, all the integers in this array are distinct).

**My Note:**
* Counting the correct numbers ```cnt```
* ```if cnt == len(arr): return True```

Solution1:
*Time: O(n)*
*Space: O(1)*
```python
class Solution:
    def canFormArray(self, arr: List[int], pieces: List[List[int]]) -> bool:
        cnt = 0
        for p in pieces:
            if p[0] in arr:
                idx = arr.index(p[0])
                for ch in p:
                    if idx >= len(arr):
                        return False
                    if ch == arr[idx]:
                        cnt += 1
                    idx += 1
        return cnt == len(arr)
```

**My Note:**
* Similar to solution1
* Using ```try: except:```

Solution2:
*Time: O(n)*
*Space: O(1)*
```python
class Solution:
    def canFormArray(self, arr: List[int], pieces: List[List[int]]) -> bool:
        for p in pieces:
            try:
                idx = arr.index(p[0])
                if not all([p[i] == arr[idx+i] for i in range(len(p))]):
                    return False
            except:
                return False
        return True
```
