from SlidingPuzzle import *
class Graph():
    def __init__(self,problem):
        self.nodes = [problem.initial_state()]
        self.edges = dict()
        self.edges[problem.initial_state()] = dict()
        self.problem = problem
        self.parent = {}
        self.nodes_expanded_count = 1
        self.nodes_count = 1

    def insert(self,primary_node,second_node=None,weight=-1):
        if primary_node:
            if not (primary_node in self.nodes):
                # add first_node if it doesn't exist
                self.nodes.append(primary_node)
                self.edges[primary_node] = dict()
        if second_node:
            if not(second_node in self.nodes):
                # add second node if it doesn't exist
                self.nodes.append(second_node)
                self.edges[second_node] = dict()
            # adding edge of first and second node
            self.edges[primary_node][second_node] = weight
            self.edges[second_node][primary_node] = weight
        return None

    def print_path(self,start):
        print('Nodes Expanded: ' + str(self.nodes_expanded_count))
        print('Nodes Visited: ' + str(self.nodes_count))
        path_node = start
        path_list = []
        while path_node:
            path_list.append(path_node)
            path_node = self.parent[path_node] if path_node in self.parent else None
        print('Path Cost: ' + str(len(path_list)-1))
        for i in reversed(path_list):
            print(i)

    def bfs_graph_search(self,start):
        self.__init__(self.problem)
        if start is None or start not in self.nodes:
            return None
        visited = set()
        queue = [start]
        while queue:
            current_node = queue.pop(0)
            self.nodes_expanded_count += 1
            if self.problem.is_goal_test(current_node):
                self.print_path(current_node)
                return
            if current_node not in visited:
                visited.add(current_node)
                self.nodes_count += len(list(set(self.problem.actions(current_node))))
                for node in list(set(self.problem.actions(current_node))-visited):
                    self.insert(current_node,node)
                    self.parent[node] = current_node
                queue.extend(set(self.edges[current_node].keys()) - visited)
        return visited

    def bfs_tree_search(self, start):
        self.__init__(self.problem)
        if start is None or start not in self.nodes:
            return None
        queue = [start]
        while queue:
            current_node = queue.pop(0)
            self.nodes_expanded_count += 1
            if self.problem.is_goal_test(current_node):
                self.print_path(current_node)
                return
            self.nodes_count += len(self.problem.actions(current_node))
            for node in self.problem.actions(current_node):
                self.insert(current_node, node)
                self.parent[node] = current_node
            queue.extend(set(self.edges[current_node].keys()))
        return
    
    def dfs_graph_search(self,start):
        self.__init__(self.problem)
        if start is None or start not in self.nodes:
            return None
        visited = set()
        nodes_stack = [start]
        while nodes_stack:
            current_node = nodes_stack.pop()
            self.nodes_expanded_count += 1
            if self.problem.is_goal_test(current_node):
                self.print_path(current_node)
                return 'find'
            if current_node not in visited:
                visited.add(current_node)
                self.nodes_count += len(list(set(self.problem.actions(current_node))))
                for node in list(set(self.problem.actions(current_node))-visited):
                    self.insert(current_node, node)
                    self.parent[node] = current_node
                nodes_stack.extend(set(self.edges[current_node].keys()) - visited)
        return None

    def dfs_tree_search(self, start):
        self.__init__(self.problem)
        if start is None or start not in self.nodes:
            return None
        nodes_stack = [start]
        while nodes_stack:
            current_node = nodes_stack.pop()
            self.nodes_expanded_count += 1
            if self.problem.is_goal_test(current_node):
                self.print_path(current_node)
                return 'find'
            self.nodes_count += len(self.problem.actions(current_node))
            for node in self.problem.actions(current_node):
                self.insert(current_node, node)
                self.parent[node] = current_node
            nodes_stack.extend(set(self.edges[current_node].keys()))
        return None

    def dfs_graph_limited_search(self, start,depth=0):
        self.__init__(self.problem)
        self.nodes = [(self.problem.initial_state(), 0)]
        self.edges[(self.problem.initial_state(), 0)] = dict()
        if start is None or start not in [x[0] for x in self.nodes]:
            return None
        visited = set()
        nodes_stack = [(start,0)]
        while nodes_stack:
            current_node = nodes_stack.pop()
            self.nodes_expanded_count += 1
            if self.problem.is_goal_test(current_node[0]):
                self.print_path(current_node[0])
                return 'final'
            if current_node[0] not in [x[0] for x in visited]:
                visited.add(current_node)
                if current_node[1] != depth:
                    self.nodes_count += len(list(set(self.problem.actions(current_node[0]))))
                    for node in list(set(self.problem.actions(current_node[0])) - set([x[0] for x in visited])):
                        self.insert(current_node, (node,current_node[1]+1))
                        self.parent[node] = current_node[0]
                    nodes_stack.extend(set(self.edges[current_node].keys()) - visited)
        return None

    def dfs_tree_limited_search(self, start,depth=0):
        self.__init__(self.problem)
        self.nodes = [(self.problem.initial_state(), 0)]
        self.edges[(self.problem.initial_state(), 0)] = dict()
        if start is None or start not in [x[0] for x in self.nodes]:
            return None
        nodes_stack = [start]
        while nodes_stack:
            current_node = nodes_stack.pop()
            self.nodes_expanded_count += 1
            if self.problem.is_goal_test(current_node[0]):
                self.print_path(current_node[0])
                return
            if current_node[1] != depth:
                self.nodes_count += len(self.problem.actions(current_node[0]))
                for node in self.problem.actions(current_node[0]):
                    self.insert(current_node, (node, current_node[1] + 1))
                    self.parent[node] = current_node[0]
                nodes_stack.extend(set(self.edges[current_node].keys()))
        return

    def iddfs_graph_search(self,start):
        problem_depth = 1
        res = self.dfs_graph_limited_search(start,depth=problem_depth)
        while not res:
            problem_depth += 1
            res = self.dfs_graph_limited_search(start, depth=problem_depth)


    def bidirectional_graph_search(self,start,goal):
        #this part of code is not complete and has to be completed!!!!!!!!!!
        self.__init__(self.problem)
        self.nodes = [self.problem.initial_state()]
        self.edges[self.problem.initial_state()] = dict()
        #adding destination node to start from there and reach to the start node
        dest_nodes = list()
        dest_nodes.extend(self.problem.goal_tests())
        dest_edges = dict()
        if start is None or start not in self.nodes:
            return None
        visited = set()
        visited_second = set()
        nodes_stack = [start]
        nodes_second_stack = [goal]
        while nodes_stack or nodes_second_stack:
            current_node = nodes_stack.pop()
            self.nodes_expanded_count += 1
            print(current_node)
            print('current_node')
            print(current_node)
            if self.problem.is_goal_test(current_node):
                print('FOUND!!!')
                return
            if current_node not in visited:
                visited.add(current_node)
                self.nodes_count += len(self.problem.actions(current_node))
                for node in self.problem.actions(current_node):
                    self.insert(current_node, node)
                nodes_stack.extend(set(self.edges[current_node].keys()) - visited)
            current_node_second = nodes_second_stack.pop()
            self.nodes_expanded_count += 1
            print(current_node_second)
            print('current_node_second')
            if current_node_second == self.problem.initial_state():
                print('FOUND!!!')
                return
            if current_node_second not in visited_second:
                visited_second.add(current_node_second)
                self.nodes_count += len(self.problem.actions(current_node_second, straight=False))
                for node in self.problem.actions(current_node_second,straight=False):
                    self.insert(current_node_second, node)
                nodes_second_stack.extend(set(self.edges[current_node_second].keys()) - visited_second)
            common_nodes = (set(nodes_stack) | set(visited)) & (set(nodes_second_stack) | set(visited_second))
            if len(common_nodes) > 0:
                print('findout path :D')
                return
        return visited

    def UCS_graph_search(self, start):
        self.__init__(self.problem)
        self.nodes = [self.problem.initial_state()]
        self.edges[self.problem.initial_state()] = dict()
        visited = set()
        #defining list for nodes, [node,g(n)]
        nodes = [[start, 0]]
        while nodes:
            current_node = min(nodes, key=lambda k: k[1])
            self.nodes_expanded_count += 1
            visited.add(current_node[0])
            if p.is_goal_test(current_node[0]):
                self.print_path(current_node[0])
                return current_node[0]
            self.nodes_count += len(list(set(self.problem.actions(current_node[0]))))
            for node in list(set(self.problem.actions(current_node[0])) - visited):
                cost = self.problem.edge_cost(current_node[0], node)
                self.insert(current_node[0], node, cost)
                self.parent[node] = current_node[0]
                current_cost = list(filter(lambda element: element[0] == current_node[0], nodes))[0][1] + cost
                nodes.append([node, current_cost])
            nodes.remove(current_node)

    def UCS_tree_search(self, start):
        self.__init__(self.problem)
        self.nodes = [self.problem.initial_state()]
        self.edges[self.problem.initial_state()] = dict()
        #defining list for nodes, [node,g(n)]
        nodes = [[start, 0]]
        while nodes:
            current_node = min(nodes, key=lambda k: k[1])
            self.nodes_expanded_count += 1
            if p.is_goal_test(current_node[0]):
                self.print_path(current_node[0])
                return current_node[0]
            self.nodes_count += len(list(set(self.problem.actions(current_node[0]))))
            for node in list(set(self.problem.actions(current_node[0]))):
                cost = self.problem.edge_cost(current_node[0], node)
                self.insert(current_node[0], node, cost)
                self.parent[node] = current_node[0]
                current_cost = list(filter(lambda element: element[0] == current_node[0], nodes))[0][1] + cost
                nodes.append([node, current_cost])
            nodes.remove(current_node)


    def A_Star_graph_search(self,start):
        self.__init__(self.problem)
        self.nodes = [self.problem.initial_state()]
        self.edges[self.problem.initial_state()] = dict()
        visited = set()
        #defining list for nodes, [node,g(n),h(n)+g(n)]
        nodes = [[start,0,0]]
        while nodes:
            current_node = min(nodes, key = lambda k : k[2])
            self.nodes_expanded_count += 1
            visited.add(current_node[0])
            if p.is_goal_test(current_node[0]):
                self.print_path(current_node[0])
                return current_node[0]
            self.nodes_count += len(list(set(self.problem.actions(current_node[0]))))
            for node in list(set(self.problem.actions(current_node[0])) - visited):
                cost = self.problem.edge_cost(current_node[0],node)
                self.insert(current_node[0],node,cost)
                self.parent[node] = current_node[0]
                current_cost = list(filter(lambda element: element[0] == current_node[0],nodes))[0][1] + cost
                nodes.append([node,current_cost,current_cost + self.problem.heuristic(node)])
            nodes.remove(current_node)
    
    def A_Star_tree_search(self, start):
        self.__init__(self.problem)
        self.nodes = [self.problem.initial_state()]
        self.edges[self.problem.initial_state()] = dict()
        #defining list for nodes, [node,g(n),h(n)+g(n)]
        nodes = [[start, 0, 0]]
        while nodes:
            current_node = min(nodes, key=lambda k: k[2])
            self.nodes_expanded_count += 1
            print_table(current_node)
            if p.is_goal_test(current_node[0]):
                self.print_path(current_node[0])
                return current_node[0]
            self.nodes_count += len(list(set(self.problem.actions(current_node[0]))))
            for node in list(set(self.problem.actions(current_node[0]))):
                cost = self.problem.edge_cost(current_node[0], node)
                self.insert(current_node[0], node, cost)
                self.parent[node] = current_node[0]
                current_cost = list(filter(lambda element: element[0] == current_node[0], nodes))[0][1] + cost
                nodes.append([node, current_cost, current_cost +self.problem.heuristic(node)])
            nodes.remove(current_node)

p = Problem()
g = Graph(p)
# g.A_Star_graph_search(p.initial_state())
g.iddfs_graph_search(p.initial_state())
# g.dfs_graph_search((0,0))
# g.dfs_graph_limited_search((0,0),6)
