# 735. Asteroid Collision
## Medium
### Stack
#
Relative: 605
#

We are given an array ```asteroids``` of integers representing asteroids in a row.

For each asteroid, the absolute value represents its size, and the sign represents its direction (positive meaning right, negative meaning left). Each asteroid moves at the same speed.

Find out the state of the asteroids after all collisions. If two asteroids meet, the smaller one will explode. If both are the same size, both will explode. Two asteroids moving in the same direction will never meet.

Example1:
> Input: asteroids = [5,10,-5]
> 
> Output: [5,10]
>
> Explanation: The 10 and -5 collide resulting in 10.  The 5 and 10 never collide.

Example2:
> Input: asteroids = [8,-8]
> 
> Output: []
>
> Explanation: The 8 and -8 collide exploding each other.

Example3:
> Input: asteroids = [10,2,-5]
> 
> Output: [10]
>
> Explanation: The 2 and -5 collide resulting in -5. The 10 and -5 collide resulting in 10.

Example4:
> Input: asteroids = [-2,-1,1,2]
> 
> Output: [-2,-1,1,2]
>
> Explanation: The -2 and -1 are moving left, while the 1 and 2 are moving right. Asteroids moving the same direction never meet, so no asteroids will meet each other.

**Constraints:** 
* ```1 <= asteroids <= 10^4```
* ```-1000 <= asteroids[i] <= 1000```
* ```asteroids[i] != 0```

<details><summary>Hint1</summary>
    Say a row of asteroids is stable. What happens when a new asteroid is added on the right?
    </details>

**My Note:**
* Typical Stack Problem
* Using a stack to keep the result after collisions.

Solution1:
*Time: O(n)*
*Space: O(n)*
```python
class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        s = []
        for cur in asteroids:
            while s and s[-1] > 0 and cur < 0:
                tmp = s.pop()
                if abs(tmp) < abs(cur):
                    continue
                if abs(tmp) > abs(cur):
                    cur = tmp
                    break
                if abs(tmp) == abs(cur):
                    cur = None
                    break
            if cur:
                s.append(cur)
        return s
```
