# 1094. Car Pooling
## Medium
### Greedy
#
Relative: 253
#

You are driving a vehicle that has ```capacity``` empty seats initially available for passengers.  The vehicle **only** drives east (ie. it **cannot** turn around and drive west.)

Given a list of ```trips```, ```trip[i] = [num_passengers, start_location, end_location]``` contains information about the ```i```-th trip: the number of passengers that must be picked up, and the locations to pick them up and drop them off.  The locations are given as the number of kilometers due east from your vehicle's initial location.

Return ```true``` if and only if it is possible to pick up and drop off all passengers for all the given trips. 

Example1:
> Input: trips = [[2,1,5],[3,3,7]], capacity = 4
> 
> Output: false

Example2:
> Input: trips = [[2,1,5],[3,3,7]], capacity = 5
> 
> Output: true

Example3:
> Input: trips = [[2,1,5],[3,5,7]], capacity = 3
> 
> Output: true

Example4:
> Input: trips = [[3,2,7],[3,7,9],[8,3,9]], capacity = 11
> 
> Output: true

**Constraints:** 
1. ```trips.length <= 1000```
2. ```trips[i].length == 3```
3. ```1 <= trips[i][0] <= 100```
4. ```0 <= trips[i][1] < trips[i][2] <= 1000```
5. ```1 <= capacity <= 100000```

**My Note:**
* Sort ```trips``` by start_location
* For each location #passenger must be smaller than capacity
* Using dictionary to store the #passenger of each location

Solution1:
*Time: O(nlogn)*
*Space: O(n)*
```python
class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        trips.sort(key= lambda x: x[1])
        d = {}
        # print(trips)
        for trip in trips:
            c, s, e = trip
            if c > capacity:
                return False
            for i in range(s, e):
                if i in d:
                    d[i] += c
                    if d[i] > capacity:
                        return False
                else:
                    d[i] = c
        return True
```

**My Note:**
* Using min-heap to store the information of trips

Solution2:
*Time: O(n)*
*Space: O(n)*
```python
class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        heap = []
        for c, s, e in trips:
            heapq.heappush(heap, (e, -n))
            heapq.heappush(heap, (s, n))
        while heap:
            capacity -= heapq.heappop(heap)[1]    
            if 0 > capacity:
                return False
        return True
```
