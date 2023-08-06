import itertools

from runtests.mpi import MPITest

import pybnb

from .common import mpi_available

def left_child(i):
    return 2*i + 1

def right_child(i):
    return 2*i + 2

def log2floor(n):
    assert n > 0
    return n.bit_length() - 1

def height(size):
    return log2floor(size)

def set_none(heap, i):
    if i < len(heap):
        heap[i] = None
        set_none(heap, left_child(i))
        set_none(heap, right_child(i))

def set_one(heap, i):
    if i < len(heap):
        if heap[i] is not None:
            heap[i] = 1
            set_one(heap, left_child(i))
            set_one(heap, right_child(i))

def is_terminal(heap, i):
    N = len(heap)
    c1 = left_child(i)
    c2 = right_child(i)
    return ((c1 >= N) or (heap[c1] is None)) and \
           ((c2 >= N) or (heap[c2] is None))

def get_bound(heap, how=min):
    N = len(heap)
    assert N >= 1
    assert heap[0] is not None
    terminal_bounds = []
    for i in range(N):
        if (heap[i] is not None) and is_terminal(heap, i):
            terminal_bounds.append(heap[i])
    return how(terminal_bounds)

def powerset(iterable):
    s = list(iterable)
    return itertools.chain.from_iterable(itertools.combinations(s, r) for r in range(len(s)+1))

def gen_heaps(k):
    for heap_size in range(1,2**(k+1)):
        h = height(heap_size)
        for level_none in range(h,h+1):
            level_nodes = list(filter(lambda x: x < heap_size,
                                      range((2**level_none)-1,(2**(level_none+1))-1)))
            for none_list in sorted(powerset(level_nodes)):
                if len(none_list) == len(level_nodes):
                    continue
                heap_master = [0]*heap_size
                for i in none_list:
                    set_none(heap_master, i)
                for level in range(0,h+1):
                    nodes = filter(lambda x: (x < heap_size) and (heap_master[x] is not None),
                                   range((2**level)-1,(2**(level+1))-1))
                    for nodes_list in sorted(powerset(nodes)):
                        if (len(nodes_list) == 0) and \
                           level != 0:
                            continue
                        heap = [0]*heap_size
                        for i in none_list:
                            set_none(heap, i)
                        for i in nodes_list:
                            set_one(heap, i)
                        yield heap

class Discrete(pybnb.Problem):

    def __init__(self,
                 sense,
                 objectives,
                 bound_bheap,
                 default_objective):
        assert len(bound_bheap) >= 1
        self._sense = sense
        self._objectives = objectives
        self._bound_bheap = bound_bheap
        self._default_objective = default_objective
        self._heap_idx = 0

    #
    # Implement Problem abstract methods
    #

    def sense(self):
        return self._sense

    def objective(self):
        return self._objectives.get(self._heap_idx,
                                    self._default_objective)

    def bound(self):
        return self._bound_bheap[self._heap_idx]

    def save_state(self, node):
        node.state = self._heap_idx

    def load_state(self, node):
        self._heap_idx = node.state

    def branch(self):
        i = self._heap_idx
        assert i >= 0
        assert i < len(self._bound_bheap)
        left_idx =  2*i + 1
        if (left_idx < len(self._bound_bheap)) and \
           (self._bound_bheap[left_idx] is not None):
            child = pybnb.Node()
            child.state = left_idx
            yield child
        right_idx = 2*i + 2
        if (right_idx < len(self._bound_bheap)) and \
           (self._bound_bheap[right_idx] is not None):
            child = pybnb.Node()
            child.state = right_idx
            yield child

class SmallHeap(pybnb.Problem):
    def __init__(self):
        self._heap_index = 0
        self._max_heap_index = 4
    def sense(self):
        return pybnb.minimize
    def objective(self):
        if self._heap_index == 0:
            return 3
        elif self._heap_index in (1,2):
            return 2
        elif self._heap_index == 3:
            return 0
        else:
            assert self._heap_index == 4
            return 1
    def bound(self):
        if self._heap_index == 0:
            return -3
        elif self._heap_index in (1,2):
            return -2
        else:
            assert self._heap_index in (3,4)
            return -1
    def save_state(self, node):
        node.state = self._heap_index
    def load_state(self, node):
        self._heap_index = node.state
    def branch(self):
        i = self._heap_index
        assert 0 <= i <= self._max_heap_index
        left_index =  2*i + 1
        if left_index <= self._max_heap_index:
            child = pybnb.Node()
            child.state = left_index
            yield child
        right_index = 2*i + 2
        if right_index <= self._max_heap_index:
            child = pybnb.Node()
            child.state = right_index
            yield child

def _test_heaps(comm):
    solver = pybnb.Solver(comm=comm)
    if comm is not None:
        if comm.rank == 0:
            pass
        elif comm.rank == 1:
            pass
        elif comm.rank == 3:
            pass

    problem = SmallHeap()
    results = solver.solve(problem,
                           queue_strategy='breadth')
    assert results.solution_status == "feasible"
    assert results.termination_condition == "queue_empty"
    assert results.objective == 0
    assert results.bound == -2
    assert results.best_node.objective == 0
    assert results.best_node.bound == -1
    assert results.best_node.state == 3
    _uuid = results.best_node._uuid
    queue = solver.save_dispatcher_queue()
    if solver.is_dispatcher:
        assert queue.bound() == -2
        assert queue.worst_terminal_bound == -2
        assert len(queue.nodes) == 0
    results = solver.solve(problem,
                           initialize_queue=queue,
                           best_node=results.best_node)
    assert results.solution_status == "feasible"
    assert results.termination_condition == "queue_empty"
    assert results.objective == 0
    assert results.bound == -2
    assert results.best_node.objective == 0
    assert results.best_node.bound == -1
    assert results.best_node.state == 3
    assert results.best_node._uuid == _uuid
    queue = solver.save_dispatcher_queue()
    if solver.is_dispatcher:
        assert queue.bound() == -2
        assert queue.worst_terminal_bound == -2
        assert len(queue.nodes) == 0

    for heap in gen_heaps(2):
        heap_bound = get_bound(heap)
        node_list = [None, len(heap)] + \
            [i for i in range(len(heap))
             if heap[i] is not None]
        # min
        for objective_node in node_list:
            if objective_node is not None:
                problem = Discrete(
                    pybnb.minimize,
                    {objective_node: 1},
                    heap,
                    default_objective=2)
            else:
                problem = Discrete(
                    pybnb.minimize,
                    {},
                    heap,
                    default_objective=1)
            results = solver.solve(problem, log=None)
            if objective_node == len(heap):
                assert results.objective == 2
            else:
                assert results.objective == 1
            assert results.bound == heap_bound
        # max
        heap_bound = -heap_bound
        heap = [-b_ if (b_ is not None) else None
                for b_ in heap]
        for objective_node in node_list:
            if objective_node is not None:
                problem = Discrete(
                    pybnb.maximize,
                    {objective_node: -1},
                    heap,
                    default_objective=-2)
            else:
                problem = Discrete(
                    pybnb.maximize,
                    {},
                    heap,
                    default_objective=-1)
            results = solver.solve(problem, log=None)
            if objective_node == len(heap):
                assert results.objective == -2
            else:
                assert results.objective == -1
            assert results.bound == heap_bound

def test_heaps_nocomm():
    _test_heaps(None)

if mpi_available:

    @MPITest(commsize=[1, 2, 4])
    def test_heaps_comm(comm):
        _test_heaps(comm)
