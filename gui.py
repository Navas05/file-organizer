import sys
import PyQt6
from PyQt6.QtWidgets import QApplication, QMainWindow, QLabel, QFileDialog, QPushButton, QVBoxLayout, QWidget, QMessageBox
from PyQt6.QtGui import QIcon
from PyQt6.QtCore import Qt
from PyQt6.QtGui import QFont
from main import organize_directory

folder_to_organize = ""
destination_folder = ""

app = QApplication([])

window = QMainWindow()
window.setFixedSize(800, 600)
window.setWindowTitle("File Organizer")
window.setWindowIcon(QIcon('placeholder.png'))

layout = QVBoxLayout()
widget_central = QWidget()

label_choose_message = QLabel("Choose a directory to organize:")
label_choose_message.setAlignment(Qt.AlignmentFlag.AlignCenter)
label_choose_message.setFont(QFont('Arial', 20))

label_choosedest_message = QLabel("Choose a directory as destination:")
label_choosedest_message.setAlignment(Qt.AlignmentFlag.AlignCenter)
label_choosedest_message.setFont(QFont('Arial', 20))

def choose_directory():
    global folder_to_organize
    folder = QFileDialog.getExistingDirectory(window, "Choose a directory to organize")
    if folder:
        label_choose_message.setText(f"Folder chosen to organize:\n{folder}")
        folder_to_organize = folder

def choose_destination_folder():
    global destination_folder
    folder = QFileDialog.getExistingDirectory(window, "Choose where you want your files to go")
    if folder:
        label_choosedest_message.setText(f"Folder chosen as destination:\n{folder}")
        destination_folder = folder

def run_organize_directory():
    if not folder_to_organize or not destination_folder:
        QMessageBox.warning(window, "Warning", "Please choose folders first.")
        return
    else :
        try:
            organize_directory(folder_to_organize, destination_folder)
            QMessageBox.information(window, "Success", "Organization complete!")
        except Exception as e:
            QMessageBox.critical(window, "Fatal error", f"This error happened:\n{e}")

button = QPushButton("Change folder to organize: " + folder_to_organize)
button.setFixedSize(500, 70)
button.clicked.connect(choose_directory)

button2 = QPushButton("Change destination folder: " + folder_to_organize)
button2.setFixedSize(500, 70)
button2.clicked.connect(choose_destination_folder)

button3 = QPushButton("Organize!")
button3.setFixedSize(500, 70)
button3.clicked.connect(run_organize_directory)

layout.addWidget(label_choose_message)
layout.addWidget(button, alignment=Qt.AlignmentFlag.AlignCenter)
layout.addWidget(label_choosedest_message)
layout.addWidget(button2, alignment=Qt.AlignmentFlag.AlignCenter)
layout.addWidget(button3, alignment=Qt.AlignmentFlag.AlignCenter)
widget_central.setLayout(layout)
window.setCentralWidget(widget_central)
window.show()
app.exec()