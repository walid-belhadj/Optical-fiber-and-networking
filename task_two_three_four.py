from copy import deepcopy
# graph initialisation #
def graph_init(v,d):#initialisation de graph avec nmobre des noud et la distance entre chaque paire de noued
	for i in v: #boucle
		parent[i]=i #parent de 2 c'est ces noude source (1 dans notre cas )
		if i==start :
			d[i]=0
		else:
			d[i]=10**6
# check si les  nodes sont visitées
def visited_nodes(visited): #fonction qui nous permet d'avoir si les noued sont visiter
	for i in visited:
		if i==0:
			temp = 1
			break
		else:
			temp = 0
	return temp
# dijkstra algorithm
def dijkstra(G,src):#fonction de djikstra qui nous permet de determiner le plus court chemin
	src_temp=[]  #tableau pour sauvgarder la source a chaque fois
	for s in src:
		for i in v:
			if G[s][i]!=0: #condition pour garantie que on a dans le cas diffiret de 0
				if d[i]> d[s]+ G[s][i]:#on verifiez si on peux ameliorer d(s,v)
					d[i]=d[s]+ G[s][i] #mise a jour de s et v
					parent[i]=s        #le s devenu parent de i
					#distance[s][i]=d[i]
					#print('parent',parent)
				if(visited[i]==0):
					src_temp.append(i)
		visited[s]=1
	return (src_temp)
def inverso_tranch(s): #fonction pour inversé un string elle va retourné un string s reversé
    return s[::-1]
#global variable declaration
v=[0,1,2] # ensemble des vertex
#v0=[0,1,2,3,4,5]
distance=[[0]*len(v) for _ in range(len(v))] #un tableau on parcourir de lelement 0 fois la taille de notre vertex et aprés calculé la distance vers tt les autre noued
#distance=[[0]*len(v0) for _ in range(len(v0))]
lightpath=[] # list pour sauvegarder les lightpath
lightpaths={} #sauvgerder les lighpath on sotrie
l=0 #initialisaton
start=0 #initialisation de start (vertex)
dest=3 #dest=6
# Graphe G1
'''G0=([[0,500,600,0,0,0],
	[500,0,300,400,0,0],
	[600,300,0,500,400,0],
	[0,400,500,0,300,400],
	[0,0,400,300,0,600],
	[0,0,0,400,600,0]
	])'''
G=([[0,400,0], #declaration et remplisage de notre matrice
	[400,0,600],
	[0,600,0]])
print("graph G1",G) #affichage de notre G1
i=0 #initialisation de i
neighbors=['']*len(v) #tableau des voisins fois le nombre de sommet pour determiner nomre de voisinage (v1 avec ces voisin ,v2 avec ces voisin ...ext)
#neighbors0=['']*len(v0)
while i < len(v): #boucle tq avec i inferieur a nombre de sommet
	start=i
	d=[0]*len(v)
#	d=[0]*len(v0)

	visited=[0]*len(v) #pointer sur chaque noeud
#	visited=[0]*len(v0)
	src=[] #tab pour les noued source
	tree=[] #tab des chemin parcourer
	src.append(start) #concatination de chaque noued de start avec les noued de tab des noued  source
	voisin=['']*len(v) #remplir tab des voisin avec la matrice des vertex
	src_temp=[] #source temporaire
	parent=[0]*len(v) #le premier element de tab fois la matrice des vertex pour remplir les parant de chaque noued
	path_inv=[] #stocké le chemin inversé
	graph_init(v,d)
	terminer =visited_nodes(visited) #affecté les noued visiter au variable terminer
	while terminer:
		#execution d'algo dijsktra pour avoir le shortest path
		src=dijkstra(G,src) #appele pour lalgo de djikstra
		terminer =visited_nodes(visited) #les noued qui sont déja visité
#déclartion de combination de paths possibles
	for k in v:
		path=str(k)
		if k==start:
			continue
		while 1:
			path=path+str(parent[k])
			if parent[k]==start:
			#path=path+str(k)+'>'+str(start)
				path_inv=inverso_tranch(path)
				tree.append(path_inv)
				if path_inv not in lightpath:
					l=l+1
					x='l'+str(l)
					lightpath.append(path_inv)
					lightpaths[x]=path_inv
				break
			k=parent[k]
	t=0
	while t< len(parent):
		p=parent[t]
		if t!=p:
			voisin[t]=voisin[t]+str(p)
			voisin[p]=voisin[p]+str(t)
			if str(p) not in neighbors[t]:
				neighbors[t]=neighbors[t]+str(p)
			if str(t) not in neighbors[p]:
				neighbors[p]=neighbors[p]+str(t)
		t=t+1
	i=i+1
# Coloring Algorithm
src=0 #declaration de source a 0
j=0 #declaration de j a 0
color=[0]*len(v) #calcule variable color a partir de premier noued et avec l'aide de matrice des vertex
def get_color(neighbors,src): #fonction permet de returné et attrubié les couleur a chaque noued de notre graphe
	color=[0]*len(neighbors)# init tableau des couleurs
	color[src]=1 #on attirbue la coleiur numéro 1 à la src ou le node 1
	i=0
	while i<len(neighbors): # on parcours le tab des autres nodes
		if i==src:
			color[src]=1# on attribue la couleur 1 au node 1
			i=i+1
		else:
			j=0
			color[i]=1
			while j<len(neighbors[i]):
				if color[i]==color[int(neighbors[i][j])]:# on attribue une couleur différent au vertex i+1 <> à la couleur de i
					color[i]+=1
				j+=1
			i+=1
	return color #la fonction returné a la sortie color
#appel de fonction get_color
get_color(neighbors,start)
print("\n")
print('Liste des Lighpaths:',lightpath)
print("\n")
# dessiner lightpath graph et sa colorisation
lightpath_graph=[]
lightpath2_graph=[] #utiliser pour la nouvelle liste de lightpath
i=0
lightpath_graph_num=[]
lightpath_voisin=['']*len(lightpath) #écriture de l'ensemble des lightpaths dans d'un tableau de edges
# find lightpath graph and neighbours
for i in range(len(lightpath)):
	j=0
	#Sommets du graphe d'interférence
	for j in range(len(lightpath)): #on prend en entrée la table de lightpath
		if i!=j:
			if (lightpath[i] in lightpath[j]):
				temp=[]
				temp1=''
				temp.append('L'+str(i+1)) # on prend le L on le concatine avec l'unitaire par exp 0X ==> L0
				temp.append('L'+str(j+1)) # on prend le L on le concatine avec l'unitaire par exp X1 ==> L1
				lightpath_graph.append(temp) # on concatene le resultat dans le tableau de lightpath
				if str(j) not in lightpath_voisin[j]: # on check si le node en question doesnt existe dans la table des lightpath
					lightpath_voisin[i]=lightpath_voisin[i]+str(j) # on stock dans la table ensemble des
				if str(i) not in lightpath_voisin[j]:
					lightpath_voisin[j]=lightpath_voisin[j]+str(i)
print('Interference Graph:',lightpath_graph)
print("\n")
lightpath_color=[]
lightpath_color=get_color(lightpath_voisin,start)#
print('Greedy_Coloring:',lightpath_color)
print("\n")
print("Cacule de longeurs d'ondes; ")
# Calculate the distance to reach each node
def dijkstraistance(lightpath):
	for i in lightpath:
		begin=int(i[0])
		end=int(i[len(i)-1])
		for j in range(len(i)-1):
			current=int(i[j])
			next=int(i[j+1])
			distance[begin][end]=distance[begin][end]+G[current][next]
#isntance de l'algo dijkstra pour calculer le shortest path à partir du graph de lightpath
dijkstraistance(lightpath) #on instance
Mat_debit=[
    		[0,30,50],
			[30,0,50],
			[30,50,0]
			]
Mat_lightpath_num=[[0]*len(v) for _ in range(len(v))]#construction sous forme d'un tableau de lightpath
Mat_cap=[[0]*len(v) for _ in range(len(v))] #
debit_mod=[10,40,100]
ref_dist=[1750,1800,900]
lightpath2=[]
mat_traffic_setting=[
					[10,1750,1],
					[40,1800,2.5],
					[100,900,3.5]
					]
def calc_lightpath_num(lightpath): #calcule de l'ensemble de bandwidth
	for i in lightpath: # parcours de liste des lightpath
		begin=int(i[0])
		end=int(i[len(i)-1])
		temp_debit_mod=[]
		for p in mat_traffic_setting:
			if distance[begin][end]<p[1]:
				temp_debit_mod.append(p[1])
		print('bandwith',temp_debit_mod)
calc_lightpath_num(lightpath)
def lighpath_mat_gen():
	inf=0
	sup=0
	for i in range(3):
		for j in range(3):
			if Mat_debit[i][j]==30: # on decide d'attribuer de modulateur  3 *10
				Mat_lightpath_num[i][j]=1
				Mat_cap[i][j]=debit_mod[1]
				for l in lightpath:
					if int(l[0])==i and int(l[-1])==j:
						t=0
						while t< Mat_lightpath_num[i][j]:
							lightpath2.append(l)
							t=t+1
			elif Mat_debit[i][j]==50: #5*10
				Mat_lightpath_num[i][j]=2
				Mat_cap[i][j]=debit_mod[1]+debit_mod[0]
				for l in lightpath:
					if int(l[0])==i and int(l[-1])==j:
						t=0
						while t< Mat_lightpath_num[i][j]:
							lightpath2.append(l)
							t=t+1
	print('Nombre de LighPath nécessaires:',Mat_lightpath_num)
	print('Rate_Alloc_Matrix',Mat_cap)
	print("\n")
lighpath_mat_gen()
print("\n")
print('Multiple_LightPathts',lightpath2)
print("\n")
# find lightpath graph and neighbours
i=0
lightpath2_voisin=['']*len(lightpath2)
for i in range(len(lightpath2)):
	j=0
	for j in range(len(lightpath2)):
		if i!=j:
			if (lightpath2[i] in lightpath2[j]):
				temp=[]
				temp_rev=[]
				temp1=''
				temp.append('l'+str(i+1))
				temp.append('l'+str(j+1))
				temp_rev.append('l'+str(j+1))
				temp_rev.append('l'+str(i+1))
				if temp_rev not in lightpath2_graph:
					lightpath2_graph.append(temp)
				if str(j) not in lightpath2_voisin[i]:
					lightpath2_voisin[i]=lightpath2_voisin[i]+str(j)
				if str(i) not in lightpath2_voisin[j]:
					lightpath2_voisin[j]=lightpath2_voisin[j]+str(i)
print('New_interference_graph',lightpath2_graph)
lightpath2_color=[]
lightpath2_color=get_color(lightpath2_voisin,start)
print('Greedy_Coloring_2',lightpath2_color)
#End find lightpath graph and neighbours
# Calculate the bandwidth on every link
def calc_link_deb():
	link_deb=[[0]*len(v) for _ in range(len(v))]
	for i in range(len(v)):
		for j in range(len(v)):
			temp_deb=0
			temp=str(i)+str(j)
			for k in lightpath2:
				if temp in k:
					begin=int(k[0])
					end=int(k[-1])
					temp_deb=temp_deb+Mat_debit[begin][end]
			link_deb[i][j]=temp_deb
	return link_deb
link_debit=calc_link_deb()
print("\n")
print("à partir de miltiple lightpath and la matrice de throuput on trouve la matrice:")
print('throughput_matrix:',link_debit)
# Calculate the capacity on every link
def calc_link_cap():
	link_cap=[[0]*len(v) for _ in range(len(v))]
	for i in range(len(v)):
		for j in range(len(v)):
			temp_cap=0
			temp=str(i)+str(j)
			for k in lightpath2:
				if temp in k:
					begin=int(k[0])
					end=int(k[-1])
					temp_cap=temp_cap+Mat_cap[begin][end]
			link_cap[i][j]=temp_cap
	return link_cap
link_capacity=calc_link_cap()
#using rate alloc matrix we find la matrice de capacity comme suit:
print('capacity_matrix:',link_capacity)
#*************Début task 4********************#
"""
find the shportest path
"""
def get_route(src, dest, shortPath):#fonction reterné le plus court chemin avec 3 entrés source et destination et shortpath
    if src==dest:
        return [src]
    else:
        a=get_route(src, shortPath[dest][0], shortPath)#appel récursive
        a.append(dest)
        return a
def print_list( n , key=None): # affichage noued ou matrice
    a=""
    if key!=None:
        for value in n:
            a+=value+"-->lambda"+str(key[value])+"  "
    else:
        for value in n:
            a+=value+"  "
    return a+" "
#fonction pour parcourir une liste de éléments (vertex) afin de récenser tous les lightpaths
def process(val):
    a=[]
    for i in range(len(val)-1):
        a.append(str(val[i])+str(val[i+1]))
        a.append(str(val[i+1])+str(val[i]))
    return a #output une list de valeurs de
#***********************helping functions*******************************#
    """
    return  liste des nodes qui ne font pas partie de la liste des
    voisins du node en question
    """
    def available_nodes(self, node):
        nodes =list(self._nodes.keys())
        print(nodes) #print to check liste des nodes
        nodes.remove(node)
        #peers=[x[0] for x in self._nodes[node]]
        paires=list(self._nodes[node].keys())
        print(paires)
        a=str()
        for n in nodes:
            if n not in paires:
                a+=n+"\t"
        return a
def space(size_space):  #aurevoir
    a=""
    for i in range(size_space):
        a+=" "
    return a
def display( val ,type, key=None):#affichage de plus court chemin
    #affichage de shortpath
    for k, v in val.items():
            print("{} ==> parent : {} et distance de  : {}".format(k, v[0], v[1]))
    #coloring nodes
    for k, v in val.items():
            print("{}---->{}".format(k, v))
    #coloring de lambda
    for k, v in val.items():
            print("{}---->lambda{}".format(k, v))
    #Calcul des capacités
    for k, v in val.items():
            print("{}----> lightpaths : {} ".format(k, print_list( v["lightpaths"], key=key)))
            print("{}----> nodes : {}".format(space(len(k)),print_list(v["nodes"])))
            print("{}----> occurence : {}".format(space(len(k)), v["occurence"]))
            print("{}----> debit : {}".format(space(len(k)), v["rate"]))
class Graph(object):
    """ nodes : est la dict des nodes dans le Graph
                key ==> nodes
                value ==> list de peers peers ==> paire noeud et  poid (peer et weight)
    """
    #initialisation de l'objet de Graph
    def __init__(self, nodes):
        super(Graph, self).__init__()
        self._nodes = nodes
#function pour le choix d'un noeud précis
    def vertex_choose(self):
        a=str()
        for node in self._nodes.keys():
            a+=node+"\t"
        print("All nodes : {}".format(a))
        choice=str()
        while True:
            choice=input("Choisissez un node parmi les nodes: ")# choix de node source
            if choice in self._nodes.keys():
                break
            else :
                print("Node n'existe pas.")
        return choice
    def define(self):
        while True:
            choice=self.vertex_choose()
            print("Nodes voisins disponibles : {}".format(self.available_nodes(choice)))
            while True:
                try:
                    paires=self._read_peers(choice)
                    self._make_peers(choice, paires)
                    break
                except ValueError :
                    continue
            print(self)
class Graph(object):
    """docstring for Graph.
    L'objet qui permert de representer un Graph
        nodes : est la dict des nodes dans le Graph
                key ==> nodes
                value ==> list de peers
                peers ==> tuple peer et weight
    """
    def _init_(self, nodes):
        super(Graph, self)._init_()
        self._nodes = nodes
class Graph_task4(Graph):
    """docstring for Graph_task4."""
    def _init_(self, nodes):
        super(Graph_task4, self)._init_(nodes)
        self._node_all = deepcopy(nodes)
        #self._light_path=self.toLightPathGraph()
    """
    Marquage  des node comme amplificateur en appel  recursivement pour chaque les nodes fils
    """
    def amplify_node(self, source, weight, done=[]):
        if source in done :
            return
        else:
            mark=False
            done.append(source)
            for child in self._nodes[source].keys():
                if self._light_path.are_connected(source, child) and self._nodes[source][child]+weight> self._limit:
                    mark=True
                    break
            if mark:
                self._mark_dict[source]=True
                for child, w  in self._nodes[source].items():
                    if self._light_path.are_connected(source, child):
                        self.amplify_node(child, int(w))
            else:
                for child, w  in self._nodes[source].items():
                    if self._light_path.are_connected(source, child):
                        self.amplify_node(child, weight+ int(w))
    def _not_peer(self, k, v):
        for c in v:
            if c in self._nodes[k].keys():
                b=self._nodes[k].pop(c)
    def greedy_coloring_on_LP(self):
        return self._light_path.greedy_coloring()
    def calcul(self, rate, limit):
        self.setLimit(limit)
        self._light_path=self.toLightPathGraph()
        self.amplify_node("v1", 0)
        print("lightPath number : {}".format(self._light_path.number()))
        return self._light_path.calcul(self, rate), self._mark_dict
    """
    on choisit un seul node parmis
    """
    def choose_any(self):
        for x in self._nodes.keys():
            #print(x)
            return x
    def setLimit(self, limit):
        """ fixer une limite à la longueur maximale d'un lightPath
        """
        l={}
        self._mark_dict={}
        self._limit=limit
        self._nodes=deepcopy(self._node_all)
        for node, peers in self._nodes.items():
            #print("{}-->{}".format(node, peers))
            l[node]=[]

            self._mark_dict[node]=False
            for peer, weight in peers.items():
                if weight>limit:
                    l[node].append(peer)
        for k, v in l.items():
            self._not_peer(k, v)

def display( val ,type, key=None):
    for k, v in val.items():print("{} ==> parent : {} et poids : {}".format(k, v[0], v[1]))

    for k, v in val.items():
            print("{}---->{}".format(k, v))

    for k, v in val.items():
            print("{}---->lambda{}".format(k, v))
    nodes=val[0]
    mark_dict=val[1]
    for k, v in nodes.items():
            print("{}----> lightpaths : {} ".format(k, print_list( v["lightpaths"], key=key)))
            print("{}      nodes : {}".format(space(len(k)),print_list(v["nodes"])))
            print("{}      occurence : {}".format(space(len(k)), v["occurence"]))
            print("{}      debit : {}".format(space(len(k)), v["rate"]))
    print("-------------------- Amplificateurs ----------------------")
    for k, v in mark_dict.items():
        print(" {} : {}".format(k, v))

def print_list( n , key=None):
    a=""
    if key!=None:
        for value in n:
            a+=value+"-->lambda"+str(key[value])+"  "
    else:
        for value in n:
            a+=value+"  "
    return a+" "
def space(size_space):
    a=""
    for i in range(size_space):
        a+=" "
    return a
g4=Graph_task4({
        "v1":{"v2":1100,"v3":1600,"v8":2800},
        "v2":{"v1":1100,"v3":600,"v4":1000},
        "v3":{"v1":1600,"v2":600,"v6":2000},
        "v4":{"v2":1000,"v5":600,"v11":2400},
        "v5":{"v4":600,"v6":1100,"v7":800},
        "v6":{"v3":2000,"v5":1100,"v10":1200 ,"v13":2000},
        "v7":{"v5":800,"v8":700},
        "v8":{"v1":2800,"v7":700,"v9":700},
        "v9":{"v8":700,"v10":900,"v12":500,"v14":500},
        "v10":{"v6":1200,"v9":900},
        "v11":{"v4":2400,"v12":800,"v14":300},
        "v12":{"v9":500,"v11":800,"v13":300},
        "v13":{"v6":2000,"v12":300,"v14":300},
        "v14":{"v9":500,"v11":300,"v13":300}})
limit=input("Donner le longeur limite d'un lightpath : ")

g4.setLimit(limit)
display(g4.greedy_coloring() , type="")