import sqlite3



class BaseDeDatos:
    url_base_de_datos = 'Listas_inteligentes.db'

    def _crear_conexion(self):
        try:
            self.conexion = sqlite3.connect(BaseDeDatos.url_base_de_datos)
        except Exception as e:
            print(e)

    def _cerrar_conexion(self):
        self.conexion.close()
        self.conexion = None

    def ejecutar_sql(self, sql):
        self._crear_conexion()
        cur = self.conexion.cursor()
        cur.execute(sql)

        filas = cur.fetchall()

        self.conexion.commit()
        self._cerrar_conexion()

        return filas

    def login_sql(self, sql):
        self._crear_conexion()
        cur = self.conexion.cursor()
        cur.execute(sql)

        fila = cur.fetchone()

        self.conexion.commit()
        self._cerrar_conexion()

        return fila

    def get_datos_sql(self, sql):
        self._crear_conexion()
        cur = self.conexion.cursor()
        cur.execute(sql)

        filas = cur.fetchone()

        self.conexion.commit()
        self._cerrar_conexion()
        for fila in filas:
            return fila

    def get_id_sql(self, sql):
        self._crear_conexion()
        cur = self.conexion.cursor()
        cur.execute(sql)

        filas = cur.fetchall()

        self.conexion.commit()
        self._cerrar_conexion()
        for fila in filas:
            return fila
