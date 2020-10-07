from Population import Population

def foo(a,b,c):
    return a*b*c

paras = ['a', 'b', 'c']

expected_val = 27

# Initiate a Population object
Ooh = Population(1, 20, [0,0,0], [5,5,5])
max_generation = 5

for i in range(max_generation):
    print('---')
    print(Ooh)
    # Apply a math function to the Population
    Ooh.apply_func(foo,paras)
    # Apply a test to the Population
    Ooh.apply_test(expected_val)
    # Sort by score from highest to lowest
    Ooh.sort_by_score()
    # Show top 1
    Ooh.show_top_one()
    # Invoke an event
    print('Event natural death occurred')
    Ooh.event()
    # Live on
    print('The population evolved')
    Ooh.live_on()
