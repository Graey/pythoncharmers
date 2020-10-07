import random

class Individual:
    def __init__(self, inps):
        # inps : a list of inputs
        self.inps = inps
        self.val = None
        self.score = 0.0
        return None

    def __str__(self):
        # Pretty print of Individual object
        return 'Individual: '+str(self.inps)+'. Val: '+str(self.val)+'. Score: '+str(self.score)

    def apply_func(self, func, paras):
        bar_str = ''
        for para, inp in zip(paras, self.inps):
            bar_str = bar_str + para+'='+str(inp)+','

        self.val = round(eval('func('+bar_str[:-1]+')'),5)
        return None

    def test_score(self, expected_val):
        percentage = round((self.val/expected_val)*100,5)
        if percentage < 0:
            self.score = 0.0
        else:
            if percentage > 100:
                if 200-percentage < 0:
                    self.score = 0.0
                else:
                    self.score = round(200-percentage,5)

            else:
                self.score = percentage

        return None

    @classmethod
    def breed(cls, indiv_obj_1, indiv_obj_2, type = 'single'):
        if type == 'single':
            new_inps = []
            for inp_1, inp_2 in zip(indiv_obj_1.inps, indiv_obj_2.inps):
                new_inp = ((inp_1+inp_2)/2)+random.uniform(-0.1,0.1)
                new_inps.append(round(new_inp,5))

            return Individual(new_inps)
        else:
            return None


    def evolve(self):
        self.inps = [round(inp+random.uniform(-0.1,0.1),5) for inp in self.inps]
        return None
