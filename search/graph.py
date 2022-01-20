import queue
from urllib.request import OpenerDirector
import networkx as nx

class Graph:
    """
    Class to contain a graph and your bfs function
    """
    def __init__(self, filename: str):
        """
        Initialization of graph object which serves as a container for 
        methods to load data and 
        
        """
        self.graph = nx.read_adjlist(filename, create_using=nx.DiGraph, delimiter=";")

    def bfs(self, start, end=None):
        """
        TODO: write a method that performs a breadth first traversal and pathfinding on graph G

        * If there's no end node, just return a list with the order of traversal
        * If there is an end node and a path exists, return a list of the shortest path
        * If there is an end node and a path does not exist, return None

        """
        queue = [start]
        visited = {start: True}
        if end is None:
            while queue:
                current = queue.pop(0) # It's pretty inefficient (O(N)) but whatever
                for neighbor in self.graph.neighbors(current):
                    if visited.get(neighbor) == None: # Probably should use defaultdict
                        queue.append(neighbor)
                        visited[neighbor] = True 
            return list(visited.keys()) # Maintains insertion order
        if end == start:
            return queue
        backtrack = {}
        while queue:
            current = queue.pop(0)
            for neighbor in self.graph.neighbors(current):
                if neighbor == end:
                    trace = [neighbor,current]
                    while start != current: # Traces all the way back to the start
                        current = backtrack.get(current)
                        trace.append(current)
                    return trace[::-1] # Returns from start to end
                if visited.get(neighbor) == None:
                    visited[neighbor] = True 
                    backtrack[neighbor] = current # Points backwards
                    queue.append(neighbor)
        return None # Exhausted all paths w/o a match