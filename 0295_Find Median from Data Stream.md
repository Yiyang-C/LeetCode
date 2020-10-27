# 295. Find Median from Data Stream
## Hard
### Heap/Design
#
Relative: 480
#

Median is the middle value in an ordered integer list. If the size of the list is even, there is no middle value. So the median is the mean of the two middle value.

For example,

```[2,3,4]```, the median is ```3```

```[2,3]```, the median is ```(2 + 3) / 2 = 2.5```

Design a data structure that supports the following two operations:

* void addNum(int num) - Add a integer number from the data stream to the data structure.
* double findMedian() - Return the median of all elements so far.

Example:
> addNum(1)
>
> addNum(2)
>
> findMedian() -> 1.5
>
> addNum(3) 
>
> findMedian() -> 2 


**Follow up:** 
* If all integer numbers from the stream are between 0 and 100, how would you optimize it?
* If 99% of all integer numbers from the stream are between 0 and 100, how would you optimize it?

**My Note:**
* Using list to store the numbers
* Using bisect.insort to insert the number in to list
* Keeping the numbers in list in order
* Return the medium in the middle of lsit
* Keep in mind that the O(log n) search is dominated by the slow O(n) insertion step.

Solution1:
```addNum```*Time: O(n)*
```findMedian```*Time: O(1)*
```python
class MedianFinder:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.l = []

    def addNum(self, num: int) -> None:
        bisect.insort(self.l, num)
        # print(self.l)

    def findMedian(self) -> float:
        if len(self.l) % 2 == 1:
            return self.l[len(self.l) // 2]
        else:
            return (self.l[len(self.l) // 2] + self.l[(len(self.l) // 2) - 1]) / 2


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()
```

**My Note:**
* Two heap solution
* Length of two heaps is the same or ```len(self.minh) = len(self.maxh) + 1```

Solution2:
```addNum```*Time: O(logn)*
```findMedian```*Time: O(1)*
```python
class MedianFinder:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.minh = []
        self.maxh = []

    def addNum(self, num: int) -> None:
        if not self.minh:
            heapq.heappush(self.minh, num)
        elif not self.maxh:
            if num < self.minh[0]:
                heapq.heappush(self.maxh, -num)
            else:
                heapq.heappush(self.minh, num)
                heapq.heappush(self.maxh, -heapq.heappop(self.minh))   
        elif len(self.minh) == len(self.maxh):
            if num < self.minh[0]:
                heapq.heappush(self.maxh, -num)
                heapq.heappush(self.minh, -heapq.heappop(self.maxh))
            else:
                heapq.heappush(self.minh, num)
        else:
            if num < self.minh[0]:
                heapq.heappush(self.maxh, -num)
            else:
                heapq.heappush(self.minh, num)
                heapq.heappush(self.maxh, -heapq.heappop(self.minh))
        # print(self.maxh, self.minh)

    def findMedian(self) -> float:
        if not self.minh:
            return 0
        if not self.maxh:
            return self.minh[0]
        if len(self.minh) != len(self.maxh):
            return self.minh[0]
        return (self.minh[0] - self.maxh[0]) / 2


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()
```
