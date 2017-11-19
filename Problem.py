class Problem():
    def initial_state(self):
        return (0,0)
    def actions(self,state):
        result_states = []
        result_states.append((4, state[1]))
        result_states.append((state[0], 3))
        result_states.append((0, state[1]))
        result_states.append((state[0], 0))
        result_states.append((state[0], 0))
        result_states.append((min(4, state[0] + state[1]), state[0] + state[1] - min(4, state[0] + state[1])))
        result_states.append((state[0] + state[1] - min(3, state[0] + state[1]), min(3, state[0] + state[1])))
        return list(set(result_states))
    def goal_test(self,state):
        return state[0] == 2
    def path_cost():
        return 0
