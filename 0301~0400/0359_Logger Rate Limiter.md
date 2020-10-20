# 359. Logger Rate Limiter
## Easy
### Hash Table/Design
#
Relative: 362
#

Design a logger system that receive stream of messages along with its timestamps, each message should be printed if and only if it is **not printed in the last 10 seconds**.

Given a message and a timestamp (in seconds granularity), return true if the message should be printed in the given timestamp, otherwise returns false.

It is possible that several messages arrive roughly at the same time.

Example1:
> Logger logger = new Logger();
>
> </br>
> // logging string "foo" at timestamp 1
>
> logger.shouldPrintMessage(1, "foo"); returns true; 
>
> </br>
> // logging string "bar" at timestamp 2
>
>logger.shouldPrintMessage(2,"bar"); returns true;
>
> </br>
> // logging string "foo" at timestamp 3
>
> logger.shouldPrintMessage(3,"foo"); returns false;
>
> </br>
> // logging string "bar" at timestamp 8
>
> logger.shouldPrintMessage(8,"bar"); returns false;
>
> </br>
> // logging string "foo" at timestamp 10
>
> logger.shouldPrintMessage(10,"foo"); returns false;
>
> </br>
> // logging string "foo" at timestamp 11
>
> logger.shouldPrintMessage(11,"foo"); returns true;

**My Note:**
* Using dictionary to store the timestamp of messages

Solution1:
*Time: O(1)*
*Space: O(n)*
```python
class Logger:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.log = {}

    def shouldPrintMessage(self, timestamp: int, message: str) -> bool:
        """
        Returns true if the message should be printed in the given timestamp, otherwise returns false.
        If this method returns false, the message will not be printed.
        The timestamp is in seconds granularity.
        """
        if message not in self.log:
            self.log[message] = timestamp
            return True
        else:
            if timestamp - self.log[message] >= 10:
                self.log[message] = timestamp
                return True
            else:
                return False


# Your Logger object will be instantiated and called as such:
# obj = Logger()
# param_1 = obj.shouldPrintMessage(timestamp,message)
```
