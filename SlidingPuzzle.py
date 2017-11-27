from Graph import *
class Problem():

    def initial_state(self):
        return ((3,1,2),
                (4,0,7),
                (6,8,5)
                )


    def actions(self,state,straight=True):
        from copy import deepcopy as copy
        def find_zero(state):
            for row in state:
                row_index = state.index(row)
                for element in row:
                    col_index = row.index(element)
                    if element == 0:
                        return row_index,col_index
        result_states = []
        row_index,col_index = find_zero(state)
        state = list(list(row) for row in state)
        if row_index > 0:
            tmp_state = copy(state)
            tmp_state[row_index][col_index], tmp_state[row_index - 1][col_index] = tmp_state[row_index - 1][col_index], tmp_state[row_index][col_index]
            result_states.append(tuple(tuple(row) for row in tmp_state))
        if col_index > 0:
            tmp_state = copy(state)
            tmp_state[row_index][col_index], tmp_state[row_index][col_index - 1] = tmp_state[row_index][col_index - 1], tmp_state[row_index][col_index]
            result_states.append(tuple(tuple(row) for row in tmp_state))
        if col_index < 2:
            tmp_state = copy(state)
            tmp_state[row_index][col_index], tmp_state[row_index][col_index + 1] = tmp_state[row_index][col_index + 1], tmp_state[row_index][col_index]
            result_states.append(tuple(tuple(row) for row in tmp_state))
        if row_index < 2:
            tmp_state = copy(state)
            tmp_state[row_index][col_index], tmp_state[row_index + 1][col_index] = tmp_state[row_index + 1][col_index], tmp_state[row_index][col_index]
            result_states.append(tuple(tuple(row) for row in tmp_state))
        return list(set(result_states))


    def is_goal_test(self,state):
        return state == ((0, 1, 2),
                         (3, 4, 5),
                         (6, 7, 8)
                         )

    
    def goal_tests(self):
        return [
            ((0, 1, 2),
             (3, 4, 5),
             (6, 7, 8)
             )
        ]

    def path_cost():
        return 0

    def edge_cost(self,father_state,child_state):
        return 1

    def heuristic(self,state):
        return sum([sum([abs(state.index(j[0]) - int((element) / 3)) + abs(j[0].index(element)-element%3) for element in j[0]]) for j in [[value, index] for index, value in enumerate(state)]])

p = Problem()
g = Graph(p)
g.bfs_graph_search(p.initial_state())
g.dfs_graph_limited_search(p.initial_state(),depth=8)
g.A_Star_graph_search(p.initial_state())