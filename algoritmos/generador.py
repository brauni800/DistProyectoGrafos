import sys
from anillo.ringGraph import Ring
from inundacion.floodGraph import Flood
from profundidad.depthGraph import Depth

class Generador():

    def generarGrafo(self, nodes, grafo):
        if grafo == "RING":
            Ring().run(int(nodes))
            return "graphRing.gml"
        elif grafo == "FLOOD":
            Flood().run(int(nodes))
            return "graphFlood.gml"
        elif grafo == "DEPTH":
            Depth().run(int(nodes))
            return "graphDepth.gml"

if len(sys.argv) != 3:
    print("Please supply a file name")
    raise SystemExit(1)

gen = Generador()
nodes = sys.argv[1]
grafo = sys.argv[2]
gmlUrl = gen.generarGrafo(nodes,grafo)
gmlFile = open(gmlUrl)
for x in range(len(gmlFile.readlines())):
    print(gmlFile.readline())
gmlFile.close()
