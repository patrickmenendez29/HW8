from PyQt5.QtWidgets import QWidget, QApplication, QVBoxLayout, QLabel, QDialogButtonBox, QPushButton

if __name__ == '__main__':
    app = QApplication([])
    window = QWidget()

    add_category_push_button = QPushButton("Add category")
    add_category_dialog_box = QDialogButtonBox(add_category_push_button)

    label = QLabel("Hello World")
    layout = QVBoxLayout()
    layout.addWidget(label)
    layout.addWidget(add_category_dialog_box)
    window.setLayout(layout)
    window.show()
    app.exec_()