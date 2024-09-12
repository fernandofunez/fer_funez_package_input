# Fecha  11/09/2024      ejercicio 2)
#Teniendo en cuenta la función del punto 1, crear la función get_string. La misma validará la longitud de la cadena ingresada dado
#  el parámetro recibido. El siguiente prototipo es la base para realizar el ejercicio (se puede extender):
def get_string(longitud_maxima:int, reintentos:int, mensaje:str, mensaje_error:str)->str|None:
    """Le pide al usuario una lista de caractares (str) y valida si esa lista se pasa de limite de longitud permitidos, si se pasa de 
    la longitud se le volvera a pedir otra lista hasta que se le agoten los reintentos, y si esto pasa la función retornara None, en caso 
    contrario retornara la lista de caracteres que ingreso el usuario.

    Args:
        longitud_maxima (int): El limite de caracteres que puede tener la palabra ingresada.
        reintentos (int): La cantidad de intentos que puede tener el usuario para ingresar datos invalidos, se ira decrementando hasta llegar
        a 0 y el usuario no podrea ingresar más datos.
        mensaje (str): Mensaje que indica que deve ingresar el usuraio dando contexto.
        mensaje_error (str): Mensaje que le saldra al usuario cuando el dato no sea valido pidiendo que lo vuelva a intantar.

    Returns:
        str|None: Se retornara el mmismo dato que ingreso el usuario si esté es menor o igual al limite de caracteres permitidos, 
        en caso contrario se retornara None.
    """
    print(mensaje)
    longitud = input("• ")
    longitud_str = longitud
    longitud = len(longitud)

    reintentos -= 2
    for reintentos in range(reintentos, -1, -1):
        if longitud < longitud_maxima:
            longitud = longitud_str
            return longitud
            break
        longitud = input(mensaje_error)
        longitud_str = longitud
        longitud = len(longitud)
        
    
    if longitud < longitud_maxima:
        longitud = longitud_str
        return longitud
    return None

x = get_string(5, 3, "• Ingresar palabra", "• Error, vuelva a intantar: ",)
print(x)