from networkx import *
import matplotlib.pyplot as plt
from Affichage import *
import copy


A = read_adjlist("E:\Cours_RT2\Prog_4\TP2\graphe1.txt", create_using = Graph())

#Traitement
def parcours_largeurs(E):
    set_node_attributes(A,"white", name ="color") #défini couleur des noeuds
    set_node_attributes(A,9999999999999999,name ="distance") #défini valeur à E
    A.add_node(E,color="Green",distance=0) # défini couleur de E et distance à E de E
    Liste = [list(A.nodes())[E]] #débute notre liste à

    while Liste:
        S = Liste.pop(0)

        for V in A.neighbors(S):
            if get_node_attributes(A,"color")[V]=="white":
                distance = get_node_attributes(A,"distance")[S]
                set_node_attributes(A,{V:(distance+1)}, name="distance")
                Liste.append(V)
                set_node_attributes(A, {V:"Green"},name="color")
                Arbre.add_edge(S,V)
            set_node_attributes(A, {S:"Red"},"color")
    return Arbre

def affichage_final(J,arbre_final,arbre_possible):
    print (J)
    affichage(arbre_final)
    affichage(arbre_possible)

#Initialisation

Arbre = Graph()
J = 1
E=0
n= A.number_of_nodes()
arbre_final = ()
arbre_possible = Graph()


while E !=n :
    parcours_largeurs(E)
    E+=1
    K = global_efficiency(Arbre)
    if K < J:
        arbre_final = copy.deepcopy(Arbre)
        J = K
    elif K == J:
        arbre_possible = copy.deepcopy(Arbre)



affichage_final(J,arbre_final,arbre_possible)