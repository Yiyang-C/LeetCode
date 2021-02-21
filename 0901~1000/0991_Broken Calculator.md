# 991. Broken Calculator
## Medium
### Math/Greedy
#
Relative: 650
#

On a broken calculator that has a number showing on its display, we can perform two operations:
* **Double**: Multiply the number on the display by 2, or;
* **Decrement**: Subtract 1 from the number on the display.

Initially, the calculator is displaying the number ```X```.

Return the minimum number of operations needed to display the number ```Y```.

Example1:
> Input: X = 2, Y = 3
> 
> Output: 2
>
> Explanation: Use double operation and then decrement operation {2 -> 4 -> 3}.

Example2:
> Input: X = 5, Y = 8
> 
> Output: 2
>
> Explanation: Use decrement and then double {5 -> 4 -> 8}.

Example3:
> Input: X = 3, Y = 10
> 
> Output: 3
>
> Explanation: Use double, decrement and double {3 -> 6 -> 5 -> 10}.

Example4:
> Input: X = 1024, Y = 1
> 
> Output: 1023
>
> Explanation: Use decrement operations 1023 times.

**Note:** 
* ```1 <= X <= 10^9```
* ```1 <= Y <= 10^9```

**My Note:**
* From Y to X
* Recursive

Solution1:
*Time: O(n)*
*Space: O(1)*
```python
class Solution:
    def brokenCalc(self, X: int, Y: int) -> int:
        if X >= Y:
            return X - Y
        if Y % 2 == 0:
            return self.brokenCalc(X, Y//2) + 1
        else:
            return self.brokenCalc(X, Y + 1) + 1
```

**My Note:**
* From Y to X
* While loop

Solution2:
*Time: O(n)*
*Space: O(1)*
```python
class Solution:
    def brokenCalc(self, X: int, Y: int) -> int:
        if Y <= X:
            return X - Y
        cnt = 0
        while Y > X:
            if Y % 2 == 0:
                Y //= 2
            else:
                Y += 1
            cnt += 1
        return cnt + X - Y
```
