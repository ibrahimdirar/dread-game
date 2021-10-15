# dread-game
Discord bot that simulates pulling from a Jenga tower for Dread.
Virtual tower starts with a Big Frightening Number (BFN) of 100.
Each pull from the tower is accomplished by generating two random numbers between 1 and 100. The lowest of these two numbers is compared to the BFN. If it is lower, you have succesfully pulled from the tower and completed your task. However, the BFN is reduced by the number rolled divided by 10, rounded up.

This increases tension.

If it is larger than the BFN, this counts as the tower falling over. The player that pulled the block is marked as dead. The tower is rebuilt and remaining players must pull from the tower as per usual Dread rules.

# Statistics
## Summary
### Death Pulls
Mean: 11.5\
Standard deviation: 4.5\
Number of trials: 10,000,000

### Big Freaking Number At Death
Mean: 59.5\
Standard deviation: 13.2\
Number of trials: 1,000,000

## Workings
```python
import seaborn as sns
import random

num_reps = 1000000
tower_standing = True
death_pulls_list = []
big_frightening_number_list = []

for i in range(0, num_reps):
    death_pulls = 0
    big_frightening_number = 100
    while True:
        roll = min(random.randint(1,100), random.randint(1,100))
        if roll > big_frightening_number:
            death_pulls_list.append(death_pulls)
            big_frightening_number_list.append(big_frightening_number)
            break
        else:
            death_pulls += 1
            big_frightening_number-=(roll+9)//10
```


```python
ax = sns.histplot(death_pulls_list, discrete=True)

ax.set(xlabel="Pulls until death", ylabel="Trials")
```




    [Text(0.5, 0, 'Pulls until death'), Text(0, 0.5, 'Trials')]


    
![svg](https://raw.githubusercontent.com/ibrahimdirar/dread-game/main/statsbook/dread-game-statsbook_1_1.svg)
    



```python
import statistics
print(f'Std Dev: {round(statistics.stdev(death_pulls_list),1)}, mean: {round(statistics.mean(death_pulls_list),1)}')
```

    Std Dev: 4.5, mean: 11.6
    


```python
ax = sns.histplot(bfn_list, discrete=True)
ax.set(xlabel="BFN at death", ylabel="Trials")
```




    [Text(0.5, 0, 'BFN at death'), Text(0, 0.5, 'Trials')]




    
![svg](https://raw.githubusercontent.com/ibrahimdirar/dread-game/main/statsbook/dread-game-statsbook_3_1.svg)
    


```python
import statistics
print(f'Std Dev: {round(statistics.stdev(bfn_list),1)}, mean: {round(statistics.mean(bfn_list),1)}')
```

    Std Dev: 13.2, mean: 59.5
    


```python

```
