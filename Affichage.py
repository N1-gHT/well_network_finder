from networkx import *
import matplotlib.pyplot as plt

def affichage(A):


    pos = circular_layout(A)

    draw_networkx_labels(A, pos)
    draw_networkx_edges(A, pos, arrowsize=20)
    draw_networkx_nodes(A, pos, node_size=500)

    N = A.number_of_nodes()
    M = A.number_of_edges()
    G= A.degree(A)


    plt.show()