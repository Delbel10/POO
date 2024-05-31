class Cuenta:
    __ape:str
    __nom:str
    __dni:int
    __tel:int
    __saldo:float
    __cvu:int
    def __init__(self,a,n,d,t,s,c):
        self.__ape=a
        self.__nom=n
        self.__dni=d
        self.__tel=t
        self.__saldo=s
        self.__cvu=c
    def getApellido(self):
        return self.__ape
    def getNombre(self):
        return self.__nom
    def getDNI(self):
        return self.__dni
    def getTelefono(self):
        return self.__tel
    def getSaldo(self):
        return self.__saldo
    def getCVU(self):
        return self.__cvu

    

