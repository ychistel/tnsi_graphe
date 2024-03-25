from graphviz import Graph,Digraph

def creer_liste():
    return {}

def est_adjacent(liste,s1,s2):
    return s1 in liste[s2] and s2 in liste[s1]

def ajouter_sommet(liste,s):
    liste[s] = []
    
def ajouter_adjacent(liste,s1,s2):
    if s1 not in liste[s2]:
        liste[s2].append(s1)
    if s2 not in liste[s1]:
        liste[s1].append(s2)
        
def afficher(liste):
    """
    Le module Graphviz est utilisé. Les sous-modules Digraph et Graphe
    sont importés.
    La fonction crée un graphe pour être affiché (image format 'png')
    Le graphe est non orienté !
    - on crée les sommets du graphe
    - on crée les arcs entre les sommets adjacents
    La fonction renvoie un objet 'dot' qui contient le graphe à afficher
    """
    dot=Graph(format='png')
    # on crée les sommets du graphe
    for s in liste.keys():
        dot.node(s)
    # on crée la liste des arcs entre les sommets
    arcs = []
    for s in liste.keys():
        for s_adj in liste[s]:
            if (s,s_adj) not in arcs and (s_adj,s) not in arcs:
                arcs.append((s,s_adj))
    # on ajoute les arcs au graphe
    for arc in arcs:
        s1,s2 = arc
        dot.edge(s1,s2)
    return dot

def parcours_profondeur(graphe,sommet):
    """
    Paramètres:
    - graphe : liste des sommets adjacence du graphe (dictionnaire)
    - sommet : un sommet du graphe (départ du parcours)
    Return
    La fonction renvoie la liste vus contenant les sommets visités
    depuis le sommet de départ.
    Variables locales:
    - p représente une pile contenant les voisins de chaque sommet visité
    - s est un sommet du graphe
    """
    vus = []
    p = [sommet]
    while len(p) > 0:
        s = p.pop()
        if s not in vus:
            vus.append(s)
            for v in graphe[s]:
                p.append(v)
    return vus

if __name__ == '__main__':
    L = creer_liste()
    ajouter_sommet(L,'A')
    ajouter_sommet(L,'B')
    ajouter_sommet(L,'C')
    ajouter_sommet(L,'D')
    ajouter_adjacent(L,'A','B')
    ajouter_adjacent(L,'A','D')
    ajouter_adjacent(L,'B','D')
    ajouter_adjacent(L,'B','C')
    ajouter_adjacent(L,'C','D')
    parcours_D = parcours_profondeur(L,'D')
    parcours_A = parcours_profondeur(L,'A')
    G = afficher(L)
    G.view()
