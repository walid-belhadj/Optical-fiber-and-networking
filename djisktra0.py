s = 0; # source
src= [0]
d = []; #distance par rapport a la source
p = []; # noeud parent
v = [1, 2, 3, 4, 5, 6]; # déclaration des sommets
# INITIALISATION DE tous les d a infini:  sauf d(0)
for i in v:
	d.append(1000); # init à l'infini
	p.append(0); # init noeuds isolés
# intiaDistance du noeud source est egale a 0 de soit meme
d[s] = 0;
print ('La distance initiale: ',d)
def dijkstra(G,src):
	for j in src: # parcours de noeuds sources
		for i in v: # parcours de tous les vertex
			if (G[j][i] != 0): #si la valeur de chaque element de la matrice est différent de 0
				if d[i] > d[j] + float (G[j][i]): #on check si on peut avoir une distance mieux
					d[i] = d[j] + G[j][i] # si oui on update d(src, dest)
					p[i] = j # on sauvegarde le nouveau noeud parent
					src.append(i); # on concatène à la nouvelle liste de noeud
					print (src)
		print ('Parent: ',p,' de : ',d,'\n')

#dijkstra(G,src)

# Calculer du plus court chemin
def short_path(p,s,d):
	print ('src: ' + str(s) + ' dest: ' + str(d))
	temp = [d]

	while p[d] != s:
		temp.append(p[d]);
		d = p[d];

	temp.append(s);

	print ('Variable temporaire: ',temp)
	return temp;

voisins = {}

#for test in range(0,4):
#	voisins[test] = []
voisins[0]=[]
voisins[1]=[]
voisins[2]=[]
voisins[3]=[]
voisins[4]=[]
voisins[5]=[]
voisins[6]=[]

# Affichage inverse du chemin
"""
def formatage_chemin(chemin):
	temp = chemin;
	chemin = ''
	nbre = len(temp);
	for i in range(0,nbre):
		index = nbre-i-1
		chemin =  chemin + ' -->' +str(temp[index])
		print ('temp--: ',temp[index])
		voisins[i].append(temp[index])
	return chemin
# Affichage plus curt chemin d'un noeud a un autre
# noeud de 1 a 3
for dest in range(1,4):
	print (formatage_chemin( short_path(p,0,dest) )); # court chemin plus formatage de 0 a x
"""
print ('voisins: ', voisins)

colors = ['Green', 'White', 'Red', 'Yellow', 'Black']

states = ['1', '2', '3', '4', '5','6']
neighbors = {}
neighbors['1'] = ['2', '3']
neighbors['2'] = ['1', '3', '4']
neighbors['3'] = ['1', '2', '4', '5']
neighbors['4'] = ['2', '3', '5', '6']
neighbors['5'] = ['3', '4', '6']
neighbors['6'] = ['4', '5']
colors_of_states = {}

def promising(state, color):
    for neighbor in neighbors.get(state):
        color_of_neighbor = colors_of_states.get(neighbor)
        if color_of_neighbor == color:
            return False

    return True

def get_color_for_state(state):
    for color in colors:
        if promising(state, color):
            return color

def main():
    for state in states:
        colors_of_states[state] = get_color_for_state(state)

    print (colors_of_states)

main()
