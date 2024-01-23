import sys
import unittest
from main import MainWindow
from PySide6.QtWidgets import QApplication, QMainWindow


class MyTestCase(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.app = QApplication([])

    @classmethod
    def tearDownClass(cls):
        cls.app.quit()

    def test_single_word_input(self):
        main_window = MainWindow()
        main_window.ui.input.setText("eins")
        main_window.check()
        self.assertEqual(main_window.ui.output.text(), "1")

    def test_two_word_input(self):
        main_window = MainWindow()
        main_window.ui.input.setText("zwei hundert")
        main_window.check()
        self.assertEqual(main_window.ui.output.text(), "200")

    def test_repeated_word_input(self):
        main_window = MainWindow()
        main_window.ui.input.setText("zwei zwei")
        main_window.check()
        self.assertEqual(main_window.ui.output.text(), "Синтаксическая ошибка в слове zwei, разряд единиц не должен повторяться дважды.")

    def test_und_error(self):
        main_window = MainWindow()
        main_window.ui.input.setText("ein und")
        main_window.check()
        self.assertEqual(main_window.ui.output.text(), "Синтаксическая ошибка в слове und, разряд с und не может идти сразу после разряда единиц.")

    def test_5digits_input(self):
        main_window = MainWindow()
        main_window.ui.input.setText("zwei hundert zwei und zwanzig")
        main_window.check()
        self.assertEqual(main_window.ui.output.text(),"222")


if __name__ == '__main__':
    unittest.main()
