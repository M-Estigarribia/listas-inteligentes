from app.base_de_datos import BaseDeDatos

bd = BaseDeDatos()


def crear_usuario(nombre_usuario,correo,passwd):
    crear_usuario_sql = f"""
        INSERT INTO usuarios (nombre_usuario,correo,passwd)
        VALUES ('{nombre_usuario}','{correo}','{passwd}')
"""
    bd.ejecutar_sql(crear_usuario_sql)
    return 1


def validar_registro(nombre_usuario, correo, passwd):
    validar_registro_sql= f"""
        SELECT * FROM usuarios WHERE nombre_usuario = '{nombre_usuario}' OR correo = '{correo}'
"""
    fila=bd.ejecutar_sql(validar_registro_sql)
    if not fila:
        crear_usuario(nombre_usuario, correo, passwd)
        return 2
    else:
        return 0


def validar_login(nombre_usuario,passwd):
    validar_login_sql = f"""
        SELECT passwd FROM usuarios WHERE nombre_usuario = '{nombre_usuario}'
"""
    validar=bd.login_sql(validar_login_sql)
    if not validar:
        return 0
    else:
        if passwd == validar[0] :
            return 1
        else:
            return 0


'''que verifique contraseña, ingrese correo, entonces verifico que la pass 
sea correcta y que el correo no exista en la base de datos'''


def cambiar_correo(nombre_usuario,passwd,correo):
    if validar_login(nombre_usuario,passwd) == 1:
        buscar_correo_sql=f"""
            SELECT * FROM usuarios WHERE correo='{correo}'
"""
        buscar_correo = bd.ejecutar_sql(buscar_correo_sql)
        if not buscar_correo:
            cambiar_correo_sql=f"""
            UPDATE usuarios SET correo ='{correo}' where nombre_usuario = '{nombre_usuario}'      
    """
            bd.ejecutar_sql(cambiar_correo_sql)
            return 1 #se realiza el cambio de correo
        else:
            return 2 #el correo ya existe
    else:
        return 0 #contraseña incorrecta


def cambiar_passwd(nombre_usuario,passwd,new_passwd):
    if validar_login(nombre_usuario,passwd) == 1:
        if new_passwd==passwd:
            return 2 #La contraseña nueva debe ser diferente a la antigua
        else:
            cambiar_passwd_sql=f"""
            UPDATE usuarios SET passwd ='{new_passwd}' where nombre_usuario = '{nombre_usuario}'      
        """
            bd.ejecutar_sql(cambiar_passwd_sql)
            return 1 #se realiza el cambio de passwd
    else:
        return 0 #contraseña incorrecta


def borrar_cuenta(id_usuario,nombre_usuario,passwd):
    if validar_login(nombre_usuario,passwd) == 1:
        #A partir de acá se definen todas las consultas a realizar
        def auxiliar_producto():
            auxiliar_producto_sql = f"""
            SELECT id_producto FROM productos WHERE id_usuario = '{id_usuario}'
            """
            return bd.ejecutar_sql(auxiliar_producto_sql)

        def auxiliar_receta(aux_producto):
            auxiliar_receta_sql = f"""
            SELECT id_receta FROM relaciones_producto_receta WHERE id_producto = '{aux_producto}'
            """
            return bd.ejecutar_sql(auxiliar_receta_sql)

        def auxiliar_lista(aux_producto):
            auxiliar_lista_sql = f"""
            SELECT id_lista FROM relaciones_producto_lista WHERE id_producto = '{aux_producto}'
            """
            return bd.ejecutar_sql(auxiliar_lista_sql)

        def borrar_productos(aux_producto):
            borrar_productos_sql = f"""
            DELETE FROM productos WHERE id_producto = '{aux_producto}'
            """
            return bd.ejecutar_sql(borrar_productos_sql)

        def borrar_precios(aux_producto):
            borrar_precios_sql = f"""
            DELETE FROM precios WHERE id_producto = '{aux_producto}'
            """
            bd.ejecutar_sql(borrar_precios_sql)

        def borrar_relaciones_listas(aux_lista):
            borrar_relaciones_listas_sql = f"""
            DELETE FROM relaciones_producto_lista WHERE id_lista = '{aux_lista}'
            """
            bd.ejecutar_sql(borrar_relaciones_listas_sql)

        def borrar_relaciones_recetas(aux_receta):
            borrar_relaciones_recetas_sql = f"""
            DELETE FROM relaciones_producto_receta WHERE id_receta = '{aux_receta}'
            """
            bd.ejecutar_sql(borrar_relaciones_recetas_sql)

        def borrar_listas(id_usuario):
            borrar_listas_sql = f"""
            DELETE FROM listas WHERE id_usuario = '{id_usuario}'
            """
            bd.ejecutar_sql(borrar_listas_sql)

        def borrar_recetas(id_usuario):
            borrar_recetas_sql = f"""
            DELETE FROM recetas WHERE id_usuario = '{id_usuario}'
            """
            bd.ejecutar_sql(borrar_recetas_sql)

        def borrar_usuario():
            borrar_usuario_sql = f"""
                DELETE FROM usuarios WHERE id_usuario = '{id_usuario}'
                """
            bd.ejecutar_sql(borrar_usuario_sql)

        # inicio de la definición

        filas_producto = auxiliar_producto()
        for aux_producto in filas_producto:
            print(aux_producto)
            borrar_precios(aux_producto[0])
            filas_receta=auxiliar_receta(aux_producto[0])
            filas_lista=auxiliar_lista(aux_producto[0])
            for aux_receta in filas_receta:
                borrar_relaciones_recetas(aux_receta[0])
                borrar_recetas(id_usuario)
            for aux_lista in filas_lista:
                borrar_relaciones_listas(aux_lista[0])
                borrar_listas(id_usuario)
            borrar_productos(aux_producto[0])
        borrar_usuario()
        return 1  # se borró la cuenta correctamente
    else:
        return 0  # error al borrar la cuenta


def get_correo(nombre_usuario):
    get_correo_sql = f"""
            SELECT correo FROM usuarios WHERE nombre_usuario = '{nombre_usuario}'
    """
    validar = bd.get_datos_sql(get_correo_sql)

    def censura(string):
        correo_dividido = string.split('@')

        pre_arroba = correo_dividido[0]
        post_arroba = correo_dividido[1]

        correo_censurado = pre_arroba[0] + pre_arroba[1] + pre_arroba[2] + '•••••' + '@' + post_arroba[0] + '•••••'
        return correo_censurado
    return censura(validar)


def get_id(nombre_usuario):
    get_id_sql = f"""
            SELECT id_usuario FROM usuarios WHERE nombre_usuario = '{nombre_usuario}'
    """
    validar = bd.get_id_sql(get_id_sql)
    return validar[0]