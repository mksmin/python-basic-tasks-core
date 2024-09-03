import sys
from PyQt6.QtCore import Qt, QTimer
from PyQt6.QtWidgets import (
    QApplication,
    QWidget,
    QLCDNumber,
    QSlider,
    QPushButton,
    QVBoxLayout,
    QHBoxLayout
)


class MainWindow(QWidget):
    def __init__(self, default_value=7, min_value=1, max_value=90):
        super().__init__()

        lcd = QLCDNumber(self)
        lcd.display(default_value)

        self.lcd = lcd

        slider = QSlider(Qt.Orientation.Horizontal, self)
        # Устанавливаем мин и макс слайдера
        slider.setMinimum(min_value)
        slider.setMaximum(max_value)
        slider.setValue(default_value)
        slider.valueChanged[int].connect(lcd.display)
        self.slider = slider

        start_button = QPushButton("Start", self)
        start_button.clicked[bool].connect(self.start_button_clicked)
        self.start_button = start_button

        hbox = QHBoxLayout()
        hbox.addWidget(slider)
        hbox.addWidget(start_button)

        vbox = QVBoxLayout()
        vbox.addWidget(lcd)
        vbox.addLayout(hbox)

        self.setLayout(vbox)

        self.setWindowTitle('Test PyQT')
        self.resize(400, 300)

    def toggle_interface(self, value=True):
        self.start_button.setEnabled(value)
        self.slider.setEnabled(value)

    def start_button_clicked(self):
        # запустить отсчет
        self.toggle_interface(False)
        self.tick_timer()

    def tick_timer(self):
        lcd_value = self.lcd.value()
        if lcd_value > 0:
            self.lcd.display(lcd_value - 1)
            QTimer().singleShot(1000, self.tick_timer)
        else:
            self.toggle_interface()
            self.lcd.display(self.slider.value())






def main():
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())



if __name__ == "__main__":
    main()