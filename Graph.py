from Problem import *
class Graph():
    def __init__(self,problem):
        self.nodes = [problem.initial_state()]
        self.edges = dict()
        self.edges[problem.initial_state()] = dict()
        self.problem = problem

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

    def bfs_graph_search(self,start):
        self.__init__(self.problem)
        if start is None or start not in self.nodes:
            return None
        visited = set()
        queue = [start]
        while queue:
            current_node = queue.pop(0)
            print(current_node)
            if self.problem.is_goal_test(current_node):
                print('FOUND!!!')
                return
            if current_node not in visited:
                visited.add(current_node)
                for node in self.problem.actions(current_node):
                    self.insert(current_node,node)
                queue.extend(set(self.edges[current_node].keys()) - visited)
        return visited

    def bfs_tree_search(self, start):
        self.__init__(self.problem)
        if start is None or start not in self.nodes:
            return None
        queue = [start]
        while queue:
            current_node = queue.pop(0)
            print(current_node)
            if self.problem.is_goal_test(current_node):
                print('FOUND!!!')
                return
            for node in self.problem.actions(current_node):
                self.insert(current_node, node)
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
            print(current_node)
            if self.problem.is_goal_test(current_node):
                print('FOUND!!!')
                return
            if current_node not in visited:
                visited.add(current_node)
                for node in self.problem.actions(current_node):
                    self.insert(current_node, node)
                nodes_stack.extend(set(self.edges[current_node].keys()) - visited)
        return visited

    def dfs_tree_search(self, start):
        self.__init__(self.problem)
        if start is None or start not in self.nodes:
            return None
        nodes_stack = [start]
        while nodes_stack:
            current_node = nodes_stack.pop()
            print(current_node)
            if self.problem.is_goal_test(current_node):
                print('FOUND!!!')
                return
            for node in self.problem.actions(current_node):
                self.insert(current_node, node)
            nodes_stack.extend(set(self.edges[current_node].keys()))
        return

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
            print(current_node)
            if self.problem.is_goal_test(current_node[0]):
                print('FOUND!!!')
                return
            if current_node[0] not in [x[0] for x in visited]:
                visited.add(current_node)
                if current_node[1] != depth:
                    for node in self.problem.actions(current_node[0]):
                        self.insert(current_node, (node,current_node[1]+1))
                    nodes_stack.extend(set(self.edges[current_node].keys()) - visited)
        return visited

    def dfs_tree_limited_search(self, start,depth=0):
        self.__init__(self.problem)
        self.nodes = [(self.problem.initial_state(), 0)]
        self.edges[(self.problem.initial_state(), 0)] = dict()
        if start is None or start not in [x[0] for x in self.nodes]:
            return None
        nodes_stack = [start]
        while nodes_stack:
            current_node = nodes_stack.pop()
            print(current_node)
            if self.problem.is_goal_test(current_node[0]):
                print('FOUND!!!')
                return
            if current_node[1] != depth:
                for node in self.problem.actions(current_node[0]):
                    self.insert(current_node, (node, current_node[1] + 1))
                nodes_stack.extend(set(self.edges[current_node].keys()))
        return

    def bidirectional_graph_search(self,start):
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
        nodes_stack = [start]
        while nodes_stack:
            current_node = nodes_stack.pop()
            print(current_node)
            if self.problem.is_goal_test(current_node):
                print('FOUND!!!')
                return
            if current_node not in visited:
                visited.add(current_node)
                for node in self.problem.actions(current_node):
                    self.insert(current_node, node)
                nodes_stack.extend(
                    set(self.edges[current_node].keys()) - visited)
        return visited


p = Problem()
g = Graph(p)
# g.bfs_graph_search((0,0))
# g.dfs_graph_search((0,0))
g.dfs_graph_limited_search((0,0),6)
