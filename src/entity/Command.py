from argparse import ArgumentParser
from os import path
import os
import sys
curPath = os.path.abspath(os.path.dirname(__file__))
rootPath = os.path.split(curPath)[0]
sys.path.append(os.path.split(rootPath)[0])

class Command:
    def __init__(self, input_args):
        self.args = input_args  # 存放来自用户的输入
        self.exerciseNum = 10  # 存放生成题目的数量，默认为10
        self.exerciseRange = 10  # 存放题目中自然数、真分数、真分数分母的取值范围，默认为10
        self.exerciseFile = ""  # 指向用户输入的已存在的题目文档，默认为null
        self.answerFile = ""  # 指向用户输入的已存在的答案文档，默认为null
        self.command()

    def command(self):
        """
        输入：用户输入的参数字符串数组
        输出：void
        实现功能：检查用户输入，将用户输入保存到inputStr，并从用户输入解析出exerciseNum、exerciseRange、exerciseFile、answerFile
        """
        if self.args.number:
            if self.args.number <= 0:
                print("参数出错, 请检查参数")
            else:
                self.exerciseNum = self.args.number
        if self.args.range:
            if self.args.range <= 0:
                print("参数出错, 请检查参数")
            else:
                self.exerciseRange = self.args.range
        if self.args.exercise:
            if self.args.answer:
                if path.exists(self.args.exercise):
                    self.exerciseFile = self.args.exercise
                else:
                    print("参数出错, 请检查参数")
                if path.exists(self.args.answer):
                    self.answerFile = self.args.answer
                else:
                    print("参数出错, 请检查参数")
            else:
                print("参数出错, 请检查参数")
        elif self.args.answer:
            print("参数出错, 请检查参数")


    def getExerciseNum(self):
        """
        输入：void
        输出：int
        实现功能：返回exerciseNum
        """
        return self.exerciseNum

    def getExerciseRange(self):
        """
        输入：void
        输出：int
        实现功能：返回exerciseRange
        """
        return self.exerciseRange

    def getExerciseFile(self):
        """
        输入：void
        输出：文件类型
        实现功能：返回exerciseFile
        """
        return self.exerciseFile

    def getAnswerFile(self):
        """
        输入：void
        输出：文件类型
        实现功能：返回answerFile
        """
        return self.answerFile



# 测试
if __name__ == '__main__':
    args = parse_input()
    com = Command(args)
    print("exercise num:", com.getExerciseNum())
    print("exercise range:", com.getExerciseRange())
    print("exercise file:", com.getExerciseFile())
    print("answer file:", com.getAnswerFile())