import re
from entity import OpNum
def solver(exStr):
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
        if re.match("[0-9]",exStrTemp) != None or re.match('[-*/÷\+]',exStrTemp) != None:
            exStrList.append(exStrTemp)
        if re.match("[(]",exStrTemp) != None:
            leftBracketNum += 1
            exStrListTempIndex += 1
            # 生成子式
            while exStrListTempIndex < len(exStrListTemp):
                childStrTemp = exStrListTemp[exStrListTempIndex]
                if re.match("[(]",childStrTemp) != None:
                    leftBracketNum += 1
                if re.match("[)]",childStrTemp) != None:
                    rightBracketNum += 1
                if leftBracketNum != rightBracketNum:
                    childExStrList.append(childStrTemp)
                else:
                    childExStr = ""
                    childExStr = childExStr.join(childExStrList)
                    childOpNumResult = solver(childExStr)
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
        elif re.match("[0-9]",exObj) != None:
            exNumStrBuffer += exObj    # 将单个的数字添加到buffer中
            #当下一个字符串不是数字或已经到达列表尾部时将buffer中的数字变为OpNum存入opNumList中
            if i+1 >= len(exStrList) or re.match("[0-9]",exStrList[i+1]) == None:
                opNumList.append(OpNum.OpNum(int(exNumStrBuffer),1))
                exNumStrBuffer = ""
        elif re.match('[-*/÷\+]',exObj) != None:
            opCodeList.append(exObj)
        i += 1

    # 运算
    # 先做乘除法运算
    opCodeListIndex = 1
    while opCodeListIndex <= len(opCodeList):
        code = opCodeList[opCodeListIndex-1]
        if code == "*":
            opNumList[opCodeListIndex-1].mul(opNumList[opCodeListIndex])
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
        code = opCodeList[opCodeListIndex-1]
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
    for exObj in exStrList:
        if str(type(exObj)) == "<class '__main__.OpNum'>":
            opNumList.append(exObj)
        elif re.match("[0-9]",exObj) != None:
            opNum = OpNum.opNum(int(exObj),1)
            opNumList.append(opNum)
        elif re.match('[-*/÷\+]',exObj) != None:
            opCodeList.append(exObj)
    """

if __name__ == "__main__":
    exstr = "9/4"
    on = solver(exstr)
    on.toMixNum()
    print(on.getStr())


