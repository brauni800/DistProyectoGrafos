import matplotlib.pyplot as plt
import networkx as nx

class Depth():
    #Se genera el Grafo de profundidad
    def generateDepthGraph(self, nodes):
        G = nx.circulant_graph(nodes, [1]) #pendiente por modificar
        return G

    #Save graph G as S, where S is a string
    def saveGraph(self, G, S):
        nx.write_gml(G, S)


    def drawGraph(self, G):
        nx.draw(G)
        plt.show()

    def run(self, nodes):
        G = self.generateDepthGraph(nodes)
        str1 = "graphDepth.gml"
        self.saveGraph(G, str1)
        self.drawGraph(G)
