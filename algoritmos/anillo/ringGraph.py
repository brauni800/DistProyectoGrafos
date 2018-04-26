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

    def contarLineas(self, url):
        archivo = open(url, "r")
        num_lineas = 0
        for linea in archivo.readlines():
            if linea != "\n":
                num_lineas += 1
                print(linea)
        return num_lineas

    def run(self, url):
        num_lineas = self.contarLineas(url)
        print("Existen " + str(num_lineas) + " lineas")

        G = self.generateRingGraph(num_lineas)
        str1 = "graphRing.gml"
        self.saveGraph(G, str1)
        self.drawGraph(G)
