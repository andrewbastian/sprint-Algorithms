#### Please add your answers to the ***Analysis of  Algorithms*** exercises here.

## Exercise I

a) This algorithm has a linear runtime - *__O(n)__*.  As the length of n grows so will the runtime of the `while` loop. 


b) This algorithm has a quadradic runtime - *__O(n^2)__*.  I believe this would be the case because of the nested `while` statement.


c) This algorithm has a linear runtime - *__O(n)__*. The Algorithm's recursive function is dependant on the `len(n)` and will only run once

## Exercise II

##### Using a binary search:

> We set a midpoint variable == `len(f) // 2`

>We begin by dropping an egg at this midpoint variable

>> `if` the egg breaks, we move our pointer down one floor.

>>`if` the egg doesn't bread, we move our pointer up a floor.

> The answer is returned when the eggBreak value changes from that of the starting point.

* This algorithm would have an __O(log(n))__ run time because we are subdividing the `len(n)`. 
