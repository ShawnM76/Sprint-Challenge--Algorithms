#### Please add your answers to the **_Analysis of Algorithms_** exercises here.

## Exercise I

a)O(n) Loop is bassed on n

b)O(n^2) cause it keeps looping until J equals to n

c)O(n) its Recursion calling on itself

## Exercise II

- This function will take 1 parameter as n for the number of stories in a building
- We can assume the array is sorted starting from 1 story going up to n number of stories
- I would try a binary search way. Start off by dividing the number of stories n//2
- Then check if the egg breaks
- If it does break then repeat that process with n that is divided by 2 at the begging of the length of the building.
- We should by then reach a story that will not break the egg.
- It would be 0(log(n))
