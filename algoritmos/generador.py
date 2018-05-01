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

class Node():
    def __init__(self):
        self.id = None
        self.label = None
        self.edges = []
    
    def setId(self, id):
        self.id = id

    def setLabel(self, label):
        self.label = label
    
    def addEdge(self, item):
        self.edges.append(item)

class Edge():
    def __init__(self):
        self.source = None
        self.target = None
    
    def setSource(self, source):
        self.source = source
    
    def setTarget(self, target):
        self.target = target

def loopString(line, start, end):
    total = ""
    for char in range(start, end):
        total += line[char]
    return total

if len(sys.argv) != 3:
    print("Please supply a file name")
    raise SystemExit(1)

gen = Generador()
nodes = sys.argv[1]
grafo = sys.argv[2]

gmlUrl = gen.generarGrafo(nodes,grafo)
gmlFile = open(gmlUrl)
lines = gmlFile.readlines()

nodeArray = []
edgeArray = []

for line in lines:
    if line.find("node") != -1:
        node = Node()
        #print("node:")

    elif line.find("id") != -1:
        if line[len(line) - 2] == '\n':
            node.setId(line[6])
        else:
            node.setId(loopString(line, 6, len(line) - 1))
        #print("  id -> " + node.id)

    elif line.find("label") != -1:
        if line[len(line) - 2] == '\n':
            node.setLabel(loopString(line, 10, len(line) - 1))
        else:
            node.setLabel(loopString(line, 10, len(line) - 1))
        nodeArray.append(node)
        #print("  label -> " + node.label)

    elif line.find("edge") != -1:
        edge = Edge()
        #print("edge:")

    elif line.find("source") != -1:
        if line[len(line) - 2] == '\n':
            edge.setSource(line[10])
        else:
            edge.setSource(loopString(line, 10, len(line) - 1))
        #print("  source -> " + edge.source)

    elif line.find("target") != -1:
        if line[len(line) - 2] == '\n':
            edge.setTarget(line[10])
        else:
            edge.setTarget(loopString(line, 11, len(line) - 1))
        edgeArray.append(edge)
        #print("  target -> " + edge.target)



gmlFile.close()
