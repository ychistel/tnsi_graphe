from graphviz import Graph,Digraph


class Graphe:
    
    def __init__(self,oriente=False):
        """
        Attributs:
            adjacent : dictionnaire des sommets adjacents à chaque sommet
            oriente : booleen qui indique si le graphe est orienté
        """
        self.adjacent = {}
        self.oriente=oriente
                
    def ajouter_sommet(self,s):
        if s not in self.adjacent.keys():
            self.adjacent[s] = []
    
    def supprimer_sommet(self,s):
        """
        La suppression d'un sommet se fait en 2 temps:
        - la clé associée au sommet
        - toutes les valeurs comme sommet adjacent d'un autre sommet.
        """
        if s in self.adjacent.keys():
            for sommet in self.adjacent[s]:
                self.adjacent[s].remove(sommet)
            del self.adjacent[s]
            
    def ajouter_adjacent(self,s1,s2):
        """
        Si le graphe est orienté, alors l'arc va de s1 à s2.
        Cela implique que s2 est adjacent à s1 et pas le contraire
        """
        self.ajouter_sommet(s1)
        self.ajouter_sommet(s2)
        if self.oriente:            
            self.adjacent[s1].append(s2)
        else:
            self.adjacent[s1].append(s2)
            self.adjacent[s2].append(s1)
        
    def supprimer_adjacent(self,s1,s2):    
        if self.oriente:
            self.adjacent[s1].remove(s2)
        else:
            self.adjacent[s1].remove(s2)
            self.adjacent[s2].remove(s1)

    def arcs(self):
        arcs_graphe = []
        for s1 in self.adjacent.keys():
            for s2 in self.adjacent[s1]:
                if self.oriente:
                    if (s1,s2) not in arcs_graphe:
                        arcs_graphe.append((s1,s2))
                else:
                    if (s1,s2) not in arcs_graphe and (s2,s1) not in arcs_graphe:
                        arcs_graphe.append((s1,s2))
        return arcs_graphe
            
    def liste_adjacent(self):
        sommets = list(self.adjacent.keys())
        adj = [[] for i in range(len(sommets))]
        for s in sommets:
            i = sommets.index(s)
            for s_adj in self.adjacent[s]:
                j = sommets.index(s_adj)
                adj[i].append(j)
        return adj

    def matrice(self):
        m = [[0]*len(self.adjacent) for i in range(len(self.adjacent))]
        sommets = list(self.adjacent.keys())
        for s in sommets:
            i = sommets.index(s)
            for s_adj in self.adjacent[s]:
                j = sommets.index(s_adj)
                m[i][j] = 1
        return m
    
def afficher(graphe,dico_couleur={}):
    couleurs = ['red','green','blue','orange','purple','black']
    dot=Graph(format='png')
    # on crée les sommets du graphe
    for s in graphe.adjacent.keys():
        if dico_couleur != {}:
            dot.node(s,color=couleurs[dico_couleur[s]])
        else:
            dot.node(s,color='black')
    # on crée la liste des arcs entre les sommets
    arcs = []
    for s in graphe.adjacent.keys():
        for s_adj in graphe.adjacent[s]:
            if (s,s_adj) not in arcs and (s_adj,s) not in arcs:
                arcs.append((s,s_adj))
    # on ajoute les arcs au graphe
    for arc in arcs:
        s1,s2 = arc
        dot.edge(s1,s2)
    return dot

"""
    def afficher(self,format='svg'):
        if self.oriente:
            dot=Digraph()
        else:
            dot=Graph(format=format)
        # on crée les noeuds pour chaque sommet
        for s in self.adjacent.keys():
            dot.node(str(s))
        # on crée les arcs entre chaque sommet
        arcs = self.arcs()
        for arc in arcs:
            dot.edge(str(arc[0]),str(arc[1]))
        return dot
"""

if __name__=='__main__':
    G=Graphe()
    G.ajouter_sommet('A')
    G.ajouter_adjacent('A','B')
    G.ajouter_adjacent('C','D')
    G.ajouter_adjacent('A','E')
    d=G.afficher()
    print(d)
    adj = G.liste_adjacent()
    print(adj)

    H={'A':['B','C'],\
    'B':['C'],\
    'C':['A','D','E'],\
    'D':['E'],\
    'E':['A','B']}
    G=Graphe(oriente=True)
    G.adjacent = H
    M = G.matrice()
    print(M)
    adj = G.liste_adjacent()
    print(adj)
    d = G.afficher()
    d.view()
    
    

