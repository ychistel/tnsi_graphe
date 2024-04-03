class maillon:
    def __init__(self,x,m=None):
        self.elt=x
        self.suivant=m
        
class Pile:
    def __init__(self):
        self.taille=0
        self.sommet=None
        
    def empiler(self,x):
        m = self.sommet
        sommet=maillon(x,m)
        self.sommet=sommet
        self.taille +=1
        
    def peek(self):
        if self.taille>0:
            return self.sommet.elt
        
    def depiler(self):
        if self.taille > 0:
            sommet=self.sommet
            self.sommet = sommet.suivant
            self.taille -= 1
            return sommet.elt
     
    def est_vide(self):
        return self.taille == 0
    
    def __repr__(self):
        contenu = ''
        sommet=self.sommet
        while sommet != None:
            contenu = '|' + str(sommet.elt)+contenu
            sommet=sommet.suivant
        return contenu

def creer_pile():
    return Pile()

if __name__=='__main__':
    P=creer_pile()
    print(P.est_vide())
    P.empiler(3)
    P.empiler(7)
    P.afficher()
    P.empiler(9)
    P.afficher()
    print(P.est_vide())
    print(P.taille)
    tete=P.peek()
    print("tete:",tete)
    P.afficher()
    while not P.est_vide():
        P.depiler()
    P.afficher()