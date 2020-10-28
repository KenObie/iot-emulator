# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'emulator_gui.ui'
#
# Created by: PyQt5 UI code generator 5.12
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1121, 747)
        MainWindow.setMaximumSize(QtCore.QSize(16777215, 16777215))
        MainWindow.setStyleSheet("/*QGroupBox公用属性设置*/\n"
" QGroupBox {\n"
"     background: none;/*背景透明*/\n"
"     border: 1px solid #aaaaaa;/*边框*/\n"
"     border-radius: 5px;/*边框圆角*/\n"
"     margin-top: 2ex; /* 为title绘制留出空间，以下title子控制器的subcontrol-origin设置为margin */\n"
" }\n"
"\n"
"/*QGroupBox title子控制器属性设置*/\n"
"QGroupBox::title \n"
"{\n"
"    color:#3399ff;/*文本颜色*/\n"
"     left:10px;/*子控制器相对于父控件的精确定位*/\n"
"    subcontrol-origin: margin;/*子控制器绘制起始区域*/\n"
"    subcontrol-position: top left; /*子控制器于父控件的相对位置*/\n"
"    padding: 0px 2px;/*title文字左右padding设置使边框线条与title文字有间隔距离*/\n"
"    background: none;/*背景透明*/\n"
" }\n"
"QProgressBar {\n"
"    text-align: center;\n"
"    color: rgb(240, 240, 240);\n"
"    border-width: 1px; \n"
"    border-radius: 10px;\n"
"    border-color: rgb(230, 230, 230);\n"
"    border-style: solid;\n"
"    background-color:rgb(207,207,207);\n"
"}\n"
"QProgressBar::chunk {\n"
"    background-color: qlineargradient(spread:pad, x1:0.5, y1:1, x2:0.5, y2:0, stop:0 rgba(49, 147, 250, 255), stop:1 rgba(34, 142, 255, 255));\n"
"    border-radius: 10px;\n"
"}")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.groupBox = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox.setGeometry(QtCore.QRect(520, 10, 581, 251))
        self.groupBox.setObjectName("groupBox")
        self.bme280_temp_in_c = QtWidgets.QSlider(self.groupBox)
        self.bme280_temp_in_c.setGeometry(QtCore.QRect(40, 20, 22, 211))
        self.bme280_temp_in_c.setStyleSheet("QSlider::groove:vertical{\n"
"border: 1px solid #637EB8;\n"
"background: white;\n"
"width:7px;\n"
"height: 175px;\n"
"border-radius: 3px;\n"
"}\n"
"QSlider::add-page:vertical {\n"
"background: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"stop: 0 #ABC7EC, stop: 1 #154A98);\n"
"border: 1px solid #154A98;\n"
"width: 10px;\n"
"border-radius: 4px;\n"
"}\n"
"QSlider::sub-page:vertical {\n"
"background: #fff;\n"
"border: 1px solid #777;\n"
"width: 7px;\n"
"border-radius: 4px;\n"
"}\n"
"QSlider::handle:vertical{\n"
"background: qlineargradient(x1:0, y1:0, x2:1, y2:1,\n"
"stop:0 #fff, stop:1 #ABC7EC);\n"
"border: 1px solid #777;\n"
"height: 5px;\n"
"margin-left: -4px;\n"
"margin-right: -4px;\n"
"border-radius: 2px;\n"
"}\n"
"")
        self.bme280_temp_in_c.setMinimum(-20)
        self.bme280_temp_in_c.setMaximum(100)
        self.bme280_temp_in_c.setOrientation(QtCore.Qt.Vertical)
        self.bme280_temp_in_c.setTickPosition(QtWidgets.QSlider.TicksBothSides)
        self.bme280_temp_in_c.setObjectName("bme280_temp_in_c")
        self.bme280_humidity_pct = QtWidgets.QDial(self.groupBox)
        self.bme280_humidity_pct.setGeometry(QtCore.QRect(150, 60, 141, 111))
        self.bme280_humidity_pct.setWrapping(False)
        self.bme280_humidity_pct.setNotchesVisible(True)
        self.bme280_humidity_pct.setObjectName("bme280_humidity_pct")
        self.bme280_humidity_bar = QtWidgets.QProgressBar(self.groupBox)
        self.bme280_humidity_bar.setGeometry(QtCore.QRect(180, 170, 81, 23))
        font = QtGui.QFont()
        font.setUnderline(False)
        font.setStrikeOut(False)
        self.bme280_humidity_bar.setFont(font)
        self.bme280_humidity_bar.setFocusPolicy(QtCore.Qt.NoFocus)
        self.bme280_humidity_bar.setProperty("value", 0)
        self.bme280_humidity_bar.setObjectName("bme280_humidity_bar")
        self.bm280_humidity_lcd = QtWidgets.QLCDNumber(self.groupBox)
        self.bm280_humidity_lcd.setGeometry(QtCore.QRect(160, 90, 81, 41))
        self.bm280_humidity_lcd.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.bm280_humidity_lcd.setFrameShadow(QtWidgets.QFrame.Plain)
        self.bm280_humidity_lcd.setSegmentStyle(QtWidgets.QLCDNumber.Flat)
        self.bm280_humidity_lcd.setObjectName("bm280_humidity_lcd")
        self.bme280_pressure = QtWidgets.QDial(self.groupBox)
        self.bme280_pressure.setGeometry(QtCore.QRect(290, 60, 141, 111))
        self.bme280_pressure.setMinimum(900)
        self.bme280_pressure.setMaximum(1200)
        self.bme280_pressure.setWrapping(False)
        self.bme280_pressure.setNotchesVisible(True)
        self.bme280_pressure.setObjectName("bme280_pressure")
        self.bme280_sealevel = QtWidgets.QDial(self.groupBox)
        self.bme280_sealevel.setGeometry(QtCore.QRect(430, 60, 141, 111))
        self.bme280_sealevel.setMinimum(900)
        self.bme280_sealevel.setMaximum(1100)
        self.bme280_sealevel.setProperty("value", 900)
        self.bme280_sealevel.setWrapping(False)
        self.bme280_sealevel.setNotchesVisible(True)
        self.bme280_sealevel.setObjectName("bme280_sealevel")
        self.bme280_pressure_lcd = QtWidgets.QLCDNumber(self.groupBox)
        self.bme280_pressure_lcd.setGeometry(QtCore.QRect(320, 90, 71, 31))
        self.bme280_pressure_lcd.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.bme280_pressure_lcd.setFrameShadow(QtWidgets.QFrame.Raised)
        self.bme280_pressure_lcd.setSegmentStyle(QtWidgets.QLCDNumber.Flat)
        self.bme280_pressure_lcd.setObjectName("bme280_pressure_lcd")
        self.bme280_sealevel_lcd = QtWidgets.QLCDNumber(self.groupBox)
        self.bme280_sealevel_lcd.setGeometry(QtCore.QRect(440, 90, 81, 41))
        self.bme280_sealevel_lcd.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.bme280_sealevel_lcd.setFrameShadow(QtWidgets.QFrame.Raised)
        self.bme280_sealevel_lcd.setSegmentStyle(QtWidgets.QLCDNumber.Flat)
        self.bme280_sealevel_lcd.setObjectName("bme280_sealevel_lcd")
        self.bme280_pressure_bar = QtWidgets.QProgressBar(self.groupBox)
        self.bme280_pressure_bar.setGeometry(QtCore.QRect(320, 170, 81, 23))
        self.bme280_pressure_bar.setMinimum(900)
        self.bme280_pressure_bar.setMaximum(1200)
        self.bme280_pressure_bar.setProperty("value", 900)
        self.bme280_pressure_bar.setObjectName("bme280_pressure_bar")
        self.bme280_sealevel_bar = QtWidgets.QProgressBar(self.groupBox)
        self.bme280_sealevel_bar.setGeometry(QtCore.QRect(460, 170, 81, 23))
        self.bme280_sealevel_bar.setProperty("value", 0)
        self.bme280_sealevel_bar.setInvertedAppearance(False)
        self.bme280_sealevel_bar.setObjectName("bme280_sealevel_bar")
        self.bme2880_altitude_slider = QtWidgets.QSlider(self.groupBox)
        self.bme2880_altitude_slider.setGeometry(QtCore.QRect(110, 30, 22, 191))
        self.bme2880_altitude_slider.setStyleSheet("QSlider::groove:vertical{\n"
"border: 1px solid #637EB8;\n"
"background: white;\n"
"width:7px;\n"
"height: 175px;\n"
"border-radius: 3px;\n"
"}\n"
"QSlider::add-page:vertical {\n"
"background: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"stop: 0 #ABC7EC, stop: 1 #154A98);\n"
"border: 1px solid #154A98;\n"
"width: 10px;\n"
"border-radius: 4px;\n"
"}\n"
"QSlider::sub-page:vertical {\n"
"background: #fff;\n"
"border: 1px solid #777;\n"
"width: 7px;\n"
"border-radius: 4px;\n"
"}\n"
"QSlider::handle:vertical{\n"
"background: qlineargradient(x1:0, y1:0, x2:1, y2:1,\n"
"stop:0 #fff, stop:1 #ABC7EC);\n"
"border: 1px solid #777;\n"
"height: 5px;\n"
"margin-left: -4px;\n"
"margin-right: -4px;\n"
"border-radius: 2px;\n"
"}\n"
"")
        self.bme2880_altitude_slider.setMaximum(1500)
        self.bme2880_altitude_slider.setOrientation(QtCore.Qt.Vertical)
        self.bme2880_altitude_slider.setTickPosition(QtWidgets.QSlider.NoTicks)
        self.bme2880_altitude_slider.setObjectName("bme2880_altitude_slider")
        self.TCS_34725 = QtWidgets.QGroupBox(self.centralwidget)
        self.TCS_34725.setGeometry(QtCore.QRect(520, 270, 581, 231))
        self.TCS_34725.setStyleSheet("")
        self.TCS_34725.setObjectName("TCS_34725")
        self.color_red = QtWidgets.QSlider(self.TCS_34725)
        self.color_red.setGeometry(QtCore.QRect(40, 50, 341, 22))
        self.color_red.setCursor(QtGui.QCursor(QtCore.Qt.SizeHorCursor))
        self.color_red.setStyleSheet("QSlider::groove:horizontal {\n"
"border: 1px solid #bbb;\n"
"background: red;\n"
"height: 10px;\n"
"border-radius: 4px;\n"
"}\n"
"\n"
"QSlider::sub-page:horizontal {\n"
"border: 1px solid #777;\n"
"height: 10px;\n"
"border-radius: 4px;\n"
"}\n"
"\n"
"QSlider::add-page:horizontal {\n"
"background: #fff;\n"
"border: 1px solid #777;\n"
"height: 10px;\n"
"border-radius: 4px;\n"
"}\n"
"\n"
"QSlider::handle:horizontal {\n"
"background: qlineargradient(x1:0, y1:0, x2:1, y2:1,\n"
"    stop:0 #eee, stop:1 #ccc);\n"
"border: 1px solid #777;\n"
"width: 13px;\n"
"margin-top: -2px;\n"
"margin-bottom: -2px;\n"
"border-radius: 4px;\n"
"}\n"
"\n"
"QSlider::handle:horizontal:hover {\n"
"background: qlineargradient(x1:0, y1:0, x2:1, y2:1,\n"
"    stop:0 #fff, stop:1 #ddd);\n"
"border: 1px solid #444;\n"
"border-radius: 4px;\n"
"}")
        self.color_red.setMaximum(255)
        self.color_red.setOrientation(QtCore.Qt.Horizontal)
        self.color_red.setTickPosition(QtWidgets.QSlider.TicksBothSides)
        self.color_red.setObjectName("color_red")
        self.color_green = QtWidgets.QSlider(self.TCS_34725)
        self.color_green.setGeometry(QtCore.QRect(40, 90, 341, 22))
        self.color_green.setStyleSheet("QSlider::groove:horizontal {\n"
"border: 1px solid #bbb;\n"
"background: green;\n"
"height: 10px;\n"
"border-radius: 4px;\n"
"}\n"
"\n"
"QSlider::sub-page:horizontal {\n"
"border: 1px solid #777;\n"
"height: 10px;\n"
"border-radius: 4px;\n"
"}\n"
"\n"
"QSlider::add-page:horizontal {\n"
"background: #fff;\n"
"border: 1px solid #777;\n"
"height: 10px;\n"
"border-radius: 4px;\n"
"}\n"
"\n"
"QSlider::handle:horizontal {\n"
"background: qlineargradient(x1:0, y1:0, x2:1, y2:1,\n"
"    stop:0 #eee, stop:1 #ccc);\n"
"border: 1px solid #777;\n"
"width: 13px;\n"
"margin-top: -2px;\n"
"margin-bottom: -2px;\n"
"border-radius: 4px;\n"
"}\n"
"\n"
"QSlider::handle:horizontal:hover {\n"
"background: qlineargradient(x1:0, y1:0, x2:1, y2:1,\n"
"    stop:0 #fff, stop:1 #ddd);\n"
"border: 1px solid #444;\n"
"border-radius: 4px;\n"
"}")
        self.color_green.setMaximum(255)
        self.color_green.setOrientation(QtCore.Qt.Horizontal)
        self.color_green.setTickPosition(QtWidgets.QSlider.TicksBothSides)
        self.color_green.setObjectName("color_green")
        self.color_clear = QtWidgets.QSlider(self.TCS_34725)
        self.color_clear.setGeometry(QtCore.QRect(40, 190, 341, 22))
        self.color_clear.setStyleSheet("QSlider::groove:horizontal {\n"
"border: 1px solid #bbb;\n"
"background: white;\n"
"height: 10px;\n"
"border-radius: 4px;\n"
"}\n"
"\n"
"QSlider::sub-page:horizontal {\n"
"background: qlineargradient(x1: 0, y1: 0,    x2: 0, y2: 1,\n"
"    stop: 0 #66e, stop: 1 #bbf);\n"
"background: qlineargradient(x1: 0, y1: 0.2, x2: 1, y2: 1,\n"
"    stop: 0 #bbf, stop: 1 #55f);\n"
"border: 1px solid #777;\n"
"height: 10px;\n"
"border-radius: 4px;\n"
"}\n"
"\n"
"QSlider::add-page:horizontal {\n"
"background: #fff;\n"
"border: 1px solid #777;\n"
"height: 10px;\n"
"border-radius: 4px;\n"
"}\n"
"\n"
"QSlider::handle:horizontal {\n"
"background: qlineargradient(x1:0, y1:0, x2:1, y2:1,\n"
"    stop:0 #eee, stop:1 #ccc);\n"
"border: 1px solid #777;\n"
"width: 13px;\n"
"margin-top: -2px;\n"
"margin-bottom: -2px;\n"
"border-radius: 4px;\n"
"}\n"
"\n"
"QSlider::handle:horizontal:hover {\n"
"background: qlineargradient(x1:0, y1:0, x2:1, y2:1,\n"
"    stop:0 #fff, stop:1 #ddd);\n"
"border: 1px solid #444;\n"
"border-radius: 4px;\n"
"}")
        self.color_clear.setMaximum(255)
        self.color_clear.setOrientation(QtCore.Qt.Horizontal)
        self.color_clear.setTickPosition(QtWidgets.QSlider.TicksBothSides)
        self.color_clear.setObjectName("color_clear")
        self.color_blue = QtWidgets.QSlider(self.TCS_34725)
        self.color_blue.setGeometry(QtCore.QRect(40, 140, 341, 22))
        self.color_blue.setStyleSheet("QSlider::groove:horizontal {\n"
"border: 1px solid #bbb;\n"
"background: blue;\n"
"height: 10px;\n"
"border-radius: 4px;\n"
"}\n"
"\n"
"QSlider::sub-page:horizontal {\n"
"border: 1px solid #777;\n"
"height: 10px;\n"
"border-radius: 4px;\n"
"}\n"
"\n"
"QSlider::add-page:horizontal {\n"
"background: #fff;\n"
"border: 1px solid #777;\n"
"height: 10px;\n"
"border-radius: 4px;\n"
"}\n"
"\n"
"QSlider::handle:horizontal {\n"
"background: qlineargradient(x1:0, y1:0, x2:1, y2:1,\n"
"    stop:0 #eee, stop:1 #ccc);\n"
"border: 1px solid #777;\n"
"width: 13px;\n"
"margin-top: -2px;\n"
"margin-bottom: -2px;\n"
"border-radius: 4px;\n"
"}\n"
"\n"
"QSlider::handle:horizontal:hover {\n"
"background: qlineargradient(x1:0, y1:0, x2:1, y2:1,\n"
"    stop:0 #fff, stop:1 #ddd);\n"
"border: 1px solid #444;\n"
"border-radius: 4px;\n"
"}")
        self.color_blue.setMaximum(255)
        self.color_blue.setOrientation(QtCore.Qt.Horizontal)
        self.color_blue.setTickPosition(QtWidgets.QSlider.TicksBothSides)
        self.color_blue.setObjectName("color_blue")
        self.red_spinbox = QtWidgets.QSpinBox(self.TCS_34725)
        self.red_spinbox.setGeometry(QtCore.QRect(390, 50, 48, 24))
        self.red_spinbox.setMaximum(255)
        self.red_spinbox.setObjectName("red_spinbox")
        self.green_spinbox = QtWidgets.QSpinBox(self.TCS_34725)
        self.green_spinbox.setGeometry(QtCore.QRect(390, 90, 48, 24))
        self.green_spinbox.setMaximum(255)
        self.green_spinbox.setObjectName("green_spinbox")
        self.blue_spinbox = QtWidgets.QSpinBox(self.TCS_34725)
        self.blue_spinbox.setGeometry(QtCore.QRect(390, 140, 48, 24))
        self.blue_spinbox.setMaximum(255)
        self.blue_spinbox.setObjectName("blue_spinbox")
        self.clear_spinbox = QtWidgets.QSpinBox(self.TCS_34725)
        self.clear_spinbox.setGeometry(QtCore.QRect(390, 190, 48, 24))
        self.clear_spinbox.setMaximum(255)
        self.clear_spinbox.setObjectName("clear_spinbox")
        self.color_hue = QtWidgets.QLabel(self.TCS_34725)
        self.color_hue.setGeometry(QtCore.QRect(460, 60, 91, 91))
        self.color_hue.setAutoFillBackground(True)
        self.color_hue.setFrameShape(QtWidgets.QFrame.Box)
        self.color_hue.setText("")
        self.color_hue.setObjectName("color_hue")
        self.groupBox1 = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox1.setGeometry(QtCore.QRect(20, 10, 481, 291))
        self.groupBox1.setFocusPolicy(QtCore.Qt.NoFocus)
        self.groupBox1.setAcceptDrops(False)
        self.groupBox1.setAutoFillBackground(False)
        self.groupBox1.setFlat(False)
        self.groupBox1.setCheckable(False)
        self.groupBox1.setObjectName("groupBox1")
        self.am2302 = QtWidgets.QWidget(self.groupBox1)
        self.am2302.setGeometry(QtCore.QRect(0, 20, 481, 271))
        self.am2302.setContextMenuPolicy(QtCore.Qt.DefaultContextMenu)
        self.am2302.setAcceptDrops(False)
        self.am2302.setAutoFillBackground(False)
        self.am2302.setObjectName("am2302")
        self.am2302_temp_in_c = QtWidgets.QSlider(self.am2302)
        self.am2302_temp_in_c.setGeometry(QtCore.QRect(100, 30, 51, 221))
        self.am2302_temp_in_c.setStyleSheet("QSlider::groove:vertical{\n"
"border: 1px solid #637EB8;\n"
"background: white;\n"
"width:7px;\n"
"height: 175px;\n"
"border-radius: 3px;\n"
"}\n"
"QSlider::add-page:vertical {\n"
"background: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"stop: 0 #ABC7EC, stop: 1 #154A98);\n"
"border: 1px solid #154A98;\n"
"width: 10px;\n"
"border-radius: 4px;\n"
"}\n"
"QSlider::sub-page:vertical {\n"
"background: #fff;\n"
"border: 1px solid #777;\n"
"width: 7px;\n"
"border-radius: 4px;\n"
"}\n"
"QSlider::handle:vertical{\n"
"background: qlineargradient(x1:0, y1:0, x2:1, y2:1,\n"
"stop:0 #fff, stop:1 #ABC7EC);\n"
"border: 1px solid #777;\n"
"height: 5px;\n"
"margin-left: -4px;\n"
"margin-right: -4px;\n"
"border-radius: 2px;\n"
"}\n"
"")
        self.am2302_temp_in_c.setMinimum(-20)
        self.am2302_temp_in_c.setMaximum(100)
        self.am2302_temp_in_c.setOrientation(QtCore.Qt.Vertical)
        self.am2302_temp_in_c.setInvertedAppearance(False)
        self.am2302_temp_in_c.setTickPosition(QtWidgets.QSlider.TicksBothSides)
        self.am2302_temp_in_c.setObjectName("am2302_temp_in_c")
        self.am2302_temp_label = QtWidgets.QLCDNumber(self.am2302)
        self.am2302_temp_label.setGeometry(QtCore.QRect(20, 120, 71, 31))
        font = QtGui.QFont()
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        font.setKerning(True)
        self.am2302_temp_label.setFont(font)
        self.am2302_temp_label.setAcceptDrops(False)
        self.am2302_temp_label.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.am2302_temp_label.setLineWidth(5)
        self.am2302_temp_label.setSegmentStyle(QtWidgets.QLCDNumber.Flat)
        self.am2302_temp_label.setObjectName("am2302_temp_label")
        self.am2302_humidity_pct = QtWidgets.QDial(self.am2302)
        self.am2302_humidity_pct.setGeometry(QtCore.QRect(230, 70, 151, 141))
        self.am2302_humidity_pct.setTabletTracking(False)
        self.am2302_humidity_pct.setAcceptDrops(False)
        self.am2302_humidity_pct.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.am2302_humidity_pct.setMaximum(100)
        self.am2302_humidity_pct.setTracking(True)
        self.am2302_humidity_pct.setOrientation(QtCore.Qt.Horizontal)
        self.am2302_humidity_pct.setWrapping(False)
        self.am2302_humidity_pct.setNotchesVisible(True)
        self.am2302_humidity_pct.setObjectName("am2302_humidity_pct")
        self.progressBar = QtWidgets.QProgressBar(self.am2302)
        self.progressBar.setGeometry(QtCore.QRect(250, 210, 111, 23))
        self.progressBar.setProperty("value", 0)
        self.progressBar.setTextVisible(True)
        self.progressBar.setOrientation(QtCore.Qt.Horizontal)
        self.progressBar.setObjectName("progressBar")
        self.lcdNumber = QtWidgets.QLCDNumber(self.am2302)
        self.lcdNumber.setGeometry(QtCore.QRect(230, 120, 111, 31))
        self.lcdNumber.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.lcdNumber.setFrameShadow(QtWidgets.QFrame.Plain)
        self.lcdNumber.setLineWidth(5)
        self.lcdNumber.setSegmentStyle(QtWidgets.QLCDNumber.Flat)
        self.lcdNumber.setObjectName("lcdNumber")
        self.label_3 = QtWidgets.QLabel(self.am2302)
        self.label_3.setGeometry(QtCore.QRect(40, 158, 60, 16))
        self.label_3.setAlignment(QtCore.Qt.AlignCenter)
        self.label_3.setObjectName("label_3")
        self.pir_motion_detection = QtWidgets.QGroupBox(self.centralwidget)
        self.pir_motion_detection.setGeometry(QtCore.QRect(10, 550, 491, 141))
        self.pir_motion_detection.setObjectName("pir_motion_detection")
        self.pir_toggle_button = QtWidgets.QPushButton(self.pir_motion_detection)
        self.pir_toggle_button.setGeometry(QtCore.QRect(20, 50, 191, 61))
        self.pir_toggle_button.setStyleSheet("QPushButton{ background-color: gray; }\n"
"QPushButton:pressed{ background-color: red; }\n"
"")
        self.pir_toggle_button.setCheckable(True)
        self.pir_toggle_button.setFlat(False)
        self.pir_toggle_button.setObjectName("pir_toggle_button")
        self.pir_motion_label = QtWidgets.QLabel(self.pir_motion_detection)
        self.pir_motion_label.setGeometry(QtCore.QRect(230, 60, 141, 41))
        font = QtGui.QFont()
        font.setBold(False)
        font.setUnderline(False)
        font.setWeight(50)
        font.setStrikeOut(False)
        font.setKerning(True)
        self.pir_motion_label.setFont(font)
        self.pir_motion_label.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.pir_motion_label.setTextFormat(QtCore.Qt.AutoText)
        self.pir_motion_label.setAlignment(QtCore.Qt.AlignCenter)
        self.pir_motion_label.setTextInteractionFlags(QtCore.Qt.LinksAccessibleByMouse)
        self.pir_motion_label.setObjectName("pir_motion_label")
        self.led_board = QtWidgets.QGroupBox(self.centralwidget)
        self.led_board.setGeometry(QtCore.QRect(520, 520, 581, 171))
        self.led_board.setObjectName("led_board")
        self.led_green_icon = QtWidgets.QLabel(self.led_board)
        self.led_green_icon.setGeometry(QtCore.QRect(160, 50, 61, 51))
        self.led_green_icon.setText("")
        self.led_green_icon.setPixmap(QtGui.QPixmap("green_off.png"))
        self.led_green_icon.setScaledContents(True)
        self.led_green_icon.setObjectName("led_green_icon")
        self.led_red_icon = QtWidgets.QLabel(self.led_board)
        self.led_red_icon.setGeometry(QtCore.QRect(60, 50, 61, 51))
        self.led_red_icon.setText("")
        self.led_red_icon.setPixmap(QtGui.QPixmap("red_off2.png"))
        self.led_red_icon.setScaledContents(True)
        self.led_red_icon.setObjectName("led_red_icon")
        self.led_rblue_icon = QtWidgets.QLabel(self.led_board)
        self.led_rblue_icon.setGeometry(QtCore.QRect(270, 50, 61, 51))
        self.led_rblue_icon.setText("")
        self.led_rblue_icon.setPixmap(QtGui.QPixmap("blue_off.png"))
        self.led_rblue_icon.setScaledContents(True)
        self.led_rblue_icon.setObjectName("led_rblue_icon")
        self.led_yellow_icon = QtWidgets.QLabel(self.led_board)
        self.led_yellow_icon.setGeometry(QtCore.QRect(380, 50, 61, 51))
        self.led_yellow_icon.setText("")
        self.led_yellow_icon.setPixmap(QtGui.QPixmap("yellow_off.png"))
        self.led_yellow_icon.setScaledContents(True)
        self.led_yellow_icon.setObjectName("led_yellow_icon")
        self.led_white_icon = QtWidgets.QLabel(self.led_board)
        self.led_white_icon.setGeometry(QtCore.QRect(480, 50, 61, 51))
        self.led_white_icon.setText("")
        self.led_white_icon.setPixmap(QtGui.QPixmap("white_off.png"))
        self.led_white_icon.setScaledContents(True)
        self.led_white_icon.setObjectName("led_white_icon")
        self.led_red_button = QtWidgets.QPushButton(self.led_board)
        self.led_red_button.setGeometry(QtCore.QRect(40, 110, 90, 41))
        self.led_red_button.setCheckable(True)
        self.led_red_button.setObjectName("led_red_button")
        self.led_green_button = QtWidgets.QPushButton(self.led_board)
        self.led_green_button.setGeometry(QtCore.QRect(150, 110, 90, 41))
        self.led_green_button.setCheckable(True)
        self.led_green_button.setObjectName("led_green_button")
        self.led_blue_button = QtWidgets.QPushButton(self.led_board)
        self.led_blue_button.setGeometry(QtCore.QRect(260, 110, 90, 41))
        self.led_blue_button.setCheckable(True)
        self.led_blue_button.setChecked(False)
        self.led_blue_button.setObjectName("led_blue_button")
        self.led_yellow_button = QtWidgets.QPushButton(self.led_board)
        self.led_yellow_button.setGeometry(QtCore.QRect(370, 110, 90, 41))
        self.led_yellow_button.setCheckable(True)
        self.led_yellow_button.setObjectName("led_yellow_button")
        self.led_white_button = QtWidgets.QPushButton(self.led_board)
        self.led_white_button.setGeometry(QtCore.QRect(470, 110, 90, 41))
        self.led_white_button.setCheckable(True)
        self.led_white_button.setObjectName("led_white_button")
        self.cpu_utilization = QtWidgets.QGroupBox(self.centralwidget)
        self.cpu_utilization.setGeometry(QtCore.QRect(20, 310, 481, 241))
        self.cpu_utilization.setStyleSheet("")
        self.cpu_utilization.setObjectName("cpu_utilization")
        self.cpu_temp_slider = QtWidgets.QSlider(self.cpu_utilization)
        self.cpu_temp_slider.setGeometry(QtCore.QRect(50, 40, 22, 160))
        self.cpu_temp_slider.setOrientation(QtCore.Qt.Vertical)
        self.cpu_temp_slider.setObjectName("cpu_temp_slider")
        self.progressBar_2 = QtWidgets.QProgressBar(self.cpu_utilization)
        self.progressBar_2.setGeometry(QtCore.QRect(80, 40, 31, 161))
        self.progressBar_2.setStyleSheet("")
        self.progressBar_2.setProperty("value", 0)
        self.progressBar_2.setOrientation(QtCore.Qt.Vertical)
        self.progressBar_2.setObjectName("progressBar_2")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1121, 22))
        self.menubar.setObjectName("menubar")
        self.menuMenu = QtWidgets.QMenu(self.menubar)
        self.menuMenu.setObjectName("menuMenu")
        self.menuQuit = QtWidgets.QMenu(self.menuMenu)
        self.menuQuit.setObjectName("menuQuit")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.menuQuit.addSeparator()
        self.menuMenu.addAction(self.menuQuit.menuAction())
        self.menubar.addAction(self.menuMenu.menuAction())

        self.retranslateUi(MainWindow)
        self.am2302_temp_in_c.sliderMoved['int'].connect(self.am2302_temp_label.display)
        self.am2302_humidity_pct.sliderMoved['int'].connect(self.progressBar.setValue)
        self.am2302_humidity_pct.sliderMoved['int'].connect(self.lcdNumber.display)
        self.color_red.valueChanged['int'].connect(self.red_spinbox.setValue)
        self.color_green.valueChanged['int'].connect(self.green_spinbox.setValue)
        self.color_blue.valueChanged['int'].connect(self.blue_spinbox.setValue)
        self.color_clear.valueChanged['int'].connect(self.clear_spinbox.setValue)
        self.bme280_humidity_pct.valueChanged['int'].connect(self.bm280_humidity_lcd.display)
        self.bme280_pressure.valueChanged['int'].connect(self.bme280_pressure_lcd.display)
        self.bme280_sealevel.valueChanged['int'].connect(self.bme280_sealevel_lcd.display)
        self.bme280_humidity_pct.valueChanged['int'].connect(self.bme280_humidity_bar.setValue)
        self.bme280_pressure.valueChanged['int'].connect(self.bme280_pressure_bar.setValue)
        self.bme280_sealevel.valueChanged['int'].connect(self.bme280_sealevel_bar.setValue)
        self.cpu_temp_slider.valueChanged['int'].connect(self.progressBar_2.setValue)
        self.red_spinbox.valueChanged['int'].connect(self.color_red.setValue)
        self.green_spinbox.valueChanged['int'].connect(self.color_green.setValue)
        self.blue_spinbox.valueChanged['int'].connect(self.color_blue.setValue)
        self.clear_spinbox.valueChanged['int'].connect(self.color_clear.setValue)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.groupBox.setTitle(_translate("MainWindow", "BME280 - Digtial Temperature, Altitude, Sealevel Pressure, Humidity Percentage, and Pressure"))
        self.bme280_pressure_bar.setFormat(_translate("MainWindow", "%p"))
        self.bme280_sealevel_bar.setFormat(_translate("MainWindow", "%p"))
        self.TCS_34725.setTitle(_translate("MainWindow", "TCS_34725"))
        self.groupBox1.setTitle(_translate("MainWindow", "AM2302 - Analog Temperature and Humidity Percentage"))
        self.label_3.setText(_translate("MainWindow", "CELCIUS"))
        self.pir_motion_detection.setTitle(_translate("MainWindow", "Pir_Motion_Detection"))
        self.pir_toggle_button.setText(_translate("MainWindow", "Motion"))
        self.pir_motion_label.setText(_translate("MainWindow", "No Motion Detected"))
        self.led_board.setTitle(_translate("MainWindow", "LED Board"))
        self.led_red_button.setText(_translate("MainWindow", "OFF"))
        self.led_green_button.setText(_translate("MainWindow", "OFF"))
        self.led_blue_button.setText(_translate("MainWindow", "OFF"))
        self.led_yellow_button.setText(_translate("MainWindow", "OFF"))
        self.led_white_button.setText(_translate("MainWindow", "OFF"))
        self.cpu_utilization.setTitle(_translate("MainWindow", "CPU Utilization"))
        self.menuMenu.setTitle(_translate("MainWindow", "Menu"))
        self.menuQuit.setTitle(_translate("MainWindow", "Quit"))




if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
