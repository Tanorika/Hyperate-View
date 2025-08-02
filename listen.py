import sys
import json
import ctypes
from PyQt5.QtCore import Qt, QUrl
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5.QtWebEngineWidgets import QWebEngineView

import win32con
import win32gui
import win32api

class TransparentBrowser(QMainWindow):
    def __init__(self, url, x, y, width, height):
        super().__init__()

        # 窗口设置：无边框 + 透明 + 置顶
        self.setWindowFlags(Qt.FramelessWindowHint | Qt.WindowStaysOnTopHint)
        self.setAttribute(Qt.WA_TranslucentBackground, True)

        # 浏览器设置：透明背景
        self.browser = QWebEngineView(self)
        self.browser.setAttribute(Qt.WA_TranslucentBackground, True)
        self.browser.setStyleSheet("background: transparent;")
        self.browser.page().setBackgroundColor(Qt.transparent)
        self.setCentralWidget(self.browser)
        self.browser.load(QUrl(url))

        # 设置窗口大小与位置
        self.setGeometry(x, y, width, height)

        # 启动后设置为点击穿透
        self.setAttribute(Qt.WA_TransparentForMouseEvents, True)  # Qt内层不吃鼠标
        self.setMouseTracking(False)

    def showEvent(self, event):
        super().showEvent(event)
        hwnd = self.winId().__int__()
        ex_style = win32gui.GetWindowLong(hwnd, win32con.GWL_EXSTYLE)
        ex_style |= win32con.WS_EX_LAYERED | win32con.WS_EX_TRANSPARENT
        win32gui.SetWindowLong(hwnd, win32con.GWL_EXSTYLE, ex_style)


def load_config():
    with open("config.json", "r", encoding="utf-8") as f:
        data = json.load(f)
        return (
            data["url"],
            data.get("x", 100),
            data.get("y", 100),
            data.get("width", 500),
            data.get("height", 200)
        )


def main():
    app = QApplication(sys.argv)
    url, x, y, width, height = load_config()
    window = TransparentBrowser(url, x, y, width, height)
    window.show()
    sys.exit(app.exec_())


if __name__ == "__main__":
    main()
