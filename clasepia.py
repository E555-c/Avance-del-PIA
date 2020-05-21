Contacto de clase :
def  __init__ ( self , telefono , nombre , correo , registro = datetime . datetime . now (), UIValido = False ):
    auto . telefono = telefono
    auto . nombre = nombre
    auto . correo = correo
    auto . registro = registro
    auto . UIValido = UIValido

importar  re
# Se importa la clase Contacto
de  definirclase  import  Contacto

# Validador de expresiones regulares
def  RegEx ( _txt , _regex ):
    coincidencia = re . partido ( _regex , _txt )
    return  bool ( coincidencia )

# Expresiones regulares para cada campo.
telefonoRegEx = "^ [0-9] {10} $"
nombreRegEx = "^ [AZ] + (([',. -] [AZ])? [AZ] *) * $"
entidadValida = Verdadero

# Pregunta de teléfono.
_telefono = ""
telefono = 0
datoValido = False
mientras  cierto :
