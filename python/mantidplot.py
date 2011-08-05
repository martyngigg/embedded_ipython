import sys
import signal

#from PyQt4.QtGui import QApplication
#from widgets.ipython_view import IPythonView

from IPython.external.qt import QtGui
from IPython.frontend.qt.kernelmanager import QtKernelManager
from IPython.frontend.qt.console.rich_ipython_widget import RichIPythonWidget

from mantidplotlib import MainWindow


def qapplication():
    """
    Return QApplication instance
    Creates it if it doesn't already exist
    """
    app = QtGui.QApplication.instance()
    if not app:
        app = QtGui.QApplication([])
    return app

def init_kernel_manager():
    # Don't let Qt or ZMQ swallow KeyboardInterupts.
    signal.signal(signal.SIGINT, signal.SIG_DFL)

    ip = '127.0.0.1'

    # Create a KernelManager and start a kernel.
    kernel_manager = QtKernelManager(
                            shell_address=(ip, 0),
                            sub_address=(ip, 0),
                            stdin_address=(ip, 0),
                            hb_address=(ip, 0)
                            #,
                            #config=self.config
    )
    # start the kernel
    kwargs = dict(ip='127.0.0.1', ipython=True)
    #kwargs['extra_arguments'] = self.kernel_argv
    kernel_manager.start_kernel(**kwargs)
    kernel_manager.start_channels()
    return kernel_manager
    
def main():
    app = qapplication()
    mainwin = MainWindow()

    shell = RichIPythonWidget(local_kernel=False)
    shell.kernel_manager = init_kernel_manager()
    mainwin.insertPythonShell(shell)
    
    mainwin.show()
    app.exec_()

if __name__ == '__main__':
    main()
