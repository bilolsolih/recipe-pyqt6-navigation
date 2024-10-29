from PyQt6.QtCore import Qt, pyqtSignal
from PyQt6.QtWidgets import QWidget, QGridLayout, QVBoxLayout, QScrollArea

from widgets.category import CategoryItem


class CategoriesPage(QScrollArea):
    categoryItemSignal = pyqtSignal(str)

    def __init__(self, columns: int = 2):
        super().__init__()
        self.columns = columns
        self.widget = QWidget()

        self.__set_up_layout()
        self.setWidget(self.widget)
        self.setVerticalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOff)
        self.setStyleSheet("border: null;")

    def get_items(self) -> list[QWidget]:
        items = [
            CategoryItem("Lunch", "assets/lunch.png", 160, 145),
            CategoryItem("Breakfast", "assets/breakfast.png", 160, 145),
            CategoryItem("Dinner", "assets/dinner.png", 160, 145),
            CategoryItem("Vegan", "assets/vegan.png", 160, 145),
            CategoryItem("Dessert", "assets/dessert.png", 160, 145),
            CategoryItem("Drinks", "assets/drinks.png", 160, 145)
        ]

        for item in items:
            item.categoryItemSignal.connect(lambda title: self.categoryItemSignal.emit(title))
        return items

    def get_item_main(self) -> QWidget:
        return CategoryItem("Seafood", "assets/seafood.png", 356, 149, reverse_title_and_photo=True)

    def __set_up_layout(self) -> None:
        layout = QGridLayout()
        layout.setHorizontalSpacing(20)
        layout.setVerticalSpacing(0)
        layout.setAlignment(Qt.AlignmentFlag.AlignCenter)

        column_index = 0
        row_index = 0

        for item in self.get_items():
            layout.addWidget(item, row_index, column_index)
            column_index += 1
            if column_index >= self.columns:
                row_index += 1
                column_index = 0

        main_layout = QVBoxLayout()
        main_layout.setAlignment(Qt.AlignmentFlag.AlignCenter)
        main_layout.addWidget(self.get_item_main())
        main_layout.addLayout(layout)

        self.widget.setLayout(main_layout)
