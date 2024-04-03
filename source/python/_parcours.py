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
    """
