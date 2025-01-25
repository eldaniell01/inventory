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
        
    def insertProducto(self, cod, nombre, stock, preciov, medida, marca):
        query = """
                    INSER INTO productos(codigo, nombre, stock, precio_v, unidad_m, marca) VALUES(%s, %s, %s, %s, %s, %s)
                """
        values = (cod, nombre, stock, preciov, medida, marca)
        self.db.execute_query(query, values)
        self.db.close_connection()
        
    def insertDetailCompra(self, cantidad, idP, precioc, desc, subtotal, idEncabezado):
        query = """
                    INSERT INTO detalle_compra(cantidad, idproducto, precio_c, descuento, sub_total, idencabezado_factura) VALUES(%s, (SELECT idproducto FROM productos WHERE codigo=%s LIMIT 1), %s, %s, %s, %s)
                """
        values = (cantidad, idP, precioc, desc, subtotal, idEncabezado)
        self.db.execute_query(query, values)
        self.db.close_connection()
        
    def insertEncabezadoCompra(self, date, state, total, idT, idProveedor):
        query = """
                    INSERT INTO encabezado_factura(fecha, estado, total, idtienda, idproveedores) VALUES(%s, %s, %s, %s, %s)
                """
        values = (date, state, total, idT, idProveedor)
        self.db.execute_query(query, values)
        self.db.close_connection()
        
    def selectProveedor(self):
        query = """
                    SELECT idProveedores, nombre FROM proveedores ORDER BY idProveedores
                """
        result = self.db.execute_query(query)
        self.db.close_connection()
        return result