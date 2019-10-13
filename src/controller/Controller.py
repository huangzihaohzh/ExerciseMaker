from PyQt5.QtWidgets import *
import sys
from entity import Exercise
from entity import Command
from view import Gui
import os

class Controller:

    def __init__(self):
        pass

    # 根据用户输入来控制流程
    def controller(self,args,userInput):
        self.args = args
        self.userInput = userInput
        # 判断用户输入是否为空，若为空则转到GUI界面，否则处理用户输入的命令
        if(len(self.userInput) == 1):
            app = QApplication(sys.argv)
            ex = Gui.Gui()
            sys.exit(app.exec_())
        else:
            command = Command.Command(self.args)
            #command.command()
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
                # 保存题目到文件
                self.writeExerciseAndAnswerFile(exerciseList)










    def readExerciseAndAnswerFile(self):
        pass

    def writeExerciseAndAnswerFile(self,exerciseList = []):
        # 检查文件是否存在，若不存在则创建
        exerciseFile = open(r"./Exercise.txt",'a',encoding='utf8')
        answerFile = open(r"./Answer.txt",'a')
        # 以追加的方式写入文件
        i = 1
        for exercise in exerciseList:
            exerciseFile.write(str(i)+"."+exercise.getExerciseStr()+'\n')
            answerFile.write(str(i)+"."+exercise.getAnswerStr()+'\n')
            i += 1


if __name__ == "__main__":
    print(sys.argv)    # test
    con = Controller()
    con.controller(Command.parse_input(),sys.argv)

