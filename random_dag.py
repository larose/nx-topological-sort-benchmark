import random
import sys

def main():
    num_nodes = int(sys.argv[1])
    num_arcs = int(sys.argv[2])
    seed = int(sys.argv[3])

    max_num_arcs = (num_nodes ** 2 - num_nodes) / 2

    num_arcs = min(num_arcs, max_num_arcs)
    
    arcs = set()

    rand = random.Random(seed)

    while len(arcs) < num_arcs:
        i = rand.randint(0, num_nodes - 1)
        j = rand.randint(0, num_nodes - 1)
        
        if i < j:
            arcs.add((i,j))


    for arc in arcs:
        print(','.join(map(str, arc)))

if __name__ == '__main__':
    main()
