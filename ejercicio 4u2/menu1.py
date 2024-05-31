from GestorM import GestorMoto
from GestorP import GestorPedido
def menu():
    print('1 _ Leer datos de las motos desde un archivo csv')
    print('2 _ Leer datos de los pedidos desde un archivo csv')
    print('3 _ Cargar nuevo pedido')
    print('4 _ Modificar Tiempo real')
    print('5 _ Generar un listado para cada moto')
    op = int(input('Ingrese la opcion: '))
    while op!=0:
        if op == 1:
            m = GestorMoto()
            m.testMoto()
            print ('operacion 1 realizada')
        elif op == 2:
            p = GestorPedido()
            p.testPedido()
            p.mostar()
            print ('operacion 2 realizada')
        elif op == 3:
            pa= input('Ingrese patente de la moto: ')
            r= m.validarpatente(pa)
            if r == 1:
                print('Patente valida')
                p.ingresarpedidos(pa)
                print ('Operacion 3 realizada')
            else:
                print('Patente invalida')
        elif op == 4:
            pat= input('ingrese patente: ')
            ide= int(input('Ingrese identificador: '))
            re= p.modificartiempo(ide)
            if re == 1:
                print('Operacion 4 realizada')
            else:
                print('Operacion no realizada')
        elif op == 5:
            pate= input('Ingrese patente: ')
            b= m.datos(pate)
            if b==1:
                print('El conductor fue encontrado con exito')
            else:
                print('El conductor se encontro')
            p.promedio(pate)
            print ('Operacion 5 realizada')
        elif op == 6:
            m.calcomisiones(p)
    
        op = int(input('Ingrese la opcion: '))
        

        
 


