from argparse import ArgumentParser
from os import path

def parse_input():
    parser = ArgumentParser(description="Input relevant parameters to generate four primary school operation problems, default is 10.")
    parser.add_argument('-n', '--number', type=int, help="Control the number of generated questions, default is 10.")
    parser.add_argument('-r', '--range', type=int, help="Controls the range of values (natural Numbers, true fractions, and true fraction denominators).")
    parser.add_argument('-e', '--exercise', type=str, help="Given exercise file.")
    parser.add_argument('-a', '--answer', type=str, help="Given answer file, for two files, make a number of statistics")
    args = parser.parse_args()
    return args

class Command:
    def __init__(self, input_args):
        self.args = input_args  # 存放来自用户的输入
        self.exerciseNum = 10  # 存放生成题目的数量，默认为10
        self.exerciseRange = 10  # 存放题目中自然数、真分数、真分数分母的取值范围，默认为10
        self.exerciseFile = ""  # 指向用户输入的已存在的题目文档，默认为null
        self.answerFile = ""  # 指向用户输入的已存在的答案文档，默认为null

    def command(self):
        """
        输入：用户输入的参数字符串数组
        输出：void
        实现功能：检查用户输入，将用户输入保存到inputStr，并从用户输入解析出exerciseNum、exerciseRange、exerciseFile、answerFile
        """
        if self.args.number:
            if self.args.number <= 0:
                print(1)
            else:
                self.exerciseNum = self.args.number
        if self.args.range:
            if self.args.range <= 0:
                print(2)
            else:
                self.exerciseRange = self.args.range
        if self.args.exercise:
            if self.args.answer:
                if path.exists(self.args.exercise):
                    self.exerciseFile = self.args.exercise
                else:
                    print(3)
                if path.exists(self.args.answer):
                    self.answerFile = self.args.answer
                else:
                    print(4)
            else:
                print(5)
        elif self.args.answer:
            print(6)


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

if __name__ == '__main__':
    args = parse_input()
    com = Command(args)
    com.command()
    print("exercise num:", com.getExerciseNum())
    print("exercise range:", com.getExerciseRange())
    print("exercise file:", com.getExerciseFile())
    print("answer file:", com.getAnswerFile())