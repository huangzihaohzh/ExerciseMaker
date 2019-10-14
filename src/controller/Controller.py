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
                exerciseMaker = Exercise.Exercise()
                exerciseList = exerciseMaker.makeExerciseWithNumAndRange(exerciseNum,exerciseRange)
                # 打印题目
                outputText = ""
                for exercise in exerciseList:
                    outputText += "Exercise:" + exercise.getExerciseStr() + "    Answer:" + exercise.getAnswerStr() + "\n"
                print(outputText)
                # 保存题目到文件
                self.writeExerciseAndAnswerFile(exerciseList)
            # 用户有指定读取文件时
            elif(command.getExerciseFile() != "" and command.getAnswerFile() != ""):
                # 获取判断结果列表
                resultList = self.readExerciseAndAnswerFile(command.getExerciseFile(),command.getAnswerFile())
                # 构造正确结果输出字符串
                correctResultStr = "Correct:" + str(len(resultList[0])) + "("
                i = 0
                while i < len(resultList[0]):
                    correctResultStr = correctResultStr + str(resultList[0][i])
                    if i < len(resultList[0])-1:
                        correctResultStr += ','
                    i += 1
                correctResultStr += ')\n'

                # 构造错误结果输出字符串
                wrongResultStr = "Wrong:" + str(len(resultList[1])) + "("
                i = 0
                while i < len(resultList[1]):
                    wrongResultStr = wrongResultStr + str(resultList[1][i])
                    if i < len(resultList[1])-1:
                        wrongResultStr += ','
                    i += 1
                wrongResultStr += ')\n'

                # 显示
                print(correctResultStr + wrongResultStr)



    def readExerciseAndAnswerFile(self,exerciseFilePath="",answerFilePath=""):
        #读取文件
        try:
            exerciseFile = open(exerciseFilePath,'r',encoding="utf8")
            answerFile = open(answerFilePath,'r',encoding="utf8")
        except:
            print("文件读取失败")
        #逐行读取题目文件和答案文件，生成Exercise对象并判断对错
        exerciseLine = []
        for line in exerciseFile:
            exerciseLine.append(line.split('.')[1])
        answerLine = []
        for line in answerFile:
            answerLine.append(line.split('.')[1])
        # 创建Exercise对象的列表
        exerciseList = []
        i = 0
        for exerciseStr in exerciseLine:
            exerciseTemp = Exercise.Exercise()
            exerciseTemp.makeExerciseByStr(exerciseStr,answerLine[i])
            exerciseList.append(exerciseTemp)
            i += 1
        # 检查结果是否正确并以列表的形式保存
        correctList = []
        wrongList = []
        i = 1
        for exercise in exerciseList:
            if(exercise.isRight()):
                correctList.append(i)
            else:
                wrongList.append(i)
            i += 1
        # 返回包含正确题号列表和错误题号列表的列表
        return [correctList,wrongList]

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
        exerciseFile.close()
        answerFile.close()


if __name__ == "__main__":
    print(sys.argv)    # test
    con = Controller()
    con.controller(Command.parse_input(),sys.argv)

