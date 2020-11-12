from collections import defaultdict
from graph_utils import *


class Graph:

    def __init__(self):
        self.adjacency_list = defaultdict(list)

    def find_mother_util(self, starting_vertex, visited):
        visited.add(starting_vertex)

        for neighbour in self.adjacency_list[starting_vertex]:
            if neighbour not in visited:
                self.find_mother_util(neighbour, visited)

    def dfs_recursive_util(self, starting_vertex, visited, sequence):

        if starting_vertex not in visited:
            visited.add(starting_vertex)
            for neighbour in self.adjacency_list[starting_vertex]:
                self.dfs_recursive_util(neighbour, visited, sequence)
                if neighbour not in sequence: sequence.append(neighbour)
        return sequence

    def dfs(self):
        visited = set()
        sequence = []
        starting_vertex = self.find_mother()
        self.dfs_recursive_util(starting_vertex, visited, sequence)
        sequence.append(starting_vertex)
        return sequence

    def add_edge(self, key, value):
        if isinstance(value, list):
            self.adjacency_list[key] = value
        else:
            self.adjacency_list[key].append(value)

    def find_mother(self):

        visited = set()
        mother_vertex = ''

        for vertex in list(self.adjacency_list):
            if vertex not in visited:
                self.find_mother_util(vertex, visited)
                mother_vertex = vertex

        self.find_mother_util(mother_vertex, visited)
        if len(visited) != len(self.adjacency_list):
            return -1
        else:
            return mother_vertex


if __name__ == '__main__':

    write_to_file('govern.out', build_graph('govern.in').dfs())
