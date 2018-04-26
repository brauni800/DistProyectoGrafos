import sys
from anillo.ringGraph import Ring
from inundacion.floodGraph import Flood
from profundidad.depthGraph import Depth

class Generador():
    url = "../simulador/" + sys.argv[1] + ".txt"
    archivo = open(url)

    def decidirGrafo(self):
        for linea in self.archivo.readlines():
            """ Aqui se parsea la linea, verifica que tipo de grafo es y devuelve una bandera con el tipo de grafo """
            print("provicional")
            return "ANILLO"
        

if len(sys.argv) != 2:
    print("Please supply a file name")
    raise SystemExit(1)




gen = Generador()

if gen.decidirGrafo() == "ANILLO":
    anillo = Ring()
    anillo.run(gen.url)
elif gen.decidirGrafo() == "INUNDACION":
    inundacion = Flood()
    inundacion.run()
elif gen.decidirGrafo() == "PROFUNDIDAD":
    profundidad = Depth()
    profundidad.run()
