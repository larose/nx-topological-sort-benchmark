import networkx as nx

def sort(G,nbunch=None):
    if not G.is_directed():
        raise nx.NetworkXError(
                "Topological sort not defined on undirected graphs.")

    # nonrecursive version
    seen={}
    order_explored=[] # provide order and 
    explored={}       # fast search without more general priorityDictionary
                     
    if nbunch is None:
        nbunch = G.nodes_iter() 
    for v in nbunch:     # process all vertices in G
        if v in explored: 
            continue
        fringe=[v]   # nodes yet to look at
        while fringe:
            w=fringe[-1]  # depth first search
            if w in explored: # already looked down this branch
                fringe.pop()
                continue
            seen[w]=1     # mark as seen
            # Check successors for cycles and for new nodes
            new_nodes=[]
            for n in G[w]:
                if n not in explored:
                    if n in seen: #CYCLE !!
                        raise nx.NetworkXUnfeasible("Graph contains a cycle.")
                    new_nodes.append(n)
            if new_nodes:   # Add new_nodes to fringe
                fringe.extend(new_nodes)
            else:           # No new nodes so w is fully explored
                explored[w]=1
                order_explored.insert(0,w) # reverse order explored
                fringe.pop()    # done considering this node
    return order_explored
