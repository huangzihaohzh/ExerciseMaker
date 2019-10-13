import random
import fractions
import re
# 题目类
# 用于生成存储题目、答案


class Exercise:


    # 构造函数
    def __init__(self):
        super().__init__()
        self.exerciseStr = ""
        self.answerStr = ""
        self.givenAnswerStr = ""
        self.range = 10

    # 按range生成一道题目
    def makeExercise(self):
        operatingFigureList = []  # 用于存放生成练习式子的数字
        operationCodeList = []  # 数学式中的运算代码，代表关系：0：+，1：-，2：*，3：÷，4：/
        operatingFigureNum = random.randint(2, 4)  # 操作数的个数
        operationCodeNum = operatingFigureNum - 1  # 运算操作的个数
        # 用随机数生成用于运算的数字
        i = 1
        while i <= operatingFigureNum:
            operatingFigureList.append(random.randint(0, self.range))
            i += 1
        # 生成运算代码
        i = 1
        while i <= operationCodeNum:
            operationCodeList.append(random.randint(0, 4))
            i += 1
        if(not self.fourOp(operatingFigureList,operationCodeList)):
            self.makeExercise()

    # 按给定的range和num生成num道题目
    def makeExerciseWithNumAndRange(self,num,range):
        self.range = int(range)
        exerciseList = []
        i = 1
        #生成num道题目
        while i <= num:
            exercise = Exercise()
            exercise.makeExercise()
            #print(exercise.getExerciseStr())    #test
            exerciseList.append(exercise)
            i += 1
        return exerciseList


    # 按给定的题目字符串
    def makeExerciseByStr(self,exeStr = "",ansStr = ""):
        self.givenAnswerStr = ansStr
        exeStrTemp = exeStr[:]
        exeFigureList = []
        opCodeList = []
        codeRegx = '[-*/÷\+]'
        figureRegx = '[0-9]'
        #根据运算符进行划分，并将划分出的数字字符串转为数字存入exeFigureList
        exeFigureStrList = re.split(codeRegx,exeStr)
        for figureStr in exeFigureStrList:
            exeFigureList.append(int(figureStr))
        #根据数字进行划分，提取运算符并存入opCodeList
        opCodeListTemp = re.split(figureRegx,exeStr)
        for opCode in opCodeListTemp:
            if(opCode == "+"):
                opCodeList.append(0)
            if (opCode == "-"):
                opCodeList.append(1)
            if (opCode == "*"):
                opCodeList.append(2)
            if (opCode == "÷"):
                opCodeList.append(3)
            if (opCode == "/"):
                opCodeList.append(4)
        self.fourOp(exeFigureList,opCodeList)
        return


    # 以字符串的形式返回题目
    def getExerciseStr(self):
        return self.exerciseStr

    # 以字符串形式返回答案
    def getAnswerStr(self):
        return self.answerStr

    def getAnswerNum(self):
        return fractions.Fraction(self.answerStr)

    def isRight(self):
        if(float(fractions.Fraction(self.givenAnswerStr)) == float(fractions.Fraction(self.answerStr))):
            return True
        else:
            return False
    """
    四则运算函数
    参数：opFigureList    包含参与运算的数的列表
          opCodeList      包含参与运算的符号，代表关系：0：+，1：-，2：*，3：÷，4：/
    """
    def fourOp(self,opFigureList = [],opCodeList = []):
        # 进行四则运算
        opFigureTempList = opFigureList.copy()
        opCodeTempList = opCodeList.copy()
        answer = 0
        i = 0
        while i < len(opCodeList):
            codeIndex = 1  # 运算符索引
            # 若有乘除法运算，则先做乘除法
            if (2 in opCodeTempList or 3 in opCodeTempList or 4 in opCodeTempList):
                # 遍历操作符列表，查找第一个乘法或除法
                for opCode in opCodeTempList:
                    # 若为乘法
                    if (opCode == 2):
                        # 从运算数临时列表中取出两个操作数
                        figure1 = opFigureTempList[codeIndex - 1]
                        figure2 = opFigureTempList[codeIndex]
                        # 从运算数临时列表中删掉两个操作数中的后者
                        del opFigureTempList[codeIndex]
                        opFigureTempList[codeIndex - 1] = figure1 * figure2
                        del opCodeTempList[codeIndex - 1]
                        break
                    # 若为除法或分数
                    if (opCode == 3 or opCode == 4):
                        figure1 = opFigureTempList[codeIndex - 1]
                        figure2 = opFigureTempList[codeIndex]
                        del opFigureTempList[codeIndex]
                        if(figure2 != 0):
                            opFigureTempList[codeIndex - 1] = figure1 / figure2
                        else:
                            return False
                        del opCodeTempList[codeIndex - 1]
                        break
                    codeIndex += 1
                    # 从运算符临时列表中删除已经进行运算的运算符
                    #del opCodeTempList[codeIndex - 1]
                    #break
            else:
                # opcodeTempList不包含乘除法或做完乘除法后,做加减法
                codeIndex = 1
                for opCode in opCodeTempList:
                    # 从运算数临时列表中取出两个操作数
                    figure1 = opFigureTempList[codeIndex - 1]
                    figure2 = opFigureTempList[codeIndex]
                    # 从运算数临时列表中删掉两个操作数中的后者
                    del opFigureTempList[codeIndex]
                    # 若为加法
                    if (opCode == 0):
                        opFigureTempList[codeIndex - 1] = figure1 + figure2
                        del opCodeTempList[codeIndex - 1]
                        break
                    # 若为减法
                    if (opCode == 1):
                        opFigureTempList[codeIndex - 1] = figure1 - figure2
                        del opCodeTempList[codeIndex - 1]
                        break
                    # 从运算符临时列表中删除已经进行运算的运算符
                    #del opCodeTempList[codeIndex - 1]
                    #break
            i += 1
        answer = opFigureTempList[0]
        # 生成练习字符串
        opCodeIndex = 0
        for opFigure in opFigureList:
            self.exerciseStr += str(opFigure)
            if (opCodeIndex < len(opCodeList)):
                if (opCodeList[opCodeIndex] == 0):
                    self.exerciseStr += "+"
                if (opCodeList[opCodeIndex] == 1):
                    self.exerciseStr += "-"
                if (opCodeList[opCodeIndex] == 2):
                    self.exerciseStr += "*"
                if (opCodeList[opCodeIndex] == 3):
                    self.exerciseStr += "÷"
                if (opCodeList[opCodeIndex] == 4):
                    self.exerciseStr += "/"
            opCodeIndex += 1
        # 生成答案字符串
        self.answerStr = str(fractions.Fraction(answer))
        ##### test begin
        """
        print(self.exerciseStr)
        if(self.answerStr == "" or self.exerciseStr == ""):
            print("###############\n")
            print("#    EMPTY    #")
            print("###############\n")
        """
        return True