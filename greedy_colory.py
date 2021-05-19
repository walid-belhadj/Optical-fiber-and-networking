# GREEDY COLOR - ALGORITHM

colors = ['0-rouge','1-vert','2-jaune','3-white'];

nodes = {}
# Ii on definit les voisins de chaque noeuds
nodes['0'] = ['1', '2']
nodes['1'] = ['0', '2', '3']
nodes['2'] = ['0', '1', '3']
nodes['3'] = ['1', '2']

def voisins_2_noeuds (a , b):

	for i in nodes[str(a)]:
		print (b);
		print (i);
		if b == i:
			print ("ils sont voisins") ;
			break;

voisins_2_noeuds(1,2);
