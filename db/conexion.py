import mysql.connector

class ConexionMysql:
    def __init__(self):
        self.host = 'localhost'
        self.user = 'root'
        self.password = '123'
        self.data_base = 'tienda'
        self.conexion = None
        self.cursor = None
    
    def connection(self):
        try:
            self.conexion = mysql.connector.connect(
                host=self.host,
                user=self.user,
                password=self.password,
                database=self.data_base,
                charset='utf8mb4',  # Establecer el charset
                collation='utf8mb4_general_ci' 
            )
            self.cursor = self.conexion.cursor()
            print(f"Conectado a {self.data_base}")
        except mysql.connector.Error as error:
            print(f"Error al conectar a la base de datos: {error}")
            self.conexion = None  # Para asegurar que la conexión se detecte como fallida
    
    
    def execute_query(self, query, values=None):
        if not self.conexion or not self.cursor:
            print("No hay conexión a la base de datos.", self.conexion, self.cursor)
            return None
        
        try:
            if values:
                self.cursor.execute(query, values)
            else:
                self.cursor.execute(query)
            
            result = self.cursor.fetchall()
            self.conexion.commit()
            return result
        except mysql.connector.Error as e:
            print(f"Error en la consulta: {e}")
            return None
    
    def close_connection(self):
        if self.cursor:
            self.cursor.close()
            print("conexion cerrada")
            
        if self.conexion:
            self.conexion.close()
            return f"{self.conexion} sea cerrado"