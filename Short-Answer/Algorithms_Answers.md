#### Please add your answers to the ***Analysis of  Algorithms*** exercises here.

## Exercise I

a)
This while loop would be O(n).
The reason for this is with each increment, n^2 is also being added on to var a, and this basically cancels out the conditional a < n^3 into a < n^1

b)
Function b is O(n log n).
The parent for loop is O(n), and the nested while loop forms a multiplication relationship with the for loop. This would normally be O(n), but since J is being doubled in each WHILE iteration, the runtime complexity ends up being log n.

Multiplying the complexity of the for loop, 'n', with the nested while loop, 'log n', gives us the runtime complexity of O(n log n)

c)
Function C is O(n)
The reason for this is for n bunnies, the function will recursively call itself, decrementing the bunnies by 1 each time, until bunnies == 0.
The only other part to this function is an if statement checking if bunnies == 0, which is O(1), so we can drop the constant and get the runtime complexity of O(n)

## Exercise II

Pseudocode follows:

def egg_breaker(n_stories, lower_bound = 0 (ground floor), upper_bound = len(n_stories) ):
   
   if lower_bound is equal to upper_bound:
      return either of the values. this is the floor we are looking for.
   
   else:

   middle = (lower + upper bounds) / 2

   if the egg breaks on this middle floor, 
      we're too high up, try the lower half of floors
      return egg_breaker(n_stories, lower_bound, upper_bound = middle) --- now we're only dropping the egg from the lower half of floors
   
   else if the egg doesn't break:
      we're too low, try upper half of floors
      return egg_breaker(n_stories, lower_bound = middle, upper_bound) --- opposite, dropping eggs from higher up


Runtime complexity of O(log n) since we're basically halving our input each time. Binary search!




