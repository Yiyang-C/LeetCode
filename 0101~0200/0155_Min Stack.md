# 155. Min Stack
## Easy
### Stack/Design
#
Relative: [239](https://github.com/Yiyang-C/LeetCode/blob/master/0201~0300/0239_Sliding%20Window%20Maximum.md), 716
#

Design a stack that supports push, pop, top, and retrieving the minimum element in constant time.

* push(x) -- Push element x onto stack.
* pop() -- Removes the element on top of the stack.
* top() -- Get the top element.
* getMin() -- Retrieve the minimum element in the stack.

Example1:
> Input
>
> ["MinStack","push","push","push","getMin","pop","top","getMin"]
>
> [[],[-2],[0],[-3],[],[],[],[]]
>
></br>
> Output
>
> [null,null,null,null,-3,null,0,-2]
>
></br>
> Explanation
> 
> MinStack minStack = new MinStack();
>
> minStack.push(-2);
>
> minStack.push(0);
>
> minStack.push(-3);
>
> minStack.getMin(); // return -3
>
> minStack.pop();
>
> minStack.top();    // return 0
>
> minStack.getMin(); // return -2

**Constraints:** 
* Methods ```pop```, ```top``` and ```getMin``` operations will always be called on **non-empty** stacks.

<details><summary>Hint1</summary>
Consider each node in the stack having a minimum value.
</details>

**My Note:**
* Using a stack and a heap to keep the numbers

Solution1:
```push```*Time: O(logn)*
```pop```*Time: O(nlogn)*
```top```*Time: O(1)*
```getMin```*Time: O(1)*
```python
class MinStack:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.s = []
        self.h = []

    def push(self, x: int) -> None:
        self.s.append(x)
        heapq.heappush(self.h, x)

    def pop(self) -> None:
        tmp = self.s.pop()
        self.h.remove(tmp)
        heapq.heapify(self.h)

    def top(self) -> int:
        return self.s[-1]

    def getMin(self) -> int:
        return self.h[0]


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(x)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()
```

**My Note:**
* Stack with (cur_number, min_num) inside

Solution2:
```push```*Time: O(1)*
```pop```*Time: O(1)*
```top```*Time: O(1)*
```getMin```*Time: O(1)*
```python
class MinStack:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.s = []

    def push(self, x: int) -> None:
        if not self.s:
            self.s.append((x, x))
        elif x < self.s[-1][1]:
            self.s.append((x, x))
        else:
            self.s.append((x, self.s[-1][1]))

    def pop(self) -> None:
        self.s.pop()

    def top(self) -> int:
        return self.s[-1][0]

    def getMin(self) -> int:
        return self.s[-1][1]


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(x)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()
```
