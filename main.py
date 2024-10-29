import sys

from PyQt6.QtCore import Qt, QLine
from PyQt6.QtWidgets import QApplication, QWidget, QVBoxLayout, QStackedWidget, QLabel

from pages.categories import CategoriesPage
from widgets.bottom_navigation import BottomNavigationBar
from widgets.top_navigation import TopNavigationBar


class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Recipes")
        self.setFixedSize(430, 800)
        self.main_layout = QVBoxLayout()
        self.main_layout.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.__set_up_layout()
        self.setStyleSheet("background-color: #1C0F0D;")

    def __set_up_layout(self) -> None:
        top_navigation_bar = TopNavigationBar()
        self.stacked_widget = QStackedWidget()

        categories_page = CategoriesPage()
        self.stacked_widget.addWidget(categories_page)
        categories_page.categoryItemSignal.connect(self.create_a_new_page)

        bottom_navigation_bar = BottomNavigationBar()
        self.main_layout.addWidget(top_navigation_bar, alignment=Qt.AlignmentFlag.AlignTop)
        self.main_layout.addWidget(self.stacked_widget, alignment=Qt.AlignmentFlag.AlignHCenter)
        self.main_layout.addWidget(bottom_navigation_bar, alignment=Qt.AlignmentFlag.AlignHCenter | Qt.AlignmentFlag.AlignBottom)
        self.setLayout(self.main_layout)

    def create_a_new_page(self, title):
        label = QLabel(title)
        self.stacked_widget.addWidget(label)
        self.stacked_widget.setCurrentWidget(label)


app = QApplication(sys.argv)
app.setStyleSheet("* {padding: 0px; margin: 0px;}")
window = MainWindow()
window.show()

sys.exit(app.exec())
