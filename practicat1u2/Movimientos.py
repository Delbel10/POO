class Movimiento:
    __Numtarjeta: int
    __Fecha: str
    __Descripcion: str
    __Tipo: str
    __Importe: float
    def __init__(self, numtarjeta,fecha,descripcion,tipo,importe):
        self.__Numtarjeta= numtarjeta
        self.__Fecha= fecha
        self.__Descripcion= descripcion
        self.__Tipo= tipo
        self.__Importe= importe
    def getNumtarjeta(self):
        return self.__Numtarjeta
    def getFecha(self):
        return self.__Fecha
    def getDescripcion(self):
        return self.__Descripcion
    def getTipo(self):
        return self.__Tipo
    def getImporte(self):
        return self.__Importe
    def __it__(self, otro):
        return self.__Numtarjeta < otro.getNumtarjeta
    def __gt__(self, otro):
        return self.__Numtarjeta > otro.__Numtarjeta
    
    