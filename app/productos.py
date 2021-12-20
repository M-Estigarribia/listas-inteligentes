from app.base_de_datos import BaseDeDatos
import sqlite3
bd = BaseDeDatos()


def get_id_producto(id_usuario, nombre_producto):
    get_id_producto_sql = f"""
    SELECT id_producto FROM productos WHERE id_usuario = '{id_usuario}' AND nombre_producto = '{nombre_producto}'
    """
    validar = bd.ejecutar_sql(get_id_producto_sql)
    return validar


def crear_producto(nombre_producto, id_usuario):
    crear_producto_sql = f"""
    INSERT INTO productos (nombre_producto, id_usuario)
    VALUES ('{nombre_producto}', '{id_usuario}')
    """
    bd.ejecutar_sql(crear_producto_sql)
    return 1



def validar_producto(nombre_producto, id_usuario):
    validar_producto_sql = f"""
    SELECT * FROM productos WHERE nombre_producto = '{nombre_producto}' AND id_usuario = '{id_usuario}'
    """
    fila = bd.ejecutar_sql(validar_producto_sql)
    if not fila:
        return 1
    else:
        return 0


def borrar_producto(nombre_producto, id_usuario):
    borrar_producto_sql = f"""
    DELETE FROM productos WHERE nombre_producto ='{nombre_producto}' AND id_usuario = '{id_usuario}'      
    """
    bd.ejecutar_sql(borrar_producto_sql)
    return 1


def buscar_producto(iduser, busqueda):
    busq = busqueda
    id = iduser
    conexion = sqlite3.connect('Listas_inteligentes.db')
    cur = conexion.cursor()
    cur.execute("SELECT nombre_producto, id_producto FROM productos WHERE id_usuario = ? AND nombre_producto LIKE ?", (id, '%'+busq+'%',))
    filas = cur.fetchall()
    return filas
