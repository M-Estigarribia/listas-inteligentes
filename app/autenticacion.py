import re
from app import usuario as plantilla_usuario
from app import productos as plantilla_productos
from app import precios as plantilla_precios
from app import listas as plantilla_listas
from app import recetas as plantilla_recetas

#regex para verificar mail en formato xxx@xxx.xxx
regex = r'[A-Za-z0-9._+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}'

'''
///////////////////////////////////////////
     autenticación funciones usuario
///////////////////////////////////////////
'''


def validar_correo(correo):
    var = re.fullmatch(regex,correo)
    return var


#creación de variable auxiliar para la función plantilla_usuario.validar_registro, para tomar los datos del return, ver notas.
def validar_registro(nombre_usuario,correo,passwd):
    var = plantilla_usuario.validar_registro(nombre_usuario,correo,passwd)
    return var


def validar_login(nombre_usuario,passwd):
    #creación de variable auxiliar para la función plantilla_usuario.validar_login, para tomar los datos del return, ver notas.
    var = plantilla_usuario.validar_login(nombre_usuario,passwd)
    return var


def cambiar_correo(nombre_usuario,passwd,correo):
    var = plantilla_usuario.cambiar_correo(nombre_usuario,passwd,correo)
    return var


def cambiar_passwd(nombre_usuario,passwd,new_passwd):
    var = plantilla_usuario.cambiar_passwd(nombre_usuario,passwd,new_passwd)
    return var


def borrar_cuenta(id_usuario,nombre_usuario,passwd):
    var = plantilla_usuario.borrar_cuenta(id_usuario,nombre_usuario,passwd)
    return var


def get_correo(nombre_usuario):
    var = plantilla_usuario.get_correo(nombre_usuario)
    return var


def get_id(nombre_usuario):
    var = plantilla_usuario.get_id(nombre_usuario)
    return var


'''
///////////////////////////////////////////
    autenticación funciones productos
///////////////////////////////////////////
'''


def crear_producto(nombre_producto, id_usuario):
    var = plantilla_productos.crear_producto(nombre_producto, id_usuario)
    return var


def get_id_producto(id_usuario, nombre_producto):
    var = plantilla_productos.get_id_producto(id_usuario, nombre_producto)
    return var


def ingresar_precio(precio, id_producto):
    var = plantilla_precios.ingresar_precio(precio, id_producto)
    return var


def get_id_precio(id_producto, fecha_registro):
    var = plantilla_precios.get_id_precio(id_producto, fecha_registro)
    return var


def buscar_producto(id, busqueda):
    var = plantilla_productos.buscar_producto(id, busqueda)
    return var


def buscar_precio(id_producto):
    var = plantilla_precios.buscar_precio(id_producto)
    return var


def validar_producto(nombre_producto, id_usuario):
    var = plantilla_productos.validar_producto(nombre_producto, id_usuario)
    return var


'''
///////////////////////////////////////////
      autenticación funciones listas
///////////////////////////////////////////
'''

def crear_lista(nombre_lista, color, id_usuario):
    var = plantilla_listas.crear_lista(nombre_lista, color, id_usuario)
    return var


def ingresar_datos_lista(id_lista, id_producto, cantidad, notas):
    var = plantilla_listas.ingresar_datos_lista(id_lista, id_producto, cantidad, notas)
    return var


def get_id_lista_cre(id_usuario):
    var = plantilla_listas.get_id_lista_cre(id_usuario)
    return var


def get_id_lista(id_usuario):
    var = plantilla_listas.get_id_lista(id_usuario)
    return var


def mostrar_datos_lista(id_lista):
    var = plantilla_listas.mostrar_datos_lista(id_lista)
    return var


def mostrar_lista_relacion(id_lista):
    var = plantilla_listas.mostrar_lista_relacion(id_lista)
    return var


def mostrar_listas(id_lista):
    var = plantilla_listas.mostrar_listas(id_lista)
    return var


def get_nombre_lista(id_lista):
    var = plantilla_listas.get_nombre_lista(id_lista)
    return var



'''
///////////////////////////////////////////
      autenticación funciones listas
///////////////////////////////////////////
'''


def crear_receta(nombre_receta, color, id_usuario):
    var = plantilla_recetas.crear_receta(nombre_receta, color, id_usuario)
    return var


def get_id_receta_cre(id_usuario):
    var = plantilla_recetas.get_id_receta_cre(id_usuario)
    return var


def get_id_receta(id_usuario):
    var = plantilla_recetas.get_id_receta(id_usuario)
    return var


def ingresar_datos_receta(id_receta, id_producto, cantidad, unidad):
    var = plantilla_recetas.ingresar_datos_receta(id_receta, id_producto, cantidad, unidad)
    return var


def mostrar_datos_receta(id_receta):
    var = plantilla_recetas.mostrar_datos_receta(id_receta)
    return var


def mostrar_receta_relacion(id_receta):
    var = plantilla_recetas.mostrar_receta_relacion(id_receta)
    return var


def mostrar_recetas(id_receta):
    var = plantilla_recetas.mostrar_recetas(id_receta)
    return var


def get_nombre_receta(id_receta):
    var = plantilla_recetas.get_nombre_receta(id_receta)
    return var


def ingresar_procedimiento(id_receta, procedimiento):
    var = plantilla_recetas.ingresar_procedimiento(id_receta, procedimiento)
    return var


def get_procedimiento(id_receta):
    var = plantilla_recetas.get_procedimiento(id_receta)
    return var

