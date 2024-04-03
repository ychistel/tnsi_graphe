class Graphe_dict:
    def __init__(self):
        self.adj={}

    def ajouter_sommet(self,s):
        if s not in self.adj:
            self.adj[s]=set()
            
    def ajouter_arc(self,s1,s2):
        self.ajouter_sommet(s1)
        self.ajouter_sommet(s2)
        self.adj[s1].add(s2)
        self.adj[s2].add(s1)

    def arc(self,s1,s2):
        if s1 in self.adj[s2] or s2 in self.adj[s1]:
            return True
        else:
            return False
        
    def sommets(self):
        return list(self.adj.keys())

    def voisins(self,s):
        return list(self.adj[s])
        
    
if __name__ == '__main__':
    G=Graphe_dict()
    G.adj={'A':{'B','C'},\
   'B':{'A','C'},\
   'C':{'A','B','D','E'},\
   'D':{'C','E'},\
   'E':{'C','D'}}
    print(G.adj)
    H=Graphe_dict()
    H.ajouter_arc('A','B')
    H.ajouter_arc('A','C')
    H.ajouter_arc('B','C')
    H.ajouter_arc('C','D')
    H.ajouter_arc('C','E')
    H.ajouter_arc('D','E')
    print(H.adj)