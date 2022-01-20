# write tests for bfs
import pytest
from search import graph

@pytest.fixture
def test_bfs_traversal():
    """
    TODO: Write your unit test for a breadth-first
    traversal here. Create an instance of your Graph class 
    using the 'tiny_network.adjlist' file and assert 
    that all nodes are being traversed (ie. returns 
    the right number of nodes, in the right order, etc.)

    33232663 is only connected from Hani and Michael and
    Hani is not adjacent to Michael.
    Therefore if I remove 33232663 from Hani start node
    I should be able to get it from Michael's connection.
    So if I remove each others traversal from Hani's and
    33232663's BFS traversal it would be equivalent.
    """
    g = graph.Graph("data/tiny_network.adjlist")
    x = g.bfs("Hani Goodarzi")
    y = g.bfs("33232663")
    x = x.remove("33232663")
    y = y.remove("Hani Goodarzi")
    assert x == y

def test_bfs():
    """
    TODO: Write your unit test for your breadth-first 
    search here. You should generate an instance of a Graph
    class using the 'citation_network.adjlist' file 
    and assert that nodes that are connected return 
    a (shortest) path between them.
    
    Include an additional test for nodes that are not connected 
    which should return None. 
    """
    g = graph.Graph("data/citation_network.adjlist")
    x = g.bfs("Lani Wu",'31308376') # This can be any random connection
    y = x[1:]
    z = g.bfs(y[0], y[-1])
    assert y == z # Subset of the connection has to be true
    assert None == g.bfs("Steven Altschuler", "Me")