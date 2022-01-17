import sys
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtWebEngineWidgets import *


class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.browser = QWebEngineView()
        self.browser.setUrl(QUrl('https://google.com'))
        self.setCentralWidget(self.browser)
        self.showMaximized()

        # Navigation bar
        navbar = QToolBar()
        self.addToolBar(navbar)

        # Home bottom
        home_btn = QAction('Home', self)
        home_btn.triggered.connect(self.navigate_home)
        navbar.addAction(home_btn)

        # Back bottom
        back_btn = QAction('<<Back', self)
        back_btn.triggered.connect(self.browser.back)
        navbar.addAction(back_btn)

        # forward bottom (frd)
        frd_btn = QAction('Forward>>', self)
        frd_btn.triggered.connect(self.browser.forward)
        navbar.addAction(frd_btn)

        # Reload bottom (rld)
        rld_btn = QAction('Reload', self)
        rld_btn.triggered.connect(self.browser.reload)
        navbar.addAction(rld_btn)

        # Add url bar
        self.url_bar = QLineEdit()
        self.url_bar.returnPressed.connect(self.navigate_to_url)
        navbar.addWidget(self.url_bar)

        self.browser.urlChanged.connect(self.update_url)

    # Home method
    def navigate_home(self):
        self.browser.setUrl(QUrl('https://www.google.com'))

    # search bar method
    def navigate_to_url(self):
        url = self.url_bar.text()
        self.browser.setUrl(QUrl(url))

    # url update method
    def update_url(self, g):
        self.url_bar.setText(g.toString())


app = QApplication(sys.argv)
QApplication.setApplicationName('Jamiu Personal Browser')
window = MainWindow()
app.exec_()
