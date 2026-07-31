import bisect 
import math
from data_structures.linked_stack import LinkedStack;
from data_structures.linked_queue import LinkedQueue;

class Graph:
    '''
    Graph representing vertices and edges using adjacency list.
    '''

    def __init__(self, V):
        '''
        V: list of Vertex object to form the graph
        ''' 
        self.vertices = [None] * len(V)
        for i in range(len(V)):
            self.vertices[i] = Vertex(V[i])

    def __str__(self):
        ret_str = ''
        for i in range(len(self.vertices)):
            ret_str += 'Vertex' + str(self.vertices[i]) + '\n'

        return ret_str

    def add_edge(self, u_id, v_id, w=1):
        '''
        Add undirected edge:
        u_id = from vertex
        v_id = to vertex
        w = weight of directed edge (optional)
        '''
        u = next(vertex for vertex in self.vertices if vertex.id == u_id)
        v = next(vertex for vertex in self.vertices if vertex.id == v_id)
        bisect.insort(u.edges, Edge(u, v, w), key=lambda edge: edge.v.id)
        bisect.insort(v.edges, Edge(v, u, w), key=lambda edge: edge.v.id)

    def add_directed_edge(self, u_id, v_id, w=1):
        '''
        Add directed edge:
        u_id = from vertex
        v_id = to vertex
        w = weight of directed edge (optional)
        '''
        u = next(vertex for vertex in self.vertices if vertex.id == u_id)
        v = next(vertex for vertex in self.vertices if vertex.id == v_id)
        bisect.insort(u.edges, Edge(u, v, w), key=lambda edge: edge.v.id)

    def remove_edge(self, edge: Edge):
        pass

    def reset(self):
        '''
        Reset all edges in graph to initial unvisited and undiscovered state.
        '''
        for vertex in self.vertices:
            vertex.visited = False 
            vertex.discovered = False 

    def bfs(self, starting_vertex: Vertex):
        '''
        Breadth-first-search algorithm using adjacency list graph.
        BFS is maintained using a queue / FIFO.
        Return a visited_list arranged in BFS order
        '''
        discovered_queue = LinkedQueue()
        visited_list = []

        # append() the starting_vertex into discovered_queue
        for vertex in self.vertices:
            if vertex.id == starting_vertex.id:
                discovered_queue.append(vertex)
                vertex.discovered_vertex()

        print('discovered_queue: \n', str(discovered_queue))

        # while discovered_queue is not empty, 
        # we serve() the front-most element and append() any adjacent vertex that is not discovered + visited into discovered_queue
        while not discovered_queue.is_empty():

            # serve() out front-most element as active_vertex
            active_vertex = discovered_queue.serve()
            print('active_vertex = ', str(active_vertex))

            # append() active_vertex to visited_list
            visited_list.append(active_vertex)
            active_vertex.visited_vertex()

            visited_list_str = '[' + '\n'.join(str(vertex) for vertex in visited_list) + ']'
            print('visited_list: \n', visited_list_str)

            # check all adjacent vertices of active_vertex,
            # if vertex is not discovered + visited, append() into discovered_queue
            adjacent_edges = active_vertex.get_edges()
            for edge in adjacent_edges:
                if not edge.v.discovered and not edge.v.visited:
                    print('adjacent vertex = ', str(edge.v))
                    discovered_queue.append(edge.v)
                    edge.v.discovered_vertex()
                print('discovered_queue: \n', str(discovered_queue))

        # reset to restore originality of visited and discovered status
        self.reset()

        return visited_list 

    def dfs(self, starting_vertex: Vertex):
        '''
        Depth-first-search algorithm using adjacency list graph.
        DFS is maintained using a stack / LIFO.
        Return a visited_list arranged in DFS order
        ''' 
        discovered_stack = LinkedStack()
        visited_list = []

        # push() the starting_vertex into discovered_stack
        for vertex in self.vertices:
            if vertex.id == starting_vertex.id:
                vertex.discovered_vertex()
                discovered_stack.push(vertex)

        print('discovered_stack: \n', str(discovered_stack))

        # while discovered_stack is not empty, 
        # pop() the top-most element and push() any adjacent vertex that is not discovered + visited into discovered_stack
        while not discovered_stack.is_empty():

            # pop() out top-most element as active_vertex
            active_vertex = discovered_stack.pop()
            print('active vertex = ', active_vertex)

            # append() active_vertex to visited_list
            visited_list.append(active_vertex)
            active_vertex.visited_vertex()

            visited_list_str = '[' + '\n'.join(str(vertex) for vertex in visited_list) + ']'
            print('visited_list: \n', visited_list_str)
            
            # check all adjacent vertices of active_vertex,
            # if vertex is not discovered + visited, push() into discovered_stack
            adjacent_edges = active_vertex.get_edges()
            for edge in adjacent_edges:
                if not edge.v.discovered and not edge.v.visited:
                    print('adjacent vertex = ', str(edge.v))
                    discovered_stack.push(edge.v)
                    edge.v.discovered_vertex()
                print('discovered_stack: \n', str(discovered_stack))

        # reset to restore originality of visited and discovered status
        self.reset()
        
        return visited_list 

    def shortest_distance_bfs(self, source: Vertex, destination: Vertex):
        '''
        BFS algorithm modified to find shortest distance between 2 vertices from an unweighted graph.
        Return shortest_distance and a list of vertex_path from source to destination
        '''
        distance_from_source = 0
        vertex_path = []
        visited = []

        discovered_queue = LinkedQueue()

        # append() the starting_vertex into discovered_queue
        for vertex in self.vertices:
            if vertex.id == source.id:
                vertex_distance_tuple = (vertex, distance_from_source)
                discovered_queue.append(vertex_distance_tuple)
                vertex.discovered_vertex()

        print('discovered_queue: ', discovered_queue)

        # when discovered_queue is not empty and the front-most element is not the destination vertex,
        # serve() the top-most element and append() any adjacent vertex that is not discovered + visited into discovered_queue
        while not discovered_queue.is_empty() and discovered_queue.peek()[0].id != destination.id:
            active_vertex_distance_tuple = discovered_queue.serve()
            print('active_vertex_distance_tuple: ', active_vertex_distance_tuple)
            visited.append(active_vertex_distance_tuple)
            active_vertex_distance_tuple[0].visited_vertex()
            print('visited: ', visited)

            adjacent_edges = active_vertex_distance_tuple[0].get_edges()
        
            distance_from_source = active_vertex_distance_tuple[1] + 1

            for edge in adjacent_edges:
                print('adjacent edge: ', edge.v)
                if not edge.v.discovered and not edge.v.visited:
                    print('adding Vertex', edge.v, 'to discovered_queue')
                    vertex_distance_tuple = (edge.v, distance_from_source)
                    discovered_queue.append(vertex_distance_tuple)
                    edge.v.discovered_vertex()
                print('discovered_queue: ', discovered_queue)

        # once the front-most element of discovered_queue equals destination,
        # make a final append() to visited and extract the distance from tuple as shortest distance between source and destination
        if discovered_queue.peek()[0].id == destination_vertex.id:
            active_vertex_distance_tuple = discovered_queue.serve()
            print('active_vertex_distance_tuple: ', active_vertex_distance_tuple)
            visited.append(active_vertex_distance_tuple)
            active_vertex_distance_tuple[0].visited_vertex()
            print('visited: ', visited)

            # reset to restore originality of visited and discovered status
            self.reset()
            return visited[-1][1]
        else:
            self.reset()
            return ValueError('Destination ', destination, ' does not exist in graph.')

    def dijkstra(self, source: Vertex, destination: Vertex):
        '''
        Dijkstra algorithm to find the shortest distance between source and destination of a weighted graph.
        Combines dynamic programming and greedy algorithm.
        Return shortest_distance and a list of vertex_path from source to destination
        '''
        shortest_distance = 0 
        
        # todo    

        return shortest_distance

class Vertex:
    '''
    Vertex keep track af its adjacent vertices using a list (edges)
    '''
    def __init__(self, id):
        self.id = id 
        self.edges = []
        self.discovered = False 
        self.visited = False 

    def __str__(self):
        edges_str = ', '.join(str(edge) for edge in self.edges)
        return f'{self.id} -- [{edges_str}]'

    def __repr__(self):
        return f'Vertex({self.id!r})'

    def discovered_vertex(self):
        self.discovered = True

    def visited_vertex(self):
        self.visited = True

    def get_edges(self):
        return self.edges

    def has_outgoing(self, target: Vertex):
        for edge in self.edges:
            if edge.v.id == target.id:
                return True 

        return False

class Edge: 
    def __init__(self, u: Vertex, v: Vertex, w = 1):
        '''
        u = vertex1
        v = vertex2
        w = weight of the edge, by default is 1
        '''
        self.u = u
        self.v = v 
        self.w = w 

    def __str__(self):
        return f'< {self.u.id}, {self.v.id}, {self.w} >'

    def __repr__(self):
        return f'Edge({self.u.id!r}, {self.v.id!r}, {self.w!r})'

if __name__ == "__main__":

# %%
    vertices  = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H']
    unweighted_undirected_graph = Graph(V = vertices)
    print(unweighted_undirected_graph)

    unweighted_undirected_graph.add_edge('A', 'B')   
    unweighted_undirected_graph.add_edge('A', 'C')
    unweighted_undirected_graph.add_edge('C', 'D')
    unweighted_undirected_graph.add_edge('B', 'F')
    unweighted_undirected_graph.add_edge('B', 'E')
    unweighted_undirected_graph.add_edge('F', 'G')
    unweighted_undirected_graph.add_edge('E', 'G')
    unweighted_undirected_graph.add_edge('E', 'H')
    unweighted_undirected_graph.add_edge('G', 'H')
    print(unweighted_undirected_graph)
# %% 

# %%
    print('\n========== BREADTH FIRST SEARCH ==========\n')
    bfs_order_list = unweighted_undirected_graph.bfs(Vertex('A'))
    for item in bfs_order_list:
        print(item)
# %% 

# %%
    print('\n========== DEPTH FIRST SEARCH ==========\n')
    dfs_order_list = unweighted_undirected_graph.dfs(Vertex('A'))
    for item in dfs_order_list:
        print(item)
# %%

# %%
    print('\n========== SHORTEST DISTANCE USING BFS ==========\n')
    source_vertex = Vertex('A')
    destination_vertex = Vertex('E')
    shortest_distance = unweighted_undirected_graph.shortest_distance_bfs(source_vertex, destination_vertex)
    print('# Shortest distance between ', source_vertex.id, ' and ', destination_vertex.id, ' = ', shortest_distance)

    source_vertex = Vertex('A')
    destination_vertex = Vertex('F')
    shortest_distance = unweighted_undirected_graph.shortest_distance_bfs(source_vertex, destination_vertex)
    print('# Shortest distance between ', source_vertex.id, ' and ', destination_vertex.id, ' = ', shortest_distance)
    
    source_vertex = Vertex('A')
    destination_vertex = Vertex('G')
    shortest_distance = unweighted_undirected_graph.shortest_distance_bfs(source_vertex, destination_vertex)
    print('# Shortest distance between ', source_vertex.id, ' and ', destination_vertex.id, ' = ', shortest_distance)

    source_vertex = Vertex('A')
    destination_vertex = Vertex('H')
    shortest_distance = unweighted_undirected_graph.shortest_distance_bfs(source_vertex, destination_vertex)
    print('# Shortest distance between ', source_vertex.id, ' and ', destination_vertex.id, ' = ', shortest_distance)
# %%

# %%
    vertices  = ['A', 'B', 'C', 'D', 'E']
    weighted_directed_graph = Graph(V = vertices)
    print(weighted_directed_graph)

    weighted_directed_graph.add_directed_edge('A', 'B') 
    weighted_directed_graph.add_directed_edge('A', 'C') 
    weighted_directed_graph.add_directed_edge('B', 'C') 
    weighted_directed_graph.add_directed_edge('B', 'D') 
    weighted_directed_graph.add_directed_edge('C', 'B') 
    weighted_directed_graph.add_directed_edge('C', 'D') 
    weighted_directed_graph.add_directed_edge('C', 'E') 
    weighted_directed_graph.add_directed_edge('D', 'E') 
    weighted_directed_graph.add_directed_edge('E', 'D')  
    print(weighted_directed_graph)    
# %%   
