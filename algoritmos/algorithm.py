# Este archivo sirve de modelo para la creacion de aplicaciones, i.e. algoritmos concretos
""" Implementa la simulacion del algoritmo de Propagacion de Informacion (Segall) como ejemplo
de aplicacion """

import sys
from event import Event
from model import Model
#from process import Process
#from simulator import Simulator
from simulation import Simulation

class Algorithm(Model):

    """ La clase Algorithm desciende de la clase Model e implementa los metodos 
    "init()" y "receive()", que en la clase madre se definen como abstractos """
	
    def init(self):
        """ Aqui se definen e inicializan los atributos particulares del algoritmo """
        self.visited = False
        print("inicializo algoritmo")

    def delay(self):
        return(1.0)
    
    def receive(self, event):
        """ Aqui se definen las acciones concretas que deben ejecutarse cuando se
        recibe un evento """
        if self.visited == False:
            print("soy ", self.id, " recibo mensaje a las ", self.clock, " desde ", event.getSource())
            self.visited = True
            for t in self.neighbors: 
                newevent = Event("C", self.clock+self.delay(), t, self.id)
                print(" proximo evento a las ", newevent.getTime())
                self.transmit(newevent)

