from Gestor import Arreglo
if __name__ == '__main__':
    tam= int(input('Ingrese cantidad de cuentas: '))
    cuenta= Arreglo(tam,tam)
    cuenta.test(tam)
    cuenta.mostarDatos()