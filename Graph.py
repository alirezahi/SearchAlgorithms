from Problem import *
class Graph():
    def __init__(self,problem):
        self.nodes = list()
        self.edges = dict()
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

    def bfs(self,start):
        if start is None or start not in self.nodes:
            return None
        visited = set()
        queue = [start]
        while queue:
            current_node = queue.pop(0)
            print(current_node)
            if self.problem.goal_test(current_node):
                print('FOUND!!!')
                return
            if current_node not in visited:
                visited.add(current_node)
                for node in self.problem.actions(current_node):
                    self.insert(current_node,node)
                queue.extend(set(self.edges[current_node].keys()) - visited)
        return visited
    
    def dfs(self,start):
        if start is None or start not in self.nodes:
            return None
        visited = set()
        nodes_stack = list()
        nodes_stack.append(start)
        while nodes_stack:
            current_node = nodes_stack.pop()
            print(current_node)
            if current_node not in visited:
                visited.add(current_node)
                for node in self.problem.actions(current_node):
                    self.insert(current_node, node)
                nodes_stack.extend(set(self.edges[current_node].keys()) - visited)
        return visited


p = Problem()
g = Graph(p)
g.insert((0,0))
g.bfs((0,0))
