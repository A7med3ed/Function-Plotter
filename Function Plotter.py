import sys

import numpy as np

import matplotlib.pyplot as plt

from PySide2.QtWidgets import (
    QApplication,
    QMainWindow,
    QMessageBox,
    QWidget,
    QVBoxLayout,
    QHBoxLayout,
    QLabel,
    QLineEdit,
    QPushButton,
)

from PySide2.QtCore import Qt

from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas


class Plotter_Window(QMainWindow):
    #constractur to set main window
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Function Evaluation Plotter")

        self.setMinimumSize(800, 600)

        self.GUI()

    #GUI setup to add all widgets to Main Layout
    def GUI(self):

        # Create the main widget and layout
        main_widget = QWidget(self)
        main_layout = QVBoxLayout(main_widget)
        main_layout.setAlignment(Qt.AlignTop)

        # Create the function input section

        #First Section define inner UI as Variables
        function_label = QLabel("Function:")
        self.function_input = QLineEdit()
        self.function_input.setPlaceholderText("Enter a function of x")
        
        #Secound section add all variables to Widget
        function_layout = QHBoxLayout()
        function_layout.addWidget(function_label)
        function_layout.addWidget(self.function_input)

        # Create the Range input section

        #First Section define inner UI as Variables
        range_label = QLabel("Range:")
        self.xmin_input = QLineEdit()
        self.xmin_input.setPlaceholderText("Minimum value of X")
        self.xmax_input = QLineEdit()
        self.xmax_input.setPlaceholderText("Maximum value of X")

        #Secound section add all variables to Widget
        range_layout = QHBoxLayout()
        range_layout.addWidget(range_label)
        range_layout.addWidget(self.xmin_input)
        range_layout.addWidget(self.xmax_input)

        # Create plot button
        plot_button = QPushButton("Plot")
        plot_button.clicked.connect(self.plot_Function)

        # Create plot area
        self.figure = plt.figure()
        self.canvas = FigureCanvas(self.figure)

        # Add all widgets to  Main layout
        main_layout.addLayout(function_layout)
        main_layout.addLayout(range_layout)
        main_layout.addWidget(plot_button)
        main_layout.addWidget(self.canvas)

        # Set the Main widget at center of Main layout
        self.setCentralWidget(main_widget)

    def evaluation(self,expression, x):

        # Replace '^' with '**' 
        expression = expression.replace('^', '**')
    
        # Evaluate the modified expression as normal
        return eval(expression, {'np': np, 'x': x})
    
    def plot_Function(self):

        # Extract input from Text field
        function = self.function_input.text()
        Xmin = self.xmin_input.text()
        Xmax = self.xmax_input.text()

        # Perform input validation and show error message if needed

        try:
            # Convert the input values to appropriate types
            Xmin = np.longlong(Xmin)
            Xmax = np.longlong(Xmax)

            # Generate x values for plot
            x = np.linspace(Xmin, Xmax, 100)
            
            # Evaluate the function and get y values
            y = self.evaluation(function, x)

            # Clear the previous plot and create a new one
            self.figure.clear()
            ax = self.figure.add_subplot(111)
            ax.plot(x, y)
            self.canvas.draw()

        except Exception as error:
             #call fun To create error messageBox
             self.error_message(str(error))
    # create error message 
    def error_message(self, error_message):
        error = QMessageBox(self)
        error.setWindowTitle("Error")
        error.setText("An error occurred:")
        error.setInformativeText(error_message)
        error.setIcon(QMessageBox.Critical)
        error.exec_()

if __name__ == "__main__":

    app = QApplication(sys.argv)

    # Apply a stylesheet 

    app.setStyleSheet("""
        QMainWindow {
            background-color: #f0f0f0;
        }
        QLabel {
            color: #333;
            font-size: 14px;
        }
        QLineEdit {
            background-color: #fff;
            color: #333;
            border: 1px solid #999;
            border-radius: 5px;
            padding: 5px;
            font-size: 14px;
        }
        QPushButton {
            background-color: #4caf50;
            color: #fff;
            border: none;
            border-radius: 5px;
            padding: 8px 16px;
            font-size: 14px;
        }
    """)

    window = Plotter_Window()
    window.show()
    sys.exit(app.exec_())
