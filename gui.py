from PyQt5.QtWidgets import QApplication, QLabel, QWidget
import sys

app = QApplication(sys.argv)

window = QWidget()
window.setWindowTitle("Test")
window.setGeometry(750, 300, 400, 400)
window.show()
sys.exit(app.exec_())
