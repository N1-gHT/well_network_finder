from networkx import *
import matplotlib.pyplot as plt
import copy
import math
import ast



def transfo_fichier(A):
# Ouvrez le fichier en mode lecture
    with open(A, 'r') as f:
        lignes = f.readlines()
# Stockez les coordonnées de chaque point dans un dictionnaire
    points = {}
    for ligne in lignes:
        E, coor = ligne.split(' ')
        coor = ast.literal_eval(coor)  # coor devient un tuple
        E = int(E)  # passer E en int
        points[E] = coor
# Ouvrez le fichier de sortie en mode écriture
    with open("Sortie.txt", 'w') as g:
   # Parcourez les points
        for A in points:
       # Écrivez le numéro du point A dans le fichier
            g.write(str(A).strip(" "))
            g.write(" ")
       # Parcourez les autres points
            for B in points:
                if B == A:
                    continue  # Ignorez le point A lui-même
           # Calculez la distance entre A et B
# Calculez la distance entre A et B
                distance = math.sqrt((points[A][0] - points[B][0])**2 + (points[A][1] - points[B][1])**2)
           # Si la distance est inférieure ou égale à 12, écrivez le numéro du point B dans le fichier
                if distance <= 12 or distance == 0:
                    g.write(str(B).strip(" "))
                    g.write(" ")
       # Ajoutez un retour à la ligne pour séparer les lignes
            g.write("\n")

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

def affichage(A):
    pos = circular_layout(A)
    draw_networkx_labels(A, pos)
    draw_networkx_edges(A, pos, node_size=500)
    draw_networkx_nodes(A, pos, node_size=500)
    draw_networkx_nodes(A, pos,nodelist=[list(A.nodes())[0]], node_size=500,node_color='red')
    plt.show()

def affichage_finale(J,arbre_final,arbre_possible):
    print (f"La valeur moyenne dépensé pour le graphe n°1 est {J}")
    affichage(arbre_final)
    if is_empty(arbre_possible) == False: 
        affichage(arbre_possible)
    else:
        print("Il n'y a pas de puit alternatif de valeur équivalente")

#Initialisation
transfo_fichier("input.txt")

A = read_adjlist("Sortie.txt", create_using = Graph())

Arbre = Graph()
J = 1
E=0
n= A.number_of_nodes()
arbre_final = ()
arbre_possible = Graph()
arbre_b = Graph()

while E !=n :
    parcours_largeurs(E)
    E+=1
    K = global_efficiency(Arbre)
    if K < J:
        arbre_final = copy.deepcopy(Arbre)
        J = K
    elif K == J:
        arbre_possible = copy.deepcopy(Arbre)



affichage_finale(J,arbre_final,arbre_possible)
