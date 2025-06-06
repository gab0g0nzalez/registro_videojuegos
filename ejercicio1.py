videojuegos=[]
plataformas=('PC','PS5','Xbox Series X','Nintendo Switch')
while True:
    print('\n--- MENÚ DE VIDEOJUEGOS ---')
    print('1.   Registrar videojuego')
    print('2.   Ver videojuego')
    print('3.   Modificar videojuego')
    print('4.   Eliminar videojuego')
    print('5.   Salir')

    opcion=input('Seleccione una opción (1-5) :  ')

    if opcion=='1':
        while True:
            try:
                codigo=int(input('Ingrese el código del videojuego: '))
                if codigo<=0:
                    print('Error!   Debe ingresar números mayores a 0')
                else:
                    break
            except ValueError:
                print('Error!   Debe ingresar números enteros.')
        while True:
            nombre=input('Ingrese el nombre del videojuego: ')
            if nombre.isspace() or nombre.isdigit():
                print('Error!   Debe ingresar letras o números.')
            else:
                break

        while True:
            genero=input('Ingrese el género del videojuego: ')
            if genero.isalpha():
                break
            else:
                print('Error!   Debe ingresar letras.')

        print('\nPlataformas disponibles:')
        print('1.   PC')
        print('2.   PS5')
        print('3.   Xbox Series X')
        print('4.   Nintendo Switch')

        while True:
            try:
                plataforma_codigo=int(input('Seleccione el número de la plataforma: '))
                if plataforma_codigo in range(1,5):
                    break
                else:
                    print('Error!   Debe ingresar números entre 1-4.')
            except ValueError:
                print('Error!   Debe ingresar números enteros.')

        plataforma=plataformas[plataforma_codigo-1]
        videojuego={
            'codigo':codigo,
            'nombre':nombre,
            'genero':genero,
            'plataforma':plataforma
        }
        videojuegos.append(videojuego)
        print('Videojuego registrado correctamente.')
    elif opcion=='2':
        if len(videojuegos)==0:
            print('No hay videojuegos registrados.')
        else:
            print('\n--- LISTA DE VIDEOJUEGOS ---')
            for v in videojuegos:
                print(f'Código: {v['codigo']}, Nombre: {v['nombre']}, Género: {v['genero']}, Plataforma: {v['plataforma']}')
    elif opcion=='3':
        while True:
            try:
                codigo= int(input('Ingrese el código del videojuego a modificar:    '))
                if codigo<=0:
                    print('Error!   Debe ingresar números mayores a 0')
                else:
                    break
            except ValueError:
                print('Error!   Debe ingresar números enteros.')

        encontrado=False
        for v in videojuegos:
            if v['codigo']==codigo:

                while True:
                    nombre=input('Nuevo nombre:   ')
                    if nombre.isspace() or nombre.isdigit():
                        print('Error!   Debe ingresar letras o números.')
                    else:
                        break

                v['nombre']=nombre

                while True:
                    genero=input('Nuevo género:    ')
                    if genero.isalpha():
                        break
                    else:
                        print('Error!   Debe ingresar letras.')

                v['genero']=genero
                print('\nPlataformas disponibles:')
                print('1.   PC')
                print('2.   PS5')
                print('3.   Xbox Series X')
                print('4.   Nintendo Switch')

                while True:
                    try:
                        plataforma_codigo=int(input('Seleccione el número de la nueva plataforma: '))
                        if plataforma_codigo in range(1,5):
                            break
                        else:
                            print('Error!   Debe ingresar números entre 1-4.')
                    except ValueError:
                        print('Error!   Debe ingresar números enteros.')

                print('Videojuego modificado correctamente.')
                encontrado=True
                break
        if not encontrado:
            print('Videojuego no encontrado.')
    elif opcion=='4':
        while True:
            try:
                codigo=int(input('Ingrese el código del videojuego a eliminar:  '))#
                if codigo<=0:
                    print('Error!   Debe ingresar números mayores a 0')
                else:
                    break
            except ValueError:
                print('Error!   Debe ingresar números enteros.')

        eliminado=False
        for v in videojuegos:
            if v['codigo']==codigo:
                videojuegos.remove(v)
                eliminado=True
                break
        if not eliminado:
            print('Videojuego no encontrado.')
    elif opcion=='5':
        print('Saliendo del programa.')
        break
    else:
        print('Opción inválida.')