import sys
from anillo.ringGraph import Ring
from inundacion.floodGraph import Flood
from profundidad.depthGraph import Depth

class Generador():

    def generarGrafo(self, nodes, grafo):
        if grafo == "RING":
            Ring().run(int(nodes))
        elif grafo == "FLOOD":
            Flood().run(int(nodes))
        elif grafo == "DEPTH":
            Depth().run(int(nodes))

if len(sys.argv) != 3:
    print("Please supply a file name")
    raise SystemExit(1)

gen = Generador()
gen.generarGrafo(sys.argv[1], sys.argv[2])
