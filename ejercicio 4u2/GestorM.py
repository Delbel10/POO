from Motos import Moto
import csv 
class GestorMoto:
    __listamoto: list
    def __init__(self):
        self.__listamoto=[]
    def agregarMoto(self,unamoto):
        self.__listamoto.append(unamoto)
    def testMoto(self):
        archivo=open('datosMotos.csv')
        reader=csv.reader(archivo,delimiter=';')
        bandera = True
        for fila in reader:
            if bandera:
                bandera = not bandera
            else:
                patente = fila[0]
                marca = fila[1]
                nya = fila[2]
                kilometraje = [3]
                unamoto = Moto(patente,marca,nya,kilometraje)
                self.agregarMoto(unamoto)
        archivo.close()
    def validarpatente (self, xp):
        i=0
        valor=-1
        while i<(len(self.__listamoto)):
            if self.__listamoto[i].getPatente()==xp:
                valor=1
            i+=1
        return valor
    def datos(self, xpate):
        i=0
        valor=-1
        while i<(len(self.__listamoto)):
            if self.__listamoto[i].getPatente()==xpate:
                print('Nombre y apellido del conductor: ',self.__listamoto[i].getNyA())
                valor=1
            i+=1
        return valor
    def calcomisiones(self,p):
        for i in range (len(self.__listamoto)):
            acum= 0
            xpat= self.__listamoto[i].getPatente()
            xcon= self.__listamoto[i].getNyA()
            print(f"""        °Comisiones para moto 
                    Patente de la moto: {xpat}
                    Conductor: {xcon}
                    ID de Pedido       Tiempo  estimado       Tiempo real       Precio""")
            for j in range (len(p._GestorPedido__listaPedido)):
                if p._GestorPedido__listaPedido[j].getPatente()==xpat:
                    xid= p._GestorPedido__listaPedido[j].getID()
                    xte= p._GestorPedido__listaPedido[j].getTE()
                    xtr= p._GestorPedido__listaPedido[j].getTR()
                    xpr= p._GestorPedido__listaPedido[j].getPrecio()
                    acum+= xpr
                    print(f""" 
                        {xid}               {xte}                   {xtr}             ${xpr}""")
                    print(f"""
                            Total: ${round(acum,2)})
                            Comisión: ${round((20*acum)/100,2)}""")
                    print("----------------------------")



            
            

            
    