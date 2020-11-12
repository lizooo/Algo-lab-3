from graph import *


def convert_file_to_dict(file_name):
    last_key = []
    d = {}
    with open(file_name) as f:
        for line in f:
            if len(line) > 1:
                (key, val) = line.split()
                if key not in last_key:
                    d[key] = [val]
                    last_key.append(key)
                else:
                    d[key].append(val)

    return d


def write_to_file(file_name, obj_to_write):
    with open(file_name, 'w') as f:
        for element in obj_to_write:
            print(element, end='\n', file=f)


def build_graph(file_name):
    dictionary_to_process = convert_file_to_dict(file_name)
    graph = Graph()
    for key in dictionary_to_process.keys():
        graph.add_edge(key, dictionary_to_process[key])

    return graph




