class Cliente:
    __Nombre: str
    __Apellido: str
    __DNI: int
    __Numtar: int
    __Saldoa: float
    def __init__(self, nombre,apellido,dni,numtar,saldoa):
        self.__Nombre= nombre
        self.__Apellido= apellido
        self.__DNI= dni
        self.__Numtar= numtar
        self.__Saldoa= saldoa
    def getNombre(self):
        return self.__Nombre
    def getApellido(self):
        return self.__Apellido
    def getDNI(self):
        return self.__DNI
    def getNumtar(self):
        return self.__Numtar
    def getSaldoa(self):
        return self.__Saldoa
    