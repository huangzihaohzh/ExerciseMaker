import os
import sys
curPath = os.path.abspath(os.path.dirname(__file__))
rootPath = os.path.split(curPath)[0]
sys.path.append(os.path.split(rootPath)[0])

class OpNum:
    num = 0    # 分子
    den = 1    # 分母
    integer = 0    # 带分数的整数部分
    isMixNum = False
    isNone = False

    def __init__(self,aNum = 0,aDen = 1):
        self.num = int(aNum)
        self.den = int(aDen)
        self.isMixNum = False

    def getNum(self):
        return self.num

    def getDen(self):
        return self.den

    def getInteger(self):
        return self.integer

    def isMixNum(self):
        return self.isMixNum

    def getNoneState(self):
        return self.isNone

    # 加法函数
    def add(self,aOpNum):
        if aOpNum.getNoneState() == False or (aOpNum.getDen == 0):
            self.num = self.num * aOpNum.getDen() + aOpNum.getNum() * self.den
            self.den = self.den * aOpNum.getDen()
            self.isMixNum = False
        else:
            self.isNone = True

    # 减法函数
    def sub(self,aOpNum):
        if aOpNum.getNoneState() == False or (aOpNum.getDen == 0):
            self.num = self.num * aOpNum.getDen() - aOpNum.getNum() * self.den
            self.den = self.den * aOpNum.getDen()
            self.isMixNum = False
        else:
            self.isNone = True

    # 乘法函数
    def mul(self,aOpNum):
        if aOpNum.getNoneState() == False or (aOpNum.getDen == 0):
            self.num = self.num * aOpNum.getNum()
            self.den = self.den * aOpNum.getDen()
            self.isMixNum = False
        else:
            self.isNone = True

    # 除法函数
    def div(self,aOpNum):
        if aOpNum.getNoneState() == False or (aOpNum.getDen == 0):
            if aOpNum.getNum() != 0 or aOpNum.getDen() != 0:
                self.num = self.num * aOpNum.getDen()
                self.den = self.den * aOpNum.getNum()
                self.isMixNum = False
                return True
            else:
                self.isNone = None
                self.isMixNum = False
                return False
        else:
            self.isNone = True

    # 带分数转换函数
    def toMixNum(self):
        if self.den != 0 and self.isNone == False:
            self.integer = self.num // self.den  # 提取带分数的整数部分
            self.num = self.num - self.integer * self.den
            # 将分数部分化为真分数
            i = 0
            if self.num <= self.den:
                i = self.num
            else:
                i = self.den
            while i > 0:
                if self.num % i == 0 and self.den % i == 0:
                    self.num = self.num // i
                    self.den = self.den // i
                i -= 1
            self.isMixNum = True
        else:
            self.isNone = True

    # 输出可用于显示的带分数的字符串
    def getStr(self):
        numStr = ""
        if self.den == 0 or self.isNone == True:
            numStr = "∞"
        if self.den == 1:
            numStr = str(self.integer)
        if self.den !=0 and self.den!=1:
            if self.num == 0:
                numStr = str(self.integer)
            else:
                if self.integer == 0:
                    numStr = str(self.num) + '/' + str(self.den)
                else:
                    numStr = str(self.integer) + "'" + str(self.num) + '/' + str(self.den)



            '''
            if self.integer != 0:
                numStr += str(self.integer)
            if self.num != 0 and self.integer != 0:
                numStr += "'"
            if self.num != 0:
                numStr += str(self.num)
            
            if self.den != 1 and self.num != 0:
                numStr += "/"
                numStr += str(self.den)
            
        else:
            numStr += "∞"'''
        """
        if self.num == 0:
            numStr = str(self.integer)
        elif self.integer != 0:
            numStr = str(self.integer) + "'" + str(self.num) + "/" + str(self.den)
        else:
            numStr = str(self.num) + "/" + str(self.den)
        """
        return numStr

if __name__ == "__main__":
    opNum = OpNum(6,7)
    opNum2 = OpNum(1,7)
    opNum.sub(opNum2)
    opNum.toMixNum()
    i =0
    print(opNum.getStr(),type(i))








