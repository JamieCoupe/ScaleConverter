import sys
from PyQt5.QtWidgets import *
from PyQt5.QtCore import pyqtSlot
import scaleconverter_cli as sccli


class ScaleConverter(QDialog):

    def __init__(self):
        super().__init__()
        self.title = 'Scale Converter V1'
        self.left = 10
        self.top = 10
        self.width = 320
        self.height = 100
        self.init_ui()

    def init_ui(self):
        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)

        self.create_input_group()
        self.create_output_group()
        self.scale_selector = QComboBox()
        self.scale_selector.addItems(['N', 'OO', 'cg3', "3 1/2 Inch", "5 Inch", "7 1/4 Inch"])
        windowLayout = QVBoxLayout()
        windowLayout.addWidget(QLabel('Scale:'))
        windowLayout.addWidget(self.scale_selector)
        windowLayout.addWidget(self.inputGroupBox)
        windowLayout.addWidget(self.outputGroupBox)
        self.setLayout(windowLayout)

        self.show()

    def create_input_group(self):
        self.inputGroupBox = QGroupBox("Real Input")
        layout = QHBoxLayout()

        self.meters_in = QLineEdit()
        self.feet_in = QLineEdit('0')
        self.inches_in = QLineEdit('0')
        self.fractions_in = QLineEdit('0')

        layout.addWidget(QLabel('Meters'))
        layout.addWidget(self.meters_in)
        layout.addWidget(QLabel('Feet'))
        layout.addWidget(self.feet_in)
        layout.addWidget(QLabel('Inches'))
        layout.addWidget(self.inches_in)
        layout.addWidget(QLabel('Fractions'))
        layout.addWidget(self.fractions_in)

        self.inputGroupBox.setLayout(layout)

    def create_output_group(self):
        self.outputGroupBox = QGroupBox("Scale Output")
        layout = QHBoxLayout()

        self.measurement_out = QLineEdit()
        self.convert_button = QPushButton('Convert')
        self.convert_button.clicked.connect(self.convert_click)
        layout.addWidget(self.convert_button)
        layout.addWidget(QLabel('Output:'))
        layout.addWidget(self.measurement_out)

        self.outputGroupBox.setLayout(layout)

    @pyqtSlot()
    def convert_click(self):
        scale = 0
        scale_selector = self.scale_selector.currentText()
        if scale_selector in ['N']:
            scale = 2
        elif scale_selector in ['OO']:
            scale = 4
        elif scale_selector in ['3 1/2 Inch']:
            scale = 19.05
        elif scale_selector in ['5 Inch']:
            scale = 26.98
        elif scale_selector in ['7 1/4 Inch']:
            scale = 38.1
        elif scale_selector in ['cg3']:
            scale = 18.14

        total_feet = f'{self.feet_in.text()} {self.inches_in.text()} {self.fractions_in.text()}'

        if self.meters_in.text() in [None, ''] and total_feet not in ['  ']:
            result = sccli.convert_feet_to_scale(total_feet, scale)
        elif len(self.meters_in.text()) > 0:
            result = sccli.convert_meter_to_scale(float(self.meters_in.text()), scale)

        self.measurement_out.setText(f'{str(round(result, 2))}mm')


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = ScaleConverter()
    sys.exit(app.exec_())
