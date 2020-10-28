from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_LivingLabEmulator(object):
    def setupUi(self, LivingLabEmulator):
        LivingLabEmulator.setObjectName("LivingLabEmulator")
        LivingLabEmulator.resize(1121, 747)
        LivingLabEmulator.setMaximumSize(QtCore.QSize(16777215, 16777215))
        LivingLabEmulator.setAutoFillBackground(False)
        LivingLabEmulator.setStyleSheet("")
        LivingLabEmulator.setTabShape(QtWidgets.QTabWidget.Rounded)
        self.widget = QtWidgets.QWidget(LivingLabEmulator)
        self.widget.setStyleSheet("")
        self.widget.setObjectName("widget")
        self.groupBox = QtWidgets.QGroupBox(self.widget)
        self.groupBox.setGeometry(QtCore.QRect(470, 10, 631, 251))
        self.groupBox.setObjectName("groupBox")
        self.bme280_temp_in_c = QtWidgets.QSlider(self.groupBox)
        self.bme280_temp_in_c.setGeometry(QtCore.QRect(60, 50, 22, 181))
        self.bme280_temp_in_c.setStyleSheet("")
        self.bme280_temp_in_c.setMinimum(-20)
        self.bme280_temp_in_c.setMaximum(100)
        self.bme280_temp_in_c.setOrientation(QtCore.Qt.Vertical)
        self.bme280_temp_in_c.setTickPosition(QtWidgets.QSlider.TicksBothSides)
        self.bme280_temp_in_c.setObjectName("bme280_temp_in_c")
        self.bme280_humidity_pct = QtWidgets.QDial(self.groupBox)
        self.bme280_humidity_pct.setGeometry(QtCore.QRect(220, 60, 120, 120))
        self.bme280_humidity_pct.setMaximum(100)
        self.bme280_humidity_pct.setWrapping(False)
        self.bme280_humidity_pct.setNotchTarget(1.7)
        self.bme280_humidity_pct.setNotchesVisible(True)
        self.bme280_humidity_pct.setObjectName("bme280_humidity_pct")
        self.bm280_humidity_lcd = QtWidgets.QLCDNumber(self.groupBox)
        self.bm280_humidity_lcd.setGeometry(QtCore.QRect(210, 180, 81, 41))
        self.bm280_humidity_lcd.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.bm280_humidity_lcd.setFrameShadow(QtWidgets.QFrame.Plain)
        self.bm280_humidity_lcd.setSegmentStyle(QtWidgets.QLCDNumber.Flat)
        self.bm280_humidity_lcd.setObjectName("bm280_humidity_lcd")
        self.bme280_pressure = QtWidgets.QDial(self.groupBox)
        self.bme280_pressure.setGeometry(QtCore.QRect(360, 60, 120, 120))
        self.bme280_pressure.setMinimum(900)
        self.bme280_pressure.setMaximum(1200)
        self.bme280_pressure.setOrientation(QtCore.Qt.Horizontal)
        self.bme280_pressure.setWrapping(False)
        self.bme280_pressure.setNotchTarget(5.699999999999999)
        self.bme280_pressure.setNotchesVisible(True)
        self.bme280_pressure.setObjectName("bme280_pressure")
        self.bme280_sealevel = QtWidgets.QDial(self.groupBox)
        self.bme280_sealevel.setGeometry(QtCore.QRect(500, 60, 120, 120))
        self.bme280_sealevel.setMinimum(900)
        self.bme280_sealevel.setMaximum(1100)
        self.bme280_sealevel.setProperty("value", 900)
        self.bme280_sealevel.setWrapping(False)
        self.bme280_sealevel.setNotchesVisible(True)
        self.bme280_sealevel.setObjectName("bme280_sealevel")
        self.bme280_pressure_lcd = QtWidgets.QLCDNumber(self.groupBox)
        self.bme280_pressure_lcd.setGeometry(QtCore.QRect(370, 180, 81, 41))
        self.bme280_pressure_lcd.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.bme280_pressure_lcd.setFrameShadow(QtWidgets.QFrame.Raised)
        self.bme280_pressure_lcd.setSegmentStyle(QtWidgets.QLCDNumber.Flat)
        self.bme280_pressure_lcd.setObjectName("bme280_pressure_lcd")
        self.bme280_sealevel_lcd = QtWidgets.QLCDNumber(self.groupBox)
        self.bme280_sealevel_lcd.setGeometry(QtCore.QRect(510, 180, 81, 41))
        self.bme280_sealevel_lcd.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.bme280_sealevel_lcd.setFrameShadow(QtWidgets.QFrame.Raised)
        self.bme280_sealevel_lcd.setSegmentStyle(QtWidgets.QLCDNumber.Flat)
        self.bme280_sealevel_lcd.setObjectName("bme280_sealevel_lcd")
        self.bme280_altitude_slider = QtWidgets.QSlider(self.groupBox)
        self.bme280_altitude_slider.setGeometry(QtCore.QRect(160, 50, 22, 181))
        self.bme280_altitude_slider.setStyleSheet("")
        self.bme280_altitude_slider.setMaximum(1500)
        self.bme280_altitude_slider.setOrientation(QtCore.Qt.Vertical)
        self.bme280_altitude_slider.setTickPosition(QtWidgets.QSlider.TicksBothSides)
        self.bme280_altitude_slider.setTickInterval(150)
        self.bme280_altitude_slider.setObjectName("bme280_altitude_slider")
        self.label_2 = QtWidgets.QLabel(self.groupBox)
        self.label_2.setGeometry(QtCore.QRect(290, 190, 60, 16))
        font = QtGui.QFont()
        font.setPointSize(22)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.bme280_temp_lcd = QtWidgets.QLCDNumber(self.groupBox)
        self.bme280_temp_lcd.setGeometry(QtCore.QRect(-40, 120, 81, 41))
        self.bme280_temp_lcd.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.bme280_temp_lcd.setFrameShadow(QtWidgets.QFrame.Plain)
        self.bme280_temp_lcd.setSegmentStyle(QtWidgets.QLCDNumber.Flat)
        self.bme280_temp_lcd.setObjectName("bme280_temp_lcd")
        self.bme280_altitude_lcd = QtWidgets.QLCDNumber(self.groupBox)
        self.bme280_altitude_lcd.setGeometry(QtCore.QRect(70, 120, 81, 41))
        self.bme280_altitude_lcd.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.bme280_altitude_lcd.setFrameShadow(QtWidgets.QFrame.Plain)
        self.bme280_altitude_lcd.setSegmentStyle(QtWidgets.QLCDNumber.Flat)
        self.bme280_altitude_lcd.setObjectName("bme280_altitude_lcd")
        self.label_5 = QtWidgets.QLabel(self.groupBox)
        self.label_5.setGeometry(QtCore.QRect(38, 120, 60, 16))
        self.label_5.setObjectName("label_5")
        self.label_6 = QtWidgets.QLabel(self.groupBox)
        self.label_6.setGeometry(QtCore.QRect(150, 120, 60, 16))
        self.label_6.setObjectName("label_6")
        self.label_9 = QtWidgets.QLabel(self.groupBox)
        self.label_9.setGeometry(QtCore.QRect(30, 30, 91, 16))
        self.label_9.setObjectName("label_9")
        self.label_11 = QtWidgets.QLabel(self.groupBox)
        self.label_11.setGeometry(QtCore.QRect(150, 30, 60, 16))
        self.label_11.setObjectName("label_11")
        self.label_12 = QtWidgets.QLabel(self.groupBox)
        self.label_12.setGeometry(QtCore.QRect(250, 30, 60, 16))
        self.label_12.setObjectName("label_12")
        self.label_13 = QtWidgets.QLabel(self.groupBox)
        self.label_13.setGeometry(QtCore.QRect(390, 30, 60, 16))
        self.label_13.setObjectName("label_13")
        self.label_14 = QtWidgets.QLabel(self.groupBox)
        self.label_14.setGeometry(QtCore.QRect(500, 30, 121, 16))
        self.label_14.setObjectName("label_14")
        self.TCS_34725 = QtWidgets.QGroupBox(self.widget)
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
        self.color_green.setCursor(QtGui.QCursor(QtCore.Qt.SizeHorCursor))
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
        self.color_clear.setCursor(QtGui.QCursor(QtCore.Qt.SizeHorCursor))
        self.color_clear.setStyleSheet("QSlider::groove:horizontal {\n"
"border: 1px solid #bbb;\n"
"background: white;\n"
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
        self.color_clear.setMaximum(255)
        self.color_clear.setOrientation(QtCore.Qt.Horizontal)
        self.color_clear.setTickPosition(QtWidgets.QSlider.TicksBothSides)
        self.color_clear.setObjectName("color_clear")
        self.color_blue = QtWidgets.QSlider(self.TCS_34725)
        self.color_blue.setGeometry(QtCore.QRect(40, 140, 341, 22))
        self.color_blue.setCursor(QtGui.QCursor(QtCore.Qt.SizeHorCursor))
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
        self.color_hue.setGeometry(QtCore.QRect(460, 50, 91, 91))
        self.color_hue.setAutoFillBackground(True)
        self.color_hue.setFrameShape(QtWidgets.QFrame.Box)
        self.color_hue.setText("")
        self.color_hue.setObjectName("color_hue")
        self.label_red = QtWidgets.QLabel(self.TCS_34725)
        self.label_red.setGeometry(QtCore.QRect(20, 52, 21, 16))
        self.label_red.setTextFormat(QtCore.Qt.AutoText)
        self.label_red.setObjectName("label_red")
        self.label_green = QtWidgets.QLabel(self.TCS_34725)
        self.label_green.setGeometry(QtCore.QRect(20, 92, 21, 16))
        self.label_green.setObjectName("label_green")
        self.label_blue = QtWidgets.QLabel(self.TCS_34725)
        self.label_blue.setGeometry(QtCore.QRect(20, 142, 16, 16))
        self.label_blue.setObjectName("label_blue")
        self.label_10 = QtWidgets.QLabel(self.TCS_34725)
        self.label_10.setGeometry(QtCore.QRect(5, 192, 31, 16))
        self.label_10.setObjectName("label_10")
        self.color_temp = QtWidgets.QLabel(self.TCS_34725)
        self.color_temp.setGeometry(QtCore.QRect(460, 150, 81, 16))
        self.color_temp.setObjectName("color_temp")
        self.color_lux = QtWidgets.QLabel(self.TCS_34725)
        self.color_lux.setGeometry(QtCore.QRect(473, 170, 31, 16))
        self.color_lux.setObjectName("color_lux")
        self.color_kelvin = QtWidgets.QLabel(self.TCS_34725)
        self.color_kelvin.setGeometry(QtCore.QRect(500, 150, 61, 16))
        self.color_kelvin.setText("")
        self.color_kelvin.setObjectName("color_kelvin")
        self.lux_illu = QtWidgets.QLabel(self.TCS_34725)
        self.lux_illu.setGeometry(QtCore.QRect(500, 170, 61, 16))
        self.lux_illu.setText("")
        self.lux_illu.setObjectName("lux_illu")
        self.groupBox1 = QtWidgets.QGroupBox(self.widget)
        self.groupBox1.setGeometry(QtCore.QRect(20, 10, 431, 291))
        self.groupBox1.setFocusPolicy(QtCore.Qt.NoFocus)
        self.groupBox1.setAcceptDrops(False)
        self.groupBox1.setAutoFillBackground(False)
        self.groupBox1.setFlat(False)
        self.groupBox1.setCheckable(False)
        self.groupBox1.setObjectName("groupBox1")
        self.am2302 = QtWidgets.QWidget(self.groupBox1)
        self.am2302.setGeometry(QtCore.QRect(0, 20, 431, 271))
        self.am2302.setContextMenuPolicy(QtCore.Qt.DefaultContextMenu)
        self.am2302.setAcceptDrops(False)
        self.am2302.setAutoFillBackground(False)
        self.am2302.setObjectName("am2302")
        self.am2302_temp_in_c = QtWidgets.QSlider(self.am2302)
        self.am2302_temp_in_c.setGeometry(QtCore.QRect(100, 30, 51, 221))
        self.am2302_temp_in_c.setStyleSheet("")
        self.am2302_temp_in_c.setMinimum(-20)
        self.am2302_temp_in_c.setMaximum(100)
        self.am2302_temp_in_c.setOrientation(QtCore.Qt.Vertical)
        self.am2302_temp_in_c.setInvertedAppearance(False)
        self.am2302_temp_in_c.setTickPosition(QtWidgets.QSlider.TicksBothSides)
        self.am2302_temp_in_c.setObjectName("am2302_temp_in_c")
        self.am2302_temp_label = QtWidgets.QLCDNumber(self.am2302)
        self.am2302_temp_label.setGeometry(QtCore.QRect(0, 120, 81, 41))
        font = QtGui.QFont()
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        font.setKerning(True)
        self.am2302_temp_label.setFont(font)
        self.am2302_temp_label.setAcceptDrops(False)
        self.am2302_temp_label.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.am2302_temp_label.setFrameShadow(QtWidgets.QFrame.Plain)
        self.am2302_temp_label.setLineWidth(5)
        self.am2302_temp_label.setSmallDecimalPoint(False)
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
        self.am2302_humidity_pct.setNotchTarget(1.7)
        self.am2302_humidity_pct.setNotchesVisible(True)
        self.am2302_humidity_pct.setObjectName("am2302_humidity_pct")
        self.lcdNumber = QtWidgets.QLCDNumber(self.am2302)
        self.lcdNumber.setGeometry(QtCore.QRect(240, 210, 81, 41))
        self.lcdNumber.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.lcdNumber.setFrameShadow(QtWidgets.QFrame.Plain)
        self.lcdNumber.setLineWidth(5)
        self.lcdNumber.setSegmentStyle(QtWidgets.QLCDNumber.Flat)
        self.lcdNumber.setObjectName("lcdNumber")
        self.label = QtWidgets.QLabel(self.am2302)
        self.label.setGeometry(QtCore.QRect(80, 120, 20, 21))
        self.label.setObjectName("label")
        self.am2302_percent_label = QtWidgets.QLabel(self.am2302)
        self.am2302_percent_label.setGeometry(QtCore.QRect(320, 220, 21, 21))
        font = QtGui.QFont()
        font.setPointSize(22)
        self.am2302_percent_label.setFont(font)
        self.am2302_percent_label.setObjectName("am2302_percent_label")
        self.label_7 = QtWidgets.QLabel(self.am2302)
        self.label_7.setGeometry(QtCore.QRect(80, 10, 81, 16))
        self.label_7.setObjectName("label_7")
        self.label_8 = QtWidgets.QLabel(self.am2302)
        self.label_8.setGeometry(QtCore.QRect(280, 40, 61, 16))
        self.label_8.setObjectName("label_8")
        self.pir_motion_detection = QtWidgets.QGroupBox(self.widget)
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
        self.led_board = QtWidgets.QGroupBox(self.widget)
        self.led_board.setGeometry(QtCore.QRect(520, 510, 581, 181))
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
        self.cpu_utilization = QtWidgets.QGroupBox(self.widget)
        self.cpu_utilization.setGeometry(QtCore.QRect(20, 310, 481, 241))
        self.cpu_utilization.setStyleSheet("")
        self.cpu_utilization.setObjectName("cpu_utilization")
        self.cpu_util_slider = QtWidgets.QSlider(self.cpu_utilization)
        self.cpu_util_slider.setGeometry(QtCore.QRect(70, 54, 22, 171))
        self.cpu_util_slider.setStyleSheet("")
        self.cpu_util_slider.setMaximum(100)
        self.cpu_util_slider.setOrientation(QtCore.Qt.Vertical)
        self.cpu_util_slider.setTickPosition(QtWidgets.QSlider.TicksBothSides)
        self.cpu_util_slider.setObjectName("cpu_util_slider")
        self.progressBar_2 = QtWidgets.QProgressBar(self.cpu_utilization)
        self.progressBar_2.setGeometry(QtCore.QRect(100, 54, 41, 171))
        self.progressBar_2.setAutoFillBackground(False)
        self.progressBar_2.setStyleSheet("")
        self.progressBar_2.setProperty("value", 0)
        self.progressBar_2.setAlignment(QtCore.Qt.AlignCenter)
        self.progressBar_2.setTextVisible(True)
        self.progressBar_2.setOrientation(QtCore.Qt.Vertical)
        self.progressBar_2.setInvertedAppearance(False)
        self.progressBar_2.setTextDirection(QtWidgets.QProgressBar.TopToBottom)
        self.progressBar_2.setFormat("%p%")
        self.progressBar_2.setObjectName("progressBar_2")
        self.cpu_temp_slider = QtWidgets.QSlider(self.cpu_utilization)
        self.cpu_temp_slider.setGeometry(QtCore.QRect(340, 54, 41, 171))
        self.cpu_temp_slider.setStyleSheet("")
        self.cpu_temp_slider.setMaximum(100)
        self.cpu_temp_slider.setOrientation(QtCore.Qt.Vertical)
        self.cpu_temp_slider.setTickPosition(QtWidgets.QSlider.TicksBothSides)
        self.cpu_temp_slider.setObjectName("cpu_temp_slider")
        self.lcdNumber_2 = QtWidgets.QLCDNumber(self.cpu_utilization)
        self.lcdNumber_2.setGeometry(QtCore.QRect(240, 110, 81, 41))
        self.lcdNumber_2.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.lcdNumber_2.setFrameShadow(QtWidgets.QFrame.Plain)
        self.lcdNumber_2.setSegmentStyle(QtWidgets.QLCDNumber.Flat)
        self.lcdNumber_2.setObjectName("lcdNumber_2")
        self.cpu_utilization_lcd = QtWidgets.QLCDNumber(self.cpu_utilization)
        self.cpu_utilization_lcd.setGeometry(QtCore.QRect(70, 120, 61, 31))
        self.cpu_utilization_lcd.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.cpu_utilization_lcd.setFrameShadow(QtWidgets.QFrame.Plain)
        self.cpu_utilization_lcd.setSegmentStyle(QtWidgets.QLCDNumber.Flat)
        self.cpu_utilization_lcd.setObjectName("cpu_utilization_lcd")
        self.label_3 = QtWidgets.QLabel(self.cpu_utilization)
        self.label_3.setGeometry(QtCore.QRect(320, 110, 60, 16))
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.cpu_utilization)
        self.label_4.setGeometry(QtCore.QRect(130, 130, 60, 16))
        self.label_4.setObjectName("label_4")
        self.label_15 = QtWidgets.QLabel(self.cpu_utilization)
        self.label_15.setGeometry(QtCore.QRect(70, 30, 60, 16))
        self.label_15.setObjectName("label_15")
        self.label_16 = QtWidgets.QLabel(self.cpu_utilization)
        self.label_16.setGeometry(QtCore.QRect(320, 30, 81, 16))
        self.label_16.setObjectName("label_16")
        LivingLabEmulator.setCentralWidget(self.widget)
        self.menubar = QtWidgets.QMenuBar(LivingLabEmulator)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1121, 22))
        self.menubar.setObjectName("menubar")
        self.menuMenu = QtWidgets.QMenu(self.menubar)
        self.menuMenu.setObjectName("menuMenu")
        self.menuQuit = QtWidgets.QMenu(self.menuMenu)
        self.menuQuit.setObjectName("menuQuit")
        LivingLabEmulator.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(LivingLabEmulator)
        self.statusbar.setObjectName("statusbar")
        LivingLabEmulator.setStatusBar(self.statusbar)
        self.menuQuit.addSeparator()
        self.menuMenu.addAction(self.menuQuit.menuAction())
        self.menubar.addAction(self.menuMenu.menuAction())

        self.retranslateUi(LivingLabEmulator)
        self.am2302_temp_in_c.sliderMoved['int'].connect(self.am2302_temp_label.display)
        self.am2302_humidity_pct.sliderMoved['int'].connect(self.lcdNumber.display)
        self.bme280_humidity_pct.valueChanged['int'].connect(self.bm280_humidity_lcd.display)
        self.bme280_pressure.valueChanged['int'].connect(self.bme280_pressure_lcd.display)
        self.bme280_sealevel.valueChanged['int'].connect(self.bme280_sealevel_lcd.display)
        self.cpu_util_slider.valueChanged['int'].connect(self.progressBar_2.setValue)
        self.cpu_temp_slider.valueChanged['int'].connect(self.lcdNumber_2.display)
        self.color_red.valueChanged['int'].connect(self.red_spinbox.setValue)
        self.color_green.valueChanged['int'].connect(self.green_spinbox.setValue)
        self.color_blue.valueChanged['int'].connect(self.blue_spinbox.setValue)
        self.color_clear.valueChanged['int'].connect(self.clear_spinbox.setValue)
        self.red_spinbox.valueChanged['int'].connect(self.color_red.setValue)
        self.green_spinbox.valueChanged['int'].connect(self.color_green.setValue)
        self.blue_spinbox.valueChanged['int'].connect(self.color_blue.setValue)
        self.clear_spinbox.valueChanged['int'].connect(self.color_clear.setValue)
        self.cpu_util_slider.valueChanged['int'].connect(self.cpu_utilization_lcd.display)
        self.bme280_altitude_slider.valueChanged['int'].connect(self.bme280_altitude_lcd.display)
        self.bme280_temp_in_c.valueChanged['int'].connect(self.bme280_temp_lcd.display)
        QtCore.QMetaObject.connectSlotsByName(LivingLabEmulator)

    def retranslateUi(self, LivingLabEmulator):
        _translate = QtCore.QCoreApplication.translate
        LivingLabEmulator.setWindowTitle(_translate("LivingLabEmulator", "Living Lab Emulator"))
        self.groupBox.setTitle(_translate("LivingLabEmulator", "BME280 - Digtial Temperature, Altitude, Sealevel Pressure, Humidity Percentage, and Pressure"))
        self.label_2.setText(_translate("LivingLabEmulator", "%"))
        self.label_5.setText(_translate("LivingLabEmulator", "° C"))
        self.label_6.setText(_translate("LivingLabEmulator", "M"))
        self.label_9.setText(_translate("LivingLabEmulator", "Temperature"))
        self.label_11.setText(_translate("LivingLabEmulator", "Altitude"))
        self.label_12.setText(_translate("LivingLabEmulator", "Humidity"))
        self.label_13.setText(_translate("LivingLabEmulator", "Pressure"))
        self.label_14.setText(_translate("LivingLabEmulator", "Sea Level Pressure"))
        self.TCS_34725.setTitle(_translate("LivingLabEmulator", "TCS_34725"))
        self.label_red.setText(_translate("LivingLabEmulator", "R"))
        self.label_green.setText(_translate("LivingLabEmulator", "G"))
        self.label_blue.setText(_translate("LivingLabEmulator", "B"))
        self.label_10.setText(_translate("LivingLabEmulator", "Clear"))
        self.color_temp.setText(_translate("LivingLabEmulator", "Temp:"))
        self.color_lux.setText(_translate("LivingLabEmulator", "Lux:"))
        self.groupBox1.setTitle(_translate("LivingLabEmulator", "AM2302 - Analog Temperature and Humidity Percentage"))
        self.label.setText(_translate("LivingLabEmulator", "° C"))
        self.am2302_percent_label.setText(_translate("LivingLabEmulator", "%"))
        self.label_7.setText(_translate("LivingLabEmulator", "Temperature"))
        self.label_8.setText(_translate("LivingLabEmulator", "Humidity"))
        self.pir_motion_detection.setTitle(_translate("LivingLabEmulator", "Pir_Motion_Detection"))
        self.pir_toggle_button.setText(_translate("LivingLabEmulator", "Motion"))
        self.pir_motion_label.setText(_translate("LivingLabEmulator", "No Motion Detected"))
        self.led_board.setTitle(_translate("LivingLabEmulator", "LED Board"))
        self.led_red_button.setText(_translate("LivingLabEmulator", "OFF"))
        self.led_green_button.setText(_translate("LivingLabEmulator", "OFF"))
        self.led_blue_button.setText(_translate("LivingLabEmulator", "OFF"))
        self.led_yellow_button.setText(_translate("LivingLabEmulator", "OFF"))
        self.led_white_button.setText(_translate("LivingLabEmulator", "OFF"))
        self.cpu_utilization.setTitle(_translate("LivingLabEmulator", "CPU Utilization & Temperature"))
        self.label_3.setText(_translate("LivingLabEmulator", "° C"))
        self.label_4.setText(_translate("LivingLabEmulator", "%"))
        self.label_15.setText(_translate("LivingLabEmulator", "Utilization"))
        self.label_16.setText(_translate("LivingLabEmulator", "Temperature"))
        self.menuMenu.setTitle(_translate("LivingLabEmulator", "Menu"))
        self.menuQuit.setTitle(_translate("LivingLabEmulator", "Quit"))
        self.timer = QtCore.QTimer()
        self.timer.start(2000)




if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    LivingLabEmulator = QtWidgets.QMainWindow()
    ui = Ui_LivingLabEmulator()
    ui.setupUi(LivingLabEmulator)
    LivingLabEmulator.show()
    sys.exit(app.exec_())
