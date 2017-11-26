class Problem():


    def initial_state(self):
        return (0,0)


    def actions(self,state,straight=True):
        result_states = []
        if straight:
            result_states.append((4, state[1]))
            result_states.append((state[0], 3))
            result_states.append((0, state[1]))
            result_states.append((state[0], 0))
            result_states.append((min(4, state[0] + state[1]), state[0] + state[1] - min(4, state[0] + state[1])))
            result_states.append((state[0] + state[1] - min(3, state[0] + state[1]), min(3, state[0] + state[1])))
            return list(set(result_states))
        if state[0] == 0:
            result_states.append((4, state[1]))
        if state[1] == 0:
            result_states.append((state[0], 3))
        if state[0] == 4:
            result_states.append((0, state[1]))
        if state[1] == 3:
            result_states.append((state[0], 0))
        result_states.append((min(4, state[0] + state[1]), state[0] + state[1] - min(4, state[0] + state[1])))
        result_states.append((state[0] + state[1] - min(3, state[0] + state[1]), min(3, state[0] + state[1])))
        return list(set(result_states))


    def is_goal_test(self,state):
        return state[0] == 2

    
    def goal_tests(self):
        return [
            (2,0),
            (2,1),
            (2,2),
            (2,3),
        ]

    def path_cost():
        return 0

    def edge_cost(father_state,child_state):
        return 1
