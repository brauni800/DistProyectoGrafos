import matplotlib.pyplot as plt
import networkx as nx

def generateRingGraph(nodes):
    G = nx.circulant_graph(nodes, [1])
    return G

#Save graph G as S, where S is a string
def saveGraph(G, S):
    nx.write_gml(G, S)


def drawGraph(G):
    nx.draw(G)
    plt.show()

def main():
    G = generateRingGraph(20)
    str1 = "graphRing.gml"
    saveGraph(G, str1)
    drawGraph(G)

if __name__ == "__main__":
    main()