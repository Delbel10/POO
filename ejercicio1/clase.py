class CajadeAhorro:
    __nrocuenta: str
    __cuil: str
    __apellido: str
    __nombre: str
    __saldo: float
    def __init__(self, nc, c, a, n, s):
        self.__nrocuenta=nc
        self.__cuil=c
        self.__apellido=a
        self.__nombre=n
        self.__saldo=s
    def mostrarDatos(self):
        print("--- SUS DATOS SON: ---".center(100))
        print('Numero de cuenta: ', self.__nrocuenta)
        print('CUIL: ', self.__cuil)
        print('Apellido: ', self.__apellido)
        print('Nombre: ', self.__nombre)
        print('Saldo: ', self.__saldo)
    def extraer(self, importe):
        resultado=-1
        if (self.__saldo >= importe):
            resultado=self.__saldo - importe
            return resultado
    def depositar (self, ximporte):
        if (ximporte > 0):
            self.__saldo=self.__saldo + ximporte
        else:
            print ('Ingrese negativo no se puede realizar la funcion')
    def validarcuil(self):
        mul=[5, 4, 3, 2, 7, 6, 5, 4, 3, 2]
        indice=[1, 2, 3, 4, 5, 6, 7, 8, 9, 0]
        parte=self.__cuil.split('-')
        dato=parte[0] + parte[1]
        for i in range (len(dato)):
            if i in indice:
                suma=suma + (int(dato[i]) * mul[i])
                print(f"({suma})")
                calculo=suma % 11
                resto=suma - (calculo * 11)
                if (resto == 0):
                    if(self.__cuil[12] == 0):
                        print ("Cuil valido")
                    else:
                        print ("Cuil invalido")
                if (resto >=1):
                    if (self.__cuil[12] == 9):
                        if (self.__cuil[0:2]==20):
                            print ("cuil valido")
                        else:
                            print ("cuil invalido porque debe comenzar con 20 si es hombre")
                    if (self.__cuil[12]==4):
                        if (self.__cuil[0:2]==27):
                            print ("cuil vakido")
                        else:
                            print ("cuil invalido porque debe comenzar con 27 si es mujer")
                    if (self.__cuil[0:2]==30):
                        z=11 - resto
                    else:
                        print ("cuil invalido porque si es una empresa debe terminar con este digito",z)

                





