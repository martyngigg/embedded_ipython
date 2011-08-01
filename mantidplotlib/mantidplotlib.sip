%Module mantidplotlib 0

%Import QtCore/QtCoremod.sip
%Import QtGui/QtGuimod.sip

class MainWindow : QMainWindow
{
%TypeHeaderCode
#include "mainwindow.h"
%End

public:
    MainWindow();
    ~MainWindow();

    void insertPythonShell(QWidget*);

private slots:
    void newFile();
    void open();
    void save();
    void saveAs();
    void about();
    void aboutQt();
};
