import random
import fractions
import re
from entity import OpNum
import time
import os
import sys
curPath = os.path.abspath(os.path.dirname(__file__))
rootPath = os.path.split(curPath)[0]
sys.path.append(os.path.split(rootPath)[0])
# 题目类
# 用于生成存储题目、答案


class Exercise:
    exerciseStr = ""
    answerStr = ""
    givenAnswerStr = ""
    range

    # 构造函数
    def __init__(self):
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
        # 将运算代码转为运算符号
        i = 0
        while i < len(operationCodeList):
            operationCode = operationCodeList[i]
            if operationCode == 0:
                operationCodeList[i] = '+'
            if operationCode == 1:
                operationCodeList[i] = '-'
            if operationCode == 2:
                operationCodeList[i] = '*'
            if operationCode == 3:
                operationCodeList[i] = '÷'
            if operationCode == 4:
                operationCodeList[i] = '/'
            i += 1
        # 向式子中加括号
        # 随机确定是否需要加括号
        isAddBracket = random.randint(0,1)
        if isAddBracket == 1 and operatingFigureNum > 2:
            # 生成两个添加括号的位置
            bracketLocation = []
            while True:
                bracket1 = random.randint(0,operatingFigureNum-1)
                bracket2 = random.randint(0,operatingFigureNum-1)
                if not((bracket1 == 0 and bracket2 == operatingFigureNum -1)
                    or (bracket2 == 0 and bracket1 == operatingFigureNum -1)
                    or bracket1 >= bracket2):
                    bracketLocation.append(bracket1)
                    bracketLocation.append(bracket2)
                    break
            # 将括号添加进运算数中
            operatingFigureList[bracketLocation[0]] = '(' + str(operatingFigureList[bracketLocation[0]])
            operatingFigureList[bracketLocation[1]] = str(operatingFigureList[bracketLocation[1]]) + ')'
        # 生成式子字符串
        self.exerciseStr += str(operatingFigureList[0])
        i = 1
        while i < len(operatingFigureList):
            self.exerciseStr += str(operationCodeList[i-1])
            self.exerciseStr += str(operatingFigureList[i])
            i += 1
        self.fourOp()


        '''
        if(not self.fourOp(operatingFigureList,operationCodeList)):
            self.makeExercise()
        '''

    # 按给定的range和num生成num道题目
    def makeExerciseWithNumAndRange(self,num,range):
        # self.range = int(range)
        exerciseList = []
        i = 1
        #生成num道题目
        while i <= num:
            exercise = Exercise()
            exercise.setRange(range)
            exercise.makeExercise()
            #print(exercise.getExerciseStr())    #test
            exerciseList.append(exercise)
            i += 1
        return exerciseList


    # 按给定的题目字符串
    def makeExerciseByStr(self,exeStr = "",ansStr = ""):
        self.exerciseStr = exeStr
        self.givenAnswerStr = ansStr[:-1]
        opNumResult = self.solver(exeStr)
        opNumResult.toMixNum()
        self.answerStr = opNumResult.getStr()
        '''
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
        '''

    def setRange(self,range):
        self.range = range
    # 以字符串的形式返回题目
    def getExerciseStr(self):
        return self.exerciseStr

    # 以字符串形式返回答案
    def getAnswerStr(self):
        return self.answerStr

    def getAnswerNum(self):
        return fractions.Fraction(self.answerStr)

    def isRight(self):
        if self.givenAnswerStr == self.answerStr:
            return True
        else:
            return False
    """
    四则运算函数
    参数：opFigureList    包含参与运算的数的列表
          opCodeList      包含参与运算的符号，代表关系：0：+，1：-，2：*，3：÷，4：/
    """
    def fourOp(self,opFigureList = [],opCodeList = []):
        opNumResult = self.solver(self.exerciseStr)
        opNumResult.toMixNum()
        self.answerStr = opNumResult.getStr()
        '''
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
        '''

    # 求解器
    def solver(self,exStr):
        # 将str变为列表
        exStrListTemp = list(exStr)
        exStrList = []
        childExStrList = []

        # 遍历题目字符临时列表
        # 将括号前的式子添加到exStrList中
        # 在遇到括号后以类似栈的原理来提取括号中的子式，在遇到对应的右括号时停止
        # 并递归调用solver()来计算出子式的值并插入exStrList中
        leftBracketNum = 0
        rightBracketNum = 0
        exStrListTempIndex = 0
        while exStrListTempIndex < len(exStrListTemp):
            exStrTemp = exStrListTemp[exStrListTempIndex]
            if re.match("[0-9]", exStrTemp) != None or re.match('[-*/÷\+]', exStrTemp) != None:
                exStrList.append(exStrTemp)
            if re.match("[(]", exStrTemp) != None:
                leftBracketNum += 1
                exStrListTempIndex += 1
                # 生成子式
                while exStrListTempIndex < len(exStrListTemp):
                    childStrTemp = exStrListTemp[exStrListTempIndex]
                    if re.match("[(]", childStrTemp) != None:
                        leftBracketNum += 1
                    if re.match("[)]", childStrTemp) != None:
                        rightBracketNum += 1
                    if leftBracketNum != rightBracketNum:
                        childExStrList.append(childStrTemp)
                    else:
                        childExStr = ""
                        childExStr = childExStr.join(childExStrList)
                        childOpNumResult = self.solver(childExStr)
                        exStrList.append(childOpNumResult)
                        break
                    exStrListTempIndex += 1
            exStrListTempIndex += 1
        # 合并exStrList中的数字
        # 将exStrList中的数值字符串转为OpNum转储到opNumList中
        # 将运算符存储于
        opNumList = []
        opCodeList = []
        exNumStrBuffer = ""
        i = 0
        while i < len(exStrList):
            exObj = exStrList[i]
            if "OpNum" in str(type(exObj)):
                opNumList.append((exObj))
            elif re.match("[0-9]", exObj) != None:
                exNumStrBuffer += exObj  # 将单个的数字添加到buffer中
                # 当下一个字符串不是数字或已经到达列表尾部时将buffer中的数字变为OpNum存入opNumList中
                if i + 1 >= len(exStrList) or re.match("[0-9]", exStrList[i + 1]) == None:
                    opNumList.append(OpNum.OpNum(int(exNumStrBuffer), 1))
                    exNumStrBuffer = ""
            elif re.match('[-*/÷\+]', exObj) != None:
                opCodeList.append(exObj)
            i += 1

        # 运算
        # 先做乘除法运算
        opCodeListIndex = 1
        while opCodeListIndex <= len(opCodeList):
            code = opCodeList[opCodeListIndex - 1]
            if code == "*":
                opNumList[opCodeListIndex - 1].mul(opNumList[opCodeListIndex])
                del opNumList[opCodeListIndex]
                del opCodeList[opCodeListIndex - 1]
                continue
            if code == "/" or code == "÷":
                opNumList[opCodeListIndex - 1].div(opNumList[opCodeListIndex])
                del opNumList[opCodeListIndex]
                del opCodeList[opCodeListIndex - 1]
                continue
            opCodeListIndex += 1

        # 再做加减法运算
        opCodeListIndex = 1
        while opCodeListIndex <= len(opCodeList):
            code = opCodeList[opCodeListIndex - 1]
            if code == "+":
                opNumList[opCodeListIndex - 1].add(opNumList[opCodeListIndex])
                del opNumList[opCodeListIndex]
                del opCodeList[opCodeListIndex - 1]
                continue
            if code == "-":
                opNumList[opCodeListIndex - 1].sub(opNumList[opCodeListIndex])
                del opNumList[opCodeListIndex]
                del opCodeList[opCodeListIndex - 1]
                continue
            opCodeListIndex += 1

        # 输出
        return opNumList[0]
    """
    def solver(self,exStr = ""):
        # 获取运算数列表
        opNumList = []
        opIntOriginList = []
        opIntTemp = re.split('[()-*/÷\+]',exStr)
        for intstr in opIntTemp:
            if intstr != "":
                opNum = OpNum.OpNum(int(intstr),1)
                opNumList.append(opNum)
                opIntOriginList.append(int(intstr))
        # 获取运算符（结合括号）列表
        opCodeList = []
        opCodeTempList = re.split('[0-9]',exStr)
        for codestr in opCodeTempList:
            if codestr != '':
                opCodeList.append(codestr)
        # 去括号处理
        #搜索第一个左括号，将第一个左括号到其对应右括号之间的运算（不包括第一个左括号和其对应的右括号）
        # 作为子运算调用solver(str)递归处理
        originCodeListIndex = 0
        opNumIndex = 0
        solvingCodeList = []
        solvingNumList = []
        solvingIntList = []
        leftBracketNum = 0
        rightBracketNum = 0
        childExStr = ""
        while originCodeListIndex < len(opCodeTempList):
            # 运算符不包含括号的情况
            if not ('(' in opCodeTempList[originCodeListIndex] or ')' in opCodeTempList[originCodeListIndex]):
                # 判断是否需要将运算符加入运算符表solvingCodeList中
                if opCodeTempList[originCodeListIndex] != '':
                    solvingCodeList.append(opCodeTempList[originCodeListIndex])
                # 将参与运算的整数和OpNum对象存入solvingIntList和solvingNumList
                if originCodeListIndex != len(opCodeTempList) - 1:
                    solvingIntList.append(opIntOriginList[originCodeListIndex])
                    solvingNumList.append(opNumList[originCodeListIndex])
            # 运算符包括括号的情况
            else:
                opCodeStr = opCodeTempList[originCodeListIndex]
                if("(" in opCodeStr):
                    #标记发现了一个左括号
                    leftBracketNum += 1
                    #标记第一个左括号的位置
                    beginLeftBracketIndex = originCodeListIndex
                    #将左括号前的运算符放入solvingCodeList
                    solvingCodeList.append(opCodeStr[0])
                    # 构造子题目字符串
                    childExStr += str(opIntOriginList[beginLeftBracketIndex])
                    originCodeListIndex += 1
                    #循环搜索直到leftBracketNum == rightBracketNum
                    while originCodeListIndex < len(opCodeTempList):
                        if not (")" in opCodeTempList[originCodeListIndex]):
                            childExStr += str(opCodeTempList[originCodeListIndex])
                            childExStr += str(opIntOriginList[originCodeListIndex])
                        else:
                            rightBracketNum += 1
                            if leftBracketNum == rightBracketNum:
                                # 若最后一个运算符是
                                del opCodeTempList[originCodeListIndex][0]
                                break
                            else:
                                childExStr += str(opCodeTempList[originCodeListIndex][len(opCodeTempList[originCodeListIndex])-1])
                                childExStr += str(opIntOriginList[originCodeListIndex])
                        originCodeListIndex += 1
                    #调用solver(str),递归处理子题目
                    childResult = self.solver(childExStr)
                    opNumList.append(childResult)
            originCodeListIndex += 1
        # 对solvingNumList进行计算
        # 先进行乘除计算
        codeIndex = 1
        for opCode in solvingCodeList:
            if opCode == "*":
                solvingNumList[codeIndex - 1].mul(solvingNumList[codeIndex])
                del solvingNumList[codeIndex]
                del solvingCodeList[codeIndex -1]
            if opCode == "/" or opCode == "÷":
                solvingNumList[codeIndex - 1].div(solvingNumList[codeIndex])
                del solvingNumList[codeIndex]
                del solvingCodeList[codeIndex - 1]
            codeIndex += 1
        # 再进行加减计算
        codeIndex = 1
        for opCode in solvingCodeList:
            if opCode == "+":
                solvingNumList[codeIndex -1].add(solvingNumList[codeIndex])
                del solvingNumList[codeIndex]
                del solvingCodeList[codeIndex - 1]
            if opCode == "-":
                solvingNumList[codeIndex -1].sub(solvingNumList[codeIndex])
                del solvingNumList[codeIndex]
                del solvingCodeList[codeIndex - 1]

        #返回结果
        return solvingNumList[0]
        """

if __name__ == "__main__":
    startT = time.clock()
    exercise = Exercise()
    exerciseList = exercise.makeExerciseWithNumAndRange(10000,10)
    for e in exerciseList:
        print(e.getExerciseStr() + "  =  " + e.getAnswerStr())
    endT = time.clock()
    print(str(endT - startT))













