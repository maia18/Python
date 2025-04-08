from PySide6.QtWidgets import QPushButton, QGridLayout

from variables import MEDIUM_FONT_SIZE
from util import isNumOrNot, isEmpty

class Button(QPushButton):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.configStyle()

    def configStyle(self):
        font = self.font()
        font.setPixelSize(MEDIUM_FONT_SIZE)
        self.setFont(font)
        self.setMinimumSize(75, 75)
        
class ButtonsGrid(QGridLayout):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        
        self._grid_mask = [
             ['C', '◀', '^', '/'],
             ['7', '8', '9', '*' ],
             ['4', '5', '6', '-' ],
             ['1', '2', '3', '+' ],
             ['',  '0', '.', '=' ],
         ]
        self._makeGrid()
        
    def _makeGrid(self):
        for row_number, row_data in enumerate(self._grid_mask):
            for column_number, button_text in enumerate(row_data):
                button = Button(button_text)
                
                if not isNumOrNot(button_text) and not isEmpty(button_text):
                    button.setProperty('cssClass', 'specialButton')
                    
                self.addWidget(button, row_number, column_number)