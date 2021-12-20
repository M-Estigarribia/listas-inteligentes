from app.base_de_datos import BaseDeDatos
from datetime import datetime


bd = BaseDeDatos()


def crear_lista(nombre_lista, color, id_usuario):
    crear_lista_sql = f"""
    INSERT INTO listas (nombre_lista, fecha_creada, color,  id_usuario)
    VALUES ('{nombre_lista}', '{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}', '{color}','{id_usuario}')
    """
    bd.ejecutar_sql(crear_lista_sql)
    return 1


def ingresar_datos_lista(id_lista, id_producto, cantidad, notas):
    ingresar_datos_lista_sql=f"""
    INSERT INTO relaciones_producto_lista (id_lista, id_producto, cantidad, notas)
    VALUES ('{id_lista}', '{id_producto}', '{cantidad}', '{notas}')
    """
    try:
        bd.ejecutar_sql(ingresar_datos_lista_sql)
        return 1
    except:
        return 0


def get_id_lista_cre(id_usuario):
    get_id_lista_cre_sql=f"""
    SELECT id_lista FROM (SELECT * FROM listas WHERE id_usuario = '{id_usuario}' ORDER BY fecha_creada DESC limit 1) 
    """
    get_id = bd.ejecutar_sql(get_id_lista_cre_sql)
    return get_id


def get_id_lista(id_usuario):
    get_id_lista_sql=f"""
    SELECT id_lista, fecha_creada FROM listas WHERE id_usuario = '{id_usuario}' AND id_lista in (select id_lista from relaciones_producto_lista) ORDER BY fecha_creada DESC
"""
    id_listas=bd.ejecutar_sql(get_id_lista_sql)
    return id_listas


def mostrar_datos_lista(id_lista):
    mostrar_datos_lista_sql=f"""
    SELECT * FROM listas WHERE id_lista = '{id_lista}' 
    """
    mostrar_datos = bd.ejecutar_sql(mostrar_datos_lista_sql)
    return mostrar_datos


def mostrar_lista_relacion(id_lista):
    mostrar_lista_relacion_sql = f"""
    SELECT p.nombre_producto, r.cantidad, r.notas FROM relaciones_producto_lista as r INNER JOIN productos as p ON 
    r.id_producto = p.id_producto WHERE r.id_lista = '{id_lista}'
    """
    mostrar_lista_relacion = bd.ejecutar_sql(mostrar_lista_relacion_sql)
    return mostrar_lista_relacion


def mostrar_listas(id_lista):
    mostrar_listas_sql = f"""
    SELECT p.nombre_producto, r.cantidad, r.notas, r.id_lista FROM relaciones_producto_lista as r INNER JOIN productos as p ON 
    r.id_producto = p.id_producto WHERE r.id_lista = '{id_lista}'
    """
    mostrar_listas = bd.ejecutar_sql(mostrar_listas_sql)
    return mostrar_listas


def get_nombre_lista(id_lista):
    get_nombre_lista_sql=f"""
    SELECT nombre_lista, id_lista, color FROM listas WHERE id_lista = '{id_lista}'
    """
    get_nombre_lista = bd.ejecutar_sql(get_nombre_lista_sql)

    return get_nombre_lista