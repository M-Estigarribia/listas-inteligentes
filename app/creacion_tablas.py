import sqlite3

sql_tabla_usuario = '''
CREATE TABLE usuarios(
id_usuario integer PRIMARY KEY AUTOINCREMENT,
nombre_usuario text not null unique,
correo text not null unique,
passwd text not null
)
'''

sql_tabla_producto = '''
CREATE TABLE productos(
id_producto integer PRIMARY KEY AUTOINCREMENT,
nombre_producto text not null,
id_usuario integer,
FOREIGN KEY(id_usuario) REFERENCES usuario(id_usuario),
UNIQUE(nombre_producto, id_usuario)
)
'''

sql_tabla_precio = '''
CREATE TABLE precios(
id_precio integer PRIMARY KEY AUTOINCREMENT,
precio real,
fecha_registro text,
id_producto integer,
FOREIGN KEY(id_producto) REFERENCES producto(id_producto)
)
'''

sql_tabla_lista = '''
CREATE TABLE listas(
id_lista integer PRIMARY KEY AUTOINCREMENT,
nombre_lista text not null,
fecha_creada text, 
color text,
id_usuario integer,
FOREIGN KEY(id_usuario) REFERENCES usuario(id_usuario)
)
'''

sql_tabla_receta = '''
CREATE TABLE recetas(
id_receta integer PRIMARY KEY AUTOINCREMENT,
nombre_receta text not null,
fecha_creada text,
color text,
procedimiento text default ' ',
id_usuario integer,
FOREIGN KEY(id_usuario) REFERENCES usuario(id_usuario)
)
'''

sql_tabla_relacion_producto_receta = '''
CREATE TABLE relaciones_producto_receta(
id_receta integer,
id_producto integer,
cantidad real,
unidad text,
procedimiento text,
FOREIGN KEY(id_producto) REFERENCES producto(id_producto),
FOREIGN KEY(id_receta) REFERENCES receta(id_receta),
FOREIGN KEY(procedimiento) REFERENCES receta(procedimiento),
PRIMARY KEY (id_receta , id_producto, cantidad, unidad, procedimiento)
)
'''

sql_tabla_relacion_producto_lista = '''
CREATE TABLE relaciones_producto_lista(
id_lista integer,
id_producto integer,
cantidad real,
notas text,
FOREIGN KEY(id_lista) REFERENCES lista(id_lista),
FOREIGN KEY(id_producto) REFERENCES producto(id_producto),
PRIMARY KEY (id_lista , id_producto, notas)
)
'''

if __name__ == '__main__':
    try:
        print('Creando Base de datos')
        conexion = sqlite3.connect('Listas_inteligentes.db')

        print('Creando tablas')
        conexion.execute(sql_tabla_usuario)
        print('Tabla de usuarios creada!')
        conexion.execute(sql_tabla_precio)
        print('Tabla de precios creada!')
        conexion.execute(sql_tabla_producto)
        print('Tabla de productos creada!')
        conexion.execute(sql_tabla_lista)
        print('Tabla de listas creada!')
        conexion.execute(sql_tabla_receta)
        print('Tabla de recetas creada!')
        conexion.execute(sql_tabla_relacion_producto_lista)
        print('Tabla de productos relación listas creada!')
        conexion.execute(sql_tabla_relacion_producto_receta)
        print('Tabla de productos relación recetas creada!')

        conexion.close()

        print('Base de datos lista!')
    except Exception as e:
        print(f'Error creando base de datos: {e}', e)
