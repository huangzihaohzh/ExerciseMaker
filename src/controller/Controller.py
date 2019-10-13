from PyQt5.QtWidgets import *
import sys
from entity import Exercise
from entity import Command
from view import Gui

class Controller:

    def __init__(self,args,userInput):
        self.args = args
        self.userInput = userInput

    # 根据用户输入来控制流程
    def controller(self):
        # 判断用户输入是否为空，若为空则转到GUI界面，否则处理用户输入的命令
        if(len(self.userInput) == 1):
            app = QApplication(sys.argv)
            ex = Gui.Gui()
            sys.exit(app.exec_())
        else:
            command = Command.Command(self.args)
            # 根据用户输入的参数的不同实现不同功能
            # 用户没有指定读取的文件时
            if(command.getExerciseFile() == "" or command.getAnswerFile() == ""):
                exerciseNum = command.getExerciseNum()
                exerciseRange = command.getExerciseRange()
                exerciseList = Exercise.Exercise().makeExerciseWithNumAndRange(exerciseNum,exerciseRange)
                # 打印题目
                outputText = ""
                for exercise in exerciseList:
                    outputText += "Exercise:" + exercise.getExerciseStr() + "    Answer:" + exercise.getAnswerStr() + "\n"
                print(outputText)









    def readExerciseAndAnswerFile(self):
        pass

    def writeExerciseAndAnswerFile(self):
        # 检查文件是否存在，若不存在则创建

        #获取题目列表，
        pass

if __name__ == "__main__":
    print(sys.argv)    # test
    con = Controller(Command.parse_input(),sys.argv)
    con.controller()

