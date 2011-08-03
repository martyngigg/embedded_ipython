import sys

from PyQt4.QtGui import QApplication
from mantidplotlib import MainWindow
from widgets.ipython_view import IPythonView


def qapplication():
    """
    Return QApplication instance
    Creates it if it doesn't already exist
    """
    app = QApplication.instance()
    if not app:
        app = QApplication([])
    return app

def main():
    app = qapplication()
    mainwin = MainWindow()
    shell = IPythonView()
    mainwin.insertPythonShell(shell)
    mainwin.show()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()
