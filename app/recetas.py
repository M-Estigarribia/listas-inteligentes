from app.base_de_datos import BaseDeDatos
from datetime import datetime


bd = BaseDeDatos()


def crear_receta(nombre_receta, color, id_usuario):
    crear_receta_sql = f"""
    INSERT INTO recetas (nombre_receta, fecha_creada, color, id_usuario, procedimiento)
    VALUES ('{nombre_receta}', '{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}','{color}','{id_usuario}', ' ')
    """
    bd.ejecutar_sql(crear_receta_sql)
    return 1


def ingresar_datos_receta(id_receta, id_producto, cantidad, unidad):
    ingresar_datos_receta_sql=f"""
    INSERT INTO relaciones_producto_receta (id_receta, id_producto, cantidad, unidad)
    VALUES ('{id_receta}', '{id_producto}', '{cantidad}', '{unidad}')
    """
    try:
        bd.ejecutar_sql(ingresar_datos_receta_sql)
        return 1
    except:
        return 0


def get_id_receta_cre(id_usuario):
    get_id_receta_cre_sql=f"""
    SELECT id_receta FROM (SELECT * FROM recetas WHERE id_usuario = '{id_usuario}' ORDER BY fecha_creada DESC limit 1) 
    """
    get_id = bd.ejecutar_sql(get_id_receta_cre_sql)
    return get_id


def get_id_receta(id_usuario):
    get_id_receta_sql=f"""
    SELECT id_receta, fecha_creada FROM recetas WHERE id_usuario = '{id_usuario}' AND id_receta in (select id_receta from relaciones_producto_receta) ORDER BY fecha_creada DESC
"""
    id_recetas=bd.ejecutar_sql(get_id_receta_sql)
    return id_recetas


def mostrar_datos_receta(id_receta):
    mostrar_datos_receta_sql=f"""
    SELECT * FROM recetas WHERE id_receta = '{id_receta}' 
    """
    mostrar_datos = bd.ejecutar_sql(mostrar_datos_receta_sql)
    return mostrar_datos


def mostrar_receta_relacion(id_receta):
    mostrar_receta_relacion_sql = f"""
    SELECT p.nombre_producto, r.cantidad, r.unidad FROM relaciones_producto_receta as r INNER JOIN productos as p ON 
    r.id_producto = p.id_producto WHERE r.id_receta = '{id_receta}'
    """
    mostrar_receta_relacion = bd.ejecutar_sql(mostrar_receta_relacion_sql)
    return mostrar_receta_relacion


def mostrar_recetas(id_receta):
    mostrar_recetas_sql = f"""
    SELECT p.nombre_producto, r.cantidad, r.unidad, r.id_receta FROM relaciones_producto_receta as r INNER JOIN productos as p ON 
    r.id_producto = p.id_producto WHERE r.id_receta = '{id_receta}'
    """
    mostrar_recetas = bd.ejecutar_sql(mostrar_recetas_sql)
    return mostrar_recetas


def get_nombre_receta(id_receta):
    get_nombre_receta_sql=f"""
    SELECT nombre_receta, id_receta, color FROM recetas WHERE id_receta = '{id_receta}'
    """
    get_nombre_receta = bd.ejecutar_sql(get_nombre_receta_sql)

    return get_nombre_receta


def ingresar_procedimiento(id_receta, procedimiento):
    ingresar_procedimiento_sql=f"""
    UPDATE recetas SET procedimiento = '{procedimiento}' WHERE id_receta ='{id_receta}'
    """

    ingresar_proc = bd.ejecutar_sql(ingresar_procedimiento_sql)

    return ingresar_proc

def get_procedimiento(id_receta):
    get_procedimiento_sql = f"""
    SELECT id_receta, procedimiento FROM recetas WHERE id_receta = '{id_receta}'
    """

    get_proc = bd.ejecutar_sql(get_procedimiento_sql)
    return get_proc