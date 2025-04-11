import sys as s

from variables      import WINDOW_ICON_PATH
from main_window    import MainWindow
from buttons        import ButtonsGrid
from style          import setupTheme
from display        import Display
from info           import Info

from PySide6.QtGui      import QIcon
from PySide6.QtWidgets  import QApplication

if __name__ == '__main__':
    # Cria a aplicação
    app = QApplication(s.argv)
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
    buttonsGrid = ButtonsGrid(display)
    window.vLayout.addLayout(buttonsGrid)

    # Executa tudo
    window.adjustFixedSize()
    window.show()
    app.exec()