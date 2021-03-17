# dread-game
Discord bot that simulates pulling from a Jenga tower for Dread.
Virtual tower start with a Big Frightening Number (BFN) of 100
Each pull from the tower is accomplished by generating two random numbers between 1 and 100. The lowest of these two numbers is compared to the BFN. If it is lower, you have succesfully pulled from the tower and completed your task. However, the BFN is reduced by the number rolled divided by 10, rounded up.

This increases tension.

If it is larger than the BFN, this counts as the tower falling over. The player that pulled the block is marked as dead. The tower is rebuilt and remaining players must pull from the tower as per usual Dread rules.
