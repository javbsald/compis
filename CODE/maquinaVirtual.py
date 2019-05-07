# Maquina Virtual

from yacc import pilaQuads

import pprint

#pprint.pprint(pilaQuads)

# Variables Globales
memoriaGlobal = dict()
memoriaLocal = dict()       # Within List
localList = []
localList.append(memoriaLocal)
localListLength = len(localList)
memoriaTemporal = dict()    # Within List
from memoriaVirtual import memoriaConstante
from memoriaVirtual import memoriaConstanteDir
quadCounter = 0
quadCounterList = []
quadCounterList.append(quadCounter)
currentquadCounter=len(quadCounterList)-1

def memoryToValue(mem):
    if mem >= 1000 and mem < 10000:     # Global
        if mem in memoriaGlobal:
            return memoriaGlobal[mem]
        else:
            print("Not found in Global Memory")
    elif mem >= 10000 and mem < 20000:  # Local
        print(mem, " in ", localList, " lengh=", localListLength)
        if mem in localList[localListLength-1]:
            return localList[localListLength-1][mem]
        else:
            print(mem, "Not found Local Memory")
    elif mem >= 20000 and mem < 25000:  # Temp
        if mem in memoriaTemporal:
            return memoriaTemporal[mem]
        else:
            print("Not found in Temporal Memory")
    elif mem >= 25000 and mem < 30000:  # Const
        return memoriaConstanteDir[mem]

def assignToMemory(result, resultDir):
    if resultDir >= 1000 and resultDir < 10000:     # Global
        memoriaGlobal[resultDir] = result
    elif resultDir >= 10000 and resultDir < 20000:  # Local
        localList[localListLength-1][resultDir] = result
    elif resultDir >= 20000 and resultDir < 25000:
        memoriaTemporal[resultDir] = result
    #elif resultDir >= 25000 and resultDir < 30000:  # Const
        #memoriaConstante[resultDir] = result

while True:
    if pilaQuads[quadCounterList[currentquadCounter]][0] == "GOTO":
        quadCounterList[currentquadCounter] = pilaQuads[quadCounterList[currentquadCounter]][3]-1
        #print("Jump to Quad ", quadCounterList[currentquadCounter])
    elif pilaQuads[quadCounterList[currentquadCounter]][0] == "GOTOF":
        toCheck = memoryToValue(pilaQuads[quadCounterList[currentquadCounter]][1])
        if toCheck == False:
            quadCounterList[currentquadCounter] = pilaQuads[quadCounterList[currentquadCounter]][3]-1
            #print("Jump to Quad ", quadCounterList[currentquadCounter])
        else:
            quadCounterList[currentquadCounter] += 1
    elif pilaQuads[quadCounterList[currentquadCounter]][0] == "ERA":
        actRecord = dict()
        print("ERA")
        quadCounterList[currentquadCounter] += 1
    elif pilaQuads[quadCounterList[currentquadCounter]][0] == "PARAM":
        valueParam = memoryToValue(pilaQuads[quadCounterList[currentquadCounter]][1])
        assignTo = pilaQuads[quadCounterList[currentquadCounter]][3]
        actRecord[assignTo] = valueParam
        print("PARAM", assignTo, " = ", valueParam)
        quadCounterList[currentquadCounter] += 1
    elif pilaQuads[quadCounterList[currentquadCounter]][0] == "GOSUB":
        #quadCounterList[currentquadCounter] = pilaQuads[quadCounterList[currentquadCounter]][3] - 1
        localList.append(actRecord)
        localListLength = len(localList)
        goSubTemp = pilaQuads[quadCounterList[currentquadCounter]][3] - 1
        print("GOSUB", goSubTemp)
        quadCounterList[currentquadCounter] += 1 #para que no regrese al gosub
        quadCounterList.append(goSubTemp)
        currentquadCounter=len(quadCounterList)-1
        #print("Global", memoriaGlobal)
        #print(localList[localListLength-1])
        print(quadCounterList)
    elif pilaQuads[quadCounterList[currentquadCounter]][0] == "RETURN":
        result = pilaQuads[quadCounterList[currentquadCounter]][1]
        resultDir = pilaQuads[quadCounterList[currentquadCounter]][3]
        #print(resultDir, " = ", result)
        resultValue = memoryToValue(result)
        assignToMemory(resultValue, resultDir)
        print("RETURN", resultDir, " = ", resultValue)
        localList.pop()
        localListLength = len(localList)
        quadCounterList.pop()
        currentquadCounter=len(quadCounterList)-1
        print("POPRETURN", quadCounterList[currentquadCounter])
        print(quadCounterList)
    elif pilaQuads[quadCounterList[currentquadCounter]][0] == "ENDPROC":
        localList.pop()
        localListLength = len(localList)
        quadCounterList.pop()
        currentquadCounter=len(quadCounterList)-1
        print("ENDPROC", quadCounterList[currentquadCounter])
        print(quadCounterList)
    elif pilaQuads[quadCounterList[currentquadCounter]][0] == "write":
        toPrint = pilaQuads[quadCounterList[currentquadCounter]][3]
        if type(toPrint) == str:
            print("Print ", toPrint)
        else:
            resultValue = memoryToValue(toPrint)
            print("Print ", resultValue)
        quadCounterList[currentquadCounter] += 1
    elif pilaQuads[quadCounterList[currentquadCounter]][0] == "=":
        print(pilaQuads[quadCounterList[currentquadCounter]])
        result = pilaQuads[quadCounterList[currentquadCounter]][1]
        resultDir = pilaQuads[quadCounterList[currentquadCounter]][3]
        #print(resultDir, " = ", result)
        resultValue = memoryToValue(result)
        assignToMemory(resultValue, resultDir)
        print(resultDir, " = ", resultValue)
        #print(memoriaGlobal, memoriaLocal, memoriaTemporal)
        quadCounterList[currentquadCounter] += 1
    elif pilaQuads[quadCounterList[currentquadCounter]][0] == "+":
        operador1 = memoryToValue(pilaQuads[quadCounterList[currentquadCounter]][1])
        operador2 = memoryToValue(pilaQuads[quadCounterList[currentquadCounter]][2])
        print(operador1, " + ", operador2)
        result = operador1 + operador2
        resultDir = pilaQuads[quadCounterList[currentquadCounter]][3]
        assignToMemory(result, resultDir)
        quadCounterList[currentquadCounter] += 1
    elif pilaQuads[quadCounterList[currentquadCounter]][0] == "-":
        operador1 = memoryToValue(pilaQuads[quadCounterList[currentquadCounter]][1])
        operador2 = memoryToValue(pilaQuads[quadCounterList[currentquadCounter]][2])
        print(operador1, " - ", operador2)
        result = operador1 - operador2
        resultDir = pilaQuads[quadCounterList[currentquadCounter]][3]
        assignToMemory(result, resultDir)
        quadCounterList[currentquadCounter] += 1
    elif pilaQuads[quadCounterList[currentquadCounter]][0] == "*":
        operador1 = memoryToValue(pilaQuads[quadCounterList[currentquadCounter]][1])
        operador2 = memoryToValue(pilaQuads[quadCounterList[currentquadCounter]][2])
        print(operador1, " * ", operador2)
        result = operador1 * operador2
        resultDir = pilaQuads[quadCounterList[currentquadCounter]][3]
        assignToMemory(result, resultDir)
        quadCounterList[currentquadCounter] += 1
    elif pilaQuads[quadCounterList[currentquadCounter]][0] == "/":
        operador1 = memoryToValue(pilaQuads[quadCounterList[currentquadCounter]][1])
        operador2 = memoryToValue(pilaQuads[quadCounterList[currentquadCounter]][2])
        print(operador1, " / ", operador2)
        result = operador1 / operador2
        resultDir = pilaQuads[quadCounterList[currentquadCounter]][3]
        assignToMemory(result, resultDir)
        quadCounterList[currentquadCounter] += 1
    elif pilaQuads[quadCounterList[currentquadCounter]][0] == "<":
        operador1 = memoryToValue(pilaQuads[quadCounterList[currentquadCounter]][1])
        operador2 = memoryToValue(pilaQuads[quadCounterList[currentquadCounter]][2])
        print(operador1, " < ", operador2)
        result = operador1 < operador2
        resultDir = pilaQuads[quadCounterList[currentquadCounter]][3]
        assignToMemory(result, resultDir)
        quadCounterList[currentquadCounter] += 1
    elif pilaQuads[quadCounterList[currentquadCounter]][0] == ">":
        operador1 = memoryToValue(pilaQuads[quadCounterList[currentquadCounter]][1])
        operador2 = memoryToValue(pilaQuads[quadCounterList[currentquadCounter]][2])
        print(operador1, " > ", operador2)
        result = operador1 > operador2
        resultDir = pilaQuads[quadCounterList[currentquadCounter]][3]
        assignToMemory(result, resultDir)
        quadCounterList[currentquadCounter] += 1
    elif pilaQuads[quadCounterList[currentquadCounter]][0] == "<=":
        operador1 = memoryToValue(pilaQuads[quadCounterList[currentquadCounter]][1])
        operador2 = memoryToValue(pilaQuads[quadCounterList[currentquadCounter]][2])
        print(operador1, " <= ", operador2)
        result = operador1 <= operador2
        resultDir = pilaQuads[quadCounterList[currentquadCounter]][3]
        assignToMemory(result, resultDir)
        quadCounterList[currentquadCounter] += 1
    elif pilaQuads[quadCounterList[currentquadCounter]][0] == ">=":
        operador1 = memoryToValue(pilaQuads[quadCounterList[currentquadCounter]][1])
        operador2 = memoryToValue(pilaQuads[quadCounterList[currentquadCounter]][2])
        print(operador1, " >= ", operador2)
        result = operador1 >= operador2
        resultDir = pilaQuads[quadCounterList[currentquadCounter]][3]
        assignToMemory(result, resultDir)
        quadCounterList[currentquadCounter] += 1
    elif pilaQuads[quadCounterList[currentquadCounter]][0] == "==":
        operador1 = memoryToValue(pilaQuads[quadCounterList[currentquadCounter]][1])
        operador2 = memoryToValue(pilaQuads[quadCounterList[currentquadCounter]][2])
        result = operador1 == operador2
        print(operador1, " == ", operador2, " => ", result)
        resultDir = pilaQuads[quadCounterList[currentquadCounter]][3]
        assignToMemory(result, resultDir)
        quadCounterList[currentquadCounter] += 1
    elif pilaQuads[quadCounterList[currentquadCounter]][0] == "!=":
        operador1 = memoryToValue(pilaQuads[quadCounterList[currentquadCounter]][1])
        operador2 = memoryToValue(pilaQuads[quadCounterList[currentquadCounter]][2])
        result = operador1 != operador2
        print(operador1, " != ", operador2, " => ", result)
        resultDir = pilaQuads[quadCounterList[currentquadCounter]][3]
        assignToMemory(result, resultDir)
        quadCounterList[currentquadCounter] += 1
    elif pilaQuads[quadCounterList[currentquadCounter]][0] == "&&":
        operador1 = memoryToValue(pilaQuads[quadCounterList[currentquadCounter]][1])
        operador2 = memoryToValue(pilaQuads[quadCounterList[currentquadCounter]][2])
        result = operador1 and operador2
        print(operador1, " && ", operador2, " => ", result)
        resultDir = pilaQuads[quadCounterList[currentquadCounter]][3]
        assignToMemory(result, resultDir)
        quadCounterList[currentquadCounter] += 1
    elif pilaQuads[quadCounterList[currentquadCounter]][0] == "||":
        operador1 = memoryToValue(pilaQuads[quadCounterList[currentquadCounter]][1])
        operador2 = memoryToValue(pilaQuads[quadCounterList[currentquadCounter]][2])
        result = operador1 or operador2
        print(operador1, " ||", operador2, " => ", result)
        resultDir = pilaQuads[quadCounterList[currentquadCounter]][3]
        assignToMemory(result, resultDir)
        quadCounterList[currentquadCounter] += 1
    else:
        sys.exit(0)
#print(pilaQuads[quadCounterList[currentquadCounter]])
#print(pilaQuads[quadCounterList[currentquadCounter]][0])
