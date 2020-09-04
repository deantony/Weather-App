"""
<Project Title>
Version: <#>
Date: <Date>
Author: Anthony Dean
ALL RIGHTS RESERVED

"""
#---------------Imports------------------------------------------------------------------------------------------------------------------------------
from kivy.app import App

import kivy
from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.behaviors import ButtonBehavior
from kivy.uix.textinput import TextInput
from kivy.uix.togglebutton import ToggleButton
from kivy.uix.screenmanager import Screen, ScreenManager
from kivy.uix.dropdown import DropDown
from kivy.uix.bubble import Bubble
from kivy.uix.image import AsyncImage

from kivy.uix.floatlayout import FloatLayout
from kivy.core.window import Window
from kivy.config import Config
from kivy.clock import Clock

import pandas as pd
import datetime
from datetime import timedelta
import pandas_datareader as dr
import numpy as np
import matplotlib.pyplot as plt

import sqlite3

import json
import requests

#---------------Colors-------------------------------------------------------------------------------------------------------------------------------
black = [0, 0, 0, 1]
darkgray = [.25, .25, .25, 1]
middlegray = [.5, .5, .5, 1]
lightgray = [.75, .75, .75, 1]
white = [1, 1, 1, 1]
red = [1, 0, 0, 1]
green = [0, 1, 0, 1]
blue = [0, 0, 1, 1]
#---------------Variables----------------------------------------------------------------------------------------------------------------------------


#---------------Window-------------------------------------------------------------------------------------------------------------------------------

#---------------Classes------------------------------------------------------------------------------------------------------------------------------

#---------------Pages--------------------------------------------------------------------------------------------------------------------------------
class HomeScreen(Screen):
    def __init__(self, **kwargs):
        super(HomeScreen, self).__init__(**kwargs)

        self.layout = FloatLayout()

        #-----Add Widgets Below-----
            #---Api---
        self.api_key = "e50e7bcabef01fd68032aeb0e938e039"
        self.base_url = "http://api.openweathermap.org/data/2.5/weather?"
        self.city_name = "Great Falls"
        self.complete_url = self.base_url + "appid=" + self.api_key + "&q=" + self.city_name + "&units=imperial"
        self.response = requests.get(self.complete_url)
        self.response = self.response.json()
        if self.response["cod"] != "404":
            self.main = self.response["main"]
            self.c_temp = self.main["temp"]
            self.sc_temp = str(self.c_temp)
            self.c_press = self.main["pressure"]
            self.sc_press = str(self.c_press)
            self.c_hum = self.main["humidity"]
            self.sc_hum = str(self.c_hum)
            #---^---
        self.weathercon = AsyncImage(source = "./Images/01d.gif", pos_hint = {"x": .40, "y": .40}, size = self.size)
        self.layout.add_widget(self.weathercon)

        self.label_c_temp = Label(text = f"Temperature: {self.sc_temp} F", pos_hint = {"x": .31, "y": .28})
        self.layout.add_widget(self.label_c_temp)

        self.label_c_press = Label(text = f"Barometric\nPressure: {self.sc_press} hPa", pos_hint = {"x": .31, "y": .34})
        self.layout.add_widget(self.label_c_press)

        self.label_c_hum = Label(text = f"Humidity:{self.sc_hum}%", pos_hint = {"x": .31, "y": .24})
        self.layout.add_widget(self.label_c_hum)
        #-----Add Widgets Above-----
        self.add_widget(self.layout)

    #-----Screen Functions Below-----
    def update(self, *args):
        pass
    #-----Screen Functions Above-----canvas_weathercon

#---------------Functions----------------------------------------------------------------------------------------------------------------------------

#---------------Run App------------------------------------------------------------------------------------------------------------------------------
class AppApp(App):
    def build(self):
        root = ScreenManager()
        #-----Add Screens Below-----
        root.add_widget(HomeScreen(name = "home_screen"))

        #-----Add Screens Above-----
        return root

AppApp().run()
