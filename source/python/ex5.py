from graphe import Graphe, matrice_to_graphe2
from pile import Pile,creer_pile
import matplotlib
import matplotlib.pyplot as plt
from random import shuffle # permet le mélange d'une liste

def arcs_en_graphe(L):
    G=Graphe()
    for arc in L:
        G.ajouter_arc(arc[0],arc[1])
    return G

def voisins(pos):
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

def interdire(pos): # interdit la visite d'une position
    global nbreVisites
    nbreVisites+=1
    i,j=pos # i = pos[0] et j = pos[1]
    T[i][j] = False
    
def positionNonVisitee(): # Encore une position à visiter ?
    return nbreVisites < N*M

def parcours():
    """
    On construit le parcourt du labyrinthe avec sa solution entre entrée et sortie
    dans un carré de NxM cases
    """
    position=entree
    filDariane = creer_pile()
    filDariane.empiler(position)
    visites=[position] # mémoire des positions visitées
    while positionNonVisitee():
        voisinage = voisins(position)
        if voisinage == []: # retour arrière
            filDariane.depiler()
            position=filDariane.peek()
            visites.append(position)
        else:
            position = voisinage[0] # avancement
            filDariane.empiler(position)
            visites.append(position)
            interdire(position)
    return visites

def labyrinthe(g):
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

def affiche_labyrinthe(labyrinthe):
    plt.imshow(Labyrinthe,interpolation='nearest',cmap=matplotlib.cm.gray)
    plt.xticks([])
    plt.yticks([])
    plt.show()

def parcours_profondeur(g,vus,s):
    p=creer_pile()
    p.empiler(s)
    while not p.est_vide():
        s=p.depiler()
        print(p,'->',s)
        if s in vus:
            continue
        vus.append(s)
        for v in g.voisins(s):
            p.empiler(v)
    return vus

if __name__=='__main__':
    N,M=14,16 # dimension longueur et largeur
    nbreVisites = 0 # compteur de cases visitées
    # tableau NxN des positions non visitées
    T=[[True]*M for _ in range(N)]

    entree = (0,0) # position de l'entrée
    sortie = (N-1,M-1) # position de la sortie
    """
    arcs=[((0,0),(0,1)),((0,1),(1,1)),((0,1),(0,2)),\
          ((1,1),(1,2)),((1,1),(2,1)),\
          ((1,2),(2,2)),((2,1),(2,0)),((2,0),(1,0))]
    G3=arcs_en_graphe(arcs)
    Labyrinthe=labyrinthe(G3)
    affiche_labyrinthe(Labyrinthe)
    """
    
    """
    arcs=[]
    for j in range(N):
        for i in range(M-1):
            arcs.append(((i,j),(i+1,j)))
        if j%2==0:
            arcs.append(((i+1,j),(i+1,j+1)))
        else:
            if j<N-1:
                arcs.append(((0,j),(0,j+1)))
    print(arcs)
    G2=arcs_en_graphe(arcs)
    Labyrinthe=labyrinthe(G2)
    affiche_labyrinthe(Labyrinthe)
    """
    
    """
    visites=parcours()
    print(visites)
    k=0
    arcs=[]
    while k < len(visites)-1:
        arcs.append((visites[k],visites[k+1]))
        k+=1
    """
    
    arcs=[((0,0),(0,1)),((0,1),(0,2)),((0,2),(1,2)),\
          ((1,1),(1,2)),((1,1),(1,0)),((1,2),(2,2)),\
          ((1,0),(2,0)),((2,1),(2,0)),((2,1),(2,2)),((2,2),(2,3)),\
          ((2,3),(1,3)),((0,3),(1,3))\
        ]
    
    """
    arcs=[((0,0),(0,1)),((0,1),(0,2)),((0,2),(0,3)),\
          ((0,0),(1,0)),((1,0),(2,0)),\
          ((1,0),(1,1)),((1,1),(1,2)),((1,2),(1,3)),\
          ((1,2),(2,2)),\
          ((2,2),(2,3)),((2,2),(2,1)),\
          ((0,3),(1,3))\
        ]
    """
    G=arcs_en_graphe(arcs)
    
    N,M=3,4
    entree = (0,0) # position de l'entrée
    sortie = (N-1,M-1) # position de la sortie
    print(G.sommets())
    G.afficher().view()
    Labyrinthe=labyrinthe(G)
    affiche_labyrinthe(Labyrinthe)