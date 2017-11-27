from Graph import *
class Problem():
    def __init__(self, *args, **kwargs):
        self.blocks = [
            [0, 1, 1, 0],
            [0, 0, 1, 0],
            [0, 1, 1, 0],   
            [0, 1, 0, 0],
            [1, 1, 1, 0],
        ]

    def initial_state(self):
        return (0,0)


    def actions(self,state,straight=True):
        result = []
        if state[0] - 1 >= 0 and (self.blocks[state[1]][state[0] - 1] or self.is_goal_test((state[0] - 1, state[1]))):
            result.append('left')
        if state[0] + 1 < len(self.blocks[0]) and (self.blocks[state[1]][state[0] + 1] != 0 or self.is_goal_test((state[0] + 1, state[1]))):
            result.append('right')
        if state[1] - 1 >= 0 and (self.blocks[state[1]-1][state[0]] != 0 or self.is_goal_test((state[0], state[1]-1))):
            result.append('up')
        if state[1] + 1 < len(self.blocks) and (self.blocks[state[1] + 1][state[0]] != 0 or self.is_goal_test((state[0], state[1] + 1))):
            result.append('down')
        second_res = [self.result(state,x) for x in result]
        return second_res

    def result(self,state,action):
        actions = {
            'up': (state[0], state[1] - 1),
            'down': (state[0], state[1] + 1),
            'right': (state[0] + 1, state[1]),
            'left': (state[0] - 1, state[1])
            }
        return actions[action]

    def is_goal_test(self,state):
        return state == (len(self.blocks[0])-1,len(self.blocks)-1)

    
    def goal_tests(self):
        return [
            (len(self.blocks[0])-1,len(self.blocks)-1)
        ]

    def path_cost():
        return 0

    def edge_cost(self,father_state,child_state):
        return 1

    def heuristic(self,state):
        return (len(self.blocks[0]) - state[0]) + (len(self.blocks) - state[1])


p = Problem()
g = Graph(p)
g.UCS_graph_search(p.initial_state())
g.A_Star_graph_search(p.initial_state())
g.bidirectional_graph_search(p.initial_state(),p.goal_tests()[0])
