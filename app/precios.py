from app.base_de_datos import BaseDeDatos
from datetime import datetime


bd = BaseDeDatos()


def get_id_precio(id_producto, fecha_registro):
    get_id_precio_sql = f"""
    SELECT id_precio FROM precios WHERE id_producto = '{id_producto}' AND fecha_registro = '{fecha_registro}'
    """
    validar = bd.get_datos_sql(get_id_precio_sql)
    return validar


def ingresar_precio(precio, id_producto):
    ingresar_precio_sql = f"""
    INSERT INTO precios (precio, fecha_registro, id_producto)
    VALUES ('{precio}', '{datetime.now().strftime('%Y-%m-%d %H:%M')}', '{id_producto}')
    """
    bd.ejecutar_sql(ingresar_precio_sql)
    return 1


def buscar_precio(id_producto):
    mostrar_precio_sql = f"""
    SELECT precio, id_producto, fecha_registro FROM precios where id_producto='{id_producto}'
    """
    resultados = bd.ejecutar_sql(mostrar_precio_sql)
    return resultados



