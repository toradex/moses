import sys
import os
import distro
import gpiod
import PySide2
from PySide2.QtWidgets import QApplication
from PySide2.QtCore import QUrl, QObject
from PySide2.QtQuick import QQuickView

if __name__ == "__main__":
    print("TORIZON :: %s" % (os.environ.get("TORIZON")))     

    chip = gpiod.chip(1)    

    print(F"Inspecting GPIO chip {chip.name}")

    for line in gpiod.line_iter(chip):        
        print(F"{line.offset}\t{line.name}\t{line.consumer}\t{line.direction}")

    # qt
    app = QApplication(sys.argv)

    view = QQuickView()

    qml = QUrl("mainwindow.qml")

    view.setSource(qml)
    view.show()

    root = view.rootObject()

    text = root.findChild(QObject, "mytext")
    button = root.findChild(QObject, "mybutton")

    button.clicked.connect(
        lambda: (
            text.setProperty("text", distro.linux_distribution()[0]),
            print("button pressed.")))

    sys.exit(app.exec_())
