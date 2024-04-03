from graphviz import Graph,Digraph

class Graphe_mat:
    def __init__(self,n):
        self.valeur=[[0]*n for _ in range(n)]   

    def est_adjacent(self,i,j):
        assert (0<=i<len(self.valeur) and 0<=j<len(self.valeur)),"erreur indices sommets"
        return self.valeur[i][j]==1

    def ajouter_arc(self,i,j):
        assert (0<=i<len(self.valeur) and 0<=j<len(self.valeur)),"erreur indices sommets"
        self.valeur[i][j]=1

    def supprimer_arc(self,i,j):
        assert (0<=i<len(self.valeur) and 0<=j<len(self.valeur)),"erreur indices sommets"
        self.valeur[i][j]=0

class Graphe_dict:
    """un graphe comme un dictionnaire d'adjacence"""
    
    def __init__(self):
        self.valeur={}
        
    def ajouter_sommet(self,x):
        if x not in self.sommets():
            self.valeur[x]=set()

    def supprimer_sommet(self,x,oriente):
        if x in self.sommets():
            if not oriente:
                adj=self.voisins(x)
                for s in adj:
                    self.valeur[s].remove(x)
                self.valeur.pop(x)
            else:
                for s in self.sommets():
                    if x in self.valeur[s]:
                        self.valeur[s].remove(x)
                self.valeur.pop(x)

    def ajouter_arc(self,x,y):
        self.ajouter_sommet(x)
        self.ajouter_sommet(y)
        self.valeur[x].add(y)
        
    def supprimer_arc(self,x,y):
        if y in self.voisins(x):
            self.valeur[x].remove(y)
       
    def est_arc(self,x,y):
        if x in self.sommets() and y in self.sommets():
            return y in self.valeur[x]
        else:
            return False
    
    def sommets(self):
        return list(self.valeur.keys())
    
    def voisins(self,x):
        if x in self.sommets():
            return list(self.valeur[x])
        else:
            return []

class Graphe:
    """un graphe comme dictionnaire d'adjacence et matrice d'adjacence"""
    
    def __init__(self,n=0,oriente=False):
        self.dict=Graphe_dict()
        self.matrice=Graphe_mat(n)
        self.oriente=oriente
        self.arcs=[]
                
    def ajouter_sommet(self,s):
        if s not in self.sommets():
            self.dict.ajouter_sommet(s)
            i=self.dict.sommets().index(s)
            # inserer ligne de zeros dimension matrice
            self.matrice.valeur.insert(i,[0]*len(self.matrice.valeur))
            # inserer colonne de zéros dans chaque ligne)
            for k in range(len(self.matrice.valeur)):
                self.matrice.valeur[k].insert(i,0)
    
    def supprimer_sommet(self,s):
        if s in self.sommets():
            voisins=self.voisins(s)
            i=self.dict.sommets().index(s)
            # on supprime les sommets du dict
            self.dict.supprimer_sommet(s,self.oriente)
            # on suprimme la ligne de la matrice
            del self.matrice.valeur[i]
            # on supprime la colonne dans chaque ligne
            for k in range(len(self.matrice.valeur)):
                del self.matrice.valeur[k][i]
            # on supprime les arcs avec ce sommet
            for v in voisins:
                if (s,v) in self.arcs:
                    self.arcs.remove((s,v))
                elif (v,s) in self.arcs:
                    self.arcs.remove((v,s))
                   
    def ajouter_arc(self,s1,s2):
        self.ajouter_sommet(s1)
        self.ajouter_sommet(s2)
        if self.oriente:            
            self.dict.ajouter_arc(s1,s2)
            i=self.dict.sommets().index(s1)
            j=self.dict.sommets().index(s2)
            self.matrice.ajouter_arc(i,j)
            if (s1,s2) not in self.arcs:
                self.arcs.append((s1,s2))
        else:
            self.dict.ajouter_arc(s1,s2)
            self.dict.ajouter_arc(s2,s1)
            i=self.dict.sommets().index(s1)
            j=self.dict.sommets().index(s2)
            self.matrice.ajouter_arc(i,j)
            self.matrice.ajouter_arc(j,i)
            if (s1,s2) not in self.arcs and (s2,s1) not in self.arcs:
                self.arcs.append((s1,s2))
        
    def supprimer_arc(self,s1,s2):
        if self.est_arc(s1,s2):
            if self.oriente:
                self.dict.supprimer_arc(s1,s2)
                i=self.dict.sommets().index(s1)
                j=self.dict.sommets().index(s2)
                self.matrice.supprimer_arc(i,j)
                if (s1,s2) in self.arcs:
                    self.arcs.remove((s1,s2))
            else:
                self.dict.supprimer_arc(s1,s2)
                self.dict.supprimer_arc(s2,s1)
                i=self.dict.sommets().index(s1)
                j=self.dict.sommets().index(s2)
                self.matrice.supprimer_arc(i,j)
                self.matrice.supprimer_arc(j,i)
                if (s1,s2) in self.arcs:
                    self.arcs.remove((s1,s2))
                if (s2,s1) in self.arcs:
                    self.arcs.remove((s2,s1))
                
            
    def est_arc(self,s1,s2):
        return self.dict.est_arc(s1,s2)
    
    def sommets(self):
        return list(self.dict.sommets())
    
    def voisins(self,s):
        return self.dict.voisins(s)
    
    def afficher(self,format='svg'):
        if self.oriente:
            dot=Digraph()
        else:
            dot=Graph(format=format)
        for s in self.sommets():
            dot.node(str(s))
        for arc in self.arcs:
            dot.edge(str(arc[0]),str(arc[1]))
        return dot

def dict_to_graphe(d,oriente=False):
    # On liste les sommets du graphe
    g=Graphe(oriente=oriente)
    # On parcourt les sommets du graphe
    for s in d:
        # indice de ligne du sommet S
        for v in d[s]:
            g.ajouter_arc(s,v)
    return g

def matrice_to_graphe(m,oriente=False):
    # On crée l'objet g de type Graphe
    g=Graphe(oriente=oriente)
    # On récupère le code ascii (en décimal) de la lettre A
    rg=ord('A')
    # On parcourt chaque ligne de la matrice
    for i in range(len(m)):
        # On parcourt chaque colonne d'une ligne de matrice
        if g.oriente:
            for j in range(len(m)):
                # si le coeffient vaut 1, les sommets sont adjacents,
                if m[i][j]==1:
                    # on ajoute un arc entre les sommets i et j à l'objet Graphe_dict
                    g.ajouter_arc(chr(rg+i),chr(rg+j))
        else:
            for j in range(i,len(m)):
                # si le coeffient vaut 1, les sommets sont adjacents,
                if m[i][j]==1:
                    # on ajoute un arc entre les sommets i et j à l'objet Graphe_dict
                    g.ajouter_arc(chr(rg+i),chr(rg+j))
    return g

def matrice_to_graphe2(m,oriente=False):
    # On crée l'objet g de type Graphe
    g=Graphe(oriente=oriente)
    # On parcourt chaque ligne de la matrice
    for i in range(len(m)):
        # On parcourt chaque colonne d'une ligne de matrice
        if g.oriente:
            for j in range(len(m)):
                # si le coeffient vaut 1, les sommets sont adjacents,
                if m[i][j]==1:
                    # on ajoute un arc entre les sommets i et j à l'objet Graphe_dict
                    g.ajouter_arc((i,j))
        else:
            for j in range(i,len(m)):
                # si le coeffient vaut 1, les sommets sont adjacents,
                if m[i][j]==1:
                    # on ajoute un arc entre les sommets i et j à l'objet Graphe_dict
                    g.ajouter_arc((i,j))
    return g

if __name__=='__main__':
    G=Graphe()
    G.ajouter_sommet('A')
    G.ajouter_arc('A','B')
    G.ajouter_arc('C','D')
    G.ajouter_arc('A','E')
    d=G.afficher()
    print(d)
    G.supprimer_arc('A','E')
    d=G.afficher()
    print(d)
    d.view()

    H={'A':{'B','C'},\
    'B':{'A','C'},\
    'C':{'A','B','D','E'},\
    'D':{'C','E'},\
    'E':{'C','D'}}
    H=dict_to_graphe(H)
    print(H.dict.valeur)
    d=H.afficher()
    d.view()
    M=[[0,1,1,0,0],[1,0,1,0,0],[1,1,0,1,1],[0,0,1,0,1],[0,0,1,1,0]]
    M=matrice_to_graphe(M)
    print(M.matrice.valeur)
    print(M.dict.valeur)
    d=M.afficher()
    d.view()
    
