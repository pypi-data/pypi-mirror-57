import pybnb

class UnboundedMax(pybnb.Problem):

    #
    # Implement Problem abstract methods
    #

    def sense(self): return pybnb.maximize
    def objective(self): return self.unbounded_objective()
    def bound(self): return self.unbounded_objective()
    def save_state(self, node): pass
    def load_state(self, node): pass
    def branch(self): raise NotImplementedError()
