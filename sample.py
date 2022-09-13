from cgitb import text
from dbm.ndbm import library
from kivy.app import App
from kivy.uix.label import Label

from kivy.core.text import LabelBase, DEFAULT_FONT
from kivy.resources import resource_add_path

resource_add_path ('/System/Library/Fonts')
LabelBase.register(DEFAULT_FONT,'ヒラギノ角ゴシック W0.ttc')


class TextApp(App):
    def build(self):
        return Label(text='みなさんこんにちは。kivyのサンプルです')

TextApp().run()