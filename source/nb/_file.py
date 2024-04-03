"""
Module : implémentation d'une File par des listes chainées en POO
Objets
- Cellule : permet de construire chaque élément de la File
- File : permet de construire une liste chainée créant une file.
Fonctions
- creer_file : pour construire une file vide.
"""

class Cellule:
    """
    type : objet
    attributs : 
    - valeur : contient la valeur passée en argument, None par défaut si pas de valeur
    - suivant : None par défaut ou un objet Cellule pour construire une liste chainée.
    méthodes:
    - constructeur : __init__
    - est_vide : renvoie un booléen (False, True) si la cellule est vide ou non
    - __repr__ : affiche la Cellule sous la forme (valeur, suivant)
    """
    def __init__(self,v=None,s=None):
        self.valeur=v
        self.suivant=s
        
    def est_vide(self):
        return self.suivant==None
    
    def __repr__(self):
        if self.valeur is None:
            return str(self.valeur)
        else:
            return "("+str(self.valeur)+","+str(self.suivant)+")"

class File:
    """
    type : objet de type liste chainée
    attributs :
    - queue : objet Cellule ou None si vide
    méthodes:
    - constructeur __init__
    - enfiler : ajoute un objet Cellule à l'objet File
    - defiler : renvoie la tête de la file en le supprimant
    - est_vide : renvoie un booléen (True, False) indiquant si la File est vide
    - tete : renvoie la tete de file sans l'enlever
    - __len__ : renvoie la longueur de la File
    - __repr__ pour afficher le contenu de la file (méthode non définie dans l'interface)
    """
    
    def __init__(self):
        self.queue=Cellule()
        
    def est_vide(self):
        return self.queue.valeur==None
    
    def enfiler(self,v):
        self.queue=Cellule(v,self.queue)
        
    def defiler(self):
        if not self.est_vide():
            cell=None
            # on crée une cellule contenant les éléments de la file
            # on vide la file ! la dernière cellule créée contient les éléments de la file à l'envers
            while not self.est_vide():
                cell=Cellule(self.queue.valeur,cell)
                self.queue=self.queue.suivant
            # le premier élément de la cellule est le dernier élément de la file (tete de file)
            # on récupère la tete de la file 
            tete=cell.valeur
            while not cell.est_vide():
                cell=cell.suivant
                self.enfiler(cell.valeur)
            return tete
        
    def tete(self):
        if not self.est_vide():
            cell=self.queue
            while not cell.suivant.est_vide():
                cell=cell.suivant
                # le premier élément de la cellule est le dernier élément de la file (tete de file)
                # on récupère la tete de la file 
            tete=cell.valeur
            return tete
        
    def __len__(self):
        taille = 0
        cell=self.queue
        while not cell.est_vide():
            cell=cell.suivant
            taille += 1
            # le premier élément de la cellule est le dernier élément de la file (tete de file)
            # on récupère la tete de la file 
        return taille
        
                        
    def __repr__(self):
        contenu = '...'
        queue=self.queue
        while queue != None:
            if queue.valeur != None:
                contenu = str(queue.valeur)+ ' < ' + contenu
            queue=queue.suivant
        return contenu

def creer_file():
    return File()

if __name__=='__main__':
    F=creer_file()
    print("file vide:",F.est_vide())
    F.enfiler(3)
    F.enfiler(7)
    F.enfiler(9)
    F.enfiler(11)
    print(F)
    print("longueur de la file:",len(F))
    print("tete:",F.tete())
    print("on defile")
    F.defiler()
    print(F)
    print("tete:",F.tete())
    print("file vide:",F.est_vide())
    print("longueur de la file:",len(F))
    print("on defile")
    F.defiler()
    print(F)
    print("tete:",F.tete())
    print("file vide:",F.est_vide())
    print("longueur de la file:",len(F))
    print("on defile tout")
    while not F.est_vide():
        F.defiler()
    print(F)
    print("tete:",F.tete())
    print("file vide:",F.est_vide())
    print("longueur de la file:",len(F))
