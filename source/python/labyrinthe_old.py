import matplotlib
import matplotlib.pyplot as plt
from random import shuffle # permet le mélange d'une liste

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

def __interdire__(pos): # interdit la visite d'une position
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
    plt.imshow(Labyrinthe,interpolation='nearest',cmap=matplotlib.cm.gray)
    plt.xticks([])
    plt.yticks([])
    plt.show()



if __name__=='__main__':
    from graphe import Graphe, matrice_to_graphe2
    from pile import Pile,creer_pile
    
    N,M=10,10 # dimension longueur et largeur
    nbreVisites = 0 # compteur de cases visitées
    # tableau NxN des positions non visitées
    T=[[True]*M for _ in range(N)]

    entree = (0,0) # position de l'entrée
    sortie = (N-1,M-1) # position de la sortie
    visites=__parcours__()
    k=0
    arcs=[]
    while k < len(visites)-1:
        arcs.append((visites[k],visites[k+1]))
        k+=1
    G=Graphe()
    for arc in arcs:
        G.ajouter_arc(arc[0],arc[1])
    Labyrinthe=creer_labyrinthe(G)
    afficher_labyrinthe(Labyrinthe)