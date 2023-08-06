from PyQt5.QtCore import Qt, QMetaObject, pyqtSlot
from PyQt5.QtWidgets import (
    QWidget,
    QVBoxLayout,
    QHBoxLayout,
    QToolButton,
    QLabel,
    QSizePolicy,
)

from folderplay.utils import resource_path


class TitleBar(QWidget):
    """ Window dragger.

        Args:
            window (QWidget): Associated window.
            parent (QWidget, optional): Parent widget.
    """

    def __init__(self, window, parent=None):
        QWidget.__init__(self, parent)

        self._window = window
        self._mousePressed = False

        self.setObjectName("titleBar")
        self.setSizePolicy(QSizePolicy.Preferred, QSizePolicy.Fixed)

        layout = QHBoxLayout(self)
        layout.setContentsMargins(0, 0, 0, 0)
        layout.setSpacing(0)

        self.lblTitle = QLabel("Title")
        self.lblTitle.setObjectName("lblTitle")
        self.lblTitle.setAlignment(Qt.AlignCenter)
        layout.addWidget(self.lblTitle)

        spButtons = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)

        self.btnMinimize = QToolButton(self)
        self.btnMinimize.setObjectName("btnMinimize")
        self.btnMinimize.setSizePolicy(spButtons)
        layout.addWidget(self.btnMinimize)

        self.btnRestore = QToolButton(self)
        self.btnRestore.setObjectName("btnRestore")
        self.btnRestore.setSizePolicy(spButtons)
        self.btnRestore.setVisible(False)
        layout.addWidget(self.btnRestore)

        self.btnMaximize = QToolButton(self)
        self.btnMaximize.setObjectName("btnMaximize")
        self.btnMaximize.setSizePolicy(spButtons)
        layout.addWidget(self.btnMaximize)
        self.btnMaximize.setVisible(False)

        self.btnClose = QToolButton(self)
        self.btnClose.setObjectName("btnClose")
        self.btnClose.setSizePolicy(spButtons)
        layout.addWidget(self.btnClose)

    def mousePressEvent(self, event):
        self._mousePressed = True
        self._mousePos = event.globalPos()
        self._windowPos = self._window.pos()

    def mouseMoveEvent(self, event):
        if self._mousePressed:
            self._window.move(
                self._windowPos + (event.globalPos() - self._mousePos)
            )

    def mouseReleaseEvent(self, event):
        self._mousePressed = False


class ModernWindow(QWidget):
    """ Modern window.

        Args:
            w (QWidget): Main widget.
            parent (QWidget, optional): Parent widget.
    """

    def __init__(self, parent):
        QWidget.__init__(self, parent)
        # Main frame with round borders
        self.windowFrame = QWidget(self)
        self.windowFrame.setObjectName("windowFrame")

        # Title bar and content widgets
        self.titleBar = TitleBar(self.parent(), self.windowFrame)
        self.titleBar.lblTitle.setText(self.parent().windowTitle())

        self.windowContent = QWidget(self.windowFrame)

        # windowFrame's layout that holds the titlebar and content widgets
        self.vboxFrame = QVBoxLayout(self.windowFrame)
        self.vboxFrame.setContentsMargins(0, 0, 0, 0)
        self.vboxFrame.addWidget(self.titleBar)
        self.vboxFrame.addWidget(self.windowContent)

        # Layout that holds the main frame
        self.vboxWindow = QVBoxLayout(self)
        self.vboxWindow.setContentsMargins(0, 0, 0, 0)
        self.vboxWindow.addWidget(self.windowFrame)

        # Disable parent's window frame
        self.parent().setWindowFlags(
            Qt.Window | Qt.FramelessWindowHint | Qt.WindowSystemMenuHint
        )
        # Without this the edges will be sharp
        self.parent().setAttribute(Qt.WA_TranslucentBackground)

        # set stylesheet
        with open(resource_path("styles/frameless.qss")) as stylesheet:
            self.setStyleSheet(stylesheet.read())

        # automatically connect slots
        QMetaObject.connectSlotsByName(self)

    def setLayout(self, layout):
        self.windowContent.setLayout(layout)

    @pyqtSlot()
    def on_btnMinimize_clicked(self):
        self.parent().setWindowState(Qt.WindowMinimized)

    @pyqtSlot()
    def on_btnRestore_clicked(self):
        self.titleBar.btnRestore.setVisible(False)
        self.setWindowState(Qt.WindowNoState)

    @pyqtSlot()
    def on_btnMaximize_clicked(self):
        self.titleBar.btnRestore.setVisible(True)
        self.setWindowState(Qt.WindowMaximized)

    @pyqtSlot()
    def on_btnClose_clicked(self):
        self.parent().close()
