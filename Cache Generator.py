from PySide2 import QtGui,QtWidgets,QtCore
import os
import sys


class CacheGenerator(QtWidgets.QMainWindow):
    def _int_(self):
        super(CacheGenerator, self)._init_()
        self.create_Ui()

    def create_Ui(self):
        self.setWindowTitle("Cache Generator Tool")
        self.resize(500, 750)

        main_widget =QtWidgets.QWidget()
        self.setCentralWidget(main_widget)

        self.ver_lay = QtWidgets.QVBoxLayout()
        main_widget.setLayout(self.ver_lay)

        self.hor_lay = QtWidgets.QHBoxLayout()
        self.ver_lay.addLayout(self.hor_lay)
        self.grid_layout = QtWidgets.QGridLayout()


        self.label = QtGui.QLabel('Path')
        self.line_edit = QtGui.QLineEdit()
        self.geometry_radio_btn = QtGui.QRadioButton('Geometry Cache')
        self.alembic_radio_btn = QtGui.QRadioButton('Alembic Cache')
        self.fluid_radio_btn = QtGui.QRadioButton('GPU Cache')

        self.hor_lay.addWidget(self.geometry_radio_btn,0,0)
        self.hor_lay.addWidget(self.alembic_radio_btn,0,1)
        self.hor_lay.addWidget(self.geometry_radio_btn,0,2)

        self.generate_btn = QtGui.QPushButton('Generate Cache')

        self.grid_layout.addWidget(self.label, 0, 1)
        self.grid_layout.addWidget(self.line_edit,0,2)
        # self.grid_layout.addWidget(self.geometry_radio_btn,1,0)
        # self.grid_layout.addWidget(self.alembic_radio_btn,1,1)
        # self.grid_layout.addWidget(self.fluid_radio_btn,1,2)
        self.grid_layout.addWidget(self.generate_btn,2,2)

        self.generate_btn.clicked.connect(self.generate_cache)
        self.ver_lay.addLayout(self.grid_layout)
        self.show()

    def generate_cache(self):
        pass


if _name_ == '_main_':
    app = QtWidgets.QApplication(sys.argv)
    cache_tool = CacheGenerator()
    cache_tool.show()
    sys.exit(app.exec_())