import matplotlib
import matplotlib.pyplot as plt
from random import shuffle # permet le mélange d'une liste
from graphe import Graphe
from pile import Pile,creer_pile
from parcours import *

# Fonctions de construction du labyrinthe
    
def __voisins__(pos):
    """ Renvoie les positions voisines de pos non encore visitées"""
    i,j=pos
    liste=[]
    for dx in (-1,1):
        if 0<=i+dx<N and T[i+dx][j]:
            liste.append((i+dx,j))
        if 0<=j+dx<M and T[i][j+dx]:
            liste.append((i,j+dx))
    shuffle(liste)
    return liste

def __interdire__(pos):
    # interdit la visite d'une position
    global nbreVisites
    nbreVisites+=1
    i,j=pos # i = pos[0] et j = pos[1]
    T[i][j] = False
        
def __positionNonVisitee__(): # Encore une position à visiter ?
    return nbreVisites < N*M

def __parcours__():
    """
    On construit le parcourt du labyrinthe avec sa solution entre entrée et sortie
    dans un carré de NxM cases
    """
    position=entree
    filDariane = creer_pile()
    filDariane.empiler(position)
    visites=[position] # mémoire des positions visitées
    while __positionNonVisitee__():
        voisinage = __voisins__(position)
        if voisinage == []: # retour arrière
            filDariane.depiler()
            position=filDariane.peek()
            visites.append(position)
        else:
            position = voisinage[0] # avancement
            filDariane.empiler(position)
            visites.append(position)
            __interdire__(position)
    return visites


def creer_labyrinthe(g):
    """
    Créer un labyrinthe à partir d'un graphe défini par des coordonnées de cellules.
    Le labyrinthe est une grille, liste python (en deux dimensions) qui contient 2N+1 listes de
    longueur 2M+1 où N et M sont les dimensions du labyrinthe.
    Les valeurs des listes sont 0 ou 1:
     - 1 pour indiquer un passage;
     - 0 pour la présence d'un mur
    On initialise la grille avec les valeurs égales à 0; le labyrinthe n'est que murs au départ.
    Ensuite, selon les sommets du graphe et les arcs entre sommets, on modifie les valeurs à 1
    construisant ainsi le labyrinthe.
    """
    
    # Construction de la grille du labyrinthe
    Laby=[[0]*(2*M+1) for _ in range(2*N+1)]
    for s in g.sommets():
        i0,j0=s[0],s[1]
        Laby[2*i0+1][2*j0+1]=1
    for arc in g.arcs:
        i0,j0=arc[0][0],arc[0][1]
        i1,j1=arc[1][0],arc[1][1]
        if i0==i1: # même ligne i
            if j0<j1:
                Laby[2*i0+1][2*j0+2]=1 # percement du mur
            else:
                Laby[2*i0+1][2*j1+2]=1
        elif j0==j1:
            if i0<i1:
                Laby[2*i0+2][2*j0+1]=1 # percement du mur
            else:
                Laby[2*i1+2][2*j1+1]=1
    #entrée et sortie
    Laby[2*entree[0]+1][0] = Laby[2*sortie[0]+1][2*M] = 1
    return Laby

def afficher_labyrinthe(labyrinthe):
    plt.imshow(labyrinthe,interpolation='nearest',cmap=matplotlib.cm.gray)
    plt.xticks([])
    plt.yticks([])
    return plt

def afficher_labyrinthe_solution(labyrinthe):
    plt.imshow(labyrinthe,interpolation='nearest',cmap=matplotlib.cm.gray)
    plt.xticks([])
    plt.yticks([])
    v=chemin[0]
    for k in range(1,len(chemin)):
        w=chemin[k]
        plt.plot([v[1]*2+1,w[1]*2+1],[v[0]*2+1,w[0]*2+1],color='red',linewidth=4)
        v=w
    plt.axis([0,2*M,2*N,0])
    return plt

if __name__=='__main__':
    # largeur et hauteur du labyrinthe
    N,M=16,16
    
    # position de l'entrée
    entree = (0,0)
    
    # position de la sortie
    sortie = (N-1,M-1)
    
    # tableau NxN des positions non visitées (ne pas modifier)
    T=[[True]*M for _ in range(N)]
    
    # compteur de cases visitées (ne pas modifier)
    nbreVisites = 0
    
    # générateur automatique de labyrinthe
    #-------------------------------------
    """
    visites=__parcours__()
    k=0
    arcs=[]
    while k < len(visites)-1:
        arcs.append((visites[k],visites[k+1]))
        k+=1
    G=Graphe()
    for arc in arcs:
        G.ajouter_arc(arc[0],arc[1])
    """
    
    # Votre labyrinthe à compléter
    #------------------------------
    
    # le graphe correspondant au labyrinthe
    G=Graphe()

    i=0
    while i<N//2:
        for j in range(i+1,M-(i+1)):
            G.ajouter_arc((i,j),(i,j+1))
            G.ajouter_arc((N-i-1,j-1),(N-i-1,j))
        i+=1
    j=0
    while j<M//2:
        for i in range(j+1,N-(j+1)):
            G.ajouter_arc((i,j),(i+1,j))
            G.ajouter_arc((i-1,M-j-1),(i,M-j-1))
        j+=1
    i,j=1,0
    while i <N//2 and j<M//2:
        G.ajouter_arc((i,j),(i,j+1))
        G.ajouter_arc((N-i-1,M-j-1),(N-i-1,M-j-2))
        G.ajouter_arc((i,j+1),(i,j+2))
        G.ajouter_arc((N-i-1,M-j-2),(N-i-1,M-j-3))
        i+=1
        j+=1
    G.ajouter_arc(entree,(0,1))
    G.ajouter_arc((N-1,M-2),sortie)
    if N%2==0:
        G.ajouter_arc((N//2-1,M//2),(N//2,M//2))
        G.ajouter_arc((N//2-1,M//2-1),(N//2,M//2-1))
    else:
        G.ajouter_arc((N//2,M//2),(N//2,M//2-1))
        G.ajouter_arc((N//2,M//2),(N//2,M//2+1))

        
    # transformation du graphe en labyrinthe
    Labyrinthe=creer_labyrinthe(G)
    
    # solution du labyrinthe par un parcours de graphe
    chemin=chemin_graphe(G,entree,sortie)
    
    # affichage du labyrinthe créé
    laby=afficher_labyrinthe(Labyrinthe)
    laby.show()
    
    #affichage du labyrinthe avec sa solution
    laby_sol=afficher_labyrinthe_solution(Labyrinthe)   
    laby_sol.show()
    
    