import sys
from anillo.ringGraph import Ring
from inundacion.floodGraph import Flood
from profundidad.depthGraph import Depth
from node import Node
from edge import Edge
from algorithm import Algorithm
from event import Event
from model import Model
from simulation import Simulation

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

def loopString(line, start, end):
    total = ""
    for char in range(start, end):
        total += line[char]
    return total

def generarGrafo():
    gen = Generador()
    nodes = sys.argv[1]
    grafo = sys.argv[2]

    gmlUrl = gen.generarGrafo(nodes,grafo)
    gmlFile = open(gmlUrl)
    lines = gmlFile.readlines()

    for line in lines:
        if line.find("node") != -1:
            node = Node()

        elif line.find("id") != -1:
            if line[len(line) - 2] == '\n':
                node.setId(line[6])
            else:
                node.setId(loopString(line, 6, len(line) - 1))

        elif line.find("label") != -1:
            if line[len(line) - 2] == '\n':
                node.setLabel(loopString(line, 10, len(line) - 1))
            else:
                node.setLabel(loopString(line, 10, len(line) - 1))
            nodeArray.append(node)

        elif line.find("edge") != -1:
            edge = Edge()

        elif line.find("source") != -1:
            if line[len(line) - 2] == '\n':
                edge.setSource(line[10])
            else:
                edge.setSource(loopString(line, 10, len(line) - 1))

        elif line.find("target") != -1:
            if line[len(line) - 2] == '\n':
                edge.setTarget(line[10])
            else:
                edge.setTarget(loopString(line, 11, len(line) - 1))
            edgeArray.append(edge)
    gmlFile.close()

def generarTxt():
    file = open("grafica.txt", 'w')
    for node in nodeArray:
        for edge in edgeArray:
            if node.id == edge.source:
                file.write(edge.target + " ")
        file.write('\n')
    file.close()

if len(sys.argv) != 3:
    print(len(sys.argv))
    raise SystemExit(1)


nodeArray = []
edgeArray = []

generarGrafo()
generarTxt()

experiment = Simulation("grafica.txt", 100)

# asocia un pareja proceso/modelo con cada nodo de la grafica
for i in range(1,len(experiment.graph)+1):
    m = Algorithm()
    experiment.setModel(m, i)

# inserta un evento semilla en la agenda y arranca
seed = Event("C", 0.0, 1, 1)
experiment.init(seed)
experiment.run()
