def  RegEx ( _txt , _regex ):
    coincidencia = re . partido ( _regex , _txt )
    return  bool ( coincidencia )

def  principal ():
    mientras que ( Verdadero ):
        LimpiarPantalla ()
        imprimir ( "LISTA DE COTACTOS" )
        imprimir ( "" )
        print ( "[1] Agregar un contacto." )
        print ( "[2] Buscar un contacto." )
        print ( "[3] Eliminar un contacto." )
        print ( "[4] Mostrar contactos." )
        print ( "[5] Serializar datos." )
        print ( "[0] Salir" )
        opcion_elegida  =  input ( "¿Qué deseas hacer?>" )
        si  RegEx ( opcion_elegida , "^ [123450] {1} $" ):
            si  opcion_elegida == "0" :
                imprimir ( "GRACIAS POR UTILIZAR EL PROGRAMA" )
                rotura
            si  opcion_elegida == "1" :
                imprimir ( "Llamar procedimiento para la acción" )
            si  opcion_elegida == "2" :
                imprimir ( "Llamar procedimiento para la acción" )
            si  opcion_elegida == "3" :
                imprimir ( "Llamar procedimiento para la acción" )
            si  opcion_elegida == "4" :
                imprimir ( "Llamar procedimiento para la acción" )
            si  opcion_elegida == "5" :
                imprimir ( "Llamar procedimiento para la acción" )

            input ( "Pulsa enter para contunuar ..." )
        más :
            print ( "Esa respuesta no es válida" )
            input ( "Pulsa enter para contunuar ..." )
 def  CuantosElementosHay ():
    txt  =  "El número de elementos de la colección es {}"
    print ( txt . format ( len ( Contactos )))

def  BuscarTelefono ( telabuscar ):
    coincidencia = falso
    para  contacto  en  Contactos :
        if ( contacto . telefono == telabuscar ):
            coincidencia = verdadero
            rotura
    volver  coincidencia

def  BuscarContacto ( telabuscar ):
    contador = - 1
    indice_retorno = - 1
    para  contacto  en  Contactos :
        contador + = 1
        if ( contacto . telefono == telabuscar ):
            indice_retorno = contador
            rotura
    return  indice_retorno
Contactos  = []
CuantosElementosHay ()
Contactos . adjuntar ( Contacto ( 1234567890 , "Evelyn Obregon" , "evepacheco419@gamil.com" ))
CuantosElementosHay ()
Contactos . adjuntar ( Contacto ( 1134567890 , "Oscar Peña" , "ooscar.pg@gmail.com" ))
Contactos . adjuntar ( Contacto ( 1114567890 , "Claudia Moron" , "claudya169@gmail.com" ))
CuantosElementosHay ()
para  contacto  en  Contactos :
    print ( "------------------------------------------" )
    imprimir ( contacto . telefono )
    imprimir ( contacto . nombre )
    imprimir ( contacto . correo )
    imprimir ( contacto . registro )
    imprimir ( contacto . UIValido )

# Búsqueda de objeto y retorno de índice, usando función de
# búsqueda.
imprimir ( BuscarContacto ( 1234567890 ))
imprimir ( BuscarContacto ( 9999999999 ))

indice_obtenido = BuscarContacto ( 1234567890 )
si  indice_obtenido == - 1 :
    print ( "No se encontró el objeto" )
más :
    print ( Contactos [ indice_obtenido ]. telefono )
    print ( Contactos [ indice_obtenido ]. nombre )
    print ( Contactos [ indice_obtenido ]. correo )

indice_obtenido = BuscarContacto ( 9999999999 )
si  indice_obtenido == - 1 :
    print ( "No se encontró el objeto" )
más :
    print ( Contactos [ indice_obtenido ]. telefono )
    print ( Contactos [ indice_obtenido ]. nombre )
    print ( Contactos [ indice_obtenido ]. correo )
