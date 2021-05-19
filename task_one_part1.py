from collections import defaultdict
from heapq import heappop, heappush
def dijkstra(graph, src, dest):
    # Initialisation du dictionnaire / matrice de contiguïté
    # Construire des données claires
    dictionary = defaultdict(list)
    for i, j, k in graph:
        dictionary[i].append((k, j))#tableaux qui donne les combainaison des lien des noued
        dictionary[j].append((k, i))#creation de deux cases d etabs
    # Heap file d'attente
    # on sauvegarde chaque nœud visité et également de la distance
    # pour le chemin final (optimisé)
    q, visited, dist = [(0, src,())], set(), {src: 0} #sauvgarder chaque noued visité
    while q:
        (distance, v1, path) = heappop(q) # la fonction heappop Sortez le plus petit élément du tas, en conservant l'invariant du tas
        if v1 in visited: continue #si le noued v1 visiter on continué
        visited.add(v1) #on ajoute chaque noued visité
        path += (v1,)
        # if v1 (current node) is goal then return
        if v1 == dest: return (distance, path) #si le noued v1 c'est notre but on le retourné
        for c, v2 in dictionary.get(v1, ()):
            if v2 in visited: continue
            # Min - Max distance algorithm
            # to find the shortest path
            if v2 not in dist or distance+c < dist[v2]:
                dist[v2] = distance+c
                heappush(q, (distance+c, v2, path)) # la fonction heappush Poussez l'élément sur le tas, en conservant l'invariant du tas.
    return float("Infinity") # S'il n'y a pas de chemin disponible
if __name__ == "__main__":
    # Data for dictionary / adjacency matrix
    # (i,j,k)
    graph = [
        ("v1", "v2", 500),("v1", "v3", 600),("v2", "v3", 300),
        ("v2", "v4", 400),("v3", "v4", 500),("v3", "v5", 400),
        ("v4", "v5", 300),("v4", "v6", 400),("v5", "v6", 600)
    ]
    start=(input("Where are you?")) #entrer le noued source
    finish=(input("Where do you want to go?")) #entrer le noued distination
    src=str(start)
    dest=str(finish)
    batuhan= dijkstra(graph, src, dest)
    print("The shortest path from {} to {} is [{}] with a distance of {} "
        .format(src,dest,batuhan[1],batuhan[0]
        )
    )