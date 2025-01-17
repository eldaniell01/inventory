import sys
from views.home import Home
from PyQt6.QtWidgets import QApplication


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = Home()
    
    sys.exit(app.exec()) 