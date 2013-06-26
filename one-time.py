from sys import argv
from random import shuffle
from string import ascii_lowercase

def keygen(n, a, b):
    hojas = []
    for i in range(n):
        hojas.append(range(a,b))
        shuffle(hojas[i])
    return hojas

def guardarLista(lista, archivo='key'):
    original = open(archivo+'_Original', 'w')
    copia = open(archivo+'_Copia', 'w')
    for i in lista:
        original.write(' '.join(str(x) for x in i)+'\n')
        copia.write(' '.join(str(x) for x in i)+'\n')
    original.close()
    copia.close()

def guardarArchivo(lista, archivo='key'):
    original = open(archivo+'_Original', 'w')
    for i in lista:
        original.write(' '.join(str(x) for x in i)+'\n')
    original.close()

def listaKey(archivo):
    entrada = open(archivo, 'r')
    lista = []
    for linea in entrada:
        lista.append(linea.split())
    return lista

def valorAsociado(numero, maximo):
    if numero > maximo:
        return numero % maximo
    else:
        return numero


def E(M, keys, tipo='E', ABC = None):
    if ABC == None:
        ABC = ascii_lowercase+' 1234567890' 
    largoKey = len(keys[0]) 
    largoM = len(M)
    largoABC = len(ABC)
    ciphertext = ''
    e = 1
    if tipo != 'E':
        e = -1
    if largoM > largoKey:
        for i in range(0,(largoM / largoKey)):
            key = keys.pop(0)
            for j in range(len(key)):
                ciphertext += ABC[valorAsociado(ABC.index(M[j+(i * largoKey)])+(int(key[j])*e), largoABC)] 
            key = keys.pop(0)
        for i in range(largoM % largoKey):
            ciphertext += ABC[valorAsociado(ABC.index(M[i+((largoM/largoKey) * largoKey)])+(int(key[i])*e), largoABC)]
    else:
        key = keys.pop(0)
        print key
        for j in range(len(M)):
            ciphertext += ABC[valorAsociado(ABC.index(M[j])+(int(key[j])*e), largoABC)]
    guardarArchivo(keys, 'keys')
    return ciphertext


if __name__ == '__main__':
## cambiar menu por parametros de linea de comandos
    mensaje = ''
    while(True):
        print '1.- Generar Archivos'
        print '2.- Ingresar Mensaje'
        print '3.- Encriptar Mensaje'
        print '4.- Decifrar Mensaje'
        print '5.- Ver Mensaje Almacenado'
        print '6.- Prueba (Encripta y Desencripta)'
        print '7.- Salir'
        try:
            opcion = int(raw_input('Opcion >> '))
        except:
            print 'Ingrese una opcion del menu'
            pass
        if opcion == 1:
            try:
                n = int(raw_input('Cantidad de llaves a generar >> '))
                print 'Defina el rango de las llaves a generar a -> b'
                i = int(raw_input('Inicio de Rango >> '))
                f = int(raw_input('Finaliza el Rango  >> '))
                k = keygen(n, i, f)
                guardarLista(k, 'keys')
                print 'Se han generado las llaves!!'
            except:
                continue
        elif opcion == 2:
            mensaje = raw_input('Mensaje >>')
        elif opcion == 3:
            if len(mensaje) > 0:
                llaves = listaKey('keys_Original')
                print E(mensaje, llaves, 'E')
            else:
                print 'No hay mensaje almacenado'
        elif opcion == 4:
            if len(mensaje) > 0:
                llaves2 = listaKey('keys_Copia')
                print E(mensaje, llaves2, 'D')
            else:
                print 'No hay mensaje almacenado'
        elif opcion == 5:
            print 'Mensaje: %s' % mensaje
        elif opcion == 6:
            if len(mensaje) > 0:
                llaves = listaKey('keys_Original')
                CT = E(mensaje, llaves, 'E')
                llaves2 = listaKey('keys_Copia')
                PT = E(CT, llaves2, 'D')
                print 'Mensaje Encripado: %s \nMensaje Desencriptado: %s' %(CT, PT)
            else:
                print 'No hay mensaje almacenado'
        elif opcion == 7:
            print 'Adios!!'
            break
        else:
            print 'Ingrese opcion del menu valida'

