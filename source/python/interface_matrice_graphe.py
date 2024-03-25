from graphviz import Graph,Digraph

def creer_matrice(n):
    return [[0]*n for _ in range(n)]   

def est_adjacent(matrice,i,j):
    return matrice[i][j]==1 or matrice[j][i]==1


def ajouter_arc(matrice,i,j):
    matrice[i][j]=1
    matrice[j][i]=1
    return matrice

def supprimer_arc(matrice,i,j):
    matrice[i][j]=0
    matrice[i][i]=0
    return matrice

def afficher(matrice):
    """
    Le module Graphviz est utilisé. Les sous-modules Digraph et Graphe
    sont importés.
    La fonction crée un graphe pour être afficher (image format 'png')
    Le graphe est non orienté !
    - on crée les sommets 0->A, 1->B, 2->C,etc
    - on crée les arcs entre les sommets adjacents
    La fonction renvoie un objet 'dot' qui contient le graphe à afficher
    """
    dot=Graph(format='png')
    n = len(matrice)
    # on crée les sommets du graphe
    for i in range(n):
        dot.node(str(chr(65+i)))
    # on crée les arcs entre les sommets
    for i in range(n):
        for j in range(i,n):
            if est_adjacent(matrice,i,j):
                dot.edge(str(chr(65+i)),str(chr(65+j)))
    return dot

M = creer_matrice(4)
ajouter_arc(M,0,1)
ajouter_arc(M,0,3)
ajouter_arc(M,1,2)
ajouter_arc(M,1,3)
ajouter_arc(M,2,3)
G = afficher(M)
G.view()