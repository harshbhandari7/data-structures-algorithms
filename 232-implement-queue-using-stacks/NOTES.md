here, **2 stack implementation** is better.
​
Reason being:
​
When there's only one thread doing the read/write operation to the stack, there will always one stack empty. However, in a multi-thread application, if we have only one queue, for thread-safety, either read or write will lock the whole queue. In the two stack implementation, as long as the second stack is not empty, push operation will not lock the stack for pop.
​
​