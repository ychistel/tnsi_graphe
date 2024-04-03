from graphviz import Graph,Digraph


class Graphe:
    
    def __init__(self,oriente=False):
        self.liste = {}
        self.oriente=oriente
                
    def ajouter_sommet(self,s):
        if s not in self.liste.keys():
            self.liste[s] = []
    
    def supprimer_sommet(self,s):
        """
        La suppression d'un sommet se fait en 2 temps:
        - la clé associée au sommet
        - toutes les valeurs comme sommet adjacent d'un autre sommet.
        """
        if s in self.liste.keys():
            for sommet in self.liste[s]:
                self.liste[s].remove(sommet)
            del self.liste[s]
            
                   
    def ajouter_adjacent(self,s1,s2):
        """
        Si le graphe est orienté, alors l'arc va de s1 à s2.
        Cela implique que s2 est adjacent à s1 et pas le contraire
        """
        self.ajouter_sommet(s1)
        self.ajouter_sommet(s2)
        if self.oriente:            
            self.liste[s1].append(s2)
        else:
            self.liste[s1].append(s2)
            self.liste[s2].append(s1)
        
    def supprimer_adjacent(self,s1,s2):    
        if self.oriente:
            self.liste[s1].remove(s2)
        else:
            self.liste[s1].remove(s2)
            self.liste[s2].remove(s1)

    def arcs(self):
        arcs_graphe = []
        for s1 in self.liste.keys():
            for s2 in self.liste[s1]:
                if self.oriente:
                    if (s1,s2) not in arcs_graphe:
                        arcs_graphe.append((s1,s2))
                else:
                    if (s1,s2) not in arcs_graphe and (s2,s1) not in arcs_graphe:
                        arcs_graphe.append((s1,s2))
        return arcs_graphe
            
            
    def matrice(self):
        m = [[0]*len(self.liste) for i in range(len(self.liste))]
        sommets = list(self.liste.keys())
        for s in sommets:
            i = sommets.index(s)
            for s_adj in self.liste[s]:
                j = sommets.index(s_adj)
                m[i][j] = 1
        return m
    
    def afficher(self,format='svg'):
        if self.oriente:
            dot=Digraph()
        else:
            dot=Graph(format=format)
        # on crée les noeuds pour chaque sommet
        for s in self.liste.keys():
            dot.node(str(s))
        # on crée les arcs entre chaque sommet
        arcs = self.arcs()
        for arc in arcs:
            dot.edge(str(arc[0]),str(arc[1]))
        return dot

if __name__=='__main__':
    G=Graphe()
    G.ajouter_sommet('A')
    G.ajouter_adjacent('A','B')
    G.ajouter_adjacent('C','D')
    G.ajouter_adjacent('A','E')
    d=G.afficher()
    print(d)
    #d.view()

    H={'A':['B','C'],\
    'B':['C'],\
    'C':['A','D','E'],\
    'D':['E'],\
    'E':['A','B']}
    G=Graphe(oriente=True)
    G.liste = H
    M = G.matrice()
    print(M)
    d = G.afficher()
    d.view()
    
    

