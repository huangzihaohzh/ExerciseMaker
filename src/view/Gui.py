from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
import sys
from os import path
from PyQt5.QtWidgets import QMessageBox
<<<<<<< HEAD
from src.entity import Exercise

=======
from entity import Exercise
from controller import Controller
>>>>>>> hzh_dev

class Gui(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        """
        输入：void
        输出：void
        实现功能：设置参数
        """
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
        """
        输入：void
        输出：void
        实现功能：“生成题目”按钮事件处理
        """
        if self.text_num.text():
            if self.text_range.text():
                try:
                    if (int(self.text_num.text()) > 0) & (int(self.text_range.text()) > 0):
                        # 生成练习列表，并自GUI中输出
                        exerciseNum = int(self.text_num.text())
                        exerciseRange = int(self.text_range.text())
                        exerciseMaker = Exercise.Exercise()
                        exerciseList = exerciseMaker.makeExerciseWithNumAndRange(exerciseNum, exerciseRange)
                        outputText = ""    #存储需要显示的字符串
                        for exercise in exerciseList:
                            outputText += "Exercise:" + exercise.getExerciseStr() + "    Answer:" + exercise.getAnswerStr() + "\n"
                        self.textbox.setText(outputText)
                        #保存题目到文件
                        Controller.Controller().writeExerciseAndAnswerFile(exerciseList)
                    else:
                        QMessageBox.information(self, "提示", "请输入大于0的数字。", QMessageBox.Ok)
                except ():
                    QMessageBox.information(self, "提示", "请输入符合要求的数字。", QMessageBox.Ok)
            else:
                QMessageBox.information(self, "提示", "请输入题目数值范围。", QMessageBox.Ok)
        else:
            QMessageBox.information(self, "提示", "请输入题目数量。", QMessageBox.Ok)

    def choose_exercise(self):
        """
        输入：void
        输出：void
        实现功能：“选择题目文件”按钮事件处理
        """
        self.files, files_type = QFileDialog.getOpenFileNames()
        if len(self.files) > 0:
            if len(self.files) == 1:
                self.text_exercise.setText(self.files[0])
            else:
                QMessageBox.information(self, "提示", "请只选择一个文件。", QMessageBox.Ok)

    def choose_answer(self):
        """
        输入：void
        输出：void
        实现功能：“选择答案文件”按钮事件处理
        """
        self.files, files_type = QFileDialog.getOpenFileNames()
        if len(self.files) > 0:
            if len(self.files) == 1:
                self.text_answer.setText(self.files[0])
            else:
                QMessageBox.information(self, "提示", "请只选择一个文件。", QMessageBox.Ok)

    def judge(self):
        """
        输入：void
        输出：void
        实现功能：“判断”按钮事件处理
        """
        if self.text_exercise.text():
            if self.text_answer.text():
                if (path.exists(self.text_exercise.text())) & (path.exists(self.text_answer.text())):
                    # 给定文件判断结果
                    # 获取判断结果列表
                    controller = Controller.Controller()
                    resultList = controller.readExerciseAndAnswerFile(self.text_exercise.text(),self.text_answer.text())
                    # 构造正确结果输出字符串
                    correctResultStr = "Correct:" + str(len(resultList[0])) + "("
                    i = 0
                    while i < len(resultList[0]):
                        correctResultStr = correctResultStr + str(resultList[0][i])
                        if i < len(resultList[0]) - 1:
                            correctResultStr += ','
                        i += 1
                    correctResultStr += ')\n'

                    # 构造错误结果输出字符串
                    wrongResultStr = "Wrong:" + str(len(resultList[1])) + "("
                    i = 0
                    while i < len(resultList[1]):
                        wrongResultStr = wrongResultStr + str(resultList[1][i])
                        if i < len(resultList[1]) - 1:
                            wrongResultStr += ','
                        i += 1
                    wrongResultStr += ')\n'
                    #显示
                    self.textbox.setText(correctResultStr + wrongResultStr)
                else:
                    QMessageBox.information(self, "提示", "请输入合法的文件路径。", QMessageBox.Ok)
            else:
                QMessageBox.information(self, "提示", "请选择答案文件。", QMessageBox.Ok)
        else:
            QMessageBox.information(self, "提示", "请选择题目文件。", QMessageBox.Ok)



# 测试
if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Gui()
    sys.exit(app.exec_())
