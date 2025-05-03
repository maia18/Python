# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'workerui.ui'
##
## Created by: Qt User Interface Compiler version 6.9.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QGridLayout, QHBoxLayout, QLabel,
    QPushButton, QSizePolicy, QWidget)

class Ui_myWidget(object):
    def setupUi(self, myWidget):
        if not myWidget.objectName():
            myWidget.setObjectName(u"myWidget")
        myWidget.resize(411, 300)
        font = QFont()
        font.setPointSize(30)
        myWidget.setFont(font)
        self.horizontalLayout = QHBoxLayout(myWidget)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.gridLayout_2 = QGridLayout()
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.label2 = QLabel(myWidget)
        self.label2.setObjectName(u"label2")

        self.gridLayout_2.addWidget(self.label2, 0, 1, 1, 1)

        self.label1 = QLabel(myWidget)
        self.label1.setObjectName(u"label1")

        self.gridLayout_2.addWidget(self.label1, 0, 0, 1, 1)

        self.Button1 = QPushButton(myWidget)
        self.Button1.setObjectName(u"Button1")

        self.gridLayout_2.addWidget(self.Button1, 1, 0, 1, 1)

        self.Button2 = QPushButton(myWidget)
        self.Button2.setObjectName(u"Button2")

        self.gridLayout_2.addWidget(self.Button2, 1, 1, 1, 1)


        self.horizontalLayout.addLayout(self.gridLayout_2)


        self.retranslateUi(myWidget)

        QMetaObject.connectSlotsByName(myWidget)
    # setupUi

    def retranslateUi(self, myWidget):
        myWidget.setWindowTitle(QCoreApplication.translate("myWidget", u"Form", None))
        self.label2.setText(QCoreApplication.translate("myWidget", u"L2", None))
        self.label1.setText(QCoreApplication.translate("myWidget", u"L1", None))
        self.Button1.setText(QCoreApplication.translate("myWidget", u"B1", None))
        self.Button2.setText(QCoreApplication.translate("myWidget", u"B2", None))
    # retranslateUi

