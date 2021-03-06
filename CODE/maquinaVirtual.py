# Maquina Virtual

from yacc import pilaQuads

import pprint
import sys

import statistics

import numpy as np
import matplotlib.pyplot as plt

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

# Funcion que recibe una direccion de memoria y busca en la lista de memoria para conseguir el valor de esa direccion
def memoryToValue(mem):
    if mem >= 1000 and mem < 10000:     # Global
        if mem in memoriaGlobal:
            return memoriaGlobal[mem]
        else:
            print(mem, "Not found in Global Memory")
    elif mem >= 10000 and mem < 20000:  # Local
        #print(mem, " in ", localList, " lengh=", localListLength)
        if mem in localList[localListLength-1]:
            return localList[localListLength-1][mem]
        else:
            print(mem, "Not found Local Memory")
    elif mem >= 20000 and mem < 25000:  # Temp
        if mem in memoriaTemporal:
            return memoriaTemporal[mem]
        else:
            print(mem, "Not found in Temporal Memory")
    elif mem >= 25000 and mem < 30000:  # Const
        return memoriaConstanteDir[mem]

# Funcion que recibe result para asignar a la direccion de resultDir
def assignToMemory(result, resultDir):
    if resultDir >= 1000 and resultDir < 10000:     # Global
        memoriaGlobal[resultDir] = result
    elif resultDir >= 10000 and resultDir < 20000:  # Local
        localList[localListLength-1][resultDir] = result
    elif resultDir >= 20000 and resultDir < 25000:
        memoriaTemporal[resultDir] = result
    #elif resultDir >= 25000 and resultDir < 30000:  # Const
        #memoriaConstante[resultDir] = result

# Como podemos tener direcciones de memoria que apuntan a otra direccion de memoria
# esta funcion verifica que ninguna de los otros 3 que no es el inicial sea un apuntador
def verifyQuadDirections(quadRecieved):
    #print("Quad Recieved")
    #print(quadRecieved)
    #print(isinstance(quadRecieved[1], int))
    #print(isinstance(quadRecieved[2], int))
    #print(isinstance(quadRecieved[3], int))
    newDir1=quadRecieved[1]
    newDir2=quadRecieved[2]
    newDir3=quadRecieved[3]
    if(isinstance(quadRecieved[1], int) == False):
        if quadRecieved[1] != None:
            #print(quadRecieved[1], "NOT INT")
            newDir1 = memoryToValue(quadRecieved[1][0])
    if(isinstance(quadRecieved[2], int) == False):
        if quadRecieved[2] != None:
            #print(quadRecieved[2], "NOT INT")
            newDir2 = memoryToValue(quadRecieved[2][0])
    if(isinstance(quadRecieved[3], int) == False):
        if quadRecieved[3] != None:
            #print(quadRecieved[3], "NOT INT")
            newDir3 = memoryToValue(quadRecieved[3][0])
    newQuad = (quadRecieved[0], newDir1, newDir2, newDir3)
    #print("Quad Converted", newQuad)
    return newQuad

# Funciones Predeterminadas
def getArray(arr, dim):
    counter = 1
    arrValues = []
    #print(arr, dim)
    while(counter<=dim):
        value = memoryToValue(arr+counter)
        #print(value)
        arrValues.append(value)
        counter += 1
    # print("GET ARRAY", arrValues)
    return arrValues

# Funciones necesarias para crear Regresion Lineal
# Sacadas de: https://www.geeksforgeeks.org/linear-regression-python-implementation/
def estimate_coef(x, y):
    # number of observations/points
    n = np.size(x)

    # mean of x and y vector
    m_x, m_y = np.mean(x), np.mean(y)

    # calculating cross-deviation and deviation about x
    SS_xy = np.sum(y*x) - n*m_y*m_x
    SS_xx = np.sum(x*x) - n*m_x*m_x

    # calculating regression coefficients
    b_1 = SS_xy / SS_xx
    b_0 = m_y - b_1*m_x

    return(b_0, b_1)

def plot_regression_line(x, y, b):
    # plotting the actual points as scatter plot
    plt.scatter(x, y, color = "m",
               marker = "o", s = 30)

    # predicted response vector
    y_pred = b[0] + b[1]*x

    # plotting the regression line
    plt.plot(x, y_pred, color = "g")

    # putting labels
    plt.xlabel('x')
    plt.ylabel('y')

    # function to show plot
    plt.show()

while True:
    #print("doing", pilaQuads[quadCounterList[currentquadCounter]][0], pilaQuads[quadCounterList[currentquadCounter]])
    #print(memoriaLocal)
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
        #print("ERA")
        quadCounterList[currentquadCounter] += 1
    elif pilaQuads[quadCounterList[currentquadCounter]][0] == "PARAM":
        valueParam = memoryToValue(pilaQuads[quadCounterList[currentquadCounter]][1])
        assignTo = pilaQuads[quadCounterList[currentquadCounter]][3]
        actRecord[assignTo] = valueParam
        #print("PARAM", assignTo, " = ", valueParam)
        quadCounterList[currentquadCounter] += 1
    elif pilaQuads[quadCounterList[currentquadCounter]][0] == "GOSUB":
        #quadCounterList[currentquadCounter] = pilaQuads[quadCounterList[currentquadCounter]][3] - 1
        localList.append(actRecord)
        localListLength = len(localList)
        goSubTemp = pilaQuads[quadCounterList[currentquadCounter]][3] - 1
        #print("GOSUB", goSubTemp)
        quadCounterList[currentquadCounter] += 1 #para que no regrese al gosub
        quadCounterList.append(goSubTemp)
        currentquadCounter=len(quadCounterList)-1
        #print("Global", memoriaGlobal)
        #print(localList[localListLength-1])
        #print(quadCounterList)
    elif pilaQuads[quadCounterList[currentquadCounter]][0] == "RETURN":
        result = pilaQuads[quadCounterList[currentquadCounter]][1]
        resultDir = pilaQuads[quadCounterList[currentquadCounter]][3]
        #print(resultDir, " = ", result)
        resultValue = memoryToValue(result)
        assignToMemory(resultValue, resultDir)
        #print("RETURN", resultDir, " = ", resultValue)
        localList.pop()
        localListLength = len(localList)
        quadCounterList.pop()
        currentquadCounter=len(quadCounterList)-1
        #print("POPRETURN", quadCounterList[currentquadCounter])
        #print(quadCounterList)
    elif pilaQuads[quadCounterList[currentquadCounter]][0] == "ENDPROC":
        localList.pop()
        localListLength = len(localList)
        quadCounterList.pop()
        currentquadCounter=len(quadCounterList)-1
        #print("ENDPROC", quadCounterList[currentquadCounter])
        #print(quadCounterList)
    elif pilaQuads[quadCounterList[currentquadCounter]][0] == "write":
        toPrint = pilaQuads[quadCounterList[currentquadCounter]][3]
        if type(toPrint) == str:
            print(toPrint)
        else:
            quadToWork = verifyQuadDirections(pilaQuads[quadCounterList[currentquadCounter]])
            #print(quadToWork)
            toPrint = quadToWork[3]
            #print("Printing...", toPrint)
            resultValue = memoryToValue(toPrint)
            print(resultValue)
        quadCounterList[currentquadCounter] += 1
    elif pilaQuads[quadCounterList[currentquadCounter]][0] == "VER":
        #print("VER", pilaQuads[quadCounterList[currentquadCounter]])
        toVerifyDir = pilaQuads[quadCounterList[currentquadCounter]][3]
        toVerify = memoryToValue(toVerifyDir)
        limiteInferior = pilaQuads[quadCounterList[currentquadCounter]][1]
        limiteSuperior = pilaQuads[quadCounterList[currentquadCounter]][2]
        if toVerify > limiteInferior and toVerify <= limiteSuperior:
            quadCounterList[currentquadCounter] += 1
        else:
            print("Error: Array out of Bounds")
            sys.exit(0)
    elif pilaQuads[quadCounterList[currentquadCounter]][0] == "max":
        arrDim = pilaQuads[quadCounterList[currentquadCounter]][1]
        arrDir = pilaQuads[quadCounterList[currentquadCounter]][2]
        resultDir = pilaQuads[quadCounterList[currentquadCounter]][3]

        array=getArray(arrDir, arrDim)
        maxValue = max(array)
        #print("Max from", array, " - ", maxValue)
        #print("Assign", maxValue, " a ", resultDir)
        assignToMemory(maxValue, resultDir)
        #resultValue = memoryToValue(maxValue)
        #print("RETURN", resultDir, " = ", resultValue)
        # assignToMemory()
        quadCounterList[currentquadCounter] += 1
    elif pilaQuads[quadCounterList[currentquadCounter]][0] == "min":
        arrDim = pilaQuads[quadCounterList[currentquadCounter]][1]
        arrDir = pilaQuads[quadCounterList[currentquadCounter]][2]
        resultDir = pilaQuads[quadCounterList[currentquadCounter]][3]

        array=getArray(arrDir, arrDim)
        minValue = min(array)
        assignToMemory(minValue, resultDir)
        quadCounterList[currentquadCounter] += 1
    elif pilaQuads[quadCounterList[currentquadCounter]][0] == "range":
        arrDim = pilaQuads[quadCounterList[currentquadCounter]][1]
        arrDir = pilaQuads[quadCounterList[currentquadCounter]][2]
        resultDir = pilaQuads[quadCounterList[currentquadCounter]][3]

        array=getArray(arrDir, arrDim)
        maxValue = max(array)
        minValue = min(array)
        rangeValue = maxValue - minValue
        assignToMemory(rangeValue, resultDir)
        quadCounterList[currentquadCounter] += 1
    elif pilaQuads[quadCounterList[currentquadCounter]][0] == "median":
        arrDim = pilaQuads[quadCounterList[currentquadCounter]][1]
        arrDir = pilaQuads[quadCounterList[currentquadCounter]][2]
        resultDir = pilaQuads[quadCounterList[currentquadCounter]][3]

        array=getArray(arrDir, arrDim)
        midValue = statistics.median(array)
        assignToMemory(midValue, resultDir)
        quadCounterList[currentquadCounter] += 1
    elif pilaQuads[quadCounterList[currentquadCounter]][0] == "average":
        arrDim = pilaQuads[quadCounterList[currentquadCounter]][1]
        arrDir = pilaQuads[quadCounterList[currentquadCounter]][2]
        resultDir = pilaQuads[quadCounterList[currentquadCounter]][3]

        array=getArray(arrDir, arrDim)
        arrCounter=0
        arrSum=0
        while(arrCounter < arrDim):
            arrSum += array[arrCounter]
            #print(arrSum)
            arrCounter += 1
        arrSum /= arrDim
        #print("Avg", arrSum)
        assignToMemory(arrSum, resultDir)
        quadCounterList[currentquadCounter] += 1
    elif pilaQuads[quadCounterList[currentquadCounter]][0] == "stdev":
        arrDim = pilaQuads[quadCounterList[currentquadCounter]][1]
        arrDir = pilaQuads[quadCounterList[currentquadCounter]][2]
        resultDir = pilaQuads[quadCounterList[currentquadCounter]][3]

        array=getArray(arrDir, arrDim)
        stdevValue = statistics.stdev(array)
        assignToMemory(stdevValue, resultDir)
        quadCounterList[currentquadCounter] += 1
    elif pilaQuads[quadCounterList[currentquadCounter]][0] == "variance":
        arrDim = pilaQuads[quadCounterList[currentquadCounter]][1]
        arrDir = pilaQuads[quadCounterList[currentquadCounter]][2]
        resultDir = pilaQuads[quadCounterList[currentquadCounter]][3]

        array=getArray(arrDir, arrDim)
        varianceValue = statistics.variance(array)
        assignToMemory(varianceValue, resultDir)
        quadCounterList[currentquadCounter] += 1
    elif pilaQuads[quadCounterList[currentquadCounter]][0] == "draw":
        arrDim = pilaQuads[quadCounterList[currentquadCounter]][1]
        arrDir = pilaQuads[quadCounterList[currentquadCounter]][2]
        resultDir = pilaQuads[quadCounterList[currentquadCounter]][3]

        halfPoint = arrDim/2
        arrayX=getArray(arrDir, halfPoint)
        arrayY=getArray(arrDir+halfPoint, halfPoint)
        x=np.array(arrayX)
        y=np.array(arrayY)
        b = estimate_coef(x, y)
        plot_regression_line(x, y, b)
        quadCounterList[currentquadCounter] += 1
    elif pilaQuads[quadCounterList[currentquadCounter]][0] == "sort":
        arrDim = pilaQuads[quadCounterList[currentquadCounter]][1]
        arrDir = pilaQuads[quadCounterList[currentquadCounter]][2]
        resultDir = pilaQuads[quadCounterList[currentquadCounter]][3]

        array=getArray(arrDir, arrDim)
        array.sort()
        x=1
        while x<=arrDim:
            assignToMemory(array[x-1], resultDir+x)
            x=x+1
        #print(array)
        quadCounterList[currentquadCounter] += 1
    elif pilaQuads[quadCounterList[currentquadCounter]][0] == "=":
        #print("MAQUINA VIRTUAL ASIGNACION")
        #print(pilaQuads[quadCounterList[currentquadCounter]])
        #print("to")
        quadToWork = verifyQuadDirections(pilaQuads[quadCounterList[currentquadCounter]])
        #print(quadToWork)
        result = quadToWork[1]
        resultDir = quadToWork[3]
        #print(resultDir, " = ", result)
        # Checar si a lo que vas a asignar es apuntador
        #print("Checar si realmente es Direccion", resultDir)
        resultValue = memoryToValue(result)
        assignToMemory(resultValue, resultDir)
        #print(resultDir, " = ", resultValue)
        #print(memoriaGlobal, memoriaLocal, memoriaTemporal)
        quadCounterList[currentquadCounter] += 1
    elif pilaQuads[quadCounterList[currentquadCounter]][0] == "+":
        quadToWork = verifyQuadDirections(pilaQuads[quadCounterList[currentquadCounter]])
        operador1 = memoryToValue(quadToWork[1])
        operador2 = memoryToValue(quadToWork[2])
        #print(operador1, " + ", operador2)
        result = operador1 + operador2
        resultDir = quadToWork[3]
        assignToMemory(result, resultDir)
        quadCounterList[currentquadCounter] += 1
    elif pilaQuads[quadCounterList[currentquadCounter]][0] == "-":
        quadToWork = verifyQuadDirections(pilaQuads[quadCounterList[currentquadCounter]])
        operador1 = memoryToValue(quadToWork[1])
        operador2 = memoryToValue(quadToWork[2])
        #print(operador1, " - ", operador2)
        result = operador1 - operador2
        resultDir = quadToWork[3]
        assignToMemory(result, resultDir)
        quadCounterList[currentquadCounter] += 1
    elif pilaQuads[quadCounterList[currentquadCounter]][0] == "*":
        quadToWork = verifyQuadDirections(pilaQuads[quadCounterList[currentquadCounter]])
        operador1 = memoryToValue(quadToWork[1])
        operador2 = memoryToValue(quadToWork[2])
        #print(operador1, " * ", operador2)
        result = operador1 * operador2
        resultDir = quadToWork[3]
        assignToMemory(result, resultDir)
        quadCounterList[currentquadCounter] += 1
    elif pilaQuads[quadCounterList[currentquadCounter]][0] == "/":
        quadToWork = verifyQuadDirections(pilaQuads[quadCounterList[currentquadCounter]])
        operador1 = memoryToValue(quadToWork[1])
        operador2 = memoryToValue(quadToWork[2])
        #print(operador1, " / ", operador2)
        result = operador1 / operador2
        resultDir = quadToWork[3]
        assignToMemory(result, resultDir)
        quadCounterList[currentquadCounter] += 1
    elif pilaQuads[quadCounterList[currentquadCounter]][0] == "<":
        quadToWork = verifyQuadDirections(pilaQuads[quadCounterList[currentquadCounter]])
        operador1 = memoryToValue(quadToWork[1])
        operador2 = memoryToValue(quadToWork[2])
        #print(operador1, " < ", operador2)
        result = operador1 < operador2
        resultDir = quadToWork[3]
        assignToMemory(result, resultDir)
        quadCounterList[currentquadCounter] += 1
    elif pilaQuads[quadCounterList[currentquadCounter]][0] == ">":
        quadToWork = verifyQuadDirections(pilaQuads[quadCounterList[currentquadCounter]])
        operador1 = memoryToValue(quadToWork[1])
        operador2 = memoryToValue(quadToWork[2])
        #print(operador1, " > ", operador2)
        result = operador1 > operador2
        resultDir = quadToWork[3]
        assignToMemory(result, resultDir)
        quadCounterList[currentquadCounter] += 1
    elif pilaQuads[quadCounterList[currentquadCounter]][0] == "<=":
        quadToWork = verifyQuadDirections(pilaQuads[quadCounterList[currentquadCounter]])
        operador1 = memoryToValue(quadToWork[1])
        operador2 = memoryToValue(quadToWork[2])
        #print(operador1, " <= ", operador2)
        result = operador1 <= operador2
        resultDir = quadToWork[3]
        assignToMemory(result, resultDir)
        quadCounterList[currentquadCounter] += 1
    elif pilaQuads[quadCounterList[currentquadCounter]][0] == ">=":
        quadToWork = verifyQuadDirections(pilaQuads[quadCounterList[currentquadCounter]])
        operador1 = memoryToValue(quadToWork[1])
        operador2 = memoryToValue(quadToWork[2])
        #print(operador1, " >= ", operador2)
        result = operador1 >= operador2
        resultDir = quadToWork[3]
        assignToMemory(result, resultDir)
        quadCounterList[currentquadCounter] += 1
    elif pilaQuads[quadCounterList[currentquadCounter]][0] == "==":
        quadToWork = verifyQuadDirections(pilaQuads[quadCounterList[currentquadCounter]])
        operador1 = memoryToValue(quadToWork[1])
        operador2 = memoryToValue(quadToWork[2])
        result = operador1 == operador2
        #print(operador1, " == ", operador2, " => ", result)
        resultDir = quadToWork[3]
        assignToMemory(result, resultDir)
        quadCounterList[currentquadCounter] += 1
    elif pilaQuads[quadCounterList[currentquadCounter]][0] == "!=":
        quadToWork = verifyQuadDirections(pilaQuads[quadCounterList[currentquadCounter]])
        operador1 = memoryToValue(quadToWork[1])
        operador2 = memoryToValue(quadToWork[2])
        result = operador1 != operador2
        #print(operador1, " != ", operador2, " => ", result)
        resultDir = quadToWork[3]
        assignToMemory(result, resultDir)
        quadCounterList[currentquadCounter] += 1
    elif pilaQuads[quadCounterList[currentquadCounter]][0] == "&&":
        quadToWork = verifyQuadDirections(pilaQuads[quadCounterList[currentquadCounter]])
        operador1 = memoryToValue(quadToWork[1])
        operador2 = memoryToValue(quadToWork[2])
        result = operador1 and operador2
        #print(operador1, " && ", operador2, " => ", result)
        resultDir = quadToWork[3]
        assignToMemory(result, resultDir)
        quadCounterList[currentquadCounter] += 1
    elif pilaQuads[quadCounterList[currentquadCounter]][0] == "||":
        quadToWork = verifyQuadDirections(pilaQuads[quadCounterList[currentquadCounter]])
        operador1 = memoryToValue(quadToWork[1])
        operador2 = memoryToValue(quadToWork[2])
        result = operador1 or operador2
        #print(operador1, " ||", operador2, " => ", result)
        resultDir = quadToWork[3]
        assignToMemory(result, resultDir)
        quadCounterList[currentquadCounter] += 1
    elif pilaQuads[quadCounterList[currentquadCounter]][0] == "EOF":
        sys.exit(0)
    else:
        sys.exit(0)
#print(pilaQuads[quadCounterList[currentquadCounter]])
#print(pilaQuads[quadCounterList[currentquadCounter]][0])
