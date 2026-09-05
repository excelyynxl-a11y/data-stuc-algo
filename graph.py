import bisect 
import math
from data_structures.linked_stack import LinkedStack;
from data_structures.linked_queue import LinkedQueue;
from data_structures.array_min_heap import ArrayMinHeap;

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
        self.__length = len(self.vertices)

    def __len__(self):
        return self.__length

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
            vertex.previous = None 
            vertex.distance = math.inf 

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

    def dijkstra(self, source: Vertex, destination: Vertex) -> ArrayMinHeap:
        '''
        Dijkstra algorithm to find the shortest distance between source and destination of a weighted graph.
        Using a MinHeap to store (vertex, distance)
        Combines dynamic programming and greedy algorithm.
        '''
        discovered_heap = ArrayMinHeap(max_items = self.__len__())
        source.distance = 0
        discovered_heap.add((source, source.distance))

        while len(discovered_heap) > 0:
            # extract root = next smallest distance
            u = discovered_heap.extract_root()
            # u is visited, u distance is finalised
            u.visited = True 

            # edge relaxation on all u neighbor
            for edge in u.edges:
                v = edge.v 

                # if v is not discovered, means the distance is still inf
                # we need to update the distance to a better / smaller distance 
                if v.discovered == False: 
                    v.discovered = True 
                    v.distance = edge.w + u.distance 
                    v.previous = u # for backtracking
                    discovered_heap.add(v, v.distance)
                # v is in heap but distance not yet finalised
                elif v.visited == False:
                    if v.distance > u.distance + edge.w:
                        old_v = (v, v.distance)
                        v.distance = u.distance + edge.w 
                        v.previous = u # for backtracking 
                        new_v = (v, v.distance)
                        discovered_heap.update(old_v, new_v)  
                        # after updating, discovered_heap might undergo rising to maintain heap structure 

        return discovered_heap

    def find_cycle_undirected(self):
        '''
        Find if a cycle exist in this undirected graph using BFS approach.
        Same as bfs(), except i added a check for "if v.discovered: return True" as we have found a cycle.
        '''
        
        return False 

    def find_cycle_directed(self):
        '''
        Find if a cycle exist in this directed graph using BFS approach.
        Same as bfs(), except i added a check for "if v.discovered: return True" as we have found a cycle.
        '''
        return False

class Vertex:
    '''
    Vertex keep track af its adjacent vertices using a list (edges)
    '''
    def __init__(self, id):
        self.id = id 
        self.edges = []
        self.discovered = False 
        self.visited = False 
        self.distance = math.inf()
        self.previous = None 

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
    print('\n========== PARTY INFECTED USING BFS ==========\n') 
    vertices  = ['A', 'B', 'C', 'D', 'E']
    directed_graph = Graph(V = vertices)
    print(directed_graph)

    directed_graph.add_directed_edge('A', 'B') 
    directed_graph.add_directed_edge('A', 'C') 
    directed_graph.add_directed_edge('B', 'C') 
    directed_graph.add_directed_edge('B', 'D') 
    directed_graph.add_directed_edge('C', 'B') 
    directed_graph.add_directed_edge('C', 'D') 
    directed_graph.add_directed_edge('C', 'E') 
    directed_graph.add_directed_edge('D', 'E') 
    directed_graph.add_directed_edge('E', 'D')  
    print(directed_graph)  

    infected_first = Vertex('A')
    bfs_directed_graph = directed_graph.bfs(infected_first)
    print(infected_first.id, ' infected ', bfs_directed_graph, ' = ', len(bfs_directed_graph), ' parties')  
    infected_first = Vertex('B')
    bfs_directed_graph = directed_graph.bfs(infected_first)
    print(infected_first.id, ' infected ', bfs_directed_graph, ' = ', len(bfs_directed_graph), ' parties')  
    infected_first = Vertex('C')
    bfs_directed_graph = directed_graph.bfs(infected_first)
    print(infected_first.id, ' infected ', bfs_directed_graph, ' = ', len(bfs_directed_graph), ' parties')  
    infected_first = Vertex('D')
    bfs_directed_graph = directed_graph.bfs(infected_first)
    print(infected_first.id, ' infected ', bfs_directed_graph, ' = ', len(bfs_directed_graph), ' parties')  
    infected_first = Vertex('E')
    bfs_directed_graph = directed_graph.bfs(infected_first)
    print(infected_first.id, ' infected ', bfs_directed_graph, ' = ', len(bfs_directed_graph), ' parties')  
# %%   

# %%
    print('\n========== FINDING CYCLE USING BFS ==========\n') 
    vertices  = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H']
    no_cycle_1 = Graph(V = vertices)
    no_cycle_1.add_edge('A', 'B')   
    no_cycle_1.add_edge('A', 'C')
    no_cycle_1.add_edge('C', 'D')
    no_cycle_1.add_edge('B', 'F')
    no_cycle_1.add_edge('B', 'E')
    no_cycle_1.add_edge('F', 'G')
    no_cycle_1.add_edge('E', 'G')
    no_cycle_1.add_edge('E', 'H')
    no_cycle_1.add_edge('G', 'H')
    has_cycle = no_cycle_1.find_cycle()
    print('Has a cycle: ', has_cycle)

    # no_cycle_2 = 

    vertices  = ['A', 'B', 'C', 'D', 'E']
    has_cycle_1 = Graph(V = vertices)
    has_cycle_1.add_edge('A', 'B')   
    has_cycle_1.add_edge('A', 'C')
    has_cycle_1.add_edge('A', 'D')
    has_cycle_1.add_edge('A', 'E')
    has_cycle = has_cycle_1.find_cycle()
    print('Has a cycle: ', has_cycle)

    # has_cycle_2 = 
    # has_cycle = has_cycle_2.find_cycle()
    # print('Has a cycle: ', has_cycle)
    
# %%