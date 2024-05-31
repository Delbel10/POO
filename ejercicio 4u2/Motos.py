class Moto:
    __Patente: str
    __Marca: str
    __NyA: str
    __Kilometraje: str
    def __init__(self, patente, marca, nya, kilometraje):
        self.__Patente = patente
        self.__Marca = marca
        self.__NyA = nya
        self.__Kilometraje = kilometraje
    def getPatente(self):
        return self.__Patente
    def getMarca(self):
        return self.__Marca
    def getNyA(self):
        return self.__NyA
    def getKilometraje(self):
        return self.__Kilometraje
    
