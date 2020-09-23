# 134. Gas Station
## Medium
### Greedy
#

There are N gas stations along a circular route, where the amount of gas at station i is ```gas[i]```.

You have a car with an unlimited gas tank and it costs ```cost[i]``` of gas to travel from station i to its next station (i+1). You begin the journey with an empty tank at one of the gas stations.

Return the starting gas station's index if you can travel around the circuit once in the clockwise direction, otherwise return -1.

**Note:**
* If there exists a solution, it is guaranteed to be unique.
* Both input arrays are non-empty and have the same length.
* Each element in the input arrays is a non-negative integer.

Example1:
> Input: 
>
> gas  = [1,2,3,4,5]
>
> cost = [3,4,5,1,2]
>
> Output: 3
>
> Explanation: 
>
> Start at station 3 (index 3) and fill up with 4 unit of gas. Your tank = 0 + 4 = 4
>
> Travel to station 4. Your tank = 4 - 1 + 5 = 8
>
> Travel to station 0. Your tank = 8 - 2 + 1 = 7
>
> Travel to station 1. Your tank = 7 - 3 + 2 = 6
>
> Travel to station 2. Your tank = 6 - 4 + 3 = 5
>
> Travel to station 3. The cost is 5. Your gas is just enough to travel back to station 3.
>
> Therefore, return 3 as the starting index.

Example2:
> Input: 
>
> gas  = [2,3,4]
>
> cost = [3,4,3]
>
> Output: -1
>
> Explanation: 
>
> You can't start at station 0 or 1, as there is not enough gas to travel to the next station.
>
> Let's start at station 2 and fill up with 4 unit of gas. Your tank = 0 + 4 = 4
>
> Travel to station 0. Your tank = 4 - 3 + 2 = 3
>
> Travel to station 1. Your tank = 3 - 3 + 3 = 3
>
> You cannot travel back to station 2, as it requires 4 unit of gas but you only have 3.
>
> Therefore, you can't travel around the circuit once no matter where you start.

**My Note:**
* Iterate the start_id
* For each start_id calculate if it can return to it

Solution1:
*Time: O(n^2)*
*Space: O(1)*
```python
class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        for start_id in range(len(gas)):
            have_gas = gas[start_id]
            i = start_id + 1
            f = 0
            if i == len(gas):
                i = 0
                f = 1
            while True:
                # print(start_id, i, have_gas)
                if not i:
                    have_gas -= cost[-1]
                else:
                    have_gas -= cost[i-1]
                if have_gas < 0:
                    # f = 1
                    break
                have_gas += gas[i]
                i += 1
                if i == len(gas):
                    i = 0
                if i == start_id+1 or (f and not i):
                    return start_id
        return -1
```

**My Note:**
* Rewrite the solution1

Solution2:
*Time: O(n^2)*
*Space: O(1)*
```python
class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        for i in range(len(gas)):
            init_id = j = i
            have_gas = gas[j] - cost[j]
            if have_gas < 0:
                continue
            j += 1
            while have_gas >= 0:
                if j == len(gas):
                    j = 0
                if j == init_id:
                    return init_id
                have_gas += (gas[j] - cost[j])
                j += 1
        return -1
```

**My Note:**
* **First check the sum of ```gas``` and ```cost```**
* Append the first item to itself in both ```gas``` and ```cost```
* Iterate the idx to calculate if it can make a circuit

Solution2:
*Time: O(n)*
*Space: O(1)*
```python
class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        if sum(gas) < sum(cost):
            return -1
        have_gas = idx = 0
        gas.append(gas[0])
        cost.append(cost[0])
        for i in range(len(gas)):
            have_gas += gas[i] - cost[i]
            if have_gas < 0:
                idx = i + 1
                have_gas = 0
        if idx >= len(gas) - 1:
            return -1
        return idx
```

