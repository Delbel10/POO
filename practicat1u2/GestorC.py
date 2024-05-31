from clientes import Cliente
import csv
class GestorCliente:
    __listaCliente: list
    def __init__(self):
        self.__listaCliente= []
    def agregarcliente(self, unCliente):
        self.__listaCliente.append(unCliente)
    def testcliente(self):
        archivo= open('ClientesAbril2024.csv')
        reader= csv.reader(archivo,delimiter=';')
        bandera= True
        for fila in reader:
            if bandera:
                bandera= not bandera
            else:
                nombre = fila[0]
                apellido = fila[1]
                dni = int(fila[2])
                numtar = int(fila[3])
                saldoa = float(fila[4])
                unCliente = Cliente(nombre,apellido,dni,numtar,saldoa)
                self.agregarcliente(unCliente)
        archivo.close()
    def mostrardatos(self):
        for i in range(len(self.__listaCliente)):
            print('Nombre: ', self.__listaCliente[i].getNombre())
            print('Apellido: ', self.__listaCliente[i].getApellido())
            print('DNI: ', self.__listaCliente[i].getDNI())
            print('Numero de tarjeta: ', self.__listaCliente[i].getNumtar())
            print('Saldo: ', self.__listaCliente[i].getSaldoa())
    def buscardni(self,xd):
        i=0
        posicion = None
        bandera = False
        while not bandera and i<(len(self.__listaCliente)):
            if self.__listaCliente[i].getDNI() == xd:
                bandera= True
                posicion= i
            else:
                i+=1
        return posicion
    def actualizarsaldo(self, GM,xind):
        xape = self.__listaCliente[xind].getApellido()
        xnom = self.__listaCliente[xind].getNombre()
        xsal = self.__listaCliente[xind].getSaldoa()
        xnum = self.__listaCliente[xind].getNumtar()
        print(f"""
                Cliente: {xape} {xnom}                   Numero de tarjeta: {xnum}
                Saldo Anterior: {xsal}
                Movimientos
                Fecha          Descripcion               Importe          Tipo de movimiento""")
        for j in range(GM._GestorMovimiento__Cantidad):
            if GM._GestorMovimiento__movimiento[j].getNumtarjeta() == xnum:
                xfec= GM._GestorMovimiento__movimiento[j].getFecha()
                xdes= GM._GestorMovimiento__movimiento[j].getDescripcion()
                ximp= GM._GestorMovimiento__movimiento[j].getImporte()
                xtip= GM._GestorMovimiento__movimiento[j].getTipo()
                if xtip == "C":
                    xsal+=ximp
                if xtip == "P":
                    xsal-=ximp
                print(f""" 
                {xfec}       {xdes}     {ximp}                  {xtip}
                Saldo actualizado: {xsal}""")
    def obtenerdatos(self, xnum):
        i= None
        bandera= False
        while not bandera and i<(len(self.__listaCliente)):
            if self.__listaCliente[i].getNumtar() == xnum:
                print('Nombre: ',self.__listaCliente[i].getNombre())
                print('Apellido: ',self.__listaCliente[i].getApellido())
                bandera= True
            else:
                i+=1
                



    

        


        
    
    

            
        
                
