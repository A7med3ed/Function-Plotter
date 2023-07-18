# Function-Plotter
This Python program creates a simple GUI application for plotting mathematical functions. It allows users to enter a function and specify a range of x-values, and it will generate a plot of the function over the specified range.

##  Prerequisites
Before running the program, ensure that you have the following libraries installed:

numpy: A library for numerical operations.

matplotlib: A plotting library.

PySide2: A Python binding for the Qt framework.

## Usage
To run the program, execute the following command:

python Function Plotter.py

The application window will open, and you can interact with it using the following steps:

Enter a mathematical function in the "Function" input field. The function should be in terms of x. For example, 5*x^3 + 2*x .
Specify the range of x-values in the "Range" input fields. Enter the minimum value in the "Minimum value of X" field and the maximum value in the "Maximum value of X" field.
Click the "Plot" button to generate the plot of the function.
If any errors occur during the input validation or evaluation of the function, an error message will be displayed in a message box.

The plot will be shown in the plot area of the application window.

## Styling
The application window and its elements are styled using CSS-like stylesheets. The default styling includes a light gray background color for the main window, black text color for labels, white background color with a gray border for text input fields, and a green background color with white text for the plot button. You can modify the styles in the 'app.setStyleSheet()' section of the code.
