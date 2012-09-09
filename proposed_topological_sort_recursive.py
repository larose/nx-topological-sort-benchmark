import networkx as nx

def sort(G, nbunch=None):
    if not G.is_directed():
        raise nx.NetworkXError(
            "Topological sort not defined on undirected graphs.")

    def _dfs(v):
        ancestors.add(v)

        for w in G[v]:
            if w in ancestors:
                raise nx.NetworkXUnfeasible("Graph contains a cycle.")

            if w not in explored:
                _dfs(w)

        ancestors.remove(v)
        explored.add(v)
        order.append(v)

    ancestors = set()
    explored = set()
    order = []

    if nbunch is None:
        nbunch = G.nodes_iter()

    for v in nbunch:
        if v not in explored:
            _dfs(v)
            
    return list(reversed(order))
