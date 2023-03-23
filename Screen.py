import tkinter as tk

from models.Menu import MenuExternalIterator, Menu


class Screen:
    def __init__(self, menu: Menu):
        self.menu = menu
        self.iterator = MenuExternalIterator(menu)
        self.screen = tk.Tk()
        self.screen.bind('<Down>', self.iterator.previous)
        self.screen.bind('<Up>', self.iterator.next)

