import matplotlib.pyplot as plt
import networkx as nx

class Ring():
    #Se genera el Grafo de anillo
    def generateRingGraph(self, nodes):
        G = nx.circulant_graph(nodes, [1])
        return G

    #Save graph G as S, where S is a string
    def saveGraph(self, G, S):
        nx.write_gml(G, S)


    def drawGraph(self, G):
        nx.draw(G)
        plt.show()

    def run(self, nodes):
        G = self.generateRingGraph(nodes)
        str1 = "graphRing.gml"
        self.saveGraph(G, str1)
        self.drawGraph(G)
