import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLineEdit, QGridLayout , QPushButton 
from PyQt5.QtCore import Qt


class Calculator(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Hesap Makinası")
        self.setGeometry(100,100,400,500)

        self.result_display = QLineEdit(self)
        self.result_display.setAlignment(Qt.AlignRight)
        self.result_display.setReadOnly(True)
        self.result_display.setFixedHeight(80)
        self.result_display.setStyleSheet("font-size:30px;")


        self.init_ui()

    def init_ui(self):
        layout = QGridLayout()

        buttons = [
            ('7', 1, 0), ('8', 1, 1), ('9', 1, 2), ('/', 1, 3),
            ('4', 2, 0), ('5', 2, 1), ('6', 2, 2), ('*', 2, 3),
            ('1', 3, 0), ('2', 3, 1), ('3', 3, 2), ('-', 3, 3),
            ('0', 4, 0), ('.', 4, 1), ('=', 4, 2), ('+', 4, 3)
        ]
        for text, row ,col in buttons:
            button = QPushButton(text)
            button.clicked.connect(self.on_button_click)
            layout.addWidget(button, row, col)

        layout.addWidget(self.result_display,0,0,1,4,)
        self.setLayout(layout)

    def on_button_click(self):
        sender = self.sender()
        text = sender.text()

        if text == "=":
            try:
                result = eval(self.result_display.text())
                self.result_display.setText(str(result))
            except Exception as e:
                self.result_display.setText("Hata")
        else:
            current_text = self.result_display.text()
            self.result_display.setText(current_text + text)         
    
def main():
    app = QApplication(sys.argv)
    window = Calculator()
    window.show()
    sys.exit(app.exec_())
if __name__ == "__main__":
    main()