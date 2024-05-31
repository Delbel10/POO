from Movimientos import Movimiento
import csv
import numpy as np
class GestorMovimiento:
    __Dimension: int
    __Cantidad: int
    __Incremento= 1
    __movimiento: np.ndarray
    def __init__(self):
        self.__Dimension= 0
        self.__Cantidad= 0
        self.__Incremento= 1
        self.__movimiento= np.empty(self.__Dimension, dtype=Movimiento)
    def agregarmovimiento(self, unMovimiento):
        if self.__Cantidad == self.__Dimension:
            self.__Dimension+= self.__Incremento
            self.__movimiento.resize(self.__Dimension)
        self.__movimiento[self.__Cantidad]= unMovimiento
        self.__Cantidad+= 1
    def testmovimiento(self):
        archivo= open('MovimientosAbril2024.csv')
        reader= csv.reader(archivo,delimiter=';')
        bandera= True
        for fila in reader:
            if bandera:
                bandera= not bandera
            else:
                numtarjeta = int(fila[0])
                fecha  = fila[1]
                descripcion = fila[2]
                tipo = fila[3]
                importe = float(fila[4])
                unMovimiento = Movimiento(numtarjeta,fecha,descripcion,tipo,importe)
                self.agregarmovimiento(unMovimiento)
        archivo.close()
    def mostar(self):
        for i in range(self.__Cantidad):
            print('Numero de tarjeta: ',self.__movimiento[i].getNumtarjeta())
            print('Fecha: ',self.__movimiento[i].getFecha())
            print('Descripcion: ',self.__movimiento[i].getDescripcion())
            print('Tipo: ',self.__movimiento[i].getTipo())
            print('Importe: ',self.__movimiento[i].getImporte())
    def consultar(self, xnum):
        i= 0
        bandera= False
        while not bandera and i<self.__Cantidad:
            if self.__movimiento[i].getNumtarjeta() == xnum:
                bandera= True
            else:
                i+=1
        return bandera
    def ordenar(self):
        self.__movimiento=np.sort(self.__movimiento)
        print('------------------------LISTA ORDENADA-----------------------')
        for i in range(self.__Cantidad):
            print('Numero de tarjeta: ',self.__movimiento[i].getNumtarjeta())
            print('Fecha: ',self.__movimiento[i].getFecha())
            print('Descripcion: ',self.__movimiento[i].getDescripcion())
            print('Tipo: ',self.__movimiento[i].getTipo())
            print('Importe: ',self.__movimiento[i].getImporte())



            
            




            

            
    
    