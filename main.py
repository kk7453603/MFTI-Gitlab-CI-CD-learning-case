import sys
from PySide6.QtWidgets import QApplication, QMainWindow
from task_1 import Ui_MainWindow as Mw


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Mw()
        self.ui.setupUi(self)
        self.ui.enter_btn.clicked.connect(self.check)
        self.base_numbers = {
            "ein": 1, "eins": 1, "zwei": 2, "drei": 3, "vier": 4, "funf": 5, "sechs": 6, "sieben": 7,
            "acht": 8, "neun": 9
        }
        self.ten_nineteen = {
            "elf": 11, "zwolf": 12, "dreizehn": 13, "vierzehn": 14, "fünfzehn": 15, "sechzehn": 16, "siebzehn": 17,
            "achtzehn": 18, "neunzehn": 19
        }
        self.ten = {"zwanzig": 20, "dreizig": 30, "vierzig": 40, "funfzig": 50, "sechzig": 60, "siebzig": 70,
                    "achtzig": 80, "neunzig": 90}

    def check(self):
        inp_txt = self.ui.input.text()
        parsed_txt = inp_txt.split()

        if len(parsed_txt) == 1:
            if parsed_txt[0] in self.ten:
                self.ui.output.setText(str(self.ten[parsed_txt[0]]))
            elif parsed_txt[0] in self.ten_nineteen:
                self.ui.output.setText(str(self.ten_nineteen[parsed_txt[0]]))
            elif parsed_txt[0] in self.base_numbers:
                self.ui.output.setText(str(self.base_numbers[parsed_txt[0]]))
            else:
                self.ui.output.setText(f"Синтаксическая ошибка в слове {parsed_txt[0]}. Нет такого числа.")

        elif len(parsed_txt) == 2:
            if parsed_txt[0] in self.base_numbers:
                if parsed_txt[1] == "hundert":
                    self.ui.output.setText(str(self.base_numbers[parsed_txt[0]] * 100))
                elif parsed_txt[1] in self.ten or parsed_txt[1] in self.ten_nineteen:
                    self.ui.output.setText(
                        f"Синтаксическая ошибка в слове {parsed_txt[1]}, разряд десятков не должен повторяться дважды.")
                elif parsed_txt[1] in self.base_numbers:
                    self.ui.output.setText(
                        f"Синтаксическая ошибка в слове {parsed_txt[1]}, разряд единиц не должен повторяться дважды.")
                elif parsed_txt[1] == "und":
                    self.ui.output.setText(
                        f"Синтаксическая ошибка в слове {parsed_txt[1]}, разряд с und не может идти сразу после разряда единиц.")
                else:
                    self.ui.output.setText(f"Лексическая ошибка в слове {parsed_txt[1]}")

            elif parsed_txt[0] in self.ten or parsed_txt[0] in self.ten_nineteen or parsed_txt[0] == "und":
                self.ui.output.setText(f"Синтаксическая ошибка в слове {parsed_txt[0]}. Нет такого числа.")
            else:
                self.ui.output.setText(f"Лексическая ошибка в слове {parsed_txt[0]}")

        elif len(parsed_txt) == 3:
            if parsed_txt[0] in self.base_numbers:
                if parsed_txt[1] == "und":
                    if parsed_txt[2] in self.ten:
                        res = self.ten[parsed_txt[2]] + self.base_numbers[parsed_txt[0]]
                        self.ui.output.setText(str(res))

                    elif parsed_txt[2] in self.ten_nineteen or parsed_txt[2] in self.base_numbers:
                        self.ui.output.setText(
                            f"Синтаксическая ошибка в слове {parsed_txt[2]}. После und не может идти число десятичного формата.")
                    else:
                        self.ui.output.setText(f"Лексическая ошибка в слове {parsed_txt[2]}")

                elif parsed_txt[1] == "hundert":

                    if parsed_txt[2] in self.ten_nineteen:
                        res = self.base_numbers[parsed_txt[0]] * 100 + self.ten_nineteen[parsed_txt[2]]
                        self.ui.output.setText(str(res))
                    elif parsed_txt[2] in self.ten:
                        res = self.base_numbers[parsed_txt[0]] * 100 + self.ten[parsed_txt[2]]
                        self.ui.output.setText(str(res))
                    elif parsed_txt[2] in self.base_numbers:
                        res = self.base_numbers[parsed_txt[0]] * 100 + self.base_numbers[parsed_txt[2]]
                        self.ui.output.setText(str(res))
                    elif parsed_txt[2] == "hundert":
                        self.ui.output.setText(
                            f"Синтаксическая ошибка в слове {parsed_txt[2]}. После разряда сотен не могут снова идти сотни.")
                    elif parsed_txt[2] == "und":
                        self.ui.output.setText(
                            f"Синтаксическая ошибка в слове {parsed_txt[2]}. После разряда und ничего нет.")
                    else:
                        self.ui.output.setText(f"Лексическая ошибка в слове {parsed_txt[2]}")

                elif parsed_txt[1] in self.base_numbers or parsed_txt[1] in self.ten or parsed_txt[
                    1] in self.ten_nineteen:
                    self.ui.output.setText(
                        f"Синтаксическая ошибка в слове {parsed_txt[1]}. Второй разряд не может быть сотнями или десятками.")
                else:
                    self.ui.output.setText(f"Лексическая ошибка в слове {parsed_txt[1]}")

            elif parsed_txt[0] in self.ten or parsed_txt[0] in self.ten_nineteen:
                self.ui.output.setText(f"Синтаксическая ошибка в слове {parsed_txt[0]}. Нет такого числа.")
            else:
                self.ui.output.setText(f"Лексическая ошибка в слове {parsed_txt[0]}")

        elif len(parsed_txt) == 4:
            if "und" == parsed_txt[2]:
                if parsed_txt[3] in self.base_numbers:
                    self.ui.output.setText(f"Синтаксическая ошибка: после слова und не может идти разряд единиц.")
                elif parsed_txt[3] in self.ten or parsed_txt[3] in self.ten_nineteen:
                    self.ui.output.setText(f"Синтаксическая ошибка: после слова und не может идти разряд десятков.")
                elif parsed_txt[3] == "hundert":
                    self.ui.output.setText(f"Синтаксическая ошибка: после слова und не может идти разряд сотен.")
                elif parsed_txt[3] == "und":
                    self.ui.output.setText(f"Синтаксическая ошибка: слово und не может повторяться дважды.")
                else:
                    self.ui.output.setText(f"Лексическая ошибка в слове {parsed_txt[3]}")
            else:
                self.ui.output.setText(f"Лексическая ошибка в слове {parsed_txt[2]}")



        # zwei hundert zwei und zwanzig
        elif len(parsed_txt) == 5:
            if parsed_txt[0] in self.base_numbers:
                if parsed_txt[1] == "hundert":
                    if parsed_txt[2] in self.base_numbers:
                        if parsed_txt[3] == "und":
                            if parsed_txt[4] in self.ten:
                                res = self.base_numbers[parsed_txt[2]] + self.ten[parsed_txt[4]] + self.base_numbers[
                                    parsed_txt[0]] * 100
                                self.ui.output.setText(str(res))

                            elif parsed_txt[4] in self.base_numbers:
                                self.ui.output.setText(
                                    f"Синтаксическая ошибка в слове {parsed_txt[4]}. После {parsed_txt[4]} не может идти число единичного разряда.")
                            elif parsed_txt[4] in self.ten_nineteen:
                                self.ui.output.setText(
                                    f"Синтаксическая ошибка в слове {parsed_txt[4]}. После {parsed_txt[4]} не может идти число разряда десятков.")
                            else:
                                self.ui.output.setText(f"Лексическая ошибка в слове {parsed_txt[4]}")

                        elif parsed_txt[3] in self.base_numbers or parsed_txt[3] in self.ten or parsed_txt[
                            3] in self.ten_nineteen:
                            self.ui.output.setText(f"Синтаксическая ошибка в слове {parsed_txt[3]}. Отсутствует und.")
                        else:
                            self.ui.output.setText(f"Лексическая ошибка в слове {parsed_txt[3]}")

                    elif parsed_txt[2] in self.ten or parsed_txt[2] in self.ten_nineteen:
                        self.ui.output.setText(
                            f"Синтаксическая ошибка в слове {parsed_txt[2]}. После {parsed_txt[2]} не может идти ничего, кроме единиц.")
                    else:
                        self.ui.output.setText(f"Лексическая ошибка в слове {parsed_txt[2]}")

                elif parsed_txt[1] in self.base_numbers:
                    self.ui.output.setText(
                        f"Синтаксическая ошибка в слове {parsed_txt[1]}. После единиц не могут снова идти единциы.")
                elif parsed_txt[1] in self.ten or parsed_txt[1] in self.ten_nineteen:
                    self.ui.output.setText(
                        f"Синтаксическая ошибка в слове {parsed_txt[1]}. После {parsed_txt[1]} не может идти разряд десятков.")
                else:
                    self.ui.output.setText(f"Лексическая ошибка в слове {parsed_txt[1]}")

            elif parsed_txt[0] in self.ten or parsed_txt[0] in self.ten_nineteen:
                self.ui.output.setText(f"Синтаксическая ошибка в слове {parsed_txt[0]}. Нет такого числа!")
            else:
                self.ui.output.setText(f"Лексическая ошибка в слове {parsed_txt[0]}")

        else:
            self.ui.output.setText(f"Синтаксическая ошибка в слове {parsed_txt[-1]}. Нет такого числа!")


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())
