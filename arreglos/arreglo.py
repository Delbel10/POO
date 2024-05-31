import numpy as np 
import csv
from clasecuenta import Cuenta
class GestorCuentas:
    __cantidad: int
    __dimension: int
    __incremento: int 
    __cuentas:np.ndarray
    def __init__(self):
        self.__cantidad=0
        self.__dimension=0
        self.__incremento=5
        self.__cuentas=np.empty(self.__dimension,dtype=Cuenta)
    def agregarCuenta(self,unacuenta):
        if self.__cantidad == self.__dimension:
            self.__dimension+=self.__incremento
            self.__cuentas.resize(self.__dimension)
        self.__cuentas[self.__cantidad]=unacuenta
        self.__cantidad+=1
    def test(self):
        archivo=open('programa.csv')
        reader=csv.reader(archivo,delimiter=';')
        band=True
        for fila in reader:
            if band:
                band=not band
            else:
                self.agregarCuenta(Cuenta (fila[0],fila[1],int(fila[2]),int(fila[3]),float(fila[4]),int(fila[5])))
        archivo.close()
    def mostrarDatos(self):
        for i in range (self.__cantidad):
            print('Apellido:', self.__cuentas[i].getApellido())
            print('Nombre:', self.__cuentas[i].getNombre())
            print('DNI:', self.__cuentas[i].getDNI())
            print('Telefono:',self.__cuentas[i].getTelefono())
            print('Saldo:', self.__cuentas[i].getSaldo())
            print('CVU:', self.__cuentas[i].getCVU())






