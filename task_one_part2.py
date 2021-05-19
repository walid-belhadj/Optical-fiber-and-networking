# A class to represent a graph object
class Graph:
	# Constructor
	def __init__(self, edges, N):
		self.adj = [[] for _ in range(N+1)]
		# Ajout de edges pour un graphe non orienté
		for (src, dest) in edges:
			self.adj[src].append(dest)
			self.adj[dest].append(src)
# Fonction attirbution de couleurs aux sommets
def greedy_algorithm(graph):
	# on doit tracer la acouleur attirbuée à chaque vertex
	result = {}
	#Assignements de couleurs à chaque vertex un par un
	for u in range(N+1):
		# on check colors des voisins de chaque vertex de u et stocker dans la table assigned
		assigned = set([result.get(i) for i in graph.adj[u] if i in result])
		# check la première couleur
		color = 0
		for c in assigned:
			if color != c:
				break
			color = color + 1
		# on assigne  vertex `u` la première couleur dispo
		result[u] = color
	for v in range(6):
		print("Color assigned to vertex", v, "is", colors[result[v+1]])
# Greedy coloring of a graph
if __name__ == '__main__':

	# Add more colors for graphs with many more vertices
	colors = ["BLUE", "GREEN", "RED", "YELLOW", "ORANGE", "PINK",
			"BLACK", "BROWN", "WHITE", "PURPLE", "VOILET"]
	# of graph edges as per the above diagram
	N =6
	edges = [(1, 2),(1, 3),
				(2, 3),(2, 4),
				(3, 4),(3, 5),
				(4, 5),(4, 6),
				(5, 6)]
	edges1= [(1, 2),(2, 3)]
	# total number of nodes in the graph
	N =6
	# contruire le graphe à partir des edges
	graph = Graph(edges, N)
	# color graph using the greedy_algorithm
	greedy_algorithm(graph)
