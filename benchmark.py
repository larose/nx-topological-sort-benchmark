import csv
import importlib
import networkx as nx
import sys
import timeit

def read_arcs(filename):
    return [tuple(map(int, arc)) for arc in csv.reader(open(filename))]

def validate_solution(graph, solution):
    if set(graph.nodes()) != set(solution):
        return False

    in_degree = dict(graph.in_degree_iter())

    for node in solution:
        if in_degree[node] != 0:
            return False

        for succ in graph.succ[node]:
            in_degree[succ] -= 1

    return True    

def main():
    module_name = sys.argv[1]
    instance_name = sys.argv[2]

    module = importlib.import_module(module_name)
    dag = nx.DiGraph(read_arcs(instance_name))

    print("Module", module)
    print("Num vertices:", dag.number_of_nodes())
    print("Num arcs:", dag.number_of_edges())

    t0 = timeit.default_timer()
    solution = module.sort(dag)
    t1 = timeit.default_timer()

    print("Time: %s s" % (t1 - t0))

    feasible = validate_solution(dag, solution)

    print("Feasible solution?", feasible)


if __name__ == '__main__':
    main()
    
