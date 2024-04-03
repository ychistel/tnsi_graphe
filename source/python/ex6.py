from graphe import Graphe
from labyrinthe import creer_labyrinthe,afficher_labyrinthe

def grille_labyrinthe(n,m):
    entree=(0,0)
    sortie(n-1,m-1)
    for i in range(n):
        for j in range(m):
            
