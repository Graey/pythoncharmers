# Genetic Algorithm
## Requirements
Trust me, I use purely Python 3 to implement this algorithm. You should read [this](https://en.wikipedia.org/wiki/Genetic_algorithm) and read [that](https://www.sciencedirect.com/topics/engineering/genetic-algorithm) for more details on this algorithm. If you don't want to read these, just Google the term `Genetic Algorithm`.

## A simple diagram
by me.
```
      +-----------------------+
      | Initiate a population |
      +-----------------------+
              |
      +-------v----------+
  +-->+ Apply a function |
  |   +------------------+
  |           |
  |   +-------v------+
  |   | Apply a test |
  |   +--------------+
  |           |
  |   +-------v--------------------------------+
  |   | Sort individuals descending by score   |
  |   +----------------------------------------+
  |           |
  |   +-------v---------------+
  |   | Kill some individuals |
  |   +-------+---------------+
  |           |
  |   +-------v---------------+
  +---+ Evolve the population |
      +-----------------------+
```

Stop this population growing at step `Sort individuals descending by score` to get your answer.

## A simple implementation
Note:
  - This only works __with__ math functions __not__ class constructors.
  - You can find this implementation in `Example.py` file.

Problem: find values of a, b, c such that `27 = a*b*c` for a, b, c belong to set R.

```Python
def foo(a,b,c):
    return a*b*c

paras = ['a', 'b', 'c']
expected_val = 27
```

```Python
from Population import Population
# Initiate a Population with id = 1, size = 20
# with lower bound [0,0,0] and upper bound = [5,5,5]
# (the range of a, b, c)
Ooh = Population(1, 20, [0,0,0], [5,5,5])
max_generation = 5
```
```Python
for i in range(max_generation):
    print('---')
    # Apply a math function to the Population
    Ooh.apply_func(foo,paras)

    # Apply a test to the Population
    Ooh.apply_test(expected_val)

    # Sort by score from highest to lowest
    Ooh.sort_by_score()

    # Show top 1
    Ooh.show_top_one()

    # Invoke an event to kill some individuals
    Ooh.event()

    # Evolve the Population
    Ooh.live_on()
```
