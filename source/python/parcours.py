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

def parcours_profondeur_dict(g,vus,s,o=None):
    """
    Comme le parcours profondeur mais utilise un dictionnaire pour les sommets visités:
    -> la clef est le sommet actuellment visité;
    -> la valeur est le sommet visité juste avant, la provenance en fait
    Avant le premier sommet, pas de sommet, donc valeur à None
    """
    vus=vus
    p=creer_pile()
    p.empiler((s,o))
    while not p.est_vide():
        so=p.depiler()
        s=so[0]
        o=so[1]
        if s not in vus:
            vus[s]=o
            for v in g.voisins(s):
                p.empiler((v,s))
    return vus

def parcours_profondeur_recursif(g,vus,s):
    """
    version récursive du parcours en profondeur;
    la pile des appels récursifs remplace la pile dans la version non récursive
    On a une liste vus des sommets visités initialisée à vide à l'appel
    Si le sommet visité n'a pas été visité:
    -> on l'ajoute à la liste vus
    -> pour tous ces voisins, on appelle la fonction avec le voisin
    La récursion s'arête quand le sommet a déjà été visité et que la boucle for est finie,
    c'est à dire quand tous les voisins ont été vus.
    """
    if s not in vus:
        vus.add(s)
        for v in g.voisins(s):
            parcours_profondeur_recursif(g,vus,v)
    return vus
    
def parcours_profondeur_recursif_dict(g,vus,s,o):
    """
    version récursive mais avec dictionnaire qui établit le lien entre les sommets
    """
    if s not in vus:
        vus[s]=o
        for v in g.voisins(s):
            parcours_profondeur_recursif_dict(g,vus,v,s)
    return vus
    
def chemin_graphe(g,u,v):
    """
    on cherche un chemin pour aller du sommet u (initial) au sommet v (final);
    on construit le dictionnaire des sommets avec un parcours en profondeur du graphe
    Ensuite, on remonte du sommet final au sommet initial en utilisant le lien clef, valeur
    - 
    """
    #vus=parcours_profondeur_recursif_dict(g,{},u,None)
    vus=parcours_profondeur_dict(g,{},u)
    # on vérifie le sommet v à atteindre depuis u est dans la liste des sommets visités
    # donc accessible sinon fin de la fonction
    if v not in vus:
        return None
    # initialisation du chemin à vide
    ch = []
    # initialisation du dernier sommet ; on remonte le graphe jusqu'au premier sommet
    s = v
    # Avant le premier sommet, c'est None, donc tant que le sommet n'est pas None
    while s is not None:
        ch.append(s)
        s=vus[s]
    ch.reverse()
    return ch

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
            if len(courant)==0:
                courant,suivant=suivant,set()
    return dist


# Début du programme principal
#------------------------------
if __name__ == '__main__':
    # Dictionnaire d'adjacence du graphe G
    G={'A':{'B','C'},\
       'B':{'A','C'},\
       'C':{'A','B','D'},\
       'D':{'C'}
      }
    H={'A':{'B','C'},\
       'B':{'A','E'},\
       'C':{'A','E'},\
       'D':{'F'},\
       'E':{'B','C','F'},\
       'F':{'D','E'}\
       }
    K={ 
    'B':{'C','F'},\
    'C':{'B','F','T','D'},\
    'D':{'C','F','T','N'},\
    'F':{'B','C','D','T','N'},\
    'N':{'D','T','F'},\
    'T':{'C','D','F','N'}
    }
    L={ 
    'A':{'B','C'},\
    'B':{'A','D','E'},\
    'C':{'A','E','F'},\
    'D':{'B','F'},\
    'E':{'B','C','F'},\
    'F':{'C','D','E'}
    }
    # Conversion du dictionnaire en objet graphe
    G=dict_to_graphe(G)
    G.afficher().view()
    # parcours profondeur sous forme de liste
    p0=parcours_profondeur(G,'A')
    p1=parcours_profondeur_recursif(G,set(),'A')
    # parcours profondeur sous forme de dictionnaire
    p2=parcours_profondeur_dict(G,{},'A')
    p3=parcours_profondeur_recursif_dict(G,{},'A',None)
    # Construction du chemin de u vers v
    ch0=chemin_graphe(G,'A','D')
    # parcours en largeur depuis un sommet vers tous les autres
    l=parcours_largeur(G,'A')