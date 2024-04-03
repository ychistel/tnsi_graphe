from graphe import Graphe,matrice_to_graphe

# Question 2-a-b-c)
"""
G=Graphe()
G.ajouter_sommet('A')
G.ajouter_sommet('B')
G.ajouter_sommet('C')
G.ajouter_sommet('D')
G.ajouter_arc('A','B')
G.ajouter_arc('A','D')
G.ajouter_arc('C','B')
G.ajouter_arc('D','B')
G.ajouter_arc('D','C')
print(G.dict.valeur)
G.afficher().view()
"""
# Question 3
# a)
"""
G=Graphe()
G.ajouter_arc('A','B')
G.ajouter_arc('A','C')
G.ajouter_arc('B','D')
G.ajouter_arc('C','D')
print(G.matrice.valeur)
"""
# b)
def arcs_en_graphe(arcs):
    g=Graphe()
    for arc in arcs:
        g.ajouter_arc(arc[0],arc[1])
    return g

"""
G=arcs_en_graphe([('A','B'),('A','C'),('B','D'),\
                  ('B','E'),('C','E'),('C','F'),\
                  ('D','F'),('E','F')])
print(G.dict.valeur)
"""
# 4 - degré et chaine eulerienne
"""
def degre_sommet(g):
    degre=[]
    for sommet in g.dict.valeur:
        degre.append((sommet,len(g.dict.valeur[sommet])))
    return degre

def chaine_eulerienne(g):
    d=degre_sommet(g)
    nb_deg_impair=0
    for elt in d:
        if elt[1]%2==1:
            nb_deg_impair+=1
    return nb_deg_impair==2

# c)
H=[('A','F'),('A','C'),('C','F'),\
   ('C','D'),('C','T'),('F','D'),('F','N'),('F','T'),\
   ('T','D'),('T','N'),('D','N')]
H=arcs_en_graphe(H)
print(degre_sommet(H))
print(chaine_eulerienne(H))
"""

# 5 ) Créer un graphe avec son dictionnaire d'adjacence:
"""
G={'A':{'B','C'},\
   'B':{'A','D','E'},\
   'C':{'A','E','F'},\
   'D':{'B','F'},\
   'E':{'B','C','F'},\
   'F':{'C','D','E'}\
   }

def dico_adj_graphe(d):
    g=Graphe()
    for clef in d:
        for v in d[clef]:
            g.ajouter_arc(clef,v)
    return g

K=dico_adj_graphe(G)
print(K.dict.valeur)
print(K.matrice.valeur)
print(K.arcs)
K.afficher().view()
"""
# 6 ) Créer un graphe depuis sa matrice d'adjacence
M=[[0,1,1,0,0],[1,0,1,0,0],[1,1,0,1,1],[0,0,1,0,1],[0,0,1,1,0]]
M=matrice_to_graphe(M)
print(M.matrice.valeur)
print(M.dict.valeur)
