import sys
import os
from PySide2.QtCore import Slot
from PySide2.QtWidgets import (QApplication, QHBoxLayout, QLabel, QMainWindow, QPushButton,QVBoxLayout, QWidget)
import main


class Widget(QWidget):
    def __init__(self):
        QWidget.__init__(self)
        self.items = 0

        # Create label
        self.right = QVBoxLayout()
        self.label1 = QLabel("Looking for updates...")
        self.right.addWidget(self.label1)

        # Create buttons
        self.download = QPushButton("Download")
        self.run = QPushButton("Run")
        self.right.addWidget(self.download)
        self.download.setEnabled(False)
        self.right.addWidget(self.run)
        self.run.setEnabled(False)

        # QWidget Layout
        self.layout = QHBoxLayout()
        self.layout.addLayout(self.right)

        # Set the layout to the QWidget
        self.setLayout(self.layout)

        # Signals
        self.download.clicked.connect(self.download_latest)
        self.run.clicked.connect(self.run_meter)

        # Check version to choose option
        self.latest = main.latest_version()
        if main.check_version(self.latest) == None:
            self.label1.setText("Click Download to update.")
            self.download.setEnabled(True)
        elif main.check_version():
            self.label1.setText("Ready to update.")
            self.download.setEnabled(True)
            self.run.setEnabled(True)
        else:
            self.label1.setText("You've latest version.")
            self.run.setEnabled(True)

    # Slots
    @Slot()
    def download_latest(self):
        self.label1.setText('Downloading...please wait.')
        self.download.setEnabled(False)
        self.run.setEnabled(False)
        path = os.path.join(os.getcwd(), 'albion-online-stats-linux')
        main.download(path)
        main.version_file(self.latest)
        self.run_meter()
        sys.exit(app.exec_())

    @Slot()
    def run_meter(self):
        print("runinng app")
        sys.exit(app.exec_())


    # Main Window
class Window(QMainWindow):
    def __init__(self, widget):
        QMainWindow.__init__(self)
        self.setWindowTitle("Launcher")
        self.setCentralWidget(widget)


if __name__ == "__main__":
    # Qt Application
    app = QApplication(sys.argv)
    # QWidget
    widget = Widget()
    # QMainWindow using QWidget as central widget
    window = Window(widget)
    window.resize(200, 100)
    window.show()
    # Execute application
    sys.exit(app.exec_())
