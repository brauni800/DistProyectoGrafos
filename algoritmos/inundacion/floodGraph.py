import matplotlib.pyplot as plt
import networkx as nx

class Flood():
    #Se genera el Grafo de inundacion
    def generateFloodGraph(self, nodes):
        G = nx.random_tree(nodes, 1) #pendiente por modificar
        return G

    #Save graph G as S, where S is a string
    def saveGraph(self, G, S):
        nx.write_gml(G, S)


    def drawGraph(self, G):
        nx.draw(G)
        plt.show()

    def run(self, nodes):
        G = self.generateFloodGraph(nodes)
        str1 = "graphFlood.gml"
        self.saveGraph(G, str1)
        self.drawGraph(G)
