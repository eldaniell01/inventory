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
        
    def insertMarca(self, marca, proveedor):
        query = """
                    INSERT INTO marca(nombre, idproveedores) VALUES(%s, %s)
                """
        values = (marca, proveedor)
        self.db.execute_query(query, values)
        self.db.close_connection()
        
    def selectProveedor(self):
        query = """
                    SELECT idProveedores, nombre FROM proveedores ORDER BY idProveedores
                """
        result = self.db.execute_query(query)
        self.db.close_connection()
        return result