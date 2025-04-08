import sys

from display                 import Display
from buttons                 import ButtonsGrid
from info                    import Info
from main_window             import MainWindow
from style                   import setupTheme
from variables               import WINDOW_ICON_PATH

from PySide6.QtGui      import QIcon
from PySide6.QtWidgets  import QApplication

if __name__ == '__main__':
    # Cria a aplicação
    app = QApplication(sys.argv)
    setupTheme(app)
    window = MainWindow()

    # Define o ícone
    icon = QIcon(str(WINDOW_ICON_PATH))
    window.setWindowIcon(icon)
    app.setWindowIcon(icon)

    # Info
    info = Info('2.0 ^ 10.0 = 1024')
    window.addWidgetToVLayout(info)

    # Display
    display = Display()
    window.addWidgetToVLayout(display)
    
    # Grid
    buttonsGrid = ButtonsGrid()
    window.vLayout.addLayout(buttonsGrid)

    # Buttons
    # button1 = Button('0')
    # button2 = Button('1')
    # button3 = Button('2')
    # button4 = Button('3')

    # buttonsGrid.addWidget(button1, 0, 0)
    # buttonsGrid.addWidget(button2, 0, 1)
    # buttonsGrid.addWidget(button3, 0, 2)
    # buttonsGrid.addWidget(button4, 1, 0, 1, 3)

    # Executa tudo
    window.adjustFixedSize()
    window.show()
    app.exec()