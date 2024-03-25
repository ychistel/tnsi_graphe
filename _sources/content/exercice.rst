Exercice sur les graphes
========================

Exercice 1
----------

On donne ci-dessous un graphe ``G``:

.. figure:: ../img/graphe_4.svg
    :align: center

#.  Donner la liste d'adjacence du graphe ``G``.
#.  Donner la matrice d'adjacence du graphe ``G``.
#.  On oriente le graphe en respectant l'ordre alphabétique. Par exemple, le sommet ``A`` est relié au sommet ``B`` par un arc orienté de ``A`` vers ``B`` car A est avant B dans l'ordre alphabétique.

    a.  Redessiner le graphe orienté.
    b.  Redonner la liste d'adjacence et la matrice d'adjacence du graphe orienté si elles sont différentes de celles du graphe non orienté.

Exercice 2
-----------

On donne la liste d'adjacence d'un graphe ``G`` non orienté:

.. code-block:: python

    G = {
        'A' : ['B','C'],
        'B' : ['A','D','E'],
        'C' : ['A','E','F'],
        'D' : ['B','F'],
        'E' : ['B','C','F'],
        'F' : ['C','D','E']
    }

#.  Représenter schématiquement le graphe ``G``.
#.  Donner la matrice d'adjacence du graphe ``G``.

Exercice 3
-----------

On donne la matrice d'adjacence d'un graphe ``G`` non orienté:

.. container:: center

    :math:`M=\begin{pmatrix}
    0 & 1 & 1 & 0 & 0\\
    1 & 0 & 1 & 1 & 0\\
    1 & 1 & 0 & 1 & 1\\
    0 & 1 & 1 & 0 & 0\\
    0 & 0 & 1 & 0 & 1\\
    \end{pmatrix}`

#. Représenter schématiquement ce graphe ``G``.
#. Donner la liste d'adjacence du graphe ``G``.

Exercice 4
------------

Un groupe d'amis organise une randonnée dans les Alpes. On a représenté par le graphe ci-dessous les sommets ``A``, ``C``, ``D``, ``F``, ``T`` et ``N`` par lesquels ils peuvent choisir de passer. Une arête (arc) entre deux sommets coïncide avec l’existence d'un chemin de randonnée entre les deux sommets.

.. figure:: ../img/graphe_randonnee.png
    :align: center

#.  On appelle **degré** d'un sommet le nombre de sommets qui lui sont adjacents. Compléter le tableau avec les degrés de chaque sommet.

.. table::
    :class: bordure border-style-solid border-width-1

    +-----------------+---+---+---+---+---+---+
    |sommets          | A | C | D | F | T | N |
    +-----------------+---+---+---+---+---+---+
    |degré sommet     |   |   |   |   |   |   |
    +-----------------+---+---+---+---+---+---+

#.  On dit qu’un graphe est **connexe** lorsque 2 sommets quelconques sont reliés par un chemin. Le graphe ``G`` est-il connexe ?

#.  Le mathématicien **Euler** a montré qu'il existe un chemin reliant tous les sommets en passant une et une seule fois par toutes les arêtes du graphe lorsque le graphe contient exactement 2 sommets de degré impair. Un tel chemin est appelé **chaine eulérienne**.

    Est-il envisageable de trouver une chaine eulérienne de randonnée passant par tous les arcs une et une seule fois? Donner un tel chemin s'il existe.




