
from PyQt5 import QtCore, QtGui, QtWidgets, QtWebEngineWidgets
import concurrent.futures
import threading
class Widget(QtWidgets.QWidget):
    def __init__(self, parent=None):
        super(Widget, self).__init__(parent)
        # defining shotcuts
        self.shortcut_open = QtWidgets.QShortcut(QtGui.QKeySequence('f5'), self)
        self.shortcut_open.activated.connect(self.download)
        self.setWindowTitle("J.A.R.V.I.S")
        self.setFixedSize(700,700)
        self.setWindowFlag(QtCore.Qt.FramelessWindowHint)
        self.setStyleSheet('background-color: black;color:white')
        self.view = QtWebEngineWidgets.QWebEngineView()
        self.view .setContextMenuPolicy(QtCore.Qt.NoContextMenu)
        self.view.page().profile().downloadRequested.connect(self.on_downloadRequested)
        self.view.load(QtCore.QUrl(""))
        hbox = QtWidgets.QHBoxLayout(self)
        hbox.addWidget(self.view)
        self.setWindowIcon(QtGui.QIcon(os.path.join('images', 'source.png')))
