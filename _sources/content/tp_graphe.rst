TP : implémenter un graphe en Python (POO)
============================================

On donne la classe **Graphe** écrite en Python dont l’interface est la suivante:

Les attributs:
~~~~~~~~~~~~~~

-  **dict** qui est un objet **Graphe_dict**.

   Un objet **Graphe_dict** a pour attribut **valeur** qui contient le
   dictionnaire d’adjacence du graphe;

-  **matrice** qui est un objet **Graphe_mat**.

   Un objet **Graphe_mat** a pour attribut **valeur** qui contient la
   matrice d’adjacence du graphe;

-  **oriente** qui est booléen indiquant si le graphe est orienté; par
   défaut le graphe est non orienté.

-  **arcs** qui est une liste contenant les arcs du graphe.

Les méthodes:
~~~~~~~~~~~~~

-  **ajouter_sommet** qui ajoute un sommet au graphe;

-  **ajouter_arc** qui ajoute un arc au graphe entre deux sommets (2
   arcs si non orienté), le sommet est créé s’il n’existe pas;

-  **supprimer_sommet** qui supprime un sommet au graphe, les arcs
   associés sont supprimés;

-  **supprimer_arc** qui supprime un arc entre deux sommets;

-  **est_arc** qui renvoie un booléen d’existence d’arc entre deux
   sommets;

-  **sommets** qui renvoie la liste des sommets du graphe;

-  **voisins** qui renvoie la liste des sommets adjacents à un sommet;

-  **afficher** qui affiche une représentation du graphe.

Comment utiliser cette classe
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

::

   from graphe import Graphe

Pour créer un objet :math:`G` graphe non orienté, on doit appeler la
classe Graphe. Si le graphe est orienté, on donne en argument la valeur
**oriente=True**.

::

   G=Graphe()

L’affichage des valeurs du dictionnaire d’adjacence et de la matrice
d’adjacence se fait par les appels suivants:

::

   print(G.dict.valeur) # dictionnaire d'adjacence
   print(G.matrice.valeur) # matrice d'adjacence

L’ajout de sommets et d’arcs se fait par les méthodes de l’objet Graphe
données ci-dessus:

::

   G.ajouter_sommet('A')
   G.ajouter_arc('A','B')

Pour représenter le graphe, on utilise la méthode afficher

::

   d=G.afficher()
   d.view()

Travail à chercher
~~~~~~~~~~~~~~~~~~

#. Récupérer sur l’ENT, le fichier Python **graphe.py** contenant la
   classe Graphe et importer là dans un nouveau fichier python.

#. Créer l’objet graphe :math:`G1` représenté dans l’exercice 1 en
   ajoutant les sommets et les arcs qui le compose.

   #. Afficher le dictionnaire d’adjacence du graphe :math:`G1`.

   #. Afficher la matrice d’adjacence du graphe :math:`G1`.

   #. Afficher une vue du graphe :math:`G1`.

#. La création d’un objet graphe se fait par l’ajout des arcs du graphe.

   #. Soit L=[(’A’,’B’),(’A’,’C’),(’B’,’D’),(’C’,’D’)] la liste des arcs
      d’un graphe. En donner son dictionnaire et sa matrice d’adjacence.

   #. Écrire une fonction **arcs_en_graphe** qui a pour paramètre une
      liste d’arcs d’un graphe et renvoie un objet graphe associé à la
      liste des arcs passés en argument. Chaque arc sera un tuple
      composé des deux sommets reliés par l’arc.

   #. Vérifier votre fonction en créant le graphe :math:`G2` de
      l’exercice 2 à partir de la liste des arcs du graphe.

#. Le parcours d’un graphe consiste à prendre un chemin en suivant les
   arcs du graphe. Pour déterminer l’existence d’une chaine eulérienne,
   c’est à dire savoir si on peut parcourir un graphe en prenant chaque
   arc une et une seule fois, il est nécessaire de déterminer les degrés
   de chaque sommet.

   #. Écrire une fonction **degre_sommet** qui a pour paramètre un
      graphe et renvoie un dictionnaire dontles clefs sont chaque sommet
      du graphe et les valeurs le degré du sommet associé.

   #. Écrire une fonction **chaine_eulerienne** qui a pour paramètre un
      graphe et renvoie un booléen déterminant s’il existe une chaine
      eulérienne dans le graphe.

   #. Écrire un script python qui répond aux questions de l’exercice 4.

#. Écrire une fonction qui crée un graphe à partir de son dictionnaire
   d’adjacence. Vérifier avec les données de l’exercice 2 ou un autre
   graphe.

#. Écrire une fonction qui crée un graphe à partir de sa matrice
   d’adjacence. Vérifier avec les données de l’exercice 3 ou un autre
   graphe.
