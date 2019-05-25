'''
* Author: Tomoya Tokunaga(mailto: ttokunag@ucsd.edu)
* About this file:
* This file implements Dijkstra's shortest path algorithm with a LIST
* Complexity: O(V^2 + E) time | O(V) space (this stores node & distance pair
* to a list, so it takes a space)
'''

class graph_node(object):
    '''
    * a graph node constructor
    * @param val: the value of the node
    * @param adjacents: a list of its adjacent nodes
    '''
    def __init__(self, val, adjacents=None):
        # val is the value of a vertex. it can be location names,
        # server names, intersections in real life applications
        self.val = val
        self.prev_pointer = None
        self.distance = float('inf')
        # its adjacent nodes are stored in an array
        # this array contains tuple pair, (adjacent_node, weight)
        self.adjacents = adjacents
    
    # a method to set a previous pointer
    def set_prev(self, node):
        self.prev_pointer = node
    
    # a method to set a distance from the start node
    def set_distance(self, dist):
        self.distance = dist


class graph(object):
    '''
    * a constructor of a graph structure
    * @param vertices: a list of vertices which belong to the graph
    '''
    def __init__(self, vertices):
        # a list of graph nodes
        self.unvisited = vertices

    '''
    * a method to find a shortest path from the given start node
    * to the given destination using Dijkstra's algorithm
    * @param start: a node which one want to know the distance from
    * @param dest: a node which one want to know the distance from the start
    '''
    def dijkstra(self, start, dest):
        # a list stores visited nodes
        visited = []
        # the distance from the start to the start is 0
        # (this follows the Dijkstra's algorithm)
        start.set_distance(0)
        curr_node = None

        while self.unvisited:
            # finds the shortest unvisited node
            min_dist = float('inf')
            min_idx = None
            for i in range(len(self.unvisited)):
                if self.unvisited[i].distance < min_dist:
                    min_dist = self.unvisited[i].distance
                    min_idx = i
            curr_node = self.unvisited.pop(min_idx)
            
            # updates adjacent nodes distance
            if curr_node.adjacents is not None:
                for adj in curr_node.adjacents:
                    if curr_node.distance + adj[1] < adj[0].distance:
                        adj[0].set_distance(curr_node.distance + adj[1])
                        adj[0].set_prev(curr_node)
            
            visited.append(curr_node)
        
        # the following codes prints out the shortest path and its cost
        shortest_path = ""
        curr_node_back = dest
        while curr_node_back:
            shortest_path += curr_node_back.val
            if curr_node_back.prev_pointer:
                shortest_path += " >- "
            curr_node_back = curr_node_back.prev_pointer

        print("Shortest path: {} (cost of {})".format(shortest_path[::-1], dest.distance))
        return visited
        
            
        
F = graph_node("F")
E = graph_node("E", [(F, 4)])
D = graph_node("D", [(E, 6)])
B = graph_node("B", [(F, 6)])
C = graph_node("C", [(D, 3),(B, 2),(E, 2)])
A = graph_node("A", [(C, 4),(B, 5),(D, 2)])

nodes = [A,B,C,D,E,F]
Graph = graph(nodes)
Graph.dijkstra(A, F)
'''
* the above code prints out the following:
* Shortest path: A -> C -> E -> F (cost of 10)
'''
