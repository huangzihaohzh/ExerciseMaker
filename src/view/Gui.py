from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
import sys
from os import path
from PyQt5.QtWidgets import QMessageBox

class Gui(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        # 设置窗口
        self.setGeometry(800, 300, 570, 480)
        self.setFixedSize(self.width(), self.height())
        self.setWindowTitle('四则运算题目生成器')
        self.setWindowFlag(Qt.WindowStaysOnTopHint)
        # 窗口居中
        qr = self.frameGeometry()
        cp = QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())
        # 相关组件
        self.btn_generate = QPushButton('生成题目', self)
        self.btn_generate.setGeometry(QRect(460, 10, 100, 30))
        self.btn_generate.clicked.connect(self.generate_exercise)
        self.btn_choose_exercise = QPushButton('选择题目文件', self)
        self.btn_choose_exercise.setGeometry(QRect(10, 50, 100, 30))
        self.btn_choose_exercise.clicked.connect(self.choose_exercise)
        self.btn_choose_answer = QPushButton('选择答案文件', self)
        self.btn_choose_answer.setGeometry(QRect(10, 90, 100, 30))
        self.btn_choose_answer.clicked.connect(self.choose_answer)
        self.btn_judge = QPushButton('判断', self)
        self.btn_judge.setGeometry(QRect(500, 50, 60, 70))
        self.btn_judge.clicked.connect(self.judge)
        self.textbox = QTextBrowser(self)
        self.textbox.setGeometry(QRect(10, 130, 550, 340))
        self.label_1 = QLabel('题目数量：', self)
        self.label_1.setGeometry(QRect(10, 15, 70, 20))
        self.label_2 = QLabel('题目数值范围：', self)
        self.label_2.setGeometry(QRect(220, 15, 100, 20))
        self.text_num = QLineEdit(self)
        self.text_num.setGeometry(QRect(90, 10, 113, 30))
        self.text_num.setPlaceholderText('10')
        self.text_range = QLineEdit(self)
        self.text_range.setGeometry(QRect(330, 10, 113, 30))
        self.text_range.setPlaceholderText('10')
        self.text_exercise = QLineEdit(self)
        self.text_exercise.setGeometry(QRect(120, 50, 370, 30))
        self.text_exercise.setPlaceholderText(path.join(path.expanduser("~"), 'Desktop'))
        self.text_answer = QLineEdit(self)
        self.text_answer.setGeometry(QRect(120, 90, 370, 30))
        self.text_answer.setPlaceholderText(path.join(path.expanduser("~"), 'Desktop'))

        self.show()

    def generate_exercise(self):
        if self.text_num.text():
            if self.text_range.text():
                try:
                    if (int(self.text_num.text())>0) & (int(self.text_range.text())>0):
                        pass
                    else:
                        QMessageBox.information(self, "提示", "请输入大于0的数字。", QMessageBox.Ok)
                except:
                    QMessageBox.information(self, "提示", "请输入符合要求的数字。", QMessageBox.Ok)
            else:
                QMessageBox.information(self, "提示", "请输入题目数值范围。", QMessageBox.Ok)
        else:
            QMessageBox.information(self, "提示", "请输入题目数量。", QMessageBox.Ok)

    def choose_exercise(self):
        self.files, files_type = QFileDialog.getOpenFileNames()
        if len(self.files) > 0:
            if len(self.files) == 1:
                self.text_exercise.setText(self.files[0])
            else:
                QMessageBox.information(self, "提示", "请只选择一个文件。", QMessageBox.Ok)

    def choose_answer(self):
        self.files, files_type = QFileDialog.getOpenFileNames()
        if len(self.files) > 0:
            if len(self.files) == 1:
                self.text_answer.setText(self.files[0])
            else:
                QMessageBox.information(self, "提示", "请只选择一个文件。", QMessageBox.Ok)

    def judge(self):
        if self.text_exercise.text():
            if self.text_answer.text():
                if (path.exists(self.text_exercise.text())) & (path.exists(self.text_answer.text())):
                    pass
                else:
                    QMessageBox.information(self, "提示", "请输入合法的文件路径。", QMessageBox.Ok)
            else:
                QMessageBox.information(self, "提示", "请选择答案文件。", QMessageBox.Ok)
        else:
            QMessageBox.information(self, "提示", "请选择题目文件。", QMessageBox.Ok)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Gui()
    sys.exit(app.exec_())
