# Project 2
Breadth-first search

# BFS Implementation
* Takes in adjlist to create the underlying graph data structure using networkx
* Iterates over neighbors using networkx API and does a breadth first search (BFS) using a queue
* Gets shortest paths from any connected nodes using backtracking and returns None if no connection

# Tests
* Tests basic BFS traversal using ground truths by removing nodes that are independent to the starting node
* Tests shortest path implementation by comparing subset of the nodes' shortest path
* Tests diconnected nodes for None, including nodes not in the graph

