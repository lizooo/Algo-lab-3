from collections import defaultdict
from graph_utils import *


class Graph:

    def __init__(self):
        self.adjacency_matrix = defaultdict(list)

    def dfs_util(self, starting_vertex, visited):
        visited.add(starting_vertex)

        for neighbour in self.adjacency_matrix[starting_vertex]:
            if neighbour not in visited:
                self.dfs_util(neighbour, visited)

    def add_edge(self, key, value):
        if isinstance(value, list):
            self.adjacency_matrix[key] = value
        else: self.adjacency_matrix[key].append(value)

    def print_graph(self):
        print(dict(self.adjacency_matrix))

    def find_ancestors(self, vertex_to_process):
        ancestors = []
        for current_vertex in list(self.adjacency_matrix):
            for neighbour in self.adjacency_matrix[current_vertex]:
                if vertex_to_process == neighbour:
                    ancestors.append(current_vertex)

        return ancestors

    def find_mother(self):

        visited = set()
        mother_vertex = ''

        for vertex in list(self.adjacency_matrix):
            if vertex not in visited:
                self.dfs_util(vertex, visited)
                mother_vertex = vertex

        self.dfs_util(mother_vertex, visited)
        if len(visited) != len(self.adjacency_matrix):
            return -1
        else:
            return mother_vertex

    def bfs(self):

        starting_vertex = self.find_mother()
        visited = set()
        queue = []
        result = []

        visited.add(starting_vertex)
        queue.append(starting_vertex)

        while queue:
            current_vertex = queue.pop(0)
            result.append(current_vertex)

            for neighbour in self.adjacency_matrix[current_vertex]:
                should_append = True
                if neighbour not in visited:
                    for ancestor in self.find_ancestors(neighbour):
                        if ancestor not in visited:
                            should_append = False
                    if should_append:
                        visited.add(neighbour)
                        queue.append(neighbour)

        return result[::-1]


if __name__ == '__main__':

    write_to_file('govern.out', build_graph('govern.in').bfs())













