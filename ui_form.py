# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'form.ui'
##
## Created by: Qt User Interface Compiler version 6.9.2
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
from PySide6.QtWidgets import (QApplication, QFrame, QHeaderView, QLabel,
    QMainWindow, QPlainTextEdit, QPushButton, QSizePolicy,
    QStackedWidget, QTableWidget, QTableWidgetItem, QWidget)
import rc_images

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1090, 789)
        MainWindow.setMinimumSize(QSize(1090, 789))
        MainWindow.setMaximumSize(QSize(1090, 789))
        icon = QIcon()
        icon.addFile(u":/new/prefix1/images/mountain.jpeg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        MainWindow.setWindowIcon(icon)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.centralwidget.setMaximumSize(QSize(1090, 789))
        self.stackedWidget = QStackedWidget(self.centralwidget)
        self.stackedWidget.setObjectName(u"stackedWidget")
        self.stackedWidget.setGeometry(QRect(0, 0, 1090, 789))
        self.stackedWidget.setMaximumSize(QSize(1090, 789))
        self.stackedWidget.setStyleSheet(u"")
        self.loginpage = QWidget()
        self.loginpage.setObjectName(u"loginpage")
        self.frame_2 = QFrame(self.loginpage)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setGeometry(QRect(0, 0, 1091, 791))
        self.frame_2.setStyleSheet(u"background-color:#111827;")
        self.frame_2.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Shadow.Raised)
        self.label = QLabel(self.frame_2)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(490, 40, 111, 91))
        self.label.setPixmap(QPixmap(u":/new/prefix1/images/financial-logo-finance-logo-vector-removebg-preview.png"))
        self.label.setScaledContents(True)
        self.label_2 = QLabel(self.frame_2)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(480, 120, 171, 51))
        self.label_2.setStyleSheet(u"font: 19pt \"Tahoma\";\n"
"background-color:none;\n"
"color:white;")
        self.label_2.setScaledContents(True)
        self.label_3 = QLabel(self.frame_2)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(440, 170, 271, 51))
        self.label_3.setStyleSheet(u"font: 12pt \"Tahoma\";\n"
"background-color:none;\n"
"color: rgb(112, 112, 112);")
        self.label_3.setScaledContents(True)
        self.username_field = QPlainTextEdit(self.frame_2)
        self.username_field.setObjectName(u"username_field")
        self.username_field.setGeometry(QRect(340, 320, 421, 51))
        self.username_field.setStyleSheet(u"  background-color: #2f3b4f; /* slightly lighter than #1f2937 */\n"
"  color: white;\n"
"  padding: 10px;\n"
"  border: none;\n"
"  border-radius: 5px;\n"
"  font-size: 16px;")
        self.password_field = QPlainTextEdit(self.frame_2)
        self.password_field.setObjectName(u"password_field")
        self.password_field.setGeometry(QRect(340, 450, 421, 51))
        self.password_field.setStyleSheet(u"  background-color: #2f3b4f; /* slightly lighter than #1f2937 */\n"
"  color: white;\n"
"  padding: 10px;\n"
"  border: none;\n"
"  border-radius: 5px;\n"
"  font-size: 16px;")
        self.label_4 = QLabel(self.frame_2)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setGeometry(QRect(340, 250, 181, 51))
        self.label_4.setStyleSheet(u"font: 12pt \"Tahoma\";\n"
"background-color:none;\n"
"color: white;")
        self.label_4.setScaledContents(True)
        self.label_5 = QLabel(self.frame_2)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setGeometry(QRect(340, 390, 181, 51))
        self.label_5.setStyleSheet(u"font: 12pt \"Tahoma\";\n"
"background-color:none;\n"
"color: white;")
        self.label_5.setScaledContents(True)
        self.label_6 = QLabel(self.frame_2)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setGeometry(QRect(340, 510, 181, 51))
        self.label_6.setStyleSheet(u"font: 11pt \"Tahoma\";\n"
"background-color:none;\n"
"color:rgb(12, 131, 222)")
        self.label_6.setScaledContents(True)
        self.login_button = QPushButton(self.frame_2)
        self.login_button.setObjectName(u"login_button")
        self.login_button.setGeometry(QRect(340, 590, 431, 61))
        self.login_button.setStyleSheet(u"background-color: #137fec;\n"
"font: 12pt \"Tahoma\";\n"
"color:white;\n"
"")
        self.stackedWidget.addWidget(self.loginpage)
        self.dashboard = QWidget()
        self.dashboard.setObjectName(u"dashboard")
        self.frame = QFrame(self.dashboard)
        self.frame.setObjectName(u"frame")
        self.frame.setGeometry(QRect(0, 0, 281, 791))
        self.frame.setStyleSheet(u"background-color:#ffffff;")
        self.frame.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame.setFrameShadow(QFrame.Shadow.Raised)
        self.label_7 = QLabel(self.frame)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setGeometry(QRect(100, 0, 141, 51))
        self.label_7.setStyleSheet(u"font: 700 12pt \"Arial\";\n"
"background-color:none;\n"
"color: black;")
        self.label_7.setScaledContents(True)
        self.label_10 = QLabel(self.frame)
        self.label_10.setObjectName(u"label_10")
        self.label_10.setGeometry(QRect(30, -10, 71, 71))
        self.label_10.setPixmap(QPixmap(u":/new/prefix1/images/the-greening-logo-is-symbolized-by-the-shape-of-a-combination-of-green-leaves-logo-turns-green-go-green-logo-vector-removebg-preview.png"))
        self.label_10.setScaledContents(True)
        self.login_button_2 = QPushButton(self.frame)
        self.login_button_2.setObjectName(u"login_button_2")
        self.login_button_2.setGeometry(QRect(10, 90, 261, 51))
        self.login_button_2.setStyleSheet(u"background-color: #1dbf73;\n"
"font: 12pt \"Tahoma\";\n"
"color:white;\n"
"border-radius: 14px;")
        self.expense = QPushButton(self.frame)
        self.expense.setObjectName(u"expense")
        self.expense.setGeometry(QRect(10, 160, 261, 51))
        self.expense.setStyleSheet(u"background-color: none;\n"
"font: 12pt \"Tahoma\";\n"
"color:black;\n"
"border-radius: 14px;")
        self.outsourced = QPushButton(self.frame)
        self.outsourced.setObjectName(u"outsourced")
        self.outsourced.setGeometry(QRect(0, 230, 281, 51))
        self.outsourced.setStyleSheet(u"background-color: none;\n"
"font:  12pt \"Arial\";\n"
"\n"
"color:black;\n"
"border-radius: 14px;")
        self.pendingpayments = QPushButton(self.frame)
        self.pendingpayments.setObjectName(u"pendingpayments")
        self.pendingpayments.setGeometry(QRect(-10, 310, 281, 51))
        self.pendingpayments.setStyleSheet(u"background-color: none;\n"
"font:  12pt \"Arial\";\n"
"\n"
"color:black;\n"
"border-radius: 14px;")
        self.frame_4 = QFrame(self.frame)
        self.frame_4.setObjectName(u"frame_4")
        self.frame_4.setGeometry(QRect(-10, 720, 291, 71))
        self.frame_4.setStyleSheet(u"background-color: white; \n"
"border: grey;")
        self.frame_4.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_4.setFrameShadow(QFrame.Shadow.Raised)
        self.label_8 = QLabel(self.frame_4)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setGeometry(QRect(40, 10, 51, 51))
        self.label_8.setStyleSheet(u"font: 700 12pt \"Arial\";\n"
"background-color:none;\n"
"color: black;")
        self.label_8.setPixmap(QPixmap(u":/new/prefix1/images/saad.png"))
        self.label_8.setScaledContents(True)
        self.user = QLabel(self.frame_4)
        self.user.setObjectName(u"user")
        self.user.setGeometry(QRect(100, 20, 141, 31))
        self.user.setStyleSheet(u"font:  800 12pt \"Arial\";\n"
"background-color:none;\n"
"color: black;")
        self.user.setScaledContents(True)
        self.frame_3 = QFrame(self.dashboard)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setGeometry(QRect(280, 0, 811, 71))
        self.frame_3.setStyleSheet(u"background-color:#ffffff;")
        self.frame_3.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Shadow.Raised)
        self.label_9 = QLabel(self.frame_3)
        self.label_9.setObjectName(u"label_9")
        self.label_9.setGeometry(QRect(30, 10, 141, 51))
        self.label_9.setStyleSheet(u"font:  800 12pt \"Arial\";\n"
"background-color:none;\n"
"color: black;")
        self.label_9.setScaledContents(True)
        self.insertincome = QPushButton(self.frame_3)
        self.insertincome.setObjectName(u"insertincome")
        self.insertincome.setGeometry(QRect(660, 20, 141, 41))
        self.insertincome.setStyleSheet(u"background-color: #1dbf73;\n"
"font: 10pt \"Tahoma\";\n"
"color:white;\n"
"border-radius: 9px;")
        self.invert_color = QPushButton(self.frame_3)
        self.invert_color.setObjectName(u"invert_color")
        self.invert_color.setGeometry(QRect(610, 20, 41, 41))
        self.invert_color.setStyleSheet(u"\n"
"font: 10pt \"Tahoma\";\n"
"color:white;\n"
"border-radius: 9px;")
        icon1 = QIcon()
        icon1.addFile(u":/new/prefix1/images/night-mode.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.invert_color.setIcon(icon1)
        self.frame_5 = QFrame(self.dashboard)
        self.frame_5.setObjectName(u"frame_5")
        self.frame_5.setGeometry(QRect(300, 90, 161, 141))
        self.frame_5.setStyleSheet(u"background-color: white; \n"
"border: grey;\n"
"border-radius:19px;")
        self.frame_5.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_5.setFrameShadow(QFrame.Shadow.Raised)
        self.label_11 = QLabel(self.frame_5)
        self.label_11.setObjectName(u"label_11")
        self.label_11.setGeometry(QRect(60, 0, 101, 51))
        self.label_11.setStyleSheet(u"font: 9pt \"Tahoma\";\n"
"background-color:none;\n"
"color: rgb(112, 112, 112);")
        self.label_11.setScaledContents(True)
        self.label_15 = QLabel(self.frame_5)
        self.label_15.setObjectName(u"label_15")
        self.label_15.setGeometry(QRect(40, 60, 111, 51))
        self.label_15.setStyleSheet(u"font: 700 12pt \"Arial\";\n"
"background-color:none;\n"
"color: black;")
        self.label_15.setScaledContents(True)
        self.frame_6 = QFrame(self.dashboard)
        self.frame_6.setObjectName(u"frame_6")
        self.frame_6.setGeometry(QRect(500, 90, 161, 141))
        self.frame_6.setStyleSheet(u"background-color: white; \n"
"border: grey;\n"
"border-radius:19px;")
        self.frame_6.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_6.setFrameShadow(QFrame.Shadow.Raised)
        self.label_12 = QLabel(self.frame_6)
        self.label_12.setObjectName(u"label_12")
        self.label_12.setGeometry(QRect(60, 0, 101, 51))
        self.label_12.setStyleSheet(u"font: 9pt \"Tahoma\";\n"
"background-color:none;\n"
"color: rgb(112, 112, 112);")
        self.label_12.setScaledContents(True)
        self.label_16 = QLabel(self.frame_6)
        self.label_16.setObjectName(u"label_16")
        self.label_16.setGeometry(QRect(50, 60, 111, 51))
        self.label_16.setStyleSheet(u"font: 700 12pt \"Arial\";\n"
"background-color:none;\n"
"color: black;")
        self.label_16.setScaledContents(True)
        self.frame_7 = QFrame(self.dashboard)
        self.frame_7.setObjectName(u"frame_7")
        self.frame_7.setGeometry(QRect(710, 90, 161, 141))
        self.frame_7.setStyleSheet(u"background-color: white; \n"
"border: grey;\n"
"border-radius:19px;")
        self.frame_7.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_7.setFrameShadow(QFrame.Shadow.Raised)
        self.label_13 = QLabel(self.frame_7)
        self.label_13.setObjectName(u"label_13")
        self.label_13.setGeometry(QRect(70, 0, 81, 51))
        self.label_13.setStyleSheet(u"font: 9pt \"Tahoma\";\n"
"background-color:none;\n"
"color: rgb(112, 112, 112);")
        self.label_13.setScaledContents(True)
        self.label_17 = QLabel(self.frame_7)
        self.label_17.setObjectName(u"label_17")
        self.label_17.setGeometry(QRect(80, 60, 71, 51))
        self.label_17.setStyleSheet(u"font: 700 12pt \"Arial\";\n"
"background-color:none;\n"
"color: black;")
        self.label_17.setScaledContents(True)
        self.frame_8 = QFrame(self.dashboard)
        self.frame_8.setObjectName(u"frame_8")
        self.frame_8.setGeometry(QRect(910, 90, 161, 141))
        self.frame_8.setStyleSheet(u"background-color: white; \n"
"border: grey;\n"
"border-radius:19px;")
        self.frame_8.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_8.setFrameShadow(QFrame.Shadow.Raised)
        self.label_14 = QLabel(self.frame_8)
        self.label_14.setObjectName(u"label_14")
        self.label_14.setGeometry(QRect(40, 0, 121, 51))
        self.label_14.setStyleSheet(u"font: 9pt \"Tahoma\";\n"
"background-color:none;\n"
"color: rgb(112, 112, 112);")
        self.label_14.setScaledContents(True)
        self.label_18 = QLabel(self.frame_8)
        self.label_18.setObjectName(u"label_18")
        self.label_18.setGeometry(QRect(50, 60, 111, 51))
        self.label_18.setStyleSheet(u"font: 700 12pt \"Arial\";\n"
"background-color:none;\n"
"color: black;")
        self.label_18.setScaledContents(True)
        self.frame_9 = QFrame(self.dashboard)
        self.frame_9.setObjectName(u"frame_9")
        self.frame_9.setGeometry(QRect(300, 250, 361, 241))
        self.frame_9.setStyleSheet(u"background-color: white; \n"
"border: grey;\n"
"border-radius:19px;")
        self.frame_9.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_9.setFrameShadow(QFrame.Shadow.Raised)
        self.frame_10 = QFrame(self.dashboard)
        self.frame_10.setObjectName(u"frame_10")
        self.frame_10.setGeometry(QRect(710, 250, 361, 241))
        self.frame_10.setStyleSheet(u"background-color: white; \n"
"border: grey;\n"
"border-radius:19px;")
        self.frame_10.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_10.setFrameShadow(QFrame.Shadow.Raised)
        self.frame_11 = QFrame(self.dashboard)
        self.frame_11.setObjectName(u"frame_11")
        self.frame_11.setGeometry(QRect(280, 70, 811, 721))
        self.frame_11.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_11.setFrameShadow(QFrame.Shadow.Raised)
        self.frame_12 = QFrame(self.frame_11)
        self.frame_12.setObjectName(u"frame_12")
        self.frame_12.setGeometry(QRect(20, 450, 771, 251))
        self.frame_12.setStyleSheet(u"background-color: white; \n"
"border: grey;\n"
"border-radius:19px;")
        self.frame_12.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_12.setFrameShadow(QFrame.Shadow.Raised)
        self.stackedWidget.addWidget(self.dashboard)
        self.frame_11.raise_()
        self.frame.raise_()
        self.frame_3.raise_()
        self.frame_5.raise_()
        self.frame_6.raise_()
        self.frame_7.raise_()
        self.frame_8.raise_()
        self.frame_9.raise_()
        self.frame_10.raise_()
        self.outsourcedpage = QWidget()
        self.outsourcedpage.setObjectName(u"outsourcedpage")
        self.label_31 = QLabel(self.outsourcedpage)
        self.label_31.setObjectName(u"label_31")
        self.label_31.setGeometry(QRect(100, 0, 141, 51))
        self.label_31.setStyleSheet(u"font: 700 12pt \"Arial\";\n"
"background-color:none;\n"
"color: black;")
        self.label_31.setScaledContents(True)
        self.expense_3 = QPushButton(self.outsourcedpage)
        self.expense_3.setObjectName(u"expense_3")
        self.expense_3.setGeometry(QRect(0, 160, 271, 51))
        self.expense_3.setStyleSheet(u"background-color: none;\n"
"font: 12pt \"Tahoma\";\n"
"color:black;\n"
"border-radius: 14px;")
        self.frame_21 = QFrame(self.outsourcedpage)
        self.frame_21.setObjectName(u"frame_21")
        self.frame_21.setGeometry(QRect(0, 0, 281, 721))
        self.frame_21.setStyleSheet(u"background-color:#ffffff;")
        self.frame_21.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_21.setFrameShadow(QFrame.Shadow.Raised)
        self.frame_22 = QFrame(self.outsourcedpage)
        self.frame_22.setObjectName(u"frame_22")
        self.frame_22.setGeometry(QRect(280, 0, 811, 71))
        self.frame_22.setStyleSheet(u"background-color:#ffffff;")
        self.frame_22.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_22.setFrameShadow(QFrame.Shadow.Raised)
        self.label_32 = QLabel(self.frame_22)
        self.label_32.setObjectName(u"label_32")
        self.label_32.setGeometry(QRect(60, 10, 231, 51))
        self.label_32.setStyleSheet(u"font:  800 12pt \"Arial\";\n"
"background-color:none;\n"
"color: black;")
        self.label_32.setScaledContents(True)
        self.invert_color_3 = QPushButton(self.frame_22)
        self.invert_color_3.setObjectName(u"invert_color_3")
        self.invert_color_3.setGeometry(QRect(720, 20, 41, 41))
        self.invert_color_3.setStyleSheet(u"\n"
"font: 10pt \"Tahoma\";\n"
"color:white;\n"
"border-radius: 9px;")
        self.invert_color_3.setIcon(icon1)
        self.frame_17 = QFrame(self.outsourcedpage)
        self.frame_17.setObjectName(u"frame_17")
        self.frame_17.setGeometry(QRect(280, 70, 811, 721))
        self.frame_17.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_17.setFrameShadow(QFrame.Shadow.Raised)
        self.label_33 = QLabel(self.frame_17)
        self.label_33.setObjectName(u"label_33")
        self.label_33.setGeometry(QRect(60, 30, 201, 51))
        self.label_33.setStyleSheet(u"font:  800 12pt \"Arial\";\n"
"background-color:none;\n"
"color: black;")
        self.label_33.setScaledContents(True)
        self.pendingpaymentstable_2 = QTableWidget(self.frame_17)
        if (self.pendingpaymentstable_2.columnCount() < 5):
            self.pendingpaymentstable_2.setColumnCount(5)
        font = QFont()
        font.setFamilies([u"Calibri"])
        font.setPointSize(16)
        font.setBold(True)
        __qtablewidgetitem = QTableWidgetItem()
        __qtablewidgetitem.setFont(font);
        self.pendingpaymentstable_2.setHorizontalHeaderItem(0, __qtablewidgetitem)
        font1 = QFont()
        font1.setBold(True)
        __qtablewidgetitem1 = QTableWidgetItem()
        __qtablewidgetitem1.setFont(font1);
        self.pendingpaymentstable_2.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        __qtablewidgetitem2.setFont(font);
        self.pendingpaymentstable_2.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        __qtablewidgetitem3 = QTableWidgetItem()
        __qtablewidgetitem3.setFont(font);
        self.pendingpaymentstable_2.setHorizontalHeaderItem(3, __qtablewidgetitem3)
        __qtablewidgetitem4 = QTableWidgetItem()
        __qtablewidgetitem4.setFont(font);
        self.pendingpaymentstable_2.setHorizontalHeaderItem(4, __qtablewidgetitem4)
        if (self.pendingpaymentstable_2.rowCount() < 1):
            self.pendingpaymentstable_2.setRowCount(1)
        __qtablewidgetitem5 = QTableWidgetItem()
        self.pendingpaymentstable_2.setItem(0, 0, __qtablewidgetitem5)
        __qtablewidgetitem6 = QTableWidgetItem()
        self.pendingpaymentstable_2.setItem(0, 2, __qtablewidgetitem6)
        __qtablewidgetitem7 = QTableWidgetItem()
        self.pendingpaymentstable_2.setItem(0, 3, __qtablewidgetitem7)
        __qtablewidgetitem8 = QTableWidgetItem()
        self.pendingpaymentstable_2.setItem(0, 4, __qtablewidgetitem8)
        self.pendingpaymentstable_2.setObjectName(u"pendingpaymentstable_2")
        self.pendingpaymentstable_2.setGeometry(QRect(50, 140, 711, 231))
        self.pendingpaymentstable_2.setStyleSheet(u"QTableWidget {\n"
"    border: none;  \n"
"    border-radius: 12px;\n"
"    background-color: #ffffff;\n"
"    gridline-color: #f0f0f0; /* soft row separators */\n"
"    selection-background-color: #e6f0ff; /* soft selection */\n"
"    selection-color: black;\n"
"    padding: 8px;\n"
"}\n"
"\n"
"/* Table headers */\n"
"QHeaderView::section {\n"
"    border: none;\n"
"    background-color: #ffffff;\n"
"    color: #666666;\n"
"    font-weight: 600;\n"
"    padding: 8px;\n"
"}\n"
"\n"
"/* Table rows */\n"
"QTableWidget::item {\n"
"    padding: 10px;\n"
"    border-bottom: 1px solid #f0f0f0; /* light separators */\n"
"}\n"
"\n"
"/* Optional hover effect */\n"
"QTableWidget::item:hover {\n"
"    background-color: #f9f9f9;\n"
"}\n"
"")
        self.insertincome_4 = QPushButton(self.frame_17)
        self.insertincome_4.setObjectName(u"insertincome_4")
        self.insertincome_4.setGeometry(QRect(560, 40, 201, 41))
        self.insertincome_4.setStyleSheet(u"background-color: #1dbf73;\n"
"font: 10pt \"Tahoma\";\n"
"color:white;\n"
"border-radius: 9px;")
        self.pendingpayments_3 = QPushButton(self.outsourcedpage)
        self.pendingpayments_3.setObjectName(u"pendingpayments_3")
        self.pendingpayments_3.setGeometry(QRect(0, 310, 281, 51))
        self.pendingpayments_3.setStyleSheet(u"background-color: #1dbf73;\n"
"font: 12pt \"Tahoma\";\n"
"color:white;\n"
"border-radius: 14px;")
        self.outsourced_4 = QPushButton(self.outsourcedpage)
        self.outsourced_4.setObjectName(u"outsourced_4")
        self.outsourced_4.setGeometry(QRect(0, 230, 271, 51))
        self.outsourced_4.setStyleSheet(u"background-color: none;\n"
"font:  12pt \"Arial\";\n"
"\n"
"color:black;\n"
"border-radius: 14px;")
        self.label_35 = QLabel(self.outsourcedpage)
        self.label_35.setObjectName(u"label_35")
        self.label_35.setGeometry(QRect(30, 0, 71, 71))
        self.label_35.setPixmap(QPixmap(u":/new/prefix1/images/the-greening-logo-is-symbolized-by-the-shape-of-a-combination-of-green-leaves-logo-turns-green-go-green-logo-vector-removebg-preview.png"))
        self.label_35.setScaledContents(True)
        self.frame_18 = QFrame(self.outsourcedpage)
        self.frame_18.setObjectName(u"frame_18")
        self.frame_18.setGeometry(QRect(0, 720, 281, 71))
        self.frame_18.setStyleSheet(u"background-color: white; \n"
"border: grey;")
        self.frame_18.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_18.setFrameShadow(QFrame.Shadow.Raised)
        self.label_24 = QLabel(self.frame_18)
        self.label_24.setObjectName(u"label_24")
        self.label_24.setGeometry(QRect(40, 10, 51, 51))
        self.label_24.setStyleSheet(u"font: 700 12pt \"Arial\";\n"
"background-color:none;\n"
"color: black;")
        self.label_24.setPixmap(QPixmap(u":/new/prefix1/images/saad.png"))
        self.label_24.setScaledContents(True)
        self.user_3 = QLabel(self.frame_18)
        self.user_3.setObjectName(u"user_3")
        self.user_3.setGeometry(QRect(100, 20, 141, 31))
        self.user_3.setStyleSheet(u"font:  800 12pt \"Arial\";\n"
"background-color:none;\n"
"color: black;")
        self.user_3.setScaledContents(True)
        self.login_button_4 = QPushButton(self.outsourcedpage)
        self.login_button_4.setObjectName(u"login_button_4")
        self.login_button_4.setGeometry(QRect(0, 90, 281, 51))
        self.login_button_4.setStyleSheet(u"background-color: none;\n"
"font:  12pt \"Arial\";\n"
"\n"
"color:black;\n"
"border-radius: 14px;")
        self.stackedWidget.addWidget(self.outsourcedpage)
        self.label_31.raise_()
        self.frame_21.raise_()
        self.frame_22.raise_()
        self.frame_17.raise_()
        self.pendingpayments_3.raise_()
        self.outsourced_4.raise_()
        self.label_35.raise_()
        self.frame_18.raise_()
        self.login_button_4.raise_()
        self.expense_3.raise_()
        self.Pendingpaymentspage = QWidget()
        self.Pendingpaymentspage.setObjectName(u"Pendingpaymentspage")
        self.outsourced_2 = QPushButton(self.Pendingpaymentspage)
        self.outsourced_2.setObjectName(u"outsourced_2")
        self.outsourced_2.setGeometry(QRect(0, 230, 271, 51))
        self.outsourced_2.setStyleSheet(u"background-color: none;\n"
"font:  12pt \"Arial\";\n"
"\n"
"color:black;\n"
"border-radius: 14px;")
        self.frame_15 = QFrame(self.Pendingpaymentspage)
        self.frame_15.setObjectName(u"frame_15")
        self.frame_15.setGeometry(QRect(280, 70, 811, 721))
        self.frame_15.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_15.setFrameShadow(QFrame.Shadow.Raised)
        self.label_29 = QLabel(self.frame_15)
        self.label_29.setObjectName(u"label_29")
        self.label_29.setGeometry(QRect(60, 10, 201, 51))
        self.label_29.setStyleSheet(u"font:  800 12pt \"Arial\";\n"
"background-color:none;\n"
"color: black;")
        self.label_29.setScaledContents(True)
        self.pendingpaymentstable = QTableWidget(self.frame_15)
        if (self.pendingpaymentstable.columnCount() < 4):
            self.pendingpaymentstable.setColumnCount(4)
        __qtablewidgetitem9 = QTableWidgetItem()
        __qtablewidgetitem9.setFont(font);
        self.pendingpaymentstable.setHorizontalHeaderItem(0, __qtablewidgetitem9)
        __qtablewidgetitem10 = QTableWidgetItem()
        __qtablewidgetitem10.setFont(font);
        self.pendingpaymentstable.setHorizontalHeaderItem(1, __qtablewidgetitem10)
        __qtablewidgetitem11 = QTableWidgetItem()
        __qtablewidgetitem11.setFont(font);
        self.pendingpaymentstable.setHorizontalHeaderItem(2, __qtablewidgetitem11)
        __qtablewidgetitem12 = QTableWidgetItem()
        __qtablewidgetitem12.setFont(font);
        self.pendingpaymentstable.setHorizontalHeaderItem(3, __qtablewidgetitem12)
        if (self.pendingpaymentstable.rowCount() < 1):
            self.pendingpaymentstable.setRowCount(1)
        __qtablewidgetitem13 = QTableWidgetItem()
        self.pendingpaymentstable.setItem(0, 0, __qtablewidgetitem13)
        __qtablewidgetitem14 = QTableWidgetItem()
        self.pendingpaymentstable.setItem(0, 1, __qtablewidgetitem14)
        __qtablewidgetitem15 = QTableWidgetItem()
        self.pendingpaymentstable.setItem(0, 2, __qtablewidgetitem15)
        __qtablewidgetitem16 = QTableWidgetItem()
        self.pendingpaymentstable.setItem(0, 3, __qtablewidgetitem16)
        self.pendingpaymentstable.setObjectName(u"pendingpaymentstable")
        self.pendingpaymentstable.setGeometry(QRect(60, 70, 671, 231))
        self.pendingpaymentstable.setStyleSheet(u"QTableWidget {\n"
"    border: none;  \n"
"    border-radius: 12px;\n"
"    background-color: #ffffff;\n"
"    gridline-color: #f0f0f0; /* soft row separators */\n"
"    selection-background-color: #e6f0ff; /* soft selection */\n"
"    selection-color: black;\n"
"    padding: 8px;\n"
"}\n"
"\n"
"/* Table headers */\n"
"QHeaderView::section {\n"
"    border: none;\n"
"    background-color: #ffffff;\n"
"    color: #666666;\n"
"    font-weight: 600;\n"
"    padding: 8px;\n"
"}\n"
"\n"
"/* Table rows */\n"
"QTableWidget::item {\n"
"    padding: 10px;\n"
"    border-bottom: 1px solid #f0f0f0; /* light separators */\n"
"}\n"
"\n"
"/* Optional hover effect */\n"
"QTableWidget::item:hover {\n"
"    background-color: #f9f9f9;\n"
"}\n"
"")
        self.label_30 = QLabel(self.frame_15)
        self.label_30.setObjectName(u"label_30")
        self.label_30.setGeometry(QRect(70, 320, 201, 51))
        self.label_30.setStyleSheet(u"font:  800 12pt \"Arial\";\n"
"background-color:none;\n"
"color: black;")
        self.label_30.setScaledContents(True)
        self.expectedpaymentstable = QTableWidget(self.frame_15)
        if (self.expectedpaymentstable.columnCount() < 3):
            self.expectedpaymentstable.setColumnCount(3)
        font2 = QFont()
        font2.setFamilies([u"Calibri"])
        font2.setPointSize(16)
        font2.setBold(False)
        __qtablewidgetitem17 = QTableWidgetItem()
        __qtablewidgetitem17.setFont(font2);
        self.expectedpaymentstable.setHorizontalHeaderItem(0, __qtablewidgetitem17)
        __qtablewidgetitem18 = QTableWidgetItem()
        __qtablewidgetitem18.setFont(font2);
        self.expectedpaymentstable.setHorizontalHeaderItem(1, __qtablewidgetitem18)
        __qtablewidgetitem19 = QTableWidgetItem()
        __qtablewidgetitem19.setFont(font2);
        self.expectedpaymentstable.setHorizontalHeaderItem(2, __qtablewidgetitem19)
        if (self.expectedpaymentstable.rowCount() < 1):
            self.expectedpaymentstable.setRowCount(1)
        __qtablewidgetitem20 = QTableWidgetItem()
        self.expectedpaymentstable.setItem(0, 1, __qtablewidgetitem20)
        __qtablewidgetitem21 = QTableWidgetItem()
        self.expectedpaymentstable.setItem(0, 2, __qtablewidgetitem21)
        self.expectedpaymentstable.setObjectName(u"expectedpaymentstable")
        self.expectedpaymentstable.setGeometry(QRect(70, 390, 671, 231))
        self.expectedpaymentstable.setStyleSheet(u"QTableWidget {\n"
"    border: none;\n"
"    border-radius: 12px;\n"
"    background-color: #ffffff;\n"
"    gridline-color: #f0f0f0;       /* soft separators */\n"
"    selection-background-color: #eaf3ff; /* light blue selection */\n"
"    selection-color: #1a1a1a;\n"
"    font-family: \"Segoe UI\", \"Helvetica Neue\", Arial, sans-serif;\n"
"    font-size: 14px;\n"
"    color: #333333;\n"
"    padding: 6px;\n"
"}\n"
"\n"
"/* Table headers */\n"
"QHeaderView::section {\n"
"    border: none;\n"
"    background-color: #fafafa;\n"
"    color: #444444;\n"
"    font-family: \"Segoe UI Semibold\", \"Helvetica Neue\", Arial, sans-serif;\n"
"    font-size: 13px;\n"
"    font-weight: 600;\n"
"    padding: 10px;\n"
"    border-bottom: 1px solid #e0e0e0;\n"
"}\n"
"\n"
"/* Table rows */\n"
"QTableWidget::item {\n"
"    padding: 12px;\n"
"    border-bottom: 1px solid #f0f0f0;\n"
"}\n"
"\n"
"/* Hover effect */\n"
"QTableWidget::item:hover {\n"
"    background-color: #f5faff;\n"
"    color: #000000;\n"
"}\n"
"\n"
"/* Altern"
                        "ate row color (striped effect) */\n"
"QTableWidget::item:alternate {\n"
"    background-color: #fcfcfc;\n"
"}\n"
"")
        self.insertincome_2 = QPushButton(self.frame_15)
        self.insertincome_2.setObjectName(u"insertincome_2")
        self.insertincome_2.setGeometry(QRect(530, 20, 201, 41))
        self.insertincome_2.setStyleSheet(u"background-color: #1dbf73;\n"
"font: 10pt \"Tahoma\";\n"
"color:white;\n"
"border-radius: 9px;")
        self.insertincome_3 = QPushButton(self.frame_15)
        self.insertincome_3.setObjectName(u"insertincome_3")
        self.insertincome_3.setGeometry(QRect(520, 340, 211, 41))
        self.insertincome_3.setStyleSheet(u"background-color: #1dbf73;\n"
"font: 10pt \"Tahoma\";\n"
"color:white;\n"
"border-radius: 9px;")
        self.frame_16 = QFrame(self.Pendingpaymentspage)
        self.frame_16.setObjectName(u"frame_16")
        self.frame_16.setGeometry(QRect(0, 720, 281, 71))
        self.frame_16.setStyleSheet(u"background-color: white; \n"
"border: grey;")
        self.frame_16.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_16.setFrameShadow(QFrame.Shadow.Raised)
        self.label_23 = QLabel(self.frame_16)
        self.label_23.setObjectName(u"label_23")
        self.label_23.setGeometry(QRect(40, 10, 51, 51))
        self.label_23.setStyleSheet(u"font: 700 12pt \"Arial\";\n"
"background-color:none;\n"
"color: black;")
        self.label_23.setPixmap(QPixmap(u":/new/prefix1/images/saad.png"))
        self.label_23.setScaledContents(True)
        self.user_2 = QLabel(self.frame_16)
        self.user_2.setObjectName(u"user_2")
        self.user_2.setGeometry(QRect(100, 20, 141, 31))
        self.user_2.setStyleSheet(u"font:  800 12pt \"Arial\";\n"
"background-color:none;\n"
"color: black;")
        self.user_2.setScaledContents(True)
        self.login_button_3 = QPushButton(self.Pendingpaymentspage)
        self.login_button_3.setObjectName(u"login_button_3")
        self.login_button_3.setGeometry(QRect(0, 90, 281, 51))
        self.login_button_3.setStyleSheet(u"background-color: none;\n"
"font:  12pt \"Arial\";\n"
"\n"
"color:black;\n"
"border-radius: 14px;")
        self.pendingpayments_2 = QPushButton(self.Pendingpaymentspage)
        self.pendingpayments_2.setObjectName(u"pendingpayments_2")
        self.pendingpayments_2.setGeometry(QRect(0, 310, 281, 51))
        self.pendingpayments_2.setStyleSheet(u"background-color: #1dbf73;\n"
"font: 12pt \"Tahoma\";\n"
"color:white;\n"
"border-radius: 14px;")
        self.label_26 = QLabel(self.Pendingpaymentspage)
        self.label_26.setObjectName(u"label_26")
        self.label_26.setGeometry(QRect(100, 0, 141, 51))
        self.label_26.setStyleSheet(u"font: 700 12pt \"Arial\";\n"
"background-color:none;\n"
"color: black;")
        self.label_26.setScaledContents(True)
        self.label_27 = QLabel(self.Pendingpaymentspage)
        self.label_27.setObjectName(u"label_27")
        self.label_27.setGeometry(QRect(30, -10, 71, 71))
        self.label_27.setPixmap(QPixmap(u":/new/prefix1/images/the-greening-logo-is-symbolized-by-the-shape-of-a-combination-of-green-leaves-logo-turns-green-go-green-logo-vector-removebg-preview.png"))
        self.label_27.setScaledContents(True)
        self.frame_19 = QFrame(self.Pendingpaymentspage)
        self.frame_19.setObjectName(u"frame_19")
        self.frame_19.setGeometry(QRect(280, 0, 811, 71))
        self.frame_19.setStyleSheet(u"background-color:#ffffff;")
        self.frame_19.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_19.setFrameShadow(QFrame.Shadow.Raised)
        self.label_28 = QLabel(self.frame_19)
        self.label_28.setObjectName(u"label_28")
        self.label_28.setGeometry(QRect(70, 10, 201, 51))
        self.label_28.setStyleSheet(u"font:  800 12pt \"Arial\";\n"
"background-color:none;\n"
"color: black;")
        self.label_28.setScaledContents(True)
        self.invert_color_2 = QPushButton(self.frame_19)
        self.invert_color_2.setObjectName(u"invert_color_2")
        self.invert_color_2.setGeometry(QRect(610, 20, 41, 41))
        self.invert_color_2.setStyleSheet(u"\n"
"font: 10pt \"Tahoma\";\n"
"color:white;\n"
"border-radius: 9px;")
        self.invert_color_2.setIcon(icon1)
        self.expense_2 = QPushButton(self.Pendingpaymentspage)
        self.expense_2.setObjectName(u"expense_2")
        self.expense_2.setGeometry(QRect(-10, 160, 281, 51))
        self.expense_2.setStyleSheet(u"background-color: none;\n"
"font: 12pt \"Tahoma\";\n"
"color:black;\n"
"border-radius: 14px;")
        self.frame_20 = QFrame(self.Pendingpaymentspage)
        self.frame_20.setObjectName(u"frame_20")
        self.frame_20.setGeometry(QRect(0, 0, 281, 721))
        self.frame_20.setStyleSheet(u"background-color:#ffffff;")
        self.frame_20.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_20.setFrameShadow(QFrame.Shadow.Raised)
        self.stackedWidget.addWidget(self.Pendingpaymentspage)
        self.frame_20.raise_()
        self.outsourced_2.raise_()
        self.frame_15.raise_()
        self.frame_16.raise_()
        self.login_button_3.raise_()
        self.pendingpayments_2.raise_()
        self.label_26.raise_()
        self.label_27.raise_()
        self.frame_19.raise_()
        self.expense_2.raise_()
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        self.stackedWidget.setCurrentIndex(3)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.label.setText("")
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"FIverrTrack", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"Track Your Fiverr Journey Here", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"Email", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"Password", None))
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"Forgot Password", None))
        self.login_button.setText(QCoreApplication.translate("MainWindow", u"Login", None))
        self.label_7.setText(QCoreApplication.translate("MainWindow", u"FiverrTrack", None))
        self.label_10.setText("")
        self.login_button_2.setText(QCoreApplication.translate("MainWindow", u"Dashboard", None))
        self.expense.setText(QCoreApplication.translate("MainWindow", u"Expenses", None))
        self.outsourced.setText(QCoreApplication.translate("MainWindow", u"   Outsourced ", None))
        self.pendingpayments.setText(QCoreApplication.translate("MainWindow", u"                Pending Payments", None))
        self.label_8.setText("")
        self.user.setText(QCoreApplication.translate("MainWindow", u"Welcome Saad", None))
        self.label_9.setText(QCoreApplication.translate("MainWindow", u"Dashboard", None))
        self.insertincome.setText(QCoreApplication.translate("MainWindow", u"+ Insert Income", None))
        self.invert_color.setText("")
        self.label_11.setText(QCoreApplication.translate("MainWindow", u"Total Balance", None))
        self.label_15.setText(QCoreApplication.translate("MainWindow", u"Rs 400700", None))
        self.label_12.setText(QCoreApplication.translate("MainWindow", u"Total Expenses", None))
        self.label_16.setText(QCoreApplication.translate("MainWindow", u"Rs 1000", None))
        self.label_13.setText(QCoreApplication.translate("MainWindow", u"Net Profit", None))
        self.label_17.setText(QCoreApplication.translate("MainWindow", u"4.6%", None))
        self.label_14.setText(QCoreApplication.translate("MainWindow", u"Pending Payments", None))
        self.label_18.setText(QCoreApplication.translate("MainWindow", u"Rs 34000", None))
        self.label_31.setText(QCoreApplication.translate("MainWindow", u"FiverrTrack", None))
        self.expense_3.setText(QCoreApplication.translate("MainWindow", u"Expenses", None))
        self.label_32.setText(QCoreApplication.translate("MainWindow", u"Outsourced Payments", None))
        self.invert_color_3.setText("")
        self.label_33.setText(QCoreApplication.translate("MainWindow", u"Project Information", None))
        ___qtablewidgetitem = self.pendingpaymentstable_2.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("MainWindow", u"Project Name", None));
        ___qtablewidgetitem1 = self.pendingpaymentstable_2.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("MainWindow", u"Outsourced To", None));
        ___qtablewidgetitem2 = self.pendingpaymentstable_2.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("MainWindow", u"Amount", None));
        ___qtablewidgetitem3 = self.pendingpaymentstable_2.horizontalHeaderItem(3)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("MainWindow", u"Due By", None));
        ___qtablewidgetitem4 = self.pendingpaymentstable_2.horizontalHeaderItem(4)
        ___qtablewidgetitem4.setText(QCoreApplication.translate("MainWindow", u"Status", None));

        __sortingEnabled = self.pendingpaymentstable_2.isSortingEnabled()
        self.pendingpaymentstable_2.setSortingEnabled(False)
        ___qtablewidgetitem5 = self.pendingpaymentstable_2.item(0, 0)
        ___qtablewidgetitem5.setText(QCoreApplication.translate("MainWindow", u"Adan Ayaz", None));
        ___qtablewidgetitem6 = self.pendingpaymentstable_2.item(0, 2)
        ___qtablewidgetitem6.setText(QCoreApplication.translate("MainWindow", u"14500", None));
        ___qtablewidgetitem7 = self.pendingpaymentstable_2.item(0, 3)
        ___qtablewidgetitem7.setText(QCoreApplication.translate("MainWindow", u"8-09-2025", None));
        ___qtablewidgetitem8 = self.pendingpaymentstable_2.item(0, 4)
        ___qtablewidgetitem8.setText(QCoreApplication.translate("MainWindow", u"Pending", None));
        self.pendingpaymentstable_2.setSortingEnabled(__sortingEnabled)

        self.insertincome_4.setText(QCoreApplication.translate("MainWindow", u"+ Insert New Project", None))
        self.pendingpayments_3.setText(QCoreApplication.translate("MainWindow", u"Payments", None))
        self.outsourced_4.setText(QCoreApplication.translate("MainWindow", u"   Outsourced ", None))
        self.label_35.setText("")
        self.label_24.setText("")
        self.user_3.setText(QCoreApplication.translate("MainWindow", u"Welcome Saad", None))
        self.login_button_4.setText(QCoreApplication.translate("MainWindow", u"Dashboard", None))
        self.outsourced_2.setText(QCoreApplication.translate("MainWindow", u"   Outsourced ", None))
        self.label_29.setText(QCoreApplication.translate("MainWindow", u"Pending Payments", None))
        ___qtablewidgetitem9 = self.pendingpaymentstable.horizontalHeaderItem(0)
        ___qtablewidgetitem9.setText(QCoreApplication.translate("MainWindow", u"Name", None));
        ___qtablewidgetitem10 = self.pendingpaymentstable.horizontalHeaderItem(1)
        ___qtablewidgetitem10.setText(QCoreApplication.translate("MainWindow", u"Amount", None));
        ___qtablewidgetitem11 = self.pendingpaymentstable.horizontalHeaderItem(2)
        ___qtablewidgetitem11.setText(QCoreApplication.translate("MainWindow", u"Due By", None));
        ___qtablewidgetitem12 = self.pendingpaymentstable.horizontalHeaderItem(3)
        ___qtablewidgetitem12.setText(QCoreApplication.translate("MainWindow", u"Status", None));

        __sortingEnabled1 = self.pendingpaymentstable.isSortingEnabled()
        self.pendingpaymentstable.setSortingEnabled(False)
        ___qtablewidgetitem13 = self.pendingpaymentstable.item(0, 0)
        ___qtablewidgetitem13.setText(QCoreApplication.translate("MainWindow", u"Adan Ayaz", None));
        ___qtablewidgetitem14 = self.pendingpaymentstable.item(0, 1)
        ___qtablewidgetitem14.setText(QCoreApplication.translate("MainWindow", u"14500", None));
        ___qtablewidgetitem15 = self.pendingpaymentstable.item(0, 2)
        ___qtablewidgetitem15.setText(QCoreApplication.translate("MainWindow", u"8-09-2025", None));
        ___qtablewidgetitem16 = self.pendingpaymentstable.item(0, 3)
        ___qtablewidgetitem16.setText(QCoreApplication.translate("MainWindow", u"Pending", None));
        self.pendingpaymentstable.setSortingEnabled(__sortingEnabled1)

        self.label_30.setText(QCoreApplication.translate("MainWindow", u"Expected Payments", None))
        ___qtablewidgetitem17 = self.expectedpaymentstable.horizontalHeaderItem(0)
        ___qtablewidgetitem17.setText(QCoreApplication.translate("MainWindow", u"Project", None));
        ___qtablewidgetitem18 = self.expectedpaymentstable.horizontalHeaderItem(1)
        ___qtablewidgetitem18.setText(QCoreApplication.translate("MainWindow", u"Due By", None));
        ___qtablewidgetitem19 = self.expectedpaymentstable.horizontalHeaderItem(2)
        ___qtablewidgetitem19.setText(QCoreApplication.translate("MainWindow", u"Status", None));

        __sortingEnabled2 = self.expectedpaymentstable.isSortingEnabled()
        self.expectedpaymentstable.setSortingEnabled(False)
        ___qtablewidgetitem20 = self.expectedpaymentstable.item(0, 1)
        ___qtablewidgetitem20.setText(QCoreApplication.translate("MainWindow", u"8-09-2025", None));
        ___qtablewidgetitem21 = self.expectedpaymentstable.item(0, 2)
        ___qtablewidgetitem21.setText(QCoreApplication.translate("MainWindow", u"Pending", None));
        self.expectedpaymentstable.setSortingEnabled(__sortingEnabled2)

        self.insertincome_2.setText(QCoreApplication.translate("MainWindow", u"+ Insert Pending Payment", None))
        self.insertincome_3.setText(QCoreApplication.translate("MainWindow", u"+ Insert Expected Payment", None))
        self.label_23.setText("")
        self.user_2.setText(QCoreApplication.translate("MainWindow", u"Welcome Saad", None))
        self.login_button_3.setText(QCoreApplication.translate("MainWindow", u"Dashboard", None))
        self.pendingpayments_2.setText(QCoreApplication.translate("MainWindow", u"Payments", None))
        self.label_26.setText(QCoreApplication.translate("MainWindow", u"FiverrTrack", None))
        self.label_27.setText("")
        self.label_28.setText(QCoreApplication.translate("MainWindow", u"Payments", None))
        self.invert_color_2.setText("")
        self.expense_2.setText(QCoreApplication.translate("MainWindow", u"Expenses", None))
    # retranslateUi

