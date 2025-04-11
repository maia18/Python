from PySide6.QtWidgets  import QLineEdit
from PySide6.QtCore     import Qt

from variables import BIG_FONT_SIZE, TEXT_MARGIN, MINIMUM_WIDTH

 # Configurando o display
class Display(QLineEdit):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.configStyle()

    # Configurando o estilo do display        
    def configStyle(self):
        margins = [TEXT_MARGIN for _ in range(4)]
        
        self.setStyleSheet(f'font-size: {BIG_FONT_SIZE}px;')
        
        self.setMinimumHeight(2 * BIG_FONT_SIZE)
        self.setMinimumWidth(MINIMUM_WIDTH)
        
        self.setAlignment(Qt.AlignmentFlag.AlignRight)
        self.setTextMargins(*margins)