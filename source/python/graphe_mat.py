class Graphe_mat:
    def __init__(self,n):
        self.mat=[[0]*n for _ in range(n)]

    def est_adjacent(self,i,j):
        assert (0<=i<len(self.mat) and 0<=j<len(self.mat)),"erreur indices sommets"
        return self.mat[i][j]==1

    def ajouter_arc(self,i,j):
        assert (0<=i<len(self.mat) and 0<=j<len(self.mat)),"erreur indices sommets"
        self.mat[i][j]=1
        self.mat[j][i]=1

    def supprimer_arc(self,i,j):
        assert (0<=i<len(self.mat) and 0<=j<len(self.mat)),"erreur indices sommets"
        self.mat[i][j]=0
        self.mat[j][i]=0
        
if __name__=='__main__':
    M=Graphe_mat(5)
    M.ajouter_arc(0,1)
    M.ajouter_arc(0,2)
    M.ajouter_arc(1,0)
    M.ajouter_arc(1,2)
    M.ajouter_arc(2,0)
    M.ajouter_arc(2,1)
    M.ajouter_arc(2,3)
    M.ajouter_arc(2,4)
    M.ajouter_arc(3,2)
    M.ajouter_arc(3,4)
    M.ajouter_arc(4,2)
    M.ajouter_arc(4,3)
