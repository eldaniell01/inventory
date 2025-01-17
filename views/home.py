from PyQt6 import uic
from PyQt6.QtWidgets import QApplication, QMainWindow, QWidget, QMessageBox, QFileDialog, QTableWidget, QHeaderView, QTableWidgetItem
from PyQt6.QtGui import QFont
from db.conexion import ConexionMysql
from db.querys import Query

class Home(QMainWindow):
    def __init__(self):
        super().__init__()
        self.main = uic.loadUi('views/home.ui')
        self.main.show()
        self.main.btnProveedor.clicked.connect(self.registerProveedor)
        self.main.btnClean.clicked.connect(self.cleanTables)
        self.showTProveedor()
        
    def showTProveedor(self):
        columns = ['NIT', 'PROVEEDOR']
        self.main.tProveedor.setFont(QFont("FiraCode Nerd Font", 12))
        self.main.tProveedor.setColumnCount(len(columns))
        for column, name in enumerate(columns):
            self.main.tProveedor.setHorizontalHeaderItem(column, QTableWidgetItem(name))
        self.main.tProveedor.horizontalHeader().setSectionResizeMode(QHeaderView.ResizeMode.Stretch)
        header_style = """
        QHeaderView::section {
            font-family: "FiraCode Nerd Font";
            font-size: 12pt;
            font-weight: bold;
            background-color: rgb(255, 255, 255);
        }
        QTableWidget{
            background-color: rgb(255, 255, 255);
        }
        """
        self.main.tProveedor.setStyleSheet(header_style)
        
    def registerProveedor(self):
        query = Query()
        self.nit = self.main.txtNIT.text()
        self.nombre = self.main.txtProveedor.text()
        if self.nit:
            message_box = QMessageBox(self)
            message_box.setWindowTitle("Confirmación")
            message_box.setText("¿Estás seguro de que deseas continuar?")
            message_box.setStandardButtons(QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No)
            message_box.setIcon(QMessageBox.Icon.Question)
            response = message_box.exec()
            if response == QMessageBox.StandardButton.Yes:
                query.insertProveedor(self.nit, self.nombre)
                row = self.main.tProveedor.rowCount()
                self.main.tProveedor.insertRow(row)
                self.main.tProveedor.setItem(row, 0, QTableWidgetItem(self.nit))
                self.main.tProveedor.setItem(row, 1, QTableWidgetItem(self.nombre))
                self.main.txtNIT.setText("")
                self.main.txtProveedor.setText("")
            
        
    def cleanTables(self):
        self.main.tProveedor.setRowCount(0)
        self.main.tMarca.setRowCount(0)