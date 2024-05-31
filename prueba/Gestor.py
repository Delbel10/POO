import numpy as np
from clasecuenta import Cuenta
class Arreglo:
    __cantidad: int
    __dimension: int
    __incremento= 1
    __cuentas: np.ndarray
    def __init__(self, dimension, incremento= 1):
        self.__cuentas= np.empty(dimension, dtype= Cuenta)
        self.__cantidad= 0
        self.__dimension= dimension
    def agregarCuenta(self, unaCuenta):
        if self.__cantidad==self.__dimension:
            self.__dimension+=self.__incremento
            self.__cuentas.resize(self.__dimension)
        self.__cuentas[self.__cantidad]=unaCuenta
        self.__cantidad+= 1
    def test(self, cant):
        for i in range(cant):
            apellido= input('Ingrese apellido: ')
            nombre= input('Ingrese nombre:')
            dni= int(input('Ingrese DNI: '))
            telefono= int(input('Ingrese Telefono'))
            saldo= float(input('Ingrese saldo: '))
            cvu= int(input('Ingrese cvu: '))
            unaCuenta = Cuenta(apellido,nombre,dni,telefono,saldo,cvu)
            self.agregarCuenta(unaCuenta)
    def mostarDatos(self):
        for i in range (self.__cantidad):
            print('Apellido:',self.__cuentas[i].getApellido())
            print('Nombre: ',self.__cuentas[i].getNombre())
            print('DNI: ',self.__cuentas[i].getDNI())
            print('Telefono: ',self.__cuentas[i].getTelefono())
            print('saldo: ',self.__cuentas[i].getSaldo())
            print('CVU: ',self.__cuentas[i].getCVU())


