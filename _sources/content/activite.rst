Représentation des graphes
===========================

Introduction
------------

Un graphe ``G=(S,A)`` est un ensemble de **sommets** ``S`` reliés entre eux par un ensemble d\'**arcs** ou d\'**arêtes** ``A``.

La figure suivante représente un graphe ``G``:

..  figure:: ../img/graphe_1.svg
    :align: center

#.  Quels sont les sommets de ce graphe ? Quels sont les arcs ?
#.  On dit que 2 sommets sont adjacents s'ils sont reliés par un arc.

    a.  Donner les sommets adjacents au sommet ``A`` de ce graphe.
    b.  Donner les sommets adjacents du sommet ``E`` de ce graphe.

Matrice et liste d'adjacence
-----------------------------

Il existe des représentations d'un graphe sous forme de **matrice** d'adjacence ou de **liste** d'adjacence.

#.  La matrice d'adjacence se présente comme un tableau ou chaque colonne et chaque ligne représente un sommet du graphe dans l'ordre alphabétique. A l'intersection des lignes et colonnes on place le nombre 1 si les sommets sont adjacents et 0 si non.  

    Donner la matrice d'adjacence du graphe ``G``. 

#.  La liste d'adjacence d'un graphe associe à chaque sommet du graphe les sommets adjacents. Donner la liste d'adjacence du graphe ``G``.

Implémentation en Python
------------------------

#.  La matrice d'adjacence est implémentée par une liste en 2 dimensions. C'est donc une liste des listes représentant les lignes de la matrice d'adjacence. Le premier sommet du graphe est représenté par l'indice 0, le second par l'indice 1, et ainsi de suite.

    La variable ``M`` implémente le graphe ``G`` Donner le contenu de la variable ``M``.

#.  La liste d'adjacence est implémentée par un dictionnaire. Les clés du dictionnaires représentent les sommets du graphe et les valeurs sont des listes contenant les sommets adjacents.

    La variable ``L`` implémente le graphe ``G``. Donner le contenu de la variable ``L``.
