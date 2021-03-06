"""
Displays a NetworkX lollipop graph to screen using a CircosPlot.
"""

from nxviz.plots import CircosPlot
import networkx as nx
import matplotlib.pyplot as plt

G = nx.lollipop_graph(m=10, n=4)
c = CircosPlot(G.nodes(), G.edges(), plot_radius=5)
c.draw()
plt.show()
