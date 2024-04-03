from graphe import Graphe, dict_to_graphe
from pile import Pile, creer_pile

"""
Parcours en profondeur d'un graphe:
- g est un objet graphe de type classe Graphe
- s est un sommet du graphe g
"""

def parcours_profondeur(g,s):
    """
    on crée une liste vus qui recensent les sommet visités;
    on choisit un sommet s, on l'ajoute à la liste vus;
    on empile les sommets v voisins du sommet s
    tant que la pile n'est pas vide:
    -> soit le voisin v a déjà été visité, il est dans vus, on continue
    -> soit il n'a pas été visité, on l'ajoute et on empile ses voisins
    """
    vus=[]
    p=creer_pile()
    p.empiler(s)
    while not p.est_vide():
        s=p.depiler()
        if s in vus:
            continue
        vus.append(s)
        for v in g.voisins(s):
            p.empiler(v)
    return vus


def chemin(g,s1,s2):
    return s2 in parcours_profondeur(g,s1)

"""
Parcours en largeur d'un graphe:
- g est un objet graphe de type classe Graphe
- s est un sommet du graphe g
"""

def parcours_largeur(g,s):
    """
    on détermine la distance de tous les sommets à un sommet s
    """
    dist={s:0}
    courant={s}
    suivant=set()
    while len(courant)>0:
        sommet=courant.pop()
        for v in g.voisins(sommet):
            if v not in dist:
                suivant.add(v)
                dist[v]=dist[sommet]+1
            else:
                if dist[v]>dist[sommet]+1:
                    dist[v]=dist[sommet]+1
            if len(courant)==0:
                courant,suivant=suivant,set()
    return dist


# Début du programme principal
#------------------------------
if __name__ == '__main__':
    # Dictionnaire d'adjacence du graphe G
    G={'A':{'B','C'},\
       'B':{'A','D','E'},\
       'C':{'A','E','F'},\
       'D':{'B','E','G'},\
       'E':{'B','C','D','G'},\
       'F':{'C','H'},\
       'G':{'D','E','H'},\
       'H':{'G','F'}
      }
    H={'A':{'B','C'},\
       'B':{'A','E'},\
       'C':{'A','E'},\
       'D':{'F'},\
       'E':{'B','C','F'},\
       'F':{'D','E'}\
       }
    K={'A':{'E','C'},\
       'B':{'D','E','I'},\
       'C':{'F','L'},\
       'D':{'B','E','I'},\
       'E':{'B','D'},\
       'F':{'L'},\
       'G':{'J','H'},\
       'H':{'J','G'},\
       'I':{'B','D'},\
       'J':{'H','G'},\
       'L':{'C','F'}
      }
    # Conversion du dictionnaire en objet graphe
    # Exemple 1:
    #G=dict_to_graphe(G)
    #G.afficher().view()
    
    # Exemple 2:
    #H=dict_to_graphe(H)
    #H.afficher().view()
    
    # Exemple 3:
    K=dict_to_graphe(K)
    K.afficher().view()
    #print(chemin(K,'A','G'))
    
    
    # parcours profondeur sous forme de liste
    #p0=parcours_profondeur(K,'G')
    #p1=parcours_profondeur(H,'A')
    # parcours en largeur depuis un sommet vers tous les autres
    l0=parcours_largeur(K,'A')
    #l1=parcours_largeur(H,'A')