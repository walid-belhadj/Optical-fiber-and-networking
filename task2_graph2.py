# graph initialisation
def init_graph(v,d):
	for i in v:
		parent[i]=i
		if i==start :
			d[i]=0
		else:
			d[i]=10**6
#check if all nodes have been visited
def all_visited(visited):
	for i in visited:
		if i==0:
			temp = 1
			break
		else:
			temp = 0
	return temp
# dijstra algorithm
def calc_d(G,source):
	source_temp=[]
	for s in source:
		for i in v:
			if G[s][i]!=0:
				#if str(i) not in voisin[i]:
				#	voisin[s]=voisin[s]+str(i)
				if d[i]> d[s]+ G[s][i]:

					d[i]=d[s]+ G[s][i]
					parent[i]=s
					#distance[s][i]=d[i]
					#print('parent',parent)

				if(visited[i]==0):
					source_temp.append(i)
		visited[s]=1
		#print('d_______',d)
	return (source_temp)
#reverse a string
def reverse_slicing(s):
    return s[::-1]
#global variable declaration
#v=[0,1,2]  #enselble des vertex (noued )
v=[0,1,2,3,4,5]
distance=[[0]*len(v) for _ in range(len(v))] #la distance
lp=[] #declaration de lightpath
#print("lp :",lp)
lightpaths={}
l=0
start=0
dest=3
#graph2
G=([[0,500,600,0,0,0],
	[500,0,300,400,0,0],
	[600,300,0,500,400,0],
	[0,400,500,0,300,400],
	[0,0,400,300,0,600],
	[0,0,0,400,600,0]
	])
# Graphe G1
#G=([[0,400,0],
#[400,0,600],
#[0,600,0]])
#print("graph G1",G)
i=0
voisins=['']*len(v)
while i < len(v):
	start=i

	d=[0]*len(v)
#pointer sur chaque noeud
	visited=[0]*len(v)
	#print('visted',visited)
	source=[]
	tree=[]
	source.append(start)
	voisin=['']*len(v)
	source_temp=[]
	parent=[0]*len(v)
	#print('parent',parent)
	chemin_inv=[]


	init_graph(v,d)

	terminer =all_visited(visited)
	#print('terminer-----1',terminer)
	while terminer:
		#execution d'algo dijsktra pour avoir le mielleur chemin
		source=calc_d(G,source)
		#print('test source', source)
		#print ('parent',parent)

		terminer =all_visited(visited)
		#print('termnier____2',terminer)
#la boucle pour decalrer les chemins possible
	for k in v:
		chemin=str(k)
		if k==start:
			continue
		while 1:
			chemin=chemin+str(parent[k])
			#print('test chemin_______',chemin)
			if parent[k]==start:
				#chemin=chemin+str(k)+'>'+str(start)
				#print('chemin',reverse_slicing(chemin))
				chemin_inv=reverse_slicing(chemin)
				tree.append(chemin_inv)
				if chemin_inv not in lp:
					l=l+1
					x='l'+str(l)

					lp.append(chemin_inv)
					#print('chemin_inv',chemin_inv)
					lightpaths[x]=chemin_inv
					#print('lightpaths______',lightpaths)
				break

			k=parent[k]
	t=0
	while t< len(parent):
		p=parent[t]
		if t!=p:
			voisin[t]=voisin[t]+str(p)
			voisin[p]=voisin[p]+str(t)
			if str(p) not in voisins[t]:
				voisins[t]=voisins[t]+str(p)
			if str(t) not in voisins[p]:
				voisins[p]=voisins[p]+str(t)
		t=t+1

	i=i+1
##Coloring Algorithm
start=0
j=0
color=[0]*len(v)
def get_color(voisins,start):
	color=[0]*len(voisins)
	color[start]=1
	i=0
	while i<len(voisins):
		if i==start:
			color[start]=1
			i=i+1
		else:
			j=0
			color[i]=1

			while j<len(voisins[i]):

				if color[i]==color[int(voisins[i][j])]:
					color[i]+=1
				j+=1
			i+=1
	return color
get_color(voisins,start)
print("\n")
print('List of Lighpaths:',lp)
print("\n")
# draw lightpath graph and color it
lp_graph=[]
lp2_graph=[]
i=0
lp_graph_num=[]
lp_voisin=['']*len(lp)

#print('lp_voisin___',lp_voisin)
################################### find lightpath graph and neighbours
for i in range(len(lp)):
	j=0
	#Sommets du graphe d'interférence
	for j in range(len(lp)):
		if i!=j:
			if (lp[i] in lp[j]):
				temp=[]
				temp1=''
				temp.append('L'+str(i+1))
				#print('I',temp.append('L'+str(i+1)))
				temp.append('L'+str(j+1))
				#print('J',temp.append('L'+str(j+1)))

				lp_graph.append(temp)
				#print('lp_graph',lp_graph.append(temp))

				if str(j) not in lp_voisin[j]:
					lp_voisin[i]=lp_voisin[i]+str(j)
				if str(i) not in lp_voisin[j]:
					lp_voisin[j]=lp_voisin[j]+str(i)
################################### End find lightpath graph and neighbours
print('Interference Graph:',lp_graph)
print("\n")
#print('lp_voisin___',lp_voisin)
lp_color=[]
lp_color=get_color(lp_voisin,start)
print('Greedy_Coloring:',lp_color)
print("\n")
############################################################ end lp

################################ Calculate the distance to reach each node
def calc_distance(lp):
	for i in lp:
		beg=int(i[0])
		end=int(i[len(i)-1])
		for j in range(len(i)-1):
			cur=int(i[j])
			nex=int(i[j+1])
			distance[beg][end]=distance[beg][end]+G[cur][nex]
#
# 	print('distance!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!',distance)

######################################end calc distance
#print('distance__________________',distance)
calc_distance(lp)
Mat_debit=[[0,30,50],[30,0,50],[30,50,0]]
Mat_lp_num=[[0]*len(v) for _ in range(len(v))]
Mat_cap=[[0]*len(v) for _ in range(len(v))]
bw=[10,40,100]
ref_dist=[1750,1800,900]
lp2=[]
parameter=[[10,1750,1],[40,1800,2.5],[100,900,3.5]]
def calc_lp_num(lp):
	for i in lp:
		beg=int(i[0])
		end=int(i[len(i)-1])
		temp_bw=[]
		for p in parameter:
			if distance[beg][end]<p[1]:
				temp_bw.append(p[1])
		print('bandwith',temp_bw)
#calc_lp_num(lp)

def generate_lp_mat():
	inf=0
	sup=0
	for i in range(3):
		for j in range(3):
			if Mat_debit[i][j]==30:
				Mat_lp_num[i][j]=1
				Mat_cap[i][j]=bw[1]
				for l in lp:
					if int(l[0])==i and int(l[-1])==j:
						t=0
						while t< Mat_lp_num[i][j]:
							lp2.append(l)
							t=t+1
			elif Mat_debit[i][j]==50:
				Mat_lp_num[i][j]=2
				Mat_cap[i][j]=bw[1]+bw[0]
				for l in lp:
					if int(l[0])==i and int(l[-1])==j:
						t=0
						while t< Mat_lp_num[i][j]:
							lp2.append(l)
							t=t+1
	print('Number_Lightpath_necessaire:',Mat_lp_num, 'exemple: nous avons besoin que de R1 pour un taux de 30 donc 1 chemin')
	print('Rate_Alloc_Matrix',Mat_cap)
	print("\n")

generate_lp_mat()




print("\n")
print("\n")


print('Multiple_LightPathts',lp2)
print("\n")
################################### find lightpath graph and neighbours
i=0
lp2_voisin=['']*len(lp2)
for i in range(len(lp2)):
	j=0
	for j in range(len(lp2)):
		if i!=j:
			if (lp2[i] in lp2[j]):
				temp=[]
				temp_rev=[]
				temp1=''
				temp.append('l'+str(i+1))
				temp.append('l'+str(j+1))
				temp_rev.append('l'+str(j+1))
				temp_rev.append('l'+str(i+1))
				if temp_rev not in lp2_graph:
					lp2_graph.append(temp)
				if str(j) not in lp2_voisin[i]:
					lp2_voisin[i]=lp2_voisin[i]+str(j)
				if str(i) not in lp2_voisin[j]:
					lp2_voisin[j]=lp2_voisin[j]+str(i)
print('New_interference_graph',lp2_graph)
#print('______________________________________________________')
#print('lp2_voisin___',lp2_voisin)
lp2_color=[]
lp2_color=get_color(lp2_voisin,start)
print('Greedy_Coloring_2',lp2_color)
################################### End find lightpath graph and neighbours
################################### Calculate the bandwidth on every link
def calc_link_deb():
	link_deb=[[0]*len(v) for _ in range(len(v))]
	for i in range(len(v)):
		for j in range(len(v)):
			temp_deb=0
			temp=str(i)+str(j)
			for k in lp2:
				if temp in k:
					beg=int(k[0])
					end=int(k[-1])
					temp_deb=temp_deb+Mat_debit[beg][end]
			link_deb[i][j]=temp_deb
	return link_deb
link_debit=calc_link_deb()
print("\n")
print("from multiple lighp mat and throuput matrix we find:")
print('throughput_matrix:',link_debit)
################################### Calculate the capacity on every link
def calc_link_cap():
	link_cap=[[0]*len(v) for _ in range(len(v))]
	for i in range(len(v)):
		for j in range(len(v)):
			temp_cap=0
			temp=str(i)+str(j)
			for k in lp2:
				if temp in k:
					beg=int(k[0])
					end=int(k[-1])
					temp_cap=temp_cap+Mat_cap[beg][end]
			link_cap[i][j]=temp_cap
	return link_cap
link_capacity=calc_link_cap()
print("\nusing rate alloc matrix we find:")
print('capacity_matrix:',link_capacity)