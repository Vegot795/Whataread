import unittest
import customtkinter as ctk
import AddBookMod
from AppMod import App
import EditBookMod
import MoveButtonsMod
import main
from main import app
import BookMod


class TestAppMod(unittest.TestCase):
    def setUp(self):
        self.root = ctk.CTk()

    def tearDown(self):
        self.root.destroy()

    def test_open_add_book(self):
        add_book_window = App.open_add_book()
        self.assertIsNotNone(add_book_window)
        self.assertIsInstance(add_book_window, ctk.CTkToplevel)
        self.assertEqual(add_book_window.title(), "Dodaj książkę")