import sys
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QVBoxLayout, QTextEdit, QLineEdit, QLabel
from PyQt5.QtCore import QThread, pyqtSignal
import nmap

class Worker(QThread):
    output = pyqtSignal(str)

    def __init__(self, target):
        super().__init__()
        self.target = target

    def run(self):
        scanner = nmap.PortScanner()
        scanner.scan(self.target, '1-1024')
        for host in scanner.all_hosts():
            for proto in scanner[host].all_protocols():
                lport = scanner[host][proto].keys()
                for port in lport:
                    self.output.emit(f'Port : {port}\tState : {scanner[host][proto][port]["state"]}\n')

class App(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setGeometry(300, 300, 280, 170)
        self.setWindowTitle('Nmap Scanner')

        self.scanButton = QPushButton('Scan', self)
        self.scanButton.clicked.connect(self.scan)

        self.targetInput = QLineEdit(self)
        self.resultOutput = QTextEdit(self)
        self.resultOutput.setReadOnly(True)

        vbox = QVBoxLayout()
        vbox.addWidget(QLabel('Target:'))
        vbox.addWidget(self.targetInput)
        vbox.addWidget(self.scanButton)
        vbox.addWidget(QLabel('Result:'))
        vbox.addWidget(self.resultOutput)

        self.setLayout(vbox)

    def scan(self):
        target = self.targetInput.text()
        self.worker = Worker(target)
        self.worker.output.connect(self.update_output)
        self.worker.start()

    def update_output(self, text):
        self.resultOutput.append(text)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = App()
    ex.show()
    sys.exit(app.exec_())
