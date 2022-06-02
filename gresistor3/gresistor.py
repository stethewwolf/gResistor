#!/usr/bin/env python3
# -*- coding: UTF8 -*-

# Python module gresistor.py

import gi

gi.require_version("Gtk", "3.0")
from gi.repository import Gtk
import cairo
import os, sys
from pathlib import Path

app_name = "gResistor"
app_version = "3.2.3"
wikipedia_eletronic_color_scheme = "https://en.wikipedia.org/wiki/Electronic_color_code"
gresistor_issues = "https://gitlab.com/a2488/gresistor/-/issues"

black_code = (0,0,0)
brown_code = (165/255,42/255,42/255)
red_code = (1,0,0)
orange_code = (1,69/255,0)
yellow_code = (1,1,0)
green_code = (0,1,0)
blue_code = (0,0,1)
violet_code = (238/255,130/255,238/255)
gray_code = (128/255,128/255,128/255)
white_code = (1,1,1)
gold_code = (1,215/255,0)
silver_code = (192/255,192/255,192/255)

color_codes = dict()
color_codes['Black'] = black_code
color_codes['Brown'] = brown_code
color_codes['Red'] = red_code
color_codes['Orange'] = orange_code
color_codes['Yellow'] = yellow_code
color_codes['Green'] = green_code
color_codes['Blue'] = blue_code
color_codes['Violet'] = violet_code
color_codes['Gray'] = gray_code
color_codes['White'] = white_code
color_codes['Gold'] = gold_code
color_codes['Silver'] = silver_code

class Handler:
    def showAbout(self, *args):
        global builder
        global app_version
        global app_name
        about_window = builder.get_object("gresistor_about")
        about_window.set_version(app_version)
        about_window.run()

    def onWiki(self, *args):
        global wikipedia_eletronic_color_scheme

        if sys.platform.startswith('linux'):
            os.system("xdg-open " + wikipedia_eletronic_color_scheme)
        elif sys.platform.startswith('win'):
            os.system("start " + wikipedia_eletronic_color_scheme)
        elif sys.platform.startswith('darwin'):
            os.system("open " + wikipedia_eletronic_color_scheme)
        else:
            pass
            # todo manage this case

    def onIssue(self, *args):
        global gresistor_issues

        if sys.platform.startswith('linux'):
            os.system("xdg-open " + gresistor_issues)
        elif sys.platform.startswith('win'):
            os.system("start " + gresistor_issues)
        elif sys.platform.startswith('darwin'):
            os.system("open " + gresistor_issues)
        else:
            pass
            # todo manage this case


    def onDestroy(self, *args):
        Gtk.main_quit()

    def onKeyboardInterrupt(self, *args):
        """
        This method is called by the default implementation of run()
        after a program is finished by pressing Control-C.
        """
        pass

    def onBandsChange(self, *args):
        global builder
        text = args[0].get_active_text()

        if '4' in text:
            self.onSelect4bands()
        elif '5' in text:
            self.onSelect5bands()
        elif '6' in text:
            self.onSelect6bands()

        drawing_area = builder.get_object("main_drawing_area")
        drawing_area.queue_draw()

    def onSelect4bands(self, *args):
        global buizlder

        tollerance_chooser = builder.get_object("band_3_chooser")
        tollerance_chooser.set_sensitive(0)
        tollerance_label = builder.get_object("band_3_chooser")
        tollerance_label.set_sensitive(0)

        temperature_chooser = builder.get_object("temperature_chooser")
        temperature_chooser.set_sensitive(0)
        temperature_label = builder.get_object("temperature_label")
        temperature_label.set_sensitive(0)

    def onSelect5bands(self, *args):
        global builder

        tollerance_chooser = builder.get_object("band_3_chooser")
        tollerance_chooser.set_sensitive(1)
        tollerance_label = builder.get_object("band_3_chooser")
        tollerance_label.set_sensitive(1)

        temperature_chooser = builder.get_object("temperature_chooser")
        temperature_chooser.set_sensitive(0)
        temperature_label = builder.get_object("temperature_label")
        temperature_label.set_sensitive(0)

    def onSelect6bands(self, *args):
        global builder
        tollerance_chooser = builder.get_object("band_3_chooser")
        tollerance_chooser.set_sensitive(1)
        tollerance_label = builder.get_object("band_3_chooser")
        tollerance_label.set_sensitive(1)

        temperature_chooser = builder.get_object("temperature_chooser")
        temperature_chooser.set_sensitive(1)
        temperature_label = builder.get_object("temperature_label")
        temperature_label.set_sensitive(1)

    def onValueChange(self, *args):
        global builder
        drawing_area = builder.get_object("main_drawing_area")
        drawing_area.queue_draw()

    def onDrawResistor(self, *args):
        global value
        global builder

        value = calc_value()

        area = args[0]
        cr = args[1]

        window = builder.get_object("gresistor_main_window")
        h, w =  window.get_size()

        cr.move_to(w/3, 50)
        cr.select_font_face("Sans")
        cr.set_font_size(22)
        cr.show_text(value)

        cr.move_to(w/2, 300)


        cr.set_line_width(1)
        cr.set_line_join(cairo.LINE_JOIN_BEVEL)

     #   Trasez rezistenta
        cr.rectangle(w/3+40, 70,60, 74)
        cr.rectangle(w/3+41, 71,59, 73)

        cr.rectangle(w/3+190, 70,60, 74)
        cr.rectangle(w/3+191, 71,59, 73)

        cr.rectangle(w/3+100, 82,90, 50)
        cr.rectangle(w/3+101, 83,89, 49)
        cr.stroke()

        cr.move_to(w/3, 107)
        cr.line_to(w/3+40, 107)
        cr.stroke()

        cr.move_to(w/3+250, 107)
        cr.line_to(w/3+290, 107)
        cr.stroke()


        bands_chooser = builder.get_object("combo_num_bands")
        band_color = bands_chooser.get_active_text()

        # band 1 rectangle
        band_1_chooser = builder.get_object('band_1_chooser')
        band_1_color = band_1_chooser.get_active_text()
        band_1_color_code = color_codes[band_1_color]

        cr.set_source_rgb(
                band_1_color_code[0],
                band_1_color_code[1],
                band_1_color_code[2])
        cr.rectangle(w/3+65, 71,10, 73)
        cr.fill()
        cr.stroke()

        # band 2 rectangle
        band_2_chooser = builder.get_object('band_2_chooser')
        band_2_color = band_2_chooser.get_active_text()
        band_2_color_code = color_codes[band_2_color]

        cr.set_source_rgb(
                band_2_color_code[0],
                band_2_color_code[1],
                band_2_color_code[2])
        cr.rectangle(w/3+110, 83,10, 49)
        cr.fill()
        cr.stroke()

        # multiply rectangle
        multiply_chooser = builder.get_object("multiply_chooser")
        multiply_color = multiply_chooser.get_active_text()
        multiply_color_code = color_codes[multiply_color]

        cr.rectangle(w/3+150, 83,10, 49)
        cr.set_source_rgb(
                multiply_color_code[0],
                multiply_color_code[1],
                multiply_color_code[2])

        cr.fill()
        cr.stroke()

        # tolerance rectangle
        tolerance_chooser = builder.get_object("tolerance_chooser")
        tolerance_color = tolerance_chooser.get_active_text()
        tolerance_color_code = color_codes[tolerance_color]
        cr.set_source_rgb(
                tolerance_color_code[0],
                tolerance_color_code[1],
                tolerance_color_code[2])
        cr.rectangle(w/3+170, 83,10, 49)

        cr.fill()
        cr.stroke()

        if '5' in band_color or '6' in band_color:
            # band 3 rectangle
            band_3_chooser = builder.get_object('band_3_chooser')
            band_3_color = band_3_chooser.get_active_text()
            band_3_color_code = color_codes[band_3_color]

            cr.set_source_rgb(
                    band_3_color_code[0],
                    band_3_color_code[1],
                    band_3_color_code[2])

            cr.rectangle(w/3+130, 83,10, 49)
            cr.fill()
            cr.stroke()

        if '6' in band_color:
            # temperature rectangle
            temperature_chooser = builder.get_object("temperature_chooser")
            temperature_color = temperature_chooser.get_active_text()
            temperature_color_code = color_codes[temperature_color]
            cr.set_source_rgb(
                    temperature_color_code[0],
                    temperature_color_code[1],
                    temperature_color_code[2])

            cr.rectangle(w/3+215, 71,10, 73)
            cr.fill()
            cr.stroke()


def calc_value():
    global value
    global builder

    temperature_value=' '
    tolerance=' '
    multiply=' '
    unit_of_measure=' '
    band_1_value =' ' # 0
    band_2_value =' ' # 0
    band_3_value =' ' # 0

    # temperature
    temperature_chooser = builder.get_object("temperature_chooser")
    temperature_color = temperature_chooser.get_active_text()
    if temperature_color == 'None':
        temperature_value=' ' # None
    elif temperature_color == 'Black':
        temperature_value ='250 ppm/K'
    elif temperature_color == 'Brown':
        temperature_value ='100 ppm/K'
    elif temperature_color == 'Red':
        temperature_value ='50 ppm/K'
    elif temperature_color == 'Orange':
        temperature_value ='15 ppm/K'
    elif temperature_color == 'Yellow':
        temperature_value ='25 ppm/K'
    elif temperature_color == 'Green':
        temperature_value ='20 ppm/K'
    elif temperature_color == 'Blue':
        temperature_value ='10 ppm/K'
    elif temperature_color == 'Violet':
        temperature_value ='5 ppm/K'
    elif temperature_color == 'Gray':
        temperature_value ='1 ppm/K'

    # tolerance
    tolerance_chooser = builder.get_object("tolerance_chooser")
    tolerance_color = tolerance_chooser.get_active_text()
    if tolerance_color == 'None':
        tolerance=' '
    if tolerance_color == 'Brown':
        tolerance='1%'
    elif tolerance_color == 'Red':
        tolerance='2%'
    elif tolerance_color == 'Green':
        tolerance='0.5%'
    elif tolerance_color == 'Blue':
        tolerance='0.25%'
    elif tolerance_color == 'Violet':
        tolerance='0.1%'
    elif tolerance_color == 'Gold':
        tolerance='5%'
    elif tolerance_color == 'Silver':
        tolerance='10%'

    # multiply
    multiply_chooser = builder.get_object("multiply_chooser")
    multiply_color = multiply_chooser.get_active_text()
    if multiply_color == 'Silver':
        multiply=' '
        unit_of_measure="cΩ"
    elif multiply_color == 'Gold':
        multiply='0'
        unit_of_measure="dΩ"
    elif multiply_color == 'Black':
        multiply=''
        unit_of_measure=" Ω"
    elif multiply_color == 'Brown':
        multiply='0'
        unit_of_measure=" Ω"
    elif multiply_color == 'Red':
        multiply='00'
        unit_of_measure=" Ω"
    elif multiply_color == 'Orange':
        multiply=''
        unit_of_measure="KΩ"
    elif multiply_color == 'Yellow':
        multiply='0'
        unit_of_measure="KΩ"
    elif multiply_color == 'Green':
        multiply='00'
        unit_of_measure="KΩ"
    elif multiply_color == 'Blue':
        multiply=''
        unit_of_measure="MΩ"

    band_1_chooser = builder.get_object('band_1_chooser')
    band_1_color = band_1_chooser.get_active_text()
    band_1_value = ' '
    if band_1_color == 'Black':
        band_1_value =' ' # 0
    elif band_1_color == 'Brown':
        band_1_value ='1'
    elif band_1_color == 'Red':
        band_1_value ='2'
    elif band_1_color == 'Orange':
        band_1_value ='3'
    elif band_1_color == 'Yellow':
        band_1_value ='4'
    elif band_1_color == 'Green':
        band_1_value ='5'
    elif band_1_color == 'Blue':
        band_1_value ='6'
    elif band_1_color == 'Violet':
        band_1_value ='7'
    elif band_1_color == 'Gray':
        band_1_value ='8'
    elif band_1_color == 'White':
        band_1_value ='9'

    band_2_chooser = builder.get_object('band_2_chooser')
    band_2_color = band_2_chooser.get_active_text()
    band_2_value = ' '
    if band_2_color == 'Black':
        band_2_value ='0'
    elif band_2_color == 'Brown':
        band_2_value ='1'
    elif band_2_color == 'Red':
        band_2_value ='2'
    elif band_2_color == 'Orange':
        band_2_value ='3'
    elif band_2_color == 'Yellow':
        band_2_value ='4'
    elif band_2_color == 'Green':
        band_2_value ='5'
    elif band_2_color == 'Blue':
        band_2_value ='6'
    elif band_2_color == 'Violet':
        band_2_value ='7'
    elif band_2_color == 'Gray':
        band_2_value ='8'
    elif band_2_color == 'White':
        band_2_value ='9'

    band_3_chooser = builder.get_object('band_3_chooser')
    band_3_color = band_3_chooser.get_active_text()
    band_3_value = ' '
    if band_3_color == 'Black':
        band_3_value ='0'
    elif band_3_color == 'Brown':
        band_3_value ='1'
    elif band_3_color == 'Red':
        band_3_value ='2'
    elif band_3_color == 'Orange':
        band_3_value ='3'
    elif band_3_color == 'Yellow':
        band_3_value ='4'
    elif band_3_color == 'Green':
        band_3_value ='5'
    elif band_3_color == 'Blue':
        band_3_value ='6'
    elif band_3_color == 'Violet':
        band_3_value ='7'
    elif band_3_color == 'Gray':
        band_3_value ='8'
    elif band_3_color == 'White':
        band_3_value ='9'

    bands_chooser = builder.get_object("combo_num_bands")
    band_color = bands_chooser.get_active_text()

    if '4' in band_color:
        value=band_1_value+band_2_value+multiply+unit_of_measure+' ± '+tolerance
    elif '5' in band_color:
        value=band_1_value+band_2_value+band_3_value+multiply+unit_of_measure+' ± '+tolerance
    elif '6' in band_color:
        value=band_1_value+band_2_value+band_3_value+multiply+unit_of_measure+' ± '+tolerance+' '+temperature_value

    return value


def run_gresistor(glade_file):
    global builder
    global signal_handler
    global value

    signal_handler = Handler()
    builder = Gtk.Builder()

    builder.add_from_file(glade_file)
    builder.connect_signals(signal_handler)

    window = builder.get_object("gresistor_main_window")
    window.show_all()
    window.resize(600,400)
    window.set_title(app_name)
    window.connect("delete-event", Gtk.main_quit)

    # by default app start with only 4 band enabled
    signal_handler.onSelect4bands()

    try:
        Gtk.main()
    except KeyboardInterrupt:
        signal_handler.onKeyboardInterrupt()


def main():
    sys_glade_file = os.path.join(
            Path(__file__).parents[1],
            'share',
            'gresistor',
            'gresistor.glade'
            )

    repo_glade_file = os.path.join(
            os.path.dirname(os.path.realpath(__file__)),
            'gresistor.glade'
            )

    env_glade_file = "/null"
    if("VIRTUAL_ENV" in os.environ):
        env_glade_file = os.path.join(
            os.environ["VIRTUAL_ENV"],
                'share',
                'gresistor',
                'gresistor.glade'
            )

    local_glade_file = "/null"
    if("HOME" in os.environ):
        env_glade_file = os.path.join(
            os.environ["HOME"],
                '.local',
                'share',
                'gresistor',
                'gresistor.glade'
            )

    if os.path.exists(repo_glade_file):
        run_gresistor(repo_glade_file)
    elif os.path.exists(env_glade_file):
        run_gresistor(env_glade_file)
    elif os.path.exists(local_glade_file):
        run_gresistor(local_glade_file)
    else:
        run_gresistor(sys_glade_file)

if __name__ == "__main__":
    main()
