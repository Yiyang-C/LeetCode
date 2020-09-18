# 1041. Robot Bounded In Circle
## Medium
### Math
#

On an infinite plane, a robot initially stands at ```(0, 0)``` and faces north.  The robot can receive one of three instructions:

* ```"G"```: go straight 1 unit;
* ```"L"```: turn 90 degrees to the left;
* ```"R"```: turn 90 degress to the right.

The robot performs the ```instructions``` given in order, and repeats them forever.

Return ```true``` if and only if there exists a circle in the plane such that the robot never leaves the circle.

Example1:
> Input: "GGLLGG"
> 
> Output: true
>
> Explanation: The robot moves from (0,0) to (0,2), turns 180 degrees, and then returns to (0,0).
When repeating these instructions, the robot remains in the circle of radius 2 centered at the origin.

Example2:
> Input: "GG"
> 
> Output: false
>
> Explanation: The robot moves north indefinitely.

Example3:
> Input: "GL"
> 
> Output: true
>
> Explanation: The robot moves from (0, 0) -> (0, 1) -> (-1, 1) -> (-1, 0) -> (0, 0) -> ...

**Note:** 
1. ```1 <= instructions.length <= 100```
2. ```instructions[i] is in {'G', 'L', 'R'}```

**My Note:**
* Three posible loops that robot is bound in circle
* First, the robot return to start point in one instruction
* The robot return to start point in two instructions
* The robot return to start point in four instructions
![](https://assets.leetcode.com/users/lee215/image_1557633739.png)

Solution1:
*Time: O(n)*
*Space: O(1)*
```python
class Solution:
    def isRobotBounded(self, instructions: str) -> bool:
        x, y = 0, 0
        dx, dy = 0, 1
        for i in instructions * 4:
            if i == 'G':
                x += dx
                y += dy
            elif i == 'L':
                dx, dy = -dy, dx
            elif i == 'R':
                dx, dy = dy, -dx
        return (x, y) == (0, 0)
```
