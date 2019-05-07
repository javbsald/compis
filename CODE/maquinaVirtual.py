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

def memoryToValue(mem):
    if mem >= 1000 and mem < 10000:     # Global
        if mem in memoriaGlobal:
            return memoriaGlobal[mem]
        else:
            print("Not found in Global Memory")
    elif mem >= 10000 and mem < 20000:  # Local
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
    if pilaQuads[quadCounter][0] == "GOTO":
        quadCounter = pilaQuads[quadCounter][3]-1
        #print("Jump to Quad ", quadCounter)
    elif pilaQuads[quadCounter][0] == "GOTOF":
        toCheck = memoryToValue(pilaQuads[quadCounter][1])
        if toCheck == False:
            quadCounter = pilaQuads[quadCounter][3]-1
            #print("Jump to Quad ", quadCounter)
        else:
            quadCounter += 1
    elif pilaQuads[quadCounter][0] == "ERA":
        actRecord = dict()
        print("ERA")
        quadCounter += 1
    elif pilaQuads[quadCounter][0] == "PARAM":
        valueParam = memoryToValue(pilaQuads[quadCounter][1])
        assignTo = pilaQuads[quadCounter][3]
        actRecord[assignTo] = valueParam
        print("PARAM", assignTo, " = ", valueParam)
        quadCounter += 1
    elif pilaQuads[quadCounter][0] == "GOSUB":
        quadCounter = pilaQuads[quadCounter][3] - 1
        localList.append(actRecord)
        localListLength = len(localList)
        print("GOSUB", quadCounter, pilaQuads[quadCounter])
        print("Global", memoriaGlobal)
        print(localList[localListLength-1])
    elif pilaQuads[quadCounter][0] == "ENDPROC":
        localList.pop()
        print("ENDPROC")
        quadCounter += 1
    elif pilaQuads[quadCounter][0] == "write":
        toPrint = pilaQuads[quadCounter][3]
        if type(toPrint) == str:
            print("Print ", toPrint)
        else:
            resultValue = memoryToValue(toPrint)
            print("Print ", resultValue)
        quadCounter += 1
    elif pilaQuads[quadCounter][0] == "=":
        print(pilaQuads[quadCounter])
        result = pilaQuads[quadCounter][1]
        resultDir = pilaQuads[quadCounter][3]
        #print(resultDir, " = ", result)
        resultValue = memoryToValue(result)
        assignToMemory(resultValue, resultDir)
        print(resultDir, " = ", resultValue)
        #print(memoriaGlobal, memoriaLocal, memoriaTemporal)
        quadCounter += 1
    elif pilaQuads[quadCounter][0] == "+":
        operador1 = memoryToValue(pilaQuads[quadCounter][1])
        operador2 = memoryToValue(pilaQuads[quadCounter][2])
        print(operador1, " + ", operador2)
        result = operador1 + operador2
        resultDir = pilaQuads[quadCounter][3]
        assignToMemory(result, resultDir)
        quadCounter += 1
    elif pilaQuads[quadCounter][0] == "-":
        operador1 = memoryToValue(pilaQuads[quadCounter][1])
        operador2 = memoryToValue(pilaQuads[quadCounter][2])
        print(operador1, " - ", operador2)
        result = operador1 - operador2
        resultDir = pilaQuads[quadCounter][3]
        assignToMemory(result, resultDir)
        quadCounter += 1
    elif pilaQuads[quadCounter][0] == "*":
        operador1 = memoryToValue(pilaQuads[quadCounter][1])
        operador2 = memoryToValue(pilaQuads[quadCounter][2])
        print(operador1, " * ", operador2)
        result = operador1 * operador2
        resultDir = pilaQuads[quadCounter][3]
        assignToMemory(result, resultDir)
        quadCounter += 1
    elif pilaQuads[quadCounter][0] == "/":
        operador1 = memoryToValue(pilaQuads[quadCounter][1])
        operador2 = memoryToValue(pilaQuads[quadCounter][2])
        print(operador1, " / ", operador2)
        result = operador1 / operador2
        resultDir = pilaQuads[quadCounter][3]
        assignToMemory(result, resultDir)
        quadCounter += 1
    elif pilaQuads[quadCounter][0] == "<":
        operador1 = memoryToValue(pilaQuads[quadCounter][1])
        operador2 = memoryToValue(pilaQuads[quadCounter][2])
        print(operador1, " < ", operador2)
        result = operador1 < operador2
        resultDir = pilaQuads[quadCounter][3]
        assignToMemory(result, resultDir)
        quadCounter += 1
    elif pilaQuads[quadCounter][0] == ">":
        operador1 = memoryToValue(pilaQuads[quadCounter][1])
        operador2 = memoryToValue(pilaQuads[quadCounter][2])
        print(operador1, " > ", operador2)
        result = operador1 > operador2
        resultDir = pilaQuads[quadCounter][3]
        assignToMemory(result, resultDir)
        quadCounter += 1
    elif pilaQuads[quadCounter][0] == "<=":
        operador1 = memoryToValue(pilaQuads[quadCounter][1])
        operador2 = memoryToValue(pilaQuads[quadCounter][2])
        print(operador1, " <= ", operador2)
        result = operador1 <= operador2
        resultDir = pilaQuads[quadCounter][3]
        assignToMemory(result, resultDir)
        quadCounter += 1
    elif pilaQuads[quadCounter][0] == ">=":
        operador1 = memoryToValue(pilaQuads[quadCounter][1])
        operador2 = memoryToValue(pilaQuads[quadCounter][2])
        print(operador1, " >= ", operador2)
        result = operador1 >= operador2
        resultDir = pilaQuads[quadCounter][3]
        assignToMemory(result, resultDir)
        quadCounter += 1
    elif pilaQuads[quadCounter][0] == "==":
        operador1 = memoryToValue(pilaQuads[quadCounter][1])
        operador2 = memoryToValue(pilaQuads[quadCounter][2])
        result = operador1 == operador2
        print(operador1, " == ", operador2, " => ", result)
        resultDir = pilaQuads[quadCounter][3]
        assignToMemory(result, resultDir)
        quadCounter += 1
    elif pilaQuads[quadCounter][0] == "!=":
        operador1 = memoryToValue(pilaQuads[quadCounter][1])
        operador2 = memoryToValue(pilaQuads[quadCounter][2])
        result = operador1 != operador2
        print(operador1, " != ", operador2, " => ", result)
        resultDir = pilaQuads[quadCounter][3]
        assignToMemory(result, resultDir)
        quadCounter += 1
    elif pilaQuads[quadCounter][0] == "&&":
        operador1 = memoryToValue(pilaQuads[quadCounter][1])
        operador2 = memoryToValue(pilaQuads[quadCounter][2])
        result = operador1 and operador2
        print(operador1, " && ", operador2, " => ", result)
        resultDir = pilaQuads[quadCounter][3]
        assignToMemory(result, resultDir)
        quadCounter += 1
    elif pilaQuads[quadCounter][0] == "||":
        operador1 = memoryToValue(pilaQuads[quadCounter][1])
        operador2 = memoryToValue(pilaQuads[quadCounter][2])
        result = operador1 or operador2
        print(operador1, " ||", operador2, " => ", result)
        resultDir = pilaQuads[quadCounter][3]
        assignToMemory(result, resultDir)
        quadCounter += 1
    else:
        sys.exit(0)
#print(pilaQuads[quadCounter])
#print(pilaQuads[quadCounter][0])
