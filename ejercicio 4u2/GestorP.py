from Pedidos import Pedido
import csv
import os
class GestorPedido:
    __listaPedido: list
    def __init__(self):
        self.__listaPedido = []
    def agregarPedido(self, unpedido):
        self.__listaPedido.append(unpedido)
    def testPedido(self):
        archivo=open('datosPedidos.csv')
        reader=csv.reader(archivo,delimiter=';')
        bandera= True
        for fila in reader:
            if bandera:
                bandera = not bandera
            else:
                patente = fila[0]
                id = int(fila[1])
                comidas = fila[2]
                te = int(fila[3])
                tr = int(fila[4])
                precio = float(fila[5])
                unpedido = Pedido(patente,id,comidas,te,tr,precio)
                self.agregarPedido(unpedido)
        archivo.close()
    def mostar(self):
        for i in range (len(self.__listaPedido)):
            print('Patente: ',self.__listaPedido[i].getPatente())
            print('Identificador: ',self.__listaPedido[i].getID())
            print('Comidas: ',self.__listaPedido[i].getComidas())
            print('Tiempo de estimado: ',self.__listaPedido[i].getTE())
            print('Tiempo real: ',self.__listaPedido[i].getTR())
            print('Precio: ',self.__listaPedido[i].getPrecio())
    def ingresarpedidos(self,xp):
        p=xp
        i= int(input('Ingrese identificador del pedido: '))
        c= input('Ingrese comida: ')
        te= int(input('ingrese tiempo de entrega estimado: '))
        tr= int(input('Ingrese Tiempo de entrega real: '))
        pr= float(input('Ingrese precio: '))
        unpedido= Pedido(p,i,c,te,tr,pr)
        self.agregarPedido(unpedido)
    def modificartiempo(self, xide):
        i=0
        valor=-1
        while i<(len(self.__listaPedido)):
            if self.__listaPedido[i].getID()==xide:
                tr= int(input('Ingrese nuevo tiempo real: '))
                self.__listaPedido[i].modificar(tr)
                valor= 1
            i+=1 
        return valor
    def promedio(self, xpat):
        acum=0
        cont=0
        for i in range(len(self.__listaPedido)):
            if self.__listaPedido[i].getPatente()==xpat:
                cont+=1
                acum+= int(self.__listaPedido[i].getTR())
        if acum == 0:
            print('El conductor no realizo pedidos')
        else:
            print('El promedio real es', format(acum/cont))
    
            
                
        
        
    
                

        


            
        

        
        

