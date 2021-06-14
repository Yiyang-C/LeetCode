# 1710. Maximum Units on a Truck
## Eazy
### Greedy/Sort

You are assigned to put some amount of boxes onto **one truck**. You are given a 2D array ```boxTypes```, where ```boxTypes[i] = [numberOfBoxesi, numberOfUnitsPerBoxi]```:

* ```numberOfBoxesi``` is the number of boxes of type ```i```.
* ```numberOfUnitsPerBoxi``` is the number of units in each box of the type ```i```.

You are also given an integer ```truckSize```, which is the **maximum** number of **boxes** that can be put on the truck. You can choose any boxes to put on the truck as long as the number of boxes does not exceed ```truckSize```.

*Return the **maximum** total number of **units** that can be put on the truck.*

Example1:
> Input: boxTypes = [[1,3],[2,2],[3,1]], truckSize = 4
> 
> Output: 8
> 
> Explanation: There are:
> - 1 box of the first type that contains 3 units.
> - 2 boxes of the second type that contain 2 units each.
> - 3 boxes of the third type that contain 1 unit each.
> 
> You can take all the boxes of the first and second types, and one box of the third type.
> 
> The total number of units will be = (1 * 3) + (2 * 2) + (1 * 1) = 8.



Example2:
> Input: boxTypes = [[5,10],[2,5],[4,7],[3,9]], truckSize = 10
> 
> Output: 91

**Constraints:** 
* ```1 <= boxTypes.length <= 1000```
* ```1 <= numberOfBoxesi, numberOfUnitsPerBoxi <= 1000```
* ```1 <= truckSize <= 10^6```

<details><summary>Hint1</summary>
If we have space for at least one box, it's always optimal to put the box with the most units.
</details>
<br>
<details><summary>Hint2</summary>
Sort the box types with the number of units per box non-increasingly.
</details>
<br>
<details><summary>Hint3</summary>
Iterate on the box types and take from each type as many as you can.
</details>
<br>

**My Note:**
* Sort ```boxTypes``` by ```numberOfUnitsPerBoxi```
* Conduct Greedy Algorithm

Solution:
*Time: O(nlogn)*
*Space: O(1)*
```python
class Solution:
    def maximumUnits(self, boxTypes: List[List[int]], truckSize: int) -> int:
        boxTypes.sort(key=lambda x: x[1], reverse=True)
        max_unit = 0
        while boxTypes:
            num_box, num_unit_per_box = boxTypes.pop(0)
            while num_box and truckSize:
                max_unit += num_unit_per_box
                truckSize -= 1
                num_box -= 1
        return max_unit
```
