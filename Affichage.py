# Author : Alexandre L
# Creation : 01/2023
# This file is part of well_network_finder .
#
# well_network_finder is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
#any later version.
#
# well_network_finder is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with well_network_finder.  If not, see <https://www.gnu.org/licenses/>.

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
