from graphe import Graphe
#from graphe_dict import Graphe_dict

G=Graphe(5)
G.adj={'A':{'B','C'},\
'B':{'A','C'},\
'C':{'A','B','D','E'},\
'D':{'C','E'},\
'E':{'C','D'}}
print(G.adj)

M=Graphe(5)
M.ajouter_arc(0,1)
M.ajouter_arc(0,2)
M.ajouter_arc(1,0)
M.ajouter_arc(1,2)
M.ajouter_arc(2,0)
M.ajouter_arc(2,1)
M.ajouter_arc(2,3)
M.ajouter_arc(2,4)
M.ajouter_arc(3,2)
M.ajouter_arc(3,4)
M.ajouter_arc(4,2)
M.ajouter_arc(4,3)

def graphe_dict_to_mat(g):
    # Le nombre de sommets du graphe donne la dimension de la matrice d'adjacence
    n=len(g.sommets())
    # Création de l'abjet matrice d'adjacence
    M=Graphe_mat(n)
    # On parcourt les sommets du graphe
    for s in g.sommets():
        # indice de ligne du sommet S
        i=g.sommets().index(s)
        # On parcourt les voisins du sommet s
        for v in g.voisins(s):
            # indice de colonne du sommet adjacent
            j=g.sommets().index(v)
            # coefficient (i,j) ey (j,i) mis à 1
            M.ajouter_arc(i,j)
    return M


def graphe_mat_to_dict(m):
    # On crée l'objet g de type Graphe_dict
    g=Graphe_dict()
    # On récupère le code ascii (en décimal) de la lettre A
    rg=ord('A')
    # On parcourt chaque ligne de la matrice
    for i in range(len(m.mat)):
        # On parcourt chaque colonne d'une ligne de matrice
        for j in range(len(m.mat)):
            # si le coeffient vaut 1, les sommets sont adjacents,
            if m.mat[i][j]==1:
                # on ajoute un arc entre les sommets i et j à l'objet Graphe_dict
                g.ajouter_arc(chr(rg+i),chr(rg+j))
    return g