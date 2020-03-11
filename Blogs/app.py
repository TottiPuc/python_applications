# -*- coding: utf-8 -*-

from models.database import Database
from menu import Menu

Database.initialize()

menu = Menu()

menu.run_menu()