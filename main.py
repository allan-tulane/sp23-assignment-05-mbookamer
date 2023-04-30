from collections import defaultdict

def make_undirected_graph(edge_list):
    """ Makes an undirected graph from a list of edge tuples. """
    graph = defaultdict(set)
    for e in edge_list:
        graph[e[0]].add(e[1])
        graph[e[1]].add(e[0])
    return graph


def reachable(graph, start_node):
    """
    Returns:
      the set of nodes reachable from start_node
    """
    result = set([start_node])
    frontier = set([start_node])
    visit = set() #want a set of nodes we have already visited 
    while len(frontier) != 0:
        ###TODO
        #we want to be able to determine which graphs are accessible from our node and which are not
        #so we store this information in a queue, pop off the node we recently visited, and then add that to our resulting set of nodes
        node = frontier.pop()
        visit.add(node)
        result.add(node)
        
        #we want to determine if this node is one we have visited or have not visited
        #we do nothing if we have visited it
        #we add it to the frontier to then visit if we have not already visited it
        for x in graph[node]:
            for x not in visit:
                frontier.add(x)
        pass
    return result

def test_reachable():
    graph = make_undirected_graph([('A', 'B'), ('B', 'C'), ('C', 'D'), ('D', 'B')])
    assert sorted(reachable(graph, 'A')) == ['A', 'B', 'C', 'D']

    graph = make_undirected_graph([('A', 'B'), ('B', 'C'), ('C', 'D'), ('D', 'B'), ('E', 'F'), ('F', 'G')])
    assert sorted(reachable(graph, 'A')) == ['A', 'B', 'C', 'D']
    assert sorted(reachable(graph, 'E')) == ['E', 'F', 'G']




def connected(graph):
    ### TODO
    #we want to test if a graph is connected, that is, every node is reachable from every other node
    
    start_node = list(graph)[0]
    reachable_nodes = reachable(graph, start_node)
    if len(reachable_nodes) == len(graph): #a graph is connected iff. every node in the graph can be reached by any other node in the graph i.e. length of 
        #the graph 
        return True
    else:
        return False
    pass

def test_connected():
    graph = make_undirected_graph([('A', 'B'), ('B', 'C'), ('C', 'D'), ('D', 'B')])
    assert connected(graph) == True
    graph = make_undirected_graph([('A', 'B'), ('B', 'C'), ('C', 'D'), ('D', 'B'), ('E', 'F'), ('F', 'G')])
    assert connected(graph) == False



def n_components(graph):
    """
    Returns:
      the number of connected components in an undirected graph
    """
    ### TODO
    nodes = set(graph.keys())
    num = 0 #number of connected components initialized 
    
    while len(nodes) != 0:
        #we only want to add to num when we have a node that is successfully reachable from node_a, so we iterate over every node to find this out
        node_a = nodes.pop()
        reachable_nodes = reachable(graph, node_a) #determine which nodes are reachable from a
        nodes = nodes.difference(reachable_nodes) 
        num += 1
   return num
    pass

def test_n_components():
    graph = make_undirected_graph([('A', 'B'), ('B', 'C'), ('C', 'D'), ('D', 'B')])
    assert n_components(graph) == 1

    graph = make_undirected_graph([('A', 'B'), ('B', 'C'), ('C', 'D'), ('D', 'B'), ('E', 'F'), ('F', 'G')])
    assert n_components(graph) == 2
