import logging
import threading

from PyQt5 import QtWidgets

from gui.main_window import MainWindow
from service.time_notifier import TimeNotifier


def main():
    import sys
    time_notifier = TimeNotifier()
    app = QtWidgets.QApplication(sys.argv)
    with open("stylesheet/style.qss") as f:
        app.setStyleSheet("\n".join(f.readlines()))
        logging.info("Stylesheets are included")
    window = MainWindow(time_notifier)
    window.show()
    logging.info("Show main window, starting main thread")
    main_thread = threading.Thread(target=app.exec_)
    main_thread.run()


if __name__ == "__main__":
    logging_format = "%(asctime)s: %(message)s"
    logging.basicConfig(format=logging_format, level=logging.INFO, datefmt="%H:%M:%S")
    logging.info("Starting main...")
    main()
