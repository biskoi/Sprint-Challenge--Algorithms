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


