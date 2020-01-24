#### Please add your answers to the **_Analysis of Algorithms_** exercises here.

## Exercise I

a)I believe it is a O(n!). The while loop will just keep going because a = 0 and will always be less then the number and doesn't have a break indicator.

b)I believe its is a O(n^2). It has to loops running on each other dependant on J varaiable.

c)I believe it is a 0(n). It just runs the operation once.

## Exercise II

I would first assume that the user can input a certain integer for how many stories this building has. I would write a function that allowed one paramater to passed in (n). I would then think of way how to determine a floor to throw the egg off by the n of stories in the building by user input to help mimimize the broken eggs. I would think dividing (n) by 3 and that number would be our F. If any egg was dropped below F then it would be safe. If it was dropped higher then F then it would break. I believe the time complexity for my solution would be 0(log n)
