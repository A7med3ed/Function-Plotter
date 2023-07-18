from PySide2.QtCore import Qt
from PySide2.QtWidgets import QApplication


def test_Function_Plotter(qtbot):
    # Create the QApplication instance
    app = QApplication([])
    
    # Create widget instance
    widget = Plotter_Window()
    
    # Use the qtbot fixture to listens on signals and events
    qtbot.addWidget(widget)
    
    # Test the function plot
    widget.function_input.setText("5*x**3 + 2*x")
    widget.xmin_input.setText("0")
    widget.xmax_input.setText("10")
    qtbot.mouseClick(widget.plot_button, Qt.LeftButton)

    # Assertions or verifications
    x_data = widget.figure.axes[0].lines[0].get_data()[0]
    y_data = widget.figure.axes[0].lines[0].get_data()[1]

    assert x_data[0] == 0
    assert x_data[-1] == 10
    assert y_data[0] == 0
    assert y_data[-1] == 5020

    # Cleanup
    widget.close()
    app.quit()