import math

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

     def add_edge(self, edge: Edge, is_directed=True):
          # self.add_vertex(edge.u)
          # self.add_vertex(edge.v)

          if not is_directed:
               self.adjacency_list[edge.u].append((edge.v, edge.w)) 
               self.adjacency_list[edge.v].append((edge.u, edge.w)) 
          else: 
               self.adjacency_list[edge.u].append((edge.v, edge.w)) 

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
          pass 

     def dfs(self, source: Vertex):
          pass  

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
          return_string = ""
          return_string += self.name 
          return return_string 

class Edge():
     def __init__(self, u: Vertex, v: Vertex, w = 1):
          self.u = u 
          self.v = v 
          self.w = w

     def __str__(self):
          return_string = ""
          return_string += "<" + self.u + ", " + self.v + ">"


if "__name__" == "__name__": 
     vertices = [Vertex('A'), Vertex('B'), Vertex('C'), Vertex('D'), Vertex('E')]
     adjacency_list_graph = AdjacencyListGraph(vertices)
     adjacency_list_graph.add_edge(Edge(Vertex('A'), Vertex('B'), 2))
     adjacency_list_graph.add_edge(Edge(Vertex('A'), Vertex('C'), 3))
     adjacency_list_graph.add_edge(Edge(Vertex('B'), Vertex('D'), 4))
     adjacency_list_graph.add_edge(Edge(Vertex('C'), Vertex('D'), 5))
     adjacency_list_graph.add_edge(Edge(Vertex('C'), Vertex('E'), 1))
     adjacency_list_graph.add_edge(Edge(Vertex('E'), Vertex('D'), 6))
     print(adjacency_list_graph)
