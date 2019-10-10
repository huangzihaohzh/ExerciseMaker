import numpy

# 题目类
# 用于生成存储题目、答案


class Exercise:
    exerciseStr = ""
    answerStr = ""
    range = 10

    # 构造函数
    def __init__(self):
        pass

    # 按range = 10 生成一道题目
    def makeExercise(self):
        pass

    # 按给定的range和num生成一道题目
    def makeExerciseWithNumAndRange(self,num,range):
        pass

    # 按给定的题目字符串
    def makeExerciseByStr(self,exeStr,ansStr):
        pass

    # 以字符串的形式返回题目
    def getExerciseStr(self):
        pass

