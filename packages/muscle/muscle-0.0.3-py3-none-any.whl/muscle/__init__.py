class Reps:
    def __init__(self, name, reps, rampup=0.0):
        self.rampup = rampup
        self.name = name
        self.reps = reps
    def program(self, strategy, weight, step):
        l = len(self.reps)
        f = 1.0 - (l*self.rampup)
        reps = []
        for r in self.reps:
            f = f + self.rampup
            w = round(float(weight * strategy['ratio'] * f)/step) * step
            reps.append({'reps': r, 'weight': w})
        return reps

class Sets:
    """Sets logic containing a set of Reps logic objects."""
    def __init__(self, name, reps):
        self.name = name
        self.data = {}
        for r in reps:
            self.data[r.name] = r
    def program(self, strategy, weight, step):
        return self.data[strategy['reps']].program(strategy, weight, step)

class Modulation:
    """ Modulation logic containing a list of Set rules."""
    def __init__(self,sets):
        self.data = {}
        for s in sets:
            self.data[s.name] = s
    def program(self, strategy, weight, step):
        return self.data[strategy['sets']].program(strategy, weight, step)

class Exercise:
    """ Exercise to perform.
    An exercise has a name, a weight unit ('Kg' by default), weight
    increment step (5 by default), sets and reps that are set by
    using a Modulation object.
    """
    def __init__(self, name, modulation=None, unit="Kg", step=5):
        self.name = name
        self.sets = {}
        self.reps =  {}
        self.set_modulation(modulation)
        self.set_step(step)
        self.unit = unit
    def set_modulation(self, m):
        self.modulation = m
    def set_step(self,v):
        self.step = v
    def set_one_rep_max(self,v):
        self.orm = v
    def program(self,strategy):
        data = self.modulation.program(strategy, self.orm, self.step)
        return {'exercise':self.name,
                'sets':data,
                'unit':self.unit,
                'obj':self}

class Group:
    """ Group a list of Exercises or other Groups.
    A group will apply the training program on any contained items
    using a defined sets or reps selected and a weight ratio.
    """
    def __init__(self, name=None, sets_selector=None, reps_selector=None,
            ratio=1.0, fixed_ratio=0, plan=None):
        self.name = name
        self.sets_selector = sets_selector
        self.reps_selector = reps_selector
        self.ratio = ratio
        self.fixed_ratio = fixed_ratio
        self.parts = {}
        self.plan(plan)
    def plan(self, l):
        if l:
            for i in l:
                self.parts[i.name] = [i]
        return self
    def program(self, strategy):
        tmp = strategy.copy()
        self.augment(tmp)
        ret = {}
        for p in self.parts:
            ret[p] = []
            for k in self.parts[p]:
                data = k.program(tmp)
                ret[p].append(data)
        return ret
    def augment(self, strategy):
        if self.sets_selector:
            strategy['sets'] = self.sets_selector
        if self.reps_selector:
            strategy['reps'] = self.reps_selector
        if self.fixed_ratio>0:
            strategy['ratio'] = self.fixed_ratio
        else:
            strategy['ratio'] = strategy['ratio'] * self.ratio
    def print_block(d, level=0):
        for k in d:
            if k=='exercise':
                reps = []
                for r in d['sets']:
                    reps.append('%d x %.1f%s' %(r['reps'], r['weight'],d['unit']))
                print('\t'*(level), ' | '.join(reps))
                break
            else:
                print('\t'*level, k)
                for v in d[k]:
                    print_block(v, level+1)


def print_block(d, level=0):
    for k in d:
        if k=='exercise':
            reps = []
            for r in d['sets']:
                reps.append('%d x %.1f%s' %(r['reps'], r['weight'],d['unit']))
            print('\t'*(level), ' | '.join(reps))
            break
        else:
            print('\t'*level, k)
            for v in d[k]:
                print_block(v, level+1)

def exercises(d):
    for k in d:
        if k=='exercise':
            yield(d)
            break
        else:
            for v in d[k]:
                yield from exercises(v)

