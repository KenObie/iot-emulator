import json
from PyQt5 import QtCore, QtGui, QtWidgets
import sys
import emulator_gui_dark
import logging
import qtmodern
import qtmodern.styles
import qtmodern.windows
from PyQt5.QtCore import QTimer
from pprint import pprint


class emulatorApp(QtWidgets.QMainWindow, emulator_gui_dark.Ui_LivingLabEmulator):
    def __init__(self):
        super(self.__class__, self).__init__()
        self.setupUi(self)
        self.am2302_temp_in_c.valueChanged[int].connect(self.am2302_temp)
        self.am2302_humidity_pct.valueChanged[int].connect(self.am2302_humidity)
        self.bme280_temp_in_c.valueChanged[int].connect(self.bme280_temp)
        self.bme280_humidity_pct.valueChanged[int].connect(self.bme280_humidity)
        self.pir_toggle_button.toggled.connect(self.set_pir_label)
        self.led_red_button.toggled.connect(self.led_red)
        self.led_green_button.toggled.connect(self.led_green)
        self.led_blue_button.toggled.connect(self.led_blue)
        self.led_yellow_button.toggled.connect(self.led_yellow)
        self.led_white_button.toggled.connect(self.led_white)
        self.color_red.valueChanged[int].connect(self.color)
        self.color_green.valueChanged[int].connect(self.color)
        self.color_blue.valueChanged[int].connect(self.color)
        self.bme280_altitude_slider.valueChanged[int].connect(self.altitude_meters)
        self.bme280_sealevel.valueChanged[int].connect(self.sealevel_pressure)
        self.bme280_pressure.valueChanged[int].connect(self.pressure_in_hpa)
        self.cpu_util_slider.valueChanged[int].connect(self.cpu_util)
        self.cpu_temp_slider.valueChanged[int].connect(self.cpu_temp)
        self.timer.timeout.connect(self.update)

    def update(self):


        with open('emulator.json', 'r') as storage:
            data = json.load(storage)


        with open('emulator.json', 'w') as storage:
            json.dump(data, storage, sort_keys = True,  indent = 4)
            print(data)





    def cpu_util(self, value):
            with open('emulator.json', 'r') as storage:
                data = json.load(storage)
                data['cpu_pct_utilization'] = value

            with open('emulator.json', 'w') as storage:
                json.dump(data, storage, sort_keys = True, indent = 4)

    def cpu_temp(self, value):
            with open('emulator.json', 'r') as storage:
                data = json.load(storage)
                data['cpu_temp_in_c'] = value

            with open('emulator.json', 'w') as storage:
                json.dump(data, storage, sort_keys = True, indent = 4)

    def pressure_in_hpa(self, value):
        def sealevel_pressure(self, value):
            with open('emulator.json', 'r') as storage:
                data = json.load(storage)
                data['bme280_pressure_in_hpa'] = value

            with open('emulator.json', 'w') as storage:
                json.dump(data, storage, sort_keys = True, indent = 4)

    def sealevel_pressure(self, value):
        with open('emulator.json', 'r') as storage:
            data = json.load(storage)
            data['bme280_sea_level_pressure'] = value

        with open('emulator.json', 'w') as storage:
            json.dump(data, storage, sort_keys = True, indent = 4)


    def altitude_meters(self, value):
        with open('emulator.json', 'r') as storage:
            data = json.load(storage)
            data['bme280_altitude_in_m'] = value

        with open('emulator.json', 'w') as storage:
            json.dump(data, storage, sort_keys = True, indent = 4)



    def color(self):
        red_value = self.color_red.value()
        green_value = self.color_green.value()
        blue_value = self.color_blue.value()
        clear_value = self.color_clear.value()
        #print(red_value, green_value, blue_value)
        self.color_hue.setStyleSheet("background-color: '#%02x%02x%02x' "% (red_value, green_value, blue_value))
        illumanence  = (-0.32466 * red_value) + (1.57837 * green_value) + (-0.73191 * blue_value)
        illumanence = round(illumanence, 2)
        illumanence = str(illumanence)
        self.lux_illu.setText(illumanence)

        X = (-0.14282 * red_value) + (1.54924 * green_value) + (-0.95641 * blue_value)
        Y = (-0.32466 * red_value) + (1.57837 * green_value) + (-0.73191 * blue_value)
        Z = (-0.68202 * red_value) + (0.77073 * green_value) + ( 0.56332 * blue_value)

        if (X + Y + Z) == 0:
            pass
        xc = (X) / (X + Y + Z)
        yc = (Y) / (X + Y + Z)

        if (0.1858 - yc) == 0:
            pass

        n = (xc - 0.3320) / (0.1858 - yc)
        cct = (449.0 * (n ** 3.0)) + (3525.0 *(n ** 2.0)) + (6823.3 * n) + 5520.33
        cct = round(cct, 2)
        cct = str(cct)
        #print(cct)
        self.color_kelvin.setText(cct)

        with open('emulator.json', 'r') as storage:
            data = json.load(storage)
            data['tcs34725_color_red'] = red_value
            data['tcs34725_color_blue'] = blue_value
            data['tcs34725_color_green'] = green_value
            data['tcs34725_color_clear'] = clear_value
            data['tcs34725_color_temp_k'] = cct
            data['tcs34725_luminosity_lux'] = illumanence

        with open('emulator.json', 'w') as storage:
            json.dump(data, storage, sort_keys = True, indent = 4)


    def led_white(self):

        if self.led_white_button.isChecked():
            self.led_white_icon.setPixmap(QtGui.QPixmap("white_on.png"))
            self.led_white_button.setText('ON')
            value = "on"
        else:
            self.led_white_icon.setPixmap(QtGui.QPixmap("white_off.png"))
            self.led_white_button.setText('OFF')
            value = "off"

        with open('emulator.json', 'r') as storage:
            data = json.load(storage)
            data['LED_white'] = value
            #print(data)

        with open('emulator.json', 'w') as storage:
            json.dump(data, storage, sort_keys = True, indent = 4)

    def led_yellow(self):

        if self.led_yellow_button.isChecked():
            self.led_yellow_icon.setPixmap(QtGui.QPixmap("yellow_on.png"))
            self.led_yellow_button.setText('ON')
            value = "on"
        else:
            self.led_yellow_icon.setPixmap(QtGui.QPixmap("yellow_off.png"))
            self.led_yellow_button.setText('OFF')
            value = "off"

        with open('emulator.json', 'r') as storage:
            data = json.load(storage)
            data['LED_yellow'] = value
            #print(data)

        with open('emulator.json', 'w') as storage:
            json.dump(data, storage, sort_keys = True, indent = 4)

    def led_blue(self):

        if self.led_blue_button.isChecked():
            self.led_rblue_icon.setPixmap(QtGui.QPixmap("blue_on.png"))
            self.led_blue_button.setText('ON')
            value = "on"
        else:
            self.led_rblue_icon.setPixmap(QtGui.QPixmap("blue_off.png"))
            self.led_blue_button.setText('OFF')
            value = "off"

        with open('emulator.json', 'r') as storage:
            data = json.load(storage)
            data['LED_blue'] = value
            #print(data)

        with open('emulator.json', 'w') as storage:
            json.dump(data, storage, sort_keys = True, indent = 4)

    def led_green(self):

        if self.led_green_button.isChecked():
            self.led_green_icon.setPixmap(QtGui.QPixmap("green_on.png"))
            self.led_green_button.setText('ON')
            value = "on"
        else:
            self.led_green_icon.setPixmap(QtGui.QPixmap("green_off.png"))
            self.led_green_button.setText('OFF')
            value = "off"

        with open('emulator.json', 'r') as storage:
            data = json.load(storage)
            data['LED_green'] = value
            #print(data)

        with open('emulator.json', 'w') as storage:
            json.dump(data, storage, sort_keys = True, indent = 4)


    def led_red(self):

        if self.led_red_button.isChecked():
            self.led_red_icon.setPixmap(QtGui.QPixmap("red_on.png"))
            self.led_red_button.setText('ON')
            value = "on"
            #print(red_value)
        else:
            self.led_red_icon.setPixmap(QtGui.QPixmap("red_off2.png"))
            self.led_red_button.setText('OFF')
            value = "off"
            #print(red_value)

        with open('emulator.json', 'r') as storage:
            data = json.load(storage)
            data['LED_red'] = value
            #print(data)

        with open('emulator.json', 'w') as storage:
            json.dump(data, storage, sort_keys = True, indent = 4)

    def set_pir_label(self):

        if self.pir_toggle_button.isChecked():
            #print("checked")
            self.pir_motion_label.setText('Motion Detected')
            self.pir_toggle_button.setStyleSheet("background-color: red")
            value = True
        else:
            #print("Not Checked")
            self.pir_motion_label.setText('No Motion Detected')
            self.pir_toggle_button.setStyleSheet("background-color: grey")
            value = False

        with open('emulator.json', 'r') as storage:
            data = json.load(storage)
            data['pir_motion_detected'] = value

        with open('emulator.json', 'w') as storage:
            json.dump(data, storage, sort_keys = True, indent=4)



    def am2302_temp(self, value):
        with open('emulator.json', 'r') as storage:
            data = json.load(storage)
            data['am2302_temp_in_c'] = value

        with open('emulator.json', 'w') as storage:
            json.dump(data, storage, sort_keys=True, indent=4)

    def am2302_humidity(self, value):
        with open('emulator.json', 'r') as storage:
            data = json.load(storage)
            data['am2302_humidity_pct'] = value

        with open('emulator.json', 'w') as storage:
            json.dump(data, storage, sort_keys=True, indent=4)

    def bme280_temp(self, value):
        with open('emulator.json', 'r') as storage:
            data = json.load(storage)
            data['bme280_temp_in_c'] = value

        with open('emulator.json', 'w') as storage:
            json.dump(data, storage, sort_keys=True, indent=4)

    def bme280_humidity(self, value):
        with open('emulator.json', 'r') as storage:
            data = json.load(storage)
            data['bme280_humidity_pct'] = value

        with open('emulator.json', 'w') as storage:
            json.dump(data, storage, sort_keys=True, indent=4)





def main():
    app = QtWidgets.QApplication(sys.argv)
    form = emulatorApp()
    qtmodern.styles.dark(app)
    mw = qtmodern.windows.ModernWindow(form)
    mw.show()
    #form.show()
    app.exec()

if __name__ == '__main__':
    main()
