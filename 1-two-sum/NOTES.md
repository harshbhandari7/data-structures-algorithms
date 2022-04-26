The most important thing to solve this problem in an optimized way is to understand the **Hash Map**.
​
​
Here, we calculate the difference of each element with the target and store it in the hash map.
​
​
Here, we iterate over the nums list and store the element and it's index in the hash map.
Before storing we also check the if the difference of the target and current element exist in hash map.
​
​
If the difference of the target and current element exists, it means the current element and the element found in the hash map adds upto the target, hence we return the value for the key corresponding to the difference of target and current element(which would be index of that element) and current element's index.