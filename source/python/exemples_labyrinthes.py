# Liste des arcs du graphe
arcs=[
    ((0,0),(0,1)),((0,1),(0,2)),\
    ((0,2),(1,2)),\
    ((1,2),(1,1)),((1,1),(1,0)),((0,3),(1,3)),\
    ((1,0),(2,0)),((1,2),(2,2)),((1,3),(2,3)),\
    ((2,0),(2,1)),((2,1),(2,2)),((2,2),(2,3))
    ]

arcs=[
    ((0,0),(1,0)),((1,0),(2,0)),\
    ((2,0),(2,1)),\
    ((2,1),(1,1)),((1,1),(0,1)),\
    ((0,1),(0,2)),\
    ((0,2),(1,2)),((1,2),(2,2)),\
    ((2,2),(2,3)),\
    ((2,3),(1,3)),((1,3),(0,3))
    ]

N=5
M=8
arcs=[]
for j in range(M):
    for i in range(N-1):
        arcs.append(((i,j),(i+1,j)))
    if j%2==0 and j<M-1:
        arcs.append(((N-1,j),(N-1,j+1)))
    elif j%2==1 and j<M-1:
        arcs.append(((0,j),(0,j+1)))
print(arcs)

N=5
M=8
arcs=[
    ((0,0),(0,1)),((0,1),(0,2)),((0,2),(0,3)),\
    ((0,3),(1,3)),((1,3),(2,3)),\
    ((2,3),(2,2)),((2,2),(2,1)),\
    ((1,2),(1,1)),((1,1),(1,0)),\
    ((1,0),(2,0)),((2,0),(3,0)),\
    ((3,0),(3,1)),((3,1),(3,2)),((3,2),(3,3)),\
    ((1,1),(2,1)),((1,2),(2,2))
    ]


"""
Labyrinthe en spirale de forme carrée
N=M
"""
N,M=10,10
entree=(0,1)
sortie=(N-1,M-1)
arcs=[]
i=0
while i<N//2:
    for j in range(i+1,M-(i+1)):
        arcs.append(((i,j),(i,j+1)))
        arcs.append(((N-i-1,j-1),(N-i-1,j)))
    i+=1
j=0
while j<M//2:
    for i in range(j+1,N-(j+1)):
        arcs.append(((i,j),(i+1,j)))
        arcs.append(((i-1,M-j-1),(i,M-j-1)))
    j+=1
i,j=1,0
while i <N//2 and j<M//2:
    arcs.append(((i,j),(i,j+1)))
    arcs.append(((N-i-1,M-j-1),(N-i-1,M-j-2)))
    arcs.append(((i,j+1),(i,j+2)))
    arcs.append(((N-i-1,M-j-2),(N-i-1,M-j-3)))
    i+=1
    j+=1
arcs.append((entree,(0,1)))
arcs.append(((N-1,M-2),sortie))
if N%2==0:
    arcs.append(((N//2-1,M//2),(N//2,M//2)))
    arcs.append(((N//2-1,M//2-1),(N//2,M//2-1)))
else:
    arcs.append(((N//2,M//2),(N//2,M//2-1)))
    arcs.append(((N//2,M//2),(N//2,M//2+1)))
