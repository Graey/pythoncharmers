from Individual import Individual
import random

class Population:
    def __init__(self, id, size, lower_inps, upper_inps):
        # id : (int) population's id
        # size : (int) how many individual objects in this population
        # lower_inps : (list) list of lower-boundary inputs
        # upper_inps : (list) list of upper-boundary inputs
        self.id = id
        self.size = size
        self.lower_inps = lower_inps
        self.upper_inps = upper_inps
        self.generation = 0
        self.Individuals = []
        for i in range(self.size):
            inps = []
            for lower_inp, upper_inp in zip(lower_inps, upper_inps):
                inps.append(round(random.uniform(lower_inp, upper_inp),5))

            self.Individuals.append(Individual(inps))

        return None

    def __str__(self):
        # Pretty print of Population object
        return 'Id: '+str(self.id)+'\nSize: '+str(self.size)+'\nGeneration: '+str(self.generation)+'\nFrom '+str(self.lower_inps)+' to '+str(self.upper_inps)

    def show_individuals(self):
        if self.size == 0:
            print('The population is totally annihilated', sep = '\n')
        else:
            print(*self.Individuals, sep = '\n')

        return None

    def show_top_one(self):
        if self.size == 0:
            print('The population is totally annihilated', sep = '\n')
        else:
            print('Top 1 '+str(self.Individuals[0]))

        return None

    def show_top(self, percentage = 10):
        if self.size == 0:
            print('The population is totally annihilated', sep = '\n')
        else:
            percentage = percentage/100
            if int(len(self.Individuals)*percentage) >= 1:
                print(*self.Individuals[:int(len(self.Individuals)*percentage)], sep = '\n')
            else:
                self.show_individuals()


        return None

    def apply_func(self, func, paras):
        for indiv_obj in self.Individuals:
            if indiv_obj.val == None:
                indiv_obj.apply_func(func, paras)


        return None

    def apply_test(self, expected_val):
        for indiv_obj in self.Individuals:
            indiv_obj.test_score(expected_val)

        return None

    def sort_by_score(self):
        self.Individuals = sorted(self.Individuals, key = lambda Indiv: Indiv.score, reverse = True)
        return None

    def flatten_individual(self, indiv_obj):
        for i in range(len(indiv_obj.inps)):
            if indiv_obj.inps[i] < self.lower_inps[i]:
                indiv_obj.inps[i] = self.lower_inps[i]

            if indiv_obj.inps[i] > self.upper_inps[i]:
                indiv_obj.inps[i] = self.upper_inps[i]


        return indiv_obj

    def flatten(self):
        for indiv_obj in self.Individuals:
            indiv_obj = self.flatten_individual(indiv_obj)

        return None

    def event_kill_bot(self, percentage):
        # Annihilate Individuals objects that are in bottom
        self.sort_by_score()
        self.Individuals = self.Individuals[:int(len(self.Individuals)/100*(100-percentage))]
        self.size = len(self.Individuals)
        return None

    def event_balance(self):
        self.Individuals = random.sample(self.Individuals, int(len(self.Individuals)/2))
        self.size = len(self.Individuals)
        return None

    def event(self, mode = 'natural_death'):
        if mode == 'natural_death':
            self.event_kill_bot(10) # Should kill 10% bot

        if mode == 'poverty':
            self.event_kill_bot(25) # Should kill 25% bot

        if mode == 'plague':
            self.event_kill_bot(50) # Should kill 50% bot

        if mode == 'war':
            self.event_kill_bot(75) # Should kill 75% bot

        if mode == 'nuclear_war':
            self.event_kill_bot(90) # Should kill 90% bot

        if mode == 'Thanos':
            self.event_balance() # Should kill 50% randomly

        return None

    def live_on(self, type = 'tiny'):
        if type == 'massive':
            for i in range(len(self.Individuals)-1):
                for ii in range(i+1, len(self.Individuals)):
                    self.Individuals.append(Individual.breed(self.Individuals[i],self.Individuals[ii]))

        if type == 'tiny':
            for i in range(len(self.Individuals)-1):
                self.Individuals.append(Individual.breed(self.Individuals[i],self.Individuals[i+1]))

        for indiv_obj in self.Individuals:
            indiv_obj.evolve()

        self.flatten()
        self.generation = self.generation+1
        self.size = len(self.Individuals)
        return None
