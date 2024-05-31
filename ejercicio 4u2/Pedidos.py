class Pedido:
    __Patente: str
    __ID: int
    __Comidas: str
    __TE: int
    __TR: int
    __Precio: float
    def __init__(self, patente, id, comidas, te, tr, precio): 
        self.__Patente = patente
        self.__ID = id
        self.__Comidas = comidas
        self.__TE = te
        self.__TR = tr
        self.__Precio= precio
    def getPatente(self):
        return self.__Patente
    def getID(self):
        return self.__ID
    def getComidas(self):
        return self.__Comidas
    def getTE(self):
        return self.__TE
    def getTR(self):
        return self.__TR
    def getPrecio(self):
        return self.__Precio
    def modificar(self, xtie):
        self.__TR= xtie
        print ('tiempo real modificado')
    
    