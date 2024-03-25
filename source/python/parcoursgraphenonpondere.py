###

# un graphe représenté par listes d'adjacence. Les sommets sont numérotés de 0 à 6.
g = [
    [9,2], # voisins de 0
    [9,3], # voisins de 1
    [0,3,5,6], # voisins de 2
    [1,2,4], # voisins de 3
    [3,5], # voisins de 4
    [2,4], # voisins de 5
    [2], # voisins de 6
    [8], # voisins de 7
    [7], # voisins de 8
    [0, 1], # voisins de 9
]


##############################
# 0  ---  9   ---  1         #
# |                | \       # 
# |                |   \     #
# |                |     \   #
# 2  ------------  3 ---  4  #
# | \                   /    #
# |   \               /      #
# |     \           /        # 
# 6       \       /          #
#           \   /            #
#             5              #
#                            #
#     7 --- 8                # 
##############################

# Plutôt qu'une liste de listes, on pourrait également utiliser un dictionnaire dont les clés sont les sommets, et les valeurs les listes de voisins, ce qui permettrait que les sommets ne soient pas nécessairement les entiers numérotés de 0 à n-1. Par exemple {'a': ['b','c'], 'b' : ['a', 'd'], ...}

### Parcours en profondeur

def accessible_en_profondeur(g, i, c):
    '''g est un graphe, i et c deux sommets (initial et cible). Teste s'il existe un chemin reliant a et b, i.e. si a et b sont dans la même composante connexe du graphe.'''
    statut = [False for _ in g] # liste de 0, 1, 2. statut[i] vaut
                                #   0 si i n'est pas encore exploré
                                #   1 si i est à explorer
                                #   2 si i déjà exploré
    a_explorer = [i] # liste des sommets à explorer (implémentant une structure de pile)
    while a_explorer != []:
        s = a_explorer.pop();
        # print(s) # décommenter pour afficher l'ordre de parcours des sommets
        statut[s] = 2
        if s == c: # cible atteinte
            return True
        for v in g[s]: # parcours des voisins de s
            if statut[v] == 0:
                a_explorer.append(v);
                statut[v] = 1
    return False

print('accessibilité par parcours en profondeur')
for i in range(len(g)):
    for j in range(i+1, len(g)):
        print(i,'->',j,':',accessible_en_profondeur(g, i, j))
        
def accessible_en_profondeur_recursif(g, i, c):
    '''g est un graphe, i et c deux sommets (initial et cible). Teste s'il existe un chemin reliant a et b, i.e. si a et b sont dans la même composante connexe du graphe.'''
    statut = [False for _ in g] # liste de 0, 1, 2. statut[i] vaut
                                #   0 si i n'est pas encore exploré
                                #   1 si i est à explorer
                                #   2 si i déjà exploré
    def aux(j):
        '''teste récursivement si c est accessible à partir de j'''
        print(j) # décommenter pour afficher l'ordre de parcours des sommets

        if j == c: # cible atteinte
            return True
        statut[j] = 2
        for v in g[j]: # parcours des voisins de j
            if statut[v] == 0:
                statut[v] = 1 # on peut se passer de cette ligne: ce sommet va immédiatement être colorié passer au statut «déjà exploré» lors de l'appel récursif suivante
                if aux(v):
                    return True
        return False

    return aux(i)

print('accessibilité par parcours en profondeur récursif')
for i in range(len(g)):
    for j in range(i+1, len(g)):
        print(i,'->',j,':',accessible_en_profondeur(g, i, j))


### Parcours en profondeur avec calcul d'un chemin

def chemin(pere, c):
    '''pere est un tableau tel que pere[i] est le sommet pere de i dans le parcours s'il existe, -1 sinon. c est le sommet cible. Renvoie un chemin du sommet initial à c'''
    r = [c]
    while pere[c] != -1:
        r = [pere[c]] + r # sous-optimal, cette opération s'exécutant en temps O(len(r)). Mieux vaudrait utiliser append (qui s'exécute en temps amorti O(1)) puis effectuer une inversion de la liste finalement obtenue en temps linéaire.
        c = pere[c]
    return r
    
def chemin_en_profondeur(g, i, c):
    '''g est un graphe, i et c deux sommets (initial et cible). Renvoie s'il existe un chemin reliant a et b, None sinon.'''
    statut = [False for _ in g] # liste de 0, 1, 2. statut[i] vaut
                                #   0 si i n'est pas encore exploré
                                #   1 si i est à explorer
                                #   2 si i déjà exploré
    a_explorer = [i] # liste des sommets à explorer (implémentant une structure de pile)
    pere = [-1 for _ in g] # pere[i] est le sommet pere dans le parcours de i s'il existe, -1 s'il n'existe pas
    while a_explorer != []:
        s = a_explorer.pop();
        # print(s) # décommenter pour afficher l'ordre de parcours des sommets
        statut[s] = 2
        if s == c: # cible atteinte
            return chemin(pere, c)
        for v in g[s]: # parcours des voisins de s
            if statut[v] == 0:
                pere[v] = s
                a_explorer.append(v);
                statut[v] = 1
    return None

print('chemin par parcours en profondeur')
for i in range(len(g)):
    for j in range(i+1, len(g)):
        print(i,'->',j,':',chemin_en_profondeur(g, i, j))


### Parcours en largeur

# NB: on copie/colle les code ci-dessus, en remplaçant la liste «a_explorer» (qui implémente une structure de pile) par un «deque» (qui implémente une structure de file). On peut également garder une liste, et enlever au début (e.g. a_explorer = a_explorer[:1]), mais cela s'effectue en temps linéaire en la taille de a_explorer, alors que deque offre une complexité constante pour l'ajout à la fin ET la suppression au début.

from collections import deque

def accessible_en_largeur(g, i, c):
    '''g est un graphe, i et c deux sommets (initial et cible). Teste s'il existe un chemin reliant a et b, i.e. si a et b sont dans la même composante connexe du graphe.'''
    statut = [False for _ in g] # liste de 0, 1, 2. statut[i] vaut
                                #   0 si i n'est pas encore exploré
                                #   1 si i est à explorer
                                #   2 si i déjà exploré
    a_explorer = deque() # liste des sommets à explorer (implémentant une structure de file)
    a_explorer.append(i)
    while len(a_explorer) > 0:
        s = a_explorer.popleft();
        # print(s) # décommenter pour afficher l'ordre de parcours des sommets
        statut[s] = 2
        if s == c: # cible atteinte
            return True
        for v in g[s]: # parcours des voisins de s
            if statut[v] == 0:
                a_explorer.append(v);
                statut[v] = 1
    return False

print('accessibilité par parcours en largeur')
for i in range(len(g)):
    for j in range(i+1, len(g)):
        print(i,'->',j,':',accessible_en_largeur(g, i, j))


def distances(g, i):
    '''g est un graphe, i un sommet initial. Renvoie la liste des distances de i à tout sommet j (avec la convention que cette distance est -1 s'il n'existe pas de chemin entre i et j).'''
    statut = [False for _ in g] # liste de 0, 1, 2. statut[i] vaut
                                #   0 si i n'est pas encore exploré
                                #   1 si i est à explorer
                                #   2 si i déjà exploré
    a_explorer = deque() # liste des sommets à explorer (implémentant une structure de file)
    a_explorer.append(i)
    distance = [-1 for _ in g] # initialisation des distances
    distance[i] = 0 # i est à une distance 0 de lui-même
    while len(a_explorer) > 0:
        s = a_explorer.popleft();
        # print(s) # décommenter pour afficher l'ordre de parcours des sommets
        statut[s] = 2
        for v in g[s]: # parcours des voisins de s
            if statut[v] == 0:
                a_explorer.append(v);
                distance[v] = distance[s] + 1 
                statut[v] = 1
    return distance

print('distances par parcours en largeur')
for i in range(len(g)):
    print(i,':',distances(g, i))


        
def chemin_en_largeur(g, i, c):
    '''g est un graphe, i et c deux sommets (initial et cible). Renvoie s'il existe un plus court chemin reliant a et b, None sinon.'''
    statut = [False for _ in g] # liste de 0, 1, 2. statut[i] vaut
                                #   0 si i n'est pas encore exploré
                                #   1 si i est à explorer
                                #   2 si i déjà exploré
    a_explorer = deque() # liste des sommets à explorer (implémentant une structure de file)
    a_explorer.append(i)
    pere = [-1 for _ in g] # pere[i] est le sommet pere dans le parcours de i s'il existe, -1 s'il n'existe pas
    while len(a_explorer) > 0:
        s = a_explorer.popleft();
        # print(s) # décommenter pour afficher l'ordre de parcours des sommets
        statut[s] = 2
        if s == c: # cible atteinte
            return chemin(pere, c)
        for v in g[s]: # parcours des voisins de s
            if statut[v] == 0:
                pere[v] = s
                a_explorer.append(v);
                statut[v] = 1
    return False

print('chemin en largeur')
for i in range(len(g)):
    for j in range(i+1, len(g)):
        print(i, '->', j, ':', chemin_en_largeur(g, i, j))
