from GestorC import GestorCliente
from GestorM import GestorMovimiento
def menu():
    GC= GestorCliente()
    GC.testcliente()
    GC.mostrardatos()
    GM= GestorMovimiento()
    GM.testmovimiento()
    GM.mostar()
    print('1 _ Actualizar saldo: ')
    print('2 _ Consultar si tuvo movimientos')
    print('3 _ Ordenar Gestor de Movimiento')
    Op= int(input('Ingrese la opcion: '))
    while Op!=0:
        if Op == 1:
            d= int(input('Ingresar DNI: '))
            ind= GC.buscardni(d)
            GC.actualizarsaldo(GM,ind)
            print('Operacion 1 realizada')
        elif Op == 2:
            num= int(input('Ingrese numero de trabajo: '))
            r= GM.consultar(num)
            if r == True:
                print('Si tiene movimientos')
            else:
                GC.obtenerdatos(num)
        elif Op == 3:
            GM.ordenar()
        Op= int(input('Ingrese la opcion: '))

        
    
    
    
