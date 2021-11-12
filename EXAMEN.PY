# ASIGNACION DE DATOS
contrasena = '12345'
num_equipos = 0


#FUNCION PARA CAMBIAR CONTRASEÑA
def cambiarContrasena():
    nueva_contraseña = input('Ingrese una nueva contraseña: ')
    return nueva_contraseña

# PROCESO
while(True):
    print('''
    ELIGE UNA OPCIÓN: 
    1) OBTENER INFORMACION
    2) CAMBIAR CONTRASEÑA
    3) CAMBIAR NUMERO DE EQUIPOS
    4) SALIR''')

    opcion = int(input(''))

    if opcion == 1:
        print("CONTRASEÑA: ", contrasena)
        print("NUMERO DE EQUIPOS: ", num_equipos)
    elif opcion == 2:
        contrasena = cambiarContrasena()
        print('·····Cambios aplicacados·····')
    elif opcion == 3:
        nueva_cantidad_equipos = int(input('Ingresar cantidad de equipos: '))
        num_equipos = nueva_cantidad_equipos
        print('·····Cambios aplicacados·····')
    elif opcion == 4:
        break
    else:
        print('OPCION INCORRECTA, VUELVELO A INTENTAR')
