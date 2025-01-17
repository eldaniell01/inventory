from .conexion import ConexionMysql

class Query:
    def __init__(self) -> None:
        self.db = ConexionMysql()
        self.db.connection()
    
    def insertProveedor(self, nit, nombre):
        query = """
                    INSERT INTO proveedores(nit_dpi, nombre) VALUES(%s, %s)
                """
        values = (nit, nombre)
        self.db.execute_query(query, values)
        self.db.close_connection()