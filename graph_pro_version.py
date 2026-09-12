import math
from data_structures.linked_queue import LinkedQueue;
from data_structures.linked_stack import LinkedStack;

class AdjacencyListGraph():
     def __init__(self, V: list[Vertex]):
          '''
          AdjacencyListGraph representation.
          Example:
          adjacency_list
          {
               A: [(A, weight of A to B), (C, weight of A to C)],
               B: [(D, weight of B to D)],
               C: [(D, weight of C to D), (E, weight of C to E)],
               D: [],
               E: [(D, weight of C to E)]
          }
          '''
          self.adjacency_list = {}
          for v in V:
               self.add_vertex(v)

     def add_vertex(self, vertex: Vertex):
          if vertex not in self.adjacency_list:
               self.adjacency_list[vertex] = []

     def canonical_vertex(self, vertex: Vertex):
          '''
          Returns the single Vertex instance stored in this graph that has
          the same name, so traversal flags apply to one shared instance.
          '''
          for existing_vertex in self.adjacency_list:
               if existing_vertex == vertex:
                    return existing_vertex 
          return vertex 

     def add_edge(self, edge: Edge, is_directed=True):
          self.add_vertex(edge.u)
          self.add_vertex(edge.v)

          u = self.canonical_vertex(edge.u)
          v = self.canonical_vertex(edge.v)

          if not is_directed:
               self.adjacency_list[u].append((v, edge.w)) 
               self.adjacency_list[v].append((u, edge.w)) 
          else: 
               self.adjacency_list[u].append((v, edge.w)) 

     def get_outgoing(self, vertex: Vertex):
          return self.adjacency_list[vertex]

     def get_incoming(self, vertex: Vertex):
          incoming = []
          for u in self.adjacency_list:
               for (v, w) in self.adjacency_list[u]:
                    if v == vertex:
                         incoming.append((v, w))
          return incoming 

     def delete_edge(self, edge: Edge):
          for u in self.adjacency_list:
               for (v, w) in self.adjacency_list[u]:
                    if u == edge.u  and v == edge.v and w == edge.w:
                         self.adjacency_list[u].remove((edge.v, edge.w))

     def reset(self):
          for v in self.adjacency_list:
               v.discovered = False
               v.visited = False 
               v.distance = math.inf 
               v.previous = None 

               for (outgoing_v, w) in self.adjacency_list[v]:
                    outgoing_v.discovered = False
                    outgoing_v.visited = False 
                    outgoing_v.distance = math.inf 
                    outgoing_v.previous = None

     def bfs(self, source: Vertex):
          '''
          Ideal for undirected unweighted graph.
          Return a visited_output list in BFS order with BFSed distance from source vertex.
          '''
          source = self.canonical_vertex(source)
          discovered_queue = LinkedQueue()
          visited_output = []
          print('append ', source, ' into discovered_queue')
          discovered_queue.append(source)
          source.discovered = True 
          source.distance = 0

          while not discovered_queue.is_empty():
               visited = discovered_queue.serve()
               visited.visited = True
               print('append ', visited, ' into visited_output')
               visited_output.append((visited, visited.distance))
               for (v, w) in self.adjacency_list[visited]:
                    if not v.discovered:
                         v.discovered = True 
                         v.distance = visited.distance + 1 
                         v.previous = visited 
                         print('append ', v, ' into discovered_queue')
                         discovered_queue.append(v)

          self.reset()
          return visited_output

     def dfs(self, source: Vertex):
          '''
          Ideal for undirected unweighted graph.
          Return a visited_output list in DFS order with DFSed distance from source vertex.
          '''
          source = self.canonical_vertex(source)
          discovered_stack = LinkedStack()
          visited_output = []
          discovered_stack.push(source)
          print('push ', source, ' into discovered_stack')
          source.discovered = True 
          source.distance = 0 

          while not discovered_stack.is_empty():
               visited = discovered_stack.pop()
               visited.visited = True 
               print('append ', visited, ' into visited_output')
               visited_output.append((visited, visited.distance))
               for (v, w) in self.adjacency_list[visited]:
                    if not v.discovered:
                         v.discovered = True 
                         v.distance = visited.distance + 1
                         v.previous = visited 
                         print('push ', v, ' into discovered_stack')
                         discovered_stack.push(v)

          self.reset()
          return visited_output


     def relax_edge(self, u: Vertex, v: Vertex):
          pass 

     def __str__(self):
          return_string = "{\n"
          entries = []
          for u in self.adjacency_list:
               outgoings = ", ".join("(" + str(v) + ", " + str(w) + ")" for (v, w) in self.adjacency_list[u])
               entries.append("     " + str(u) + ": [" + outgoings + "]")
          return_string += ",\n".join(entries)
          return_string += "\n}"
          return return_string


class AdjacencyMatrixGraph():
     def __init__(self, V: list[Vertex]):
          '''
          AdjacencyMatrixGraph representation.
          Example:
          vertex_index_list = [A, B, C, D, E]
          adjacency_matrix = 
          [
               [0, 2, 3, 0, 0],
               [0, 0, 0, 4, 0],
               [0, 0, 0, 5, 1],
               [0, 0, 0, 0, 0],
               [0, 0, 0, 6, 0]
          ]
          '''
          self.vertex_index_list = []
          self.adjacency_matrix = []
          for v in V:
               self.add_vertex(v)               

     def add_vertex(self, vertex: Vertex):
          self.vertex_index_list.append(vertex)
          for row in self.adjacency_matrix:
               row.append(0)

          self.adjacency_matrix.append([0] * len(self.vertex_index_list))

     def add_edge(self, edge: Edge, is_directed=True):
          u_idx = self.vertex_list.index(edge.u)
          v_idx = self.vertex_list.index(edge.v)

          if not is_directed:
               self.adjacency_matrix[u_idx][v_idx] = edge.w 
               self.adjacency_matrix[v_idx][u_idx] = edge.w
          else: 
               self.adjacency_matrix[u_idx][v_idx] = edge.w 

     def __str__(self):
          return_string = ""
          for row in self.adjacency_matrix:
               return_string += row + ": "
               for col in row:
                    return_string += col + " "
               return_string += "/n"

          return return_string

class Vertex():
     def __init__(self, name: str):
          self.name = name
          self.edges = []
          self.discovered = False
          self.visited = False 
          self.distance = math.inf
          self.previous = None 

     def __str__(self):
          return self.name

     def __repr__(self):
          return f"{self.name}, {self.distance}"

     def __eq__(self, other):
          if not isinstance(other, Vertex):
               return NotImplemented 
          return self.name == other.name 

     def __hash__(self):
          return hash(self.name)

class Edge():
     def __init__(self, u: Vertex, v: Vertex, w = 1):
          self.u = u 
          self.v = v 
          self.w = w

     def __str__(self):
          return f"{self.u} -> {self.v} (w={self.w})"

     def __repr__(self):
          return f"Edge({self.u!r}, {self.v!r}, w={self.w})"

     def __eq__(self, other):
          pass

     def __hash__(self):
          pass


if "__name__" == "__name__": 
     vertices = [Vertex('A'), Vertex('B'), Vertex('C'), Vertex('D'), Vertex('E')]
     directed_adjacency_list_graph = AdjacencyListGraph(vertices)
     directed_adjacency_list_graph.add_edge(Edge(Vertex('A'), Vertex('B'), 2))
     directed_adjacency_list_graph.add_edge(Edge(Vertex('A'), Vertex('C'), 3))
     directed_adjacency_list_graph.add_edge(Edge(Vertex('B'), Vertex('D'), 4))
     directed_adjacency_list_graph.add_edge(Edge(Vertex('C'), Vertex('D'), 5))
     directed_adjacency_list_graph.add_edge(Edge(Vertex('C'), Vertex('E'), 1))
     directed_adjacency_list_graph.add_edge(Edge(Vertex('E'), Vertex('D'), 6))
     print(directed_adjacency_list_graph)

     vertices = [Vertex('A'), Vertex('B'), Vertex('C'), Vertex('D'), Vertex('E'), Vertex('F'), Vertex('G'), Vertex('H')]
     undirected_adjacency_list_graph = AdjacencyListGraph(vertices)
     undirected_adjacency_list_graph.add_edge(Edge(Vertex('A'), Vertex('B')), False)
     undirected_adjacency_list_graph.add_edge(Edge(Vertex('A'), Vertex('C')), False)
     undirected_adjacency_list_graph.add_edge(Edge(Vertex('C'), Vertex('D')), False)
     undirected_adjacency_list_graph.add_edge(Edge(Vertex('B'), Vertex('F')), False)
     undirected_adjacency_list_graph.add_edge(Edge(Vertex('B'), Vertex('E')), False)
     undirected_adjacency_list_graph.add_edge(Edge(Vertex('F'), Vertex('G')), False)
     undirected_adjacency_list_graph.add_edge(Edge(Vertex('E'), Vertex('G')), False)
     undirected_adjacency_list_graph.add_edge(Edge(Vertex('E'), Vertex('H')), False)
     undirected_adjacency_list_graph.add_edge(Edge(Vertex('G'), Vertex('H')), False)
     print(undirected_adjacency_list_graph)
     bfs = undirected_adjacency_list_graph.bfs(Vertex('A'))
     print(bfs)
     dfs = undirected_adjacency_list_graph.dfs(Vertex('A'))
     print(dfs)
