Exercice en Python
==================

.. note::

    Les exercices suivants proposent une implémentation en Python d'une interface de Graphe. Cette implémentation et l'interface proposée ne sont que des cas possibles parmi d'autres.

    Il faut envisager des interfaces et des implémentations différentes.

Exercice 1
-----------

On définit un graphe par sa matrice d'ajacence. Les primitives suivantes définissent l'interface de ce graphe:

    -   Le constructeur ``creer_matrice`` qui a pour paramètre ``n`` de type entier correspondant à la dimension de la matrice, c'est à dire au nombre de sommets du graphe. La fonction renvoie une liste de dimension ``n`` contenant ``n`` listes de dimension ``n`` initialisée à 0.
    -   La fonction ``est_adjacent`` qui a pour paramètres ``i`` et ``j`` de type entiers associés à 2 sommets du graphe. La fonction renvoie un booléen de valeur ``True`` si les sommets sont adjacents et valeur ``False`` s'ils ne le sont pas.
    -   La fonction ``ajouter_arc`` qui a pour paramètres ``i`` et ``j`` de type entiers associés à 2 sommets du graphe. La fonction ajoute un arc entre les 2 sommets ce qui signifie que les sommets sont adjacents. La fonction ne renvoie rien.
    -   La fonction ``supprimer_arc`` qui a pour paramètres ``i`` et ``j`` de type entiers associés à 2 sommets du graphe. La fonction supprime un arc entre les 2 sommets ce qui signifie que les sommets ne sont pas adjacents. La fonction ne renvoie rien.

Un graphe ``G`` est donné ci-après nous permettre de tester nos fonctions.

.. figure:: ../img/graphe_4.svg
    :align: center

#.  Implémenter cette interface par des fonctions en Python. 
#.  Soit ``M`` la variable associée à la matrice d'adjacence du graphe ``G``.

    a.  Écrire une instruction qui crée la variable ``M`` contenant une matrice initialisée avec des valeurs nulles.
    b.  Écrire les instructions Python qui représente la matrice d'adjacence du graphe ``G``.
#.  Le module ``Graphviz`` (disponible sur Capytale) affiche des graphes définis par des objets de la classe ``Graph`` dont ``dot`` et ``edge`` sont des attributs. Le module doit être importé pour être utilisé.

    from graphviz import Graph

    La fonction ``afficher`` prend en paramètre une matrice d'adjacence d'un graphe non orienté et en donne une représentation sous forme d'image ``png``.

    .. code-block:: python

        def afficher(matrice):
            """
            Le module Graphviz est utilisé. Les sous-modules Digraph et Graphe
            sont importés.
            La fonction crée un graphe pour être affiché (image format 'png')
            Le graphe est non orienté !
            - on crée les sommets 0->A chr(65), 1->B chr(66), 2->C chr(67),etc.
            - on crée les arcs entre les sommets adjacents
            La fonction renvoie un objet 'dot' qui contient le graphe à afficher
            """
            dot=Graph(format='png')
            n = len(matrice)
            # on crée les sommets du graphe
            for i in range(n):
                dot.node(str(chr(65+i)))
            # on crée les arcs entre les sommets
            for i in range(n):
                for j in range(i,n):
                    if est_adjacent(matrice,i,j):
                        dot.edge(str(chr(65+i)),str(chr(65+j)))
            return dot

    On définit un graphe ``G`` de la façon suivante où ``M`` est la matrice d'adjacence:

    >>> G = afficher(M)
    >>> G.view()

    Ce qui donne une représentation comme la figure ci-dessous:
    
    .. figure:: ../img/graphe_ex_1.png
        :align: center

Exercice 2
----------

On définit un graphe par sa liste d'ajacence qui contient chaque sommet du graphe et pour chaque sommet, la liste des sommets qui lui sont adjacents. Les sommets sont de type string (chaine de caractère). Les primitives suivantes définissent l'interface de ce graphe:

    -   Le constructeur ``creer_liste`` qui n'a pas de paramètre et qui renvoie un dictionnaire vide.
    -   La fonction ``est_adjacent`` qui a pour paramètres ``s1`` et ``s2`` de type string associés à 2 sommets du graphe. La fonction renvoie un booléen de valeur ``True`` si les sommets sont adjacents et valeur ``False`` s'ils ne le sont pas.
    -   La fonction ``ajouter_sommet`` qui a pour paramètre ``s`` de type string associé à 1 sommet du graphe. La fonction ajoute un sommet au graphe et lui associe une liste vide pour les sommets adjacents. La fonction ne renvoie rien ou le dictionnaire représentant le graphe.
    -   La fonction ``ajouter_adjacent`` qui a pour paramètres ``s1`` et ``s2`` de type string associé à 2 sommets adjacents du graphe. La fonction ajoute les sommets adjacents au graphe. La fonction ne renvoie rien ou le dictionnaire représentant le graphe.

Un graphe ``G`` est donné ci-après nous permettre de tester nos fonctions.

.. figure:: ../img/graphe_4.svg
    :align: center

#.  Implémenter cette interface par des fonctions en Python. 
#.  Soit ``L`` la variable associée à la liste d'adjacence du graphe ``G``.

    a.  Écrire une instruction qui crée la variable ``L``.
    b.  Écrire les instructions Python qui représente la liste d'adjacence du graphe ``G``.

#.  Le module ``Graphviz`` (disponible sur Capytale) affiche des graphes définis par des objets de la classe ``Graph`` dont ``dot`` et ``edge`` sont des attributs. Le module doit être importé pour être utilisé.

    from graphviz import Graph

    La fonction ``afficher`` prend en paramètre une matrice d'adjacence d'un graphe non orienté et en donne une représentation sous forme d'image ``png``.

    .. code-block:: python

        def afficher(liste):
            """
            Le module Graphviz est utilisé. Les sous-modules Digraph et Graphe
            sont importés.
            La fonction crée un graphe pour être affiché (image format 'png')
            Le graphe est non orienté !
            - on crée les sommets du graphe
            - on crée les arcs entre les sommets adjacents
            La fonction renvoie un objet 'dot' qui contient le graphe à afficher
            """
            dot=Graph(format='png')
            # on crée les sommets du graphe
            for s in liste.keys():
                dot.node(s)
            # on crée la liste des arcs entre les sommets
            arcs = []
            for s in liste.keys():
                for s_adj in liste[s]:
                    if (s,s_adj) not in arcs and (s_adj,s) not in arcs:
                        arcs.append((s,s_adj))
            # on ajoute les arcs au graphe
            for arc in arcs:
                s1,s2 = arc
                dot.edge(s1,s2)
            return dot