from clase import CajadeAhorro
def test():
    nc1=input ('Ingrese numero de caja de ahorro: ')
    c1=input ('Ingrese CUIL: ')
    a1=input ('Ingrese apellido: ')
    n1= input ('Ingrese nombre: ')
    s1=float (input('Ingrese saldo: '))
    caja1=CajadeAhorro(nc1, c1, a1, n1, s1)
    caja1.mostrarDatos()
    imp1=float(input('ingrese importe: '))
    caja1.extraer(imp1)
    impo1=float(input('Ingrese importe a depositar: '))
    caja1.depositar(impo1)
    caja1.validarcuil(c1)

    nc2=input ('Ingrese numero de caja de ahorro: ')
    c2=input ('Ingrese CUIL: ')
    a2=input ('Ingrese apellido: ')
    n2= input ('Ingrese nombre: ')
    s2=float (input('Ingrese saldo: '))
    caja2=CajadeAhorro(nc2, c2, a2, n2, s2)
    caja2.mostrarDatos()
    imp2=float(input('ingrese importe: '))
    caja2.extraer(imp2)
    impo2=float(input('Ingrese importe a depositar: '))
    caja2.depositar(impo2)
    caja2.validarcuil(c2)

    nc3=input ('Ingrese numero de caja de ahorro: ')
    c3=input ('Ingrese CUIL: ')
    a3=input ('Ingrese apellido: ')
    n3= input ('Ingrese nombre: ')
    s3=float (input('Ingrese saldo: '))
    caja3=CajadeAhorro(nc3, c3, a3, n3, s3)
    caja3.mostrarDatos()
    imp3=float(input('ingrese importe: '))
    caja3.extraer(imp3)
    impo3=float(input('Ingrese importe a depositar: '))
    caja3.depositar(impo3)
    caja3.validarcuil(c3)