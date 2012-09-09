import networkx as nx

def sort(G,nbunch=None):
    if not G.is_directed():
        raise nx.NetworkXError(
                "Topological sort not defined on undirected graphs.")

    # function for recursive dfs
    def _dfs(G,seen,explored,v):
        seen.add(v)
        for w in G[v]:
            if w not in seen: 
                if not _dfs(G,seen,explored,w):
                    return False
            elif w in seen and w not in explored:
                # cycle Found--- no topological sort
                raise nx.NetworkXUnfeasible("Graph contains a cycle.")
        explored.insert(0,v) # inverse order of when explored 
        return True

    seen=set()
    explored=[]

    if nbunch is None:
        nbunch = G.nodes_iter() 
    for v in nbunch:  # process all nodes
        if v not in explored:
            if not _dfs(G,seen,explored,v): 
                raise nx.NetworkXUnfeasible("Graph contains a cycle.")
    return explored
