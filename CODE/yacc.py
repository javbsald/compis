import ply.yacc as yacc
from lex import tokens

# Libreria pretty print
import pprint
import sys

# Import cubo semantico
from cuboSemantico import *

# Import memoria Virtual
from memoriaVirtual import *


# Variables globales para crear la var table
globalProgram = dict()
varList = []
paramList = []
paramListTypes = []
programID = None
currentState = "global"
currentType = None
currentDimension = 0
currentIDGlobal = None
arrBool = False
globalArr = None

# Varibles globales para Cuadruplos
vectorPolaco = []
pilaOper = []
pilaTipos = []
pilaQuads = []
pilaSaltos = []
pilaAsignacion = [] # Para guardar el ID al que se le va a asignar
goSubFunciones = dict() # Sostiene el currentQuad para hacer el salto (GOSUB)

# Variables globales para llamadas de funciones
llamadaIDExists = False
returnFlag = False
paramFlag = False
paramCounterToSend = 0
funcToCall = None

def p_programa(p):
    'programa : PROGRAM ID puntoCreateProgram SEMICOLON puntoCreateVarTable puntoCreateVarTableState programa1 programa2 puntoChangeStateLocal puntoCreateVarTableState puntoFillMainQuad main puntoPrintFinal'
def p_programa1(p):
    '''
    programa1 : vars programa1
    | empty
    '''
def p_programa2(p):
    '''
    programa2 : funciones programa2
    | empty
    '''
def p_puntoFillMainQuad(p):
    'puntoFillMainQuad : '
    goBack = pilaSaltos.pop()
    fillQuad(goBack, len(pilaQuads)+1)

def p_puntoCreateProgram(p):
    'puntoCreateProgram : '
    global programID
    programID = p[-1]
    quad = ("GOTO", None, None, None)
    pilaQuads.append(quad)
    pilaSaltos.append(len(pilaQuads)-1)

def p_puntoChangeStateLocal(p):
    'puntoChangeStateLocal : '
    global currentState
    currentState = "main"

def p_puntoPrintFinal(p):
    'puntoPrintFinal : '
    quad = ("EOF", None, None, None)
    pilaQuads.append(quad)
    pprint.pprint(globalProgram)
    pprint.pprint(pilaQuads)

def p_vars(p):
    'vars : VAR ID puntoCreateVar vars1 AS vars2 vars3 puntoCreateDimension SEMICOLON'
def p_vars1(p):
    '''
    vars1 : COMMA ID puntoCreateVar vars1
    | empty
    '''
def p_vars2(p):
    '''
    vars2 : tipo puntoCreateVarType
    | tipo_graph
    '''
def p_vars3(p):
    '''
    vars3 : LBRACKET CTE_INT puntoChangeDimension RBRACKET
    | empty
    '''

def p_puntoChangeDimension(p):
    'puntoChangeDimension : '
    global currentDimension
    global arrBool
    arrBool = True
    currentDimension = p[-1]

# Punto crear var table
def p_puntoCreateVarTable(p):
    'puntoCreateVarTable : '
    globalProgram[programID] = dict()

# Punto crear var table global/local
def p_puntoCreateVarTableState(p):
    'puntoCreateVarTableState : '
    globalProgram[programID][currentState] = dict()
    globalProgram[programID][currentState]['varTable'] = dict()

# Punto para meter variable al queue y crearla en la tabla
def p_puntoCreateVar(p):
    'puntoCreateVar : '
    currentVar = p[-1]
    varList.append(currentVar)
    globalProgram[programID][currentState]['varTable'][currentVar] = dict()
    globalProgram[programID][currentState]['varTable'][currentVar]["Name"] = currentVar
    if(paramFlag == True):
        paramList.append(currentVar)

def p_puntoCreateVarType(p):
    'puntoCreateVarType : '
    resetLocal()
    for x in varList:
        globalProgram[programID][currentState]['varTable'][x]["Type"] = currentType
        if(currentState=="global"):
            currentDireccion = getGlobalDir(currentType)
            globalProgram[programID][currentState]['varTable'][x]["Direccion"] = currentDireccion
            #print("Assign Dir", currentDireccion, "to", x, " as ", currentType)
        else:
            currentDireccion = getLocalDir(currentType)
            globalProgram[programID][currentState]['varTable'][x]["Direccion"] = currentDireccion
            #print("Assign Dir", currentDireccion, "to", x, " as ", currentType)
        #else:
            #look in param table
            #print(globalProgram[programID][currentState])
            #currentDireccion = globalProgram[programID][currentState]['paramTable'][x]["direccion"]
        #varList.pop(0)
    #pprint.pprint(globalProgram)

def p_puntoCreateDimension(p):
    'puntoCreateDimension : '
    global currentDimension
    global arrBool
    localAcum = currentDimension-1
    while (len(varList) > 0):
        globalProgram[programID][currentState]['varTable'][varList[0]]["Dimension"] = currentDimension
        tempType = globalProgram[programID][currentState]['varTable'][varList[0]]["Type"]
        varList.pop(0)
        if arrBool == True:
            if len(varList) > 0:
                #print(globalProgram[programID][currentState]['varTable'][varList[0]])
                tempDireccion = globalProgram[programID][currentState]['varTable'][varList[0]]["Direccion"]
                globalProgram[programID][currentState]['varTable'][varList[0]]["Direccion"] = tempDireccion+localAcum
                localAcum += currentDimension-1
    currentDimension = 0
    arrBool = False;

def p_tipo(p):
    '''
    tipo : INT puntoCurrentType
    | FLOAT puntoCurrentType
    | BOOL puntoCurrentType
    | CHAR puntoCurrentType
    '''
def p_puntoCurrentType(p):
    'puntoCurrentType : '
    global currentType
    currentType = p[-1]

def p_tipo_cte(p):
    '''
    tipo_cte : CTE_INT puntoPushInt
    | CTE_FLOAT puntoPushFloat
    | CTE_BOOL puntoPushBool
    | CTE_CHAR puntoPushChar
    | ID puntoPushID tipo_cte1
    | llamada
    '''
def p_tipo_cte1(p):
    '''
    tipo_cte1 : LBRACKET puntoPushFondoFalso puntoGuardarArr expresion puntoCreateArrQuad RBRACKET puntoPopFondoFalso
    | funciones_arr
    | empty
    '''
def p_puntoGuardarArr(p):
    'puntoGuardarArr : '
    global globalArr
    globalArr = currentIDGlobal;
def p_puntoPushInt(p):
    'puntoPushInt : '
    constanteInt = p[-1]
    if constanteInt in memoriaConstante:
        vectorPolaco.append(memoriaConstante[constanteInt])
    else:
        tempInt = getConstantDir("int")
        vectorPolaco.append(tempInt)
        memoriaConstante[constanteInt] =  tempInt
        memoriaConstanteDir[tempInt] = constanteInt
    #vectorPolaco.append(p[-1])
    #print("Push int", vectorPolaco)
    pilaTipos.append("int")

def p_puntoPushFloat(p):
    'puntoPushFloat : '
    constanteFloat = p[-1]
    if constanteFloat in memoriaConstante:
        vectorPolaco.append(memoriaConstante[constanteFloat])
    else:
        tempFloat = getConstantDir("float")
        vectorPolaco.append(tempFloat)
        memoriaConstante[constanteFloat] =  tempFloat
        memoriaConstanteDir[tempFloat] = constanteFloat
    #vectorPolaco.append(p[-1])
    pilaTipos.append("float")

def p_puntoPushBool(p):
    'puntoPushBool : '
    constanteBool = p[-1]
    if constanteBool in memoriaConstante:
        vectorPolaco.append(memoriaConstante[constanteBool])
    else:
        tempBool = getConstantDir("bool")
        vectorPolaco.append(tempBool)
        memoriaConstante[constanteBool] =  tempBool
        memoriaConstanteDir[tempBool] = constanteBool
    #vectorPolaco.append(p[-1])
    pilaTipos.append("bool")

def p_puntoPushChar(p):
    'puntoPushChar : '
    constanteChar = p[-1]
    if constanteChar in memoriaConstante:
        vectorPolaco.append(memoriaConstante[constanteChar])
    else:
        tempChar = getConstantDir("char")
        vectorPolaco.append(tempChar)
        memoriaConstante[constanteChar] =  tempChar
        memoriaConstanteDir[tempChar] = constanteChar
    #vectorPolaco.append(p[-1])
    pilaTipos.append("char")

def p_puntoPushID(p):
    'puntoPushID : '
    global currentIDGlobal
    currentID = p[-1]
    currentIDGlobal = currentID
    #vectorPolaco.append(currentID)
    #print("Push  ID ", currentID, " - ", globalProgram[programID][currentState]['varTable'][currentID]['Direccion'])
    if currentID in globalProgram[programID][currentState]['varTable']:
        tempDir = globalProgram[programID][currentState]['varTable'][currentID]['Direccion']
        vectorPolaco.append(tempDir)
        pilaTipos.append(globalProgram[programID][currentState]['varTable'][currentID]['Type'])
    elif currentID in globalProgram[programID]['global']['varTable']:
        tempDir = globalProgram[programID]['global']['varTable'][currentID]['Direccion']
        vectorPolaco.append(tempDir)
        pilaTipos.append(globalProgram[programID]['global']['varTable'][currentID]['Type'])
    else:
        print("ERROR: Variable not declared", str(p.lexer.lineno))
        sys.exit(0)
        #print(globalProgram[programID][currentState]['varTable'][currentID])
    #print("Push", currentIDGlobal, vectorPolaco)

def p_tipo_graph(p):
    '''
    tipo_graph : PIECHART
    | BARGRAPH
    | PLOTLINE
    '''

#def p_arr(p):
#    'arr : PUNTO arr1 LPAREN RPAREN'
#def p_arr1(p):
#    '''
#    arr1 : SIZE
#    | SORT
#    '''

def p_funciones(p):
    'funciones : FUNC puntoResetMemoria funciones1 ID puntoChangeStateFuncion puntoCreateVarTableState LPAREN puntoCreateParamTable funciones2 RPAREN puntoCreateParamCount bloque_modular puntoFinalFuncQuad'
def p_funciones1(p):
    '''
    funciones1 : VOID
    | tipo puntoReturnType
    '''
def p_funciones2(p):
    '''
    funciones2 : tipo ID puntoCreateVar puntoCreateVarType puntoPushParam funciones3
    | empty
    '''
def p_funciones3(p):
    '''
    funciones3 : COMMA tipo ID puntoCreateVar puntoCreateVarType puntoPushParam funciones3
    | empty
    '''
def p_puntoResetMemoria(p):
    'puntoResetMemoria : '
    resetLocal()
def p_puntoReturnType(p):
    'puntoReturnType : '
    global returnFlag
    returnFlag = True
def p_puntoChangeStateFuncion(p):
    'puntoChangeStateFuncion : '
    global currentState
    currentState = p[-1]
    goSubFunciones[currentState] = len(pilaQuads)+1
    #print("reset funcion local")
    #resetLocal()
def p_puntoCreateParamTable(p):
    'puntoCreateParamTable : '
    global paramFlag
    global returnFlag
    paramFlag = True;
    globalProgram[programID][currentState]['paramTable'] = dict()
    if returnFlag == True:
        globalProgram[programID][currentState]['returnType'] = currentType
        globalProgram[programID]['global']['varTable'][currentState] = dict()
        globalProgram[programID]['global']['varTable'][currentState]['Direccion'] = getGlobalDir(currentType)
        globalProgram[programID]['global']['varTable'][currentState]['Type'] = currentType
    else:
        globalProgram[programID][currentState]['returnType'] = "void"
    returnFlag = False
def p_puntoPushParam(p):
    'puntoPushParam : '
    paramListTypes.append(currentType)
def p_puntoCreateParamCount(p):
    'puntoCreateParamCount : '
    global paramFlag
    globalProgram[programID][currentState]['paramTable']['count'] = len(paramList)
    globalProgram[programID][currentState]['paramTable']['parametros'] = dict()
    globalProgram[programID][currentState]['paramTable']['types'] = dict()
    globalProgram[programID][currentState]['paramTable']['direccion'] = dict()
    resetLocal()
    while (len(paramList) > 0):
        #print("paramList - ", paramList.pop())
        globalProgram[programID][currentState]['paramTable']['parametros'][len(paramList)+1] = paramList.pop()
    while (len(paramListTypes) > 0):
        #print("paramListTypes - ", paramListTypes.pop())
        paramType = paramListTypes.pop()
        globalProgram[programID][currentState]['paramTable']['types'][len(paramListTypes)+1] = paramType
        globalProgram[programID][currentState]['paramTable']['direccion'][len(paramListTypes)+1] = getLocalDir(paramType)
    paramFlag = False
def p_puntoFinalFuncQuad(p):
    'puntoFinalFuncQuad : '
    quad = ("ENDPROC", None, None, None)
    pilaQuads.append(quad)
    # Reset memoria local porque termino la funcion
    resetLocal()

def p_main(p):
    'main : VOID MAIN LPAREN RPAREN bloque_modular'

def p_bloque_modular(p):
    'bloque_modular : LBLOQUE bloque_modular1 bloque_modular2 RBLOQUE'
def p_bloque_modular1(p):
    '''
    bloque_modular1 : vars bloque_modular1
    | empty
    '''
def p_bloque_modular2(p):
    '''
    bloque_modular2 : estatuto bloque_modular2
    | empty
    '''

def p_bloque(p):
    'bloque : LBLOQUE bloque1 RBLOQUE'
def p_bloque1(p):
    '''
    bloque1 : estatuto bloque1
    | empty
    '''

def p_estatuto(p):
    '''
    estatuto : asignacion
    | condicion
    | escritura
    | return
    | while
    | do_while
    | llamada SEMICOLON
    '''

def p_asignacion(p):
    'asignacion : ID puntoSaveIDAsignacion asignacion1 EQUALS asignacion2 SEMICOLON'
def p_asignacion1(p):
    '''
    asignacion1 : LBRACKET puntoGuardarArr puntoPushFondoFalso expresion puntoCreateArrQuad RBRACKET puntoPopFondoFalso
    | empty
    '''
def p_asignacion2(p):
    '''
    asignacion2 : expresion puntoCreateAsignacionQuad
    | leida
    '''
def p_puntoSaveIDAsignacion(p):
    'puntoSaveIDAsignacion :'
    global currentIDGlobal
    currentIDAsignacion = p[-1]
    currentIDGlobal = currentIDAsignacion
    #if currentState != "main" and currentState != "global":
    #    print("AQUIII", currentState, paramCounterToSend)
    #    print(globalProgram[programID][currentState]['paramTable'])

    #    tempDir = globalProgram[programID][currentState]['varTable'][currentIDAsignacion]['Direccion']
    #    vectorPolaco.append(tempDir)
    #    currentIDAsignacion = tempDir
    #    pilaAsignacion.append(currentIDAsignacion)
    if currentIDAsignacion in globalProgram[programID][currentState]['varTable']:
        tempDir = globalProgram[programID][currentState]['varTable'][currentIDAsignacion]['Direccion']
        vectorPolaco.append(tempDir)
        currentIDAsignacion = tempDir
        pilaAsignacion.append(currentIDAsignacion)
    elif currentIDAsignacion in globalProgram[programID]['global']['varTable']:
        tempDir = globalProgram[programID]['global']['varTable'][currentIDAsignacion]['Direccion']
        vectorPolaco.append(tempDir)
        currentIDAsignacion = tempDir
        pilaAsignacion.append(currentIDAsignacion)
    else:
        print("ERROR: Variable not declared", str(p.lexer.lineno))
        sys.exit(0)
def p_puntoCreateArrQuad(p):
    'puntoCreateArrQuad : '
    #print(vectorPolaco)
    aux2 = vectorPolaco.pop()
    aux1 = vectorPolaco.pop()
    #print(globalProgram[programID][currentState]['varTable'][currentIDGlobal])
    dimensionTemp = globalProgram[programID][currentState]['varTable'][globalArr]['Dimension']
    quad = ("VER", 0, dimensionTemp, aux2)
    pilaQuads.append(quad)
    typeTemp = globalProgram[programID][currentState]['varTable'][globalArr]['Type']
    tempDir = getTempDir(typeTemp)
    #print(memoriaConstante)
    #print(memoriaConstanteDir)
    # Hacer aux1 constante porque se le sumara la posicion del arreglo
    #quad = ("+", aux1, aux2, tempDir)
    #pilaQuads.append(quad)
    if aux1 in memoriaConstante:
        #print("10000 exists")
        tempInt = memoriaConstante[aux1]
    else:
        #print("10000 does NOT exist")
        tempInt = getConstantDir("int")
        memoriaConstante[aux1] =  tempInt
        memoriaConstanteDir[tempInt] = aux1
        #print("Assign", aux1, "a", tempInt)
    quad = ("+", tempInt, aux2, tempDir)
    #print("En la ", tempDir, "no contiene un valor, contiene una direccion")
    pilaQuads.append(quad)
    # Hacer la tempDir lista para meterlo como (tempDir)
    tempListDir = []
    tempListDir.append(tempDir)
    #print(tempListDir)
    vectorPolaco.append(tempListDir)
    pilaAsignacion.append(tempListDir)
def p_puntoCreateAsignacionQuad(p):
    'puntoCreateAsignacionQuad : '
    currentIDAsignacion = pilaAsignacion.pop()
    assignTo = vectorPolaco.pop()
    quad = ("=", assignTo, None, currentIDAsignacion)
    pilaQuads.append(quad)

def p_leida(p):
    'leida : INPUT LPAREN RPAREN'

def p_condicion(p):
    'condicion : IF LPAREN expresion RPAREN puntoCreateIfQuad bloque condicion1 puntoFillIfQuad'
def p_condicion1(p):
    '''
    condicion1 : ELSE puntoCreateElseQuad bloque
    | empty
    '''
def p_puntoCreateIfQuad(p):
    'puntoCreateIfQuad : '
    exp_type = pilaTipos.pop()
    if(exp_type != "bool"):
        print("Error: Type mismatch", str(p.lexer.lineno))
        sys.exit(0)
    else:
        result = vectorPolaco.pop()
        quad = ("GOTOF", result, None, None)
        pilaQuads.append(quad)
        pilaSaltos.append(len(pilaQuads)-1)
def p_puntoFillIfQuad(p):
    'puntoFillIfQuad : '
    end = pilaSaltos.pop()
    fillQuad(end, len(pilaQuads)+1)
def p_puntoCreateElseQuad(p):
    'puntoCreateElseQuad : '
    quad = ("GOTO", None, None, None)
    pilaQuads.append(quad)
    false = pilaSaltos.pop()
    pilaSaltos.append(len(pilaQuads)-1)
    fillQuad(false, len(pilaQuads)+1)

def fillQuad(previousJump, nextQuad):
    quad = pilaQuads[previousJump]
    newQuad = (quad[0], quad[1], quad[2], nextQuad)
    pilaQuads[previousJump] = newQuad

def p_escritura(p):
    'escritura : PRINT LPAREN puntoPushFondoFalso escritura1 RPAREN puntoPopFondoFalso SEMICOLON'
def p_escritura1(p):
    '''
    escritura1 : expresion puntoCreatePrintQuad
    | CTE_STRING puntoCreatePrintConstantQuad
    '''
def p_puntoCreatePrintQuad(p):
    'puntoCreatePrintQuad : '
    toPrint = vectorPolaco.pop()
    quad = ("write", None, None, toPrint)
    # print(quad)
    pilaQuads.append(quad);
def p_puntoCreatePrintConstantQuad(p):
    'puntoCreatePrintConstantQuad : '
    stringToPrint = p[-1]
    quad = ("write", None, None, stringToPrint)
    pilaQuads.append(quad)

def p_llamada(p):
    'llamada : CALL PUNTO puntoPushFondoFalso ID puntoVerifyLlamada LPAREN llamada1 RPAREN puntoPopFondoFalso puntoCreateGoSubQuad'
def p_llamada1(p):
    '''
    llamada1 : expresion puntoVerifyArgumento llamada2
    | empty
    '''
def p_llamada2(p):
    '''
    llamada2 : COMMA expresion puntoVerifyArgumento llamada2
    | empty
    '''
def p_puntoVerifyLlamada(p):
    'puntoVerifyLlamada : '
    global llamadaIDExists
    global paramCounterToSend
    global funcToCall
    llamadaID = p[-1]
    if llamadaID in globalProgram[programID]:
        #print (llamadaID, " found")
        funcToCall = llamadaID
        llamadaIDExists = True
        quad = ("ERA", None, None, llamadaID)
        pilaQuads.append(quad)
        paramCounterToSend = 0
    else:
        print("Error: Funcion ", llamadaID, " not found", str(p.lexer.lineno))
        sys.exit(0)
        llamadaIDExists = False
def p_puntoVerifyArgumento(p):
    'puntoVerifyArgumento : '
    global paramCounterToSend
    argumento = vectorPolaco.pop()
    argumentoType = pilaTipos.pop()
    #print("Comparing ", argumento, " - ", argumentoType, " vs. ")
    #print(globalProgram[programID][funcToCall]['paramTable']['types'][paramCounterToSend+1])
    if(argumentoType == globalProgram[programID][funcToCall]['paramTable']['types'][paramCounterToSend+1]):
        argumentoDir = globalProgram[programID][funcToCall]['paramTable']['direccion'][paramCounterToSend+1]
        quad = ("PARAM", argumento, None, argumentoDir)
        pilaQuads.append(quad)
    else:
        print("Error: Parameter Type mismatch", str(p.lexer.lineno))
        sys.exit(0)
    paramCounterToSend += 1
def p_puntoCreateGoSubQuad(p):
    'puntoCreateGoSubQuad : '
    jumpTo = goSubFunciones[funcToCall]
    quad = ("GOSUB", funcToCall, None, jumpTo)
    pilaQuads.append(quad)
    # Assign return
    if(globalProgram[programID][funcToCall]['returnType'] != "void"):
        tempDir = globalProgram[programID]['global']['varTable'][funcToCall]['Direccion']
        tempType = globalProgram[programID]['global']['varTable'][funcToCall]['Type']
        nextTempDir = getTempDir(tempType)
        quad = ("=", tempDir, None, nextTempDir)
        vectorPolaco.append(nextTempDir)
        pilaTipos.append(tempType)
        pilaQuads.append(quad)
        #print(funcToCall)
        #print(tempDir)

def p_return(p):
    'return : RETURN expresion puntoReturnQuad SEMICOLON'
def p_puntoReturnQuad(p):
    'puntoReturnQuad : '
    returnTemp = vectorPolaco.pop()
    returnDir = globalProgram[programID]['global']['varTable'][currentState]['Direccion']
    quad = ("RETURN", returnTemp, None, returnDir)
    pilaQuads.append(quad)

def p_while(p):
    'while : WHILE puntoPushSaltoWhile LPAREN expresion RPAREN puntoCreateWhileQuad bloque puntoEndWhileQuad'
def p_puntoPushSaltoWhile(p):
    'puntoPushSaltoWhile : '
    pilaSaltos.append(len(pilaQuads)+1)
def p_puntoCreateWhileQuad(p):
    'puntoCreateWhileQuad : '
    exp_type = pilaTipos.pop()
    if exp_type != "bool":
        print("Error: Type mismatch", str(p.lexer.lineno))
        sys.exit(0)
    else:
        result = vectorPolaco.pop()
        quad = ("GOTOF", result, None, None)
        pilaQuads.append(quad)
        pilaSaltos.append(len(pilaQuads)-1)
def p_puntoEndWhileQuad(p):
    'puntoEndWhileQuad : '
    end = pilaSaltos.pop()
    goBack = pilaSaltos.pop()
    quad = ("GOTO", None, None, goBack)
    pilaQuads.append(quad)
    fillQuad(end, len(pilaQuads)+1)

def p_do_while(p):
    'do_while : DO puntoPushSaltoDoWhile bloque WHILE LPAREN expresion RPAREN puntoCreateDoWhileQuad'
def p_puntoPushSaltoDoWhile(p):
    'puntoPushSaltoDoWhile : '
    pilaSaltos.append(len(pilaQuads)+1)
def p_puntoCreateDoWhileQuad(p):
    'puntoCreateDoWhileQuad : '
    exp_type = pilaTipos.pop()
    if exp_type != "bool":
        print("Error: Type mismatch", str(p.lexer.lineno))
        sys.exit(0)
    else:
        result = vectorPolaco.pop()
        goBack = pilaSaltos.pop()
        quad = ("GOTOT", None, None, goBack)
        pilaQuads.append(quad)

def p_expresion(p):
    'expresion : compare expresion2'
def p_expresion2(p):
    '''
    expresion2 : AND puntoPushOperador compare puntoAndOr
    | OR puntoPushOperador compare puntoAndOr
    | empty
    '''
def p_puntoAndOr(p):
    'puntoAndOr : '
    length = len(pilaOper)
    if length > 0:
        if pilaOper[length-1] == "&&":
            createOperationQuad()
        elif pilaOper[length-1] == "||":
            createOperationQuad()

def p_compare(p):
    'compare : exp compare1'
def p_compare1(p):
    '''
    compare1 : GREATERTHAN puntoPushOperador exp puntoOperacionRelacional
    | LESSTHAN puntoPushOperador exp puntoOperacionRelacional
    | GREATERTHANEQUAL puntoPushOperador exp puntoOperacionRelacional
    | LESSTHANEQUAL puntoPushOperador exp puntoOperacionRelacional
    | EQUALEQUAL puntoPushOperador exp puntoOperacionRelacional
    | NOTEQUAL puntoPushOperador exp puntoOperacionRelacional
    | empty
    '''
def p_puntoOperacionRelacional(p):
    'puntoOperacionRelacional : '
    length = len(pilaOper)
    if length > 0:
        if pilaOper[length-1] == "<":
            createOperationQuad()
        elif pilaOper[length-1] == ">":
            createOperationQuad()
        elif pilaOper[length-1] == ">=":
            createOperationQuad()
        elif pilaOper[length-1] == "<=":
            createOperationQuad()
        elif pilaOper[length-1] == "==":
            createOperationQuad()
        elif pilaOper[length-1] == "!=":
            createOperationQuad()

def p_exp(p):
    'exp : termino puntoSumaResta exp1'
def p_exp1(p):
    '''
    exp1 : PLUS puntoPushOperador termino puntoSumaResta exp1
    | MINUS puntoPushOperador termino puntoSumaResta exp1
    | empty
    '''

def p_puntoSumaResta(p):
    'puntoSumaResta : '
    length = len(pilaOper)
    if length > 0:
        if pilaOper[length-1] == "+":
            createOperationQuad()
        elif pilaOper[length-1] == "-":
            createOperationQuad()

# Se llama esta funcion cada vez que se uiere asignar alguna expresion aritmetica, logica o relacional
def createOperationQuad():
    right_operand = vectorPolaco.pop()
    right_Type = pilaTipos.pop()
    left_operand = vectorPolaco.pop()
    left_Type = pilaTipos.pop()
    operator = pilaOper.pop()

    operatorCube = convertSemCubeParam(operator)
    leftTypeCube = convertSemCubeParam(left_Type)
    rightTypeCube = convertSemCubeParam(right_Type)

    result_Type = semCube[operatorCube][leftTypeCube][rightTypeCube]

    result_Type = convertSemCubeParam(result_Type)

    if result_Type != "Error":
        result = getTempDir(result_Type)
        # print("create quad ", result_Type)
        quad = (operator, left_operand, right_operand, result)
        # print(quad)
        pilaQuads.append(quad)
        vectorPolaco.append(result)
        pilaTipos.append(result_Type)
    else:
        print("Error: Type mismatch", str(p.lexer.lineno))
        sys.exit(0)

def p_termino(p):
    'termino : factor puntoMultDivide termino1'
def p_termino1(p):
    '''
    termino1 : TIMES puntoPushOperador factor puntoMultDivide termino1
    | DIVIDE puntoPushOperador factor puntoMultDivide termino1
    | empty
    '''

def p_puntoMultDivide(p):
    'puntoMultDivide : '
    length = len(pilaOper)
    if length > 0:
        if pilaOper[length-1] == "*":
            createOperationQuad()
        elif pilaOper[length-1] == "/":
            createOperationQuad()

def p_puntoPushOperador(p):
    'puntoPushOperador : '
    pilaOper.append(p[-1])
    #print(p[-1], " added to pilaOper")

def p_factor(p):
    '''
    factor : LPAREN puntoPushFondoFalso expresion RPAREN puntoPopFondoFalso
    | tipo_cte
    | MINUS tipo_cte
    | NOT tipo_cte
    '''
def p_puntoPushFondoFalso(p):
    'puntoPushFondoFalso : '
    pilaOper.append("(")

def p_puntoPopFondoFalso(p):
    'puntoPopFondoFalso : '
    pilaOper.pop()

def p_funciones_arr(p):
    'funciones_arr : PUNTO funciones_arr1 LPAREN RPAREN'
def p_funciones_arr1(p):
    '''
    funciones_arr1 : MAX puntoCreateSpecial
    | MIN puntoCreateSpecial
    | RANGE puntoCreateSpecial
    | MEDIAN puntoCreateSpecial
    | AVERAGE puntoCreateSpecial
    | IQRANGE
    | STDEV puntoCreateSpecial
    | VARIANCE puntoCreateSpecial
    | MODIFY
    | DRAW puntoCreateSpecial
    | SORT puntoCreateSpecial
    '''
def p_puntoCreateSpecial(p):
    'puntoCreateSpecial : '
    specialFuncToCall = p[-1]
    arrToSend = vectorPolaco.pop()
    #print(arrToSend)
    #print(currentIDGlobal)
    arrDimToSend = globalProgram[programID][currentState]['varTable'][currentIDGlobal]["Dimension"]
    if specialFuncToCall in globalProgram[programID][currentState]['varTable']:
        resultDir = globalProgram[programID][currentState]['varTable'][specialFuncToCall]['Direccion']
        arrType = globalProgram[programID][currentState]['varTable'][specialFuncToCall]['Type']
    else:
        globalProgram[programID][currentState]['varTable'][specialFuncToCall] = dict()
        globalProgram[programID][currentState]['varTable'][specialFuncToCall]['Direccion'] = dict()
        globalProgram[programID][currentState]['varTable'][specialFuncToCall]['Type'] = dict()
        if specialFuncToCall == "max" or specialFuncToCall == "min":
            arrType = globalProgram[programID][currentState]['varTable'][currentIDGlobal]['Type']
            #print(globalProgram[programID][currentState]['varTable'][currentIDGlobal]['Type'])
        else:
            arrType = "float"
        resultDir = getTempDir(arrType)
        globalProgram[programID][currentState]['varTable'][specialFuncToCall]['Direccion'] = resultDir
        globalProgram[programID][currentState]['varTable'][specialFuncToCall]['Type'] = arrType

    #print("MAX TYPE", arrType, resultDir)
    if specialFuncToCall=="draw":
        if arrDimToSend % 2 != 0:
            print("Error: Please establish the same amount of X and Y")
            sys.exit(0)
    if specialFuncToCall=="sort":
        quad = (specialFuncToCall, arrDimToSend, arrToSend, arrToSend)
    else:
        quad = (specialFuncToCall, arrDimToSend, arrToSend, resultDir)
    pilaQuads.append(quad)

    vectorPolaco.append(resultDir)
    pilaTipos.append(arrType)
    #print(vectorPolaco)

    nextTempDir = getTempDir(arrType)
    quad = ("=", resultDir, None, nextTempDir)
    pilaQuads.append(quad)
    vectorPolaco.append(nextTempDir)
    pilaTipos.append(arrType)

def p_empty(p):
    'empty : '

def p_error(p):
    if p:
        print("Syntax error at token", p.type)
        print(p.lexer.lineno)
        sys.exit(0)
    else:
        print("Syntax error at EOF")

# Build the parser
parser = yacc.yacc()

# Get text file to read and run
#print("File to read (______.txt)")
#fileToRead = input()
#fileToRead += ".txt"
# Open and Read file
#file = open(fileToRead, "r")
#s = file.read()
s = '''
program arrays;
void main()
{
    var arr as int[6];
    var x, y, result as float;

    x=1;

    //Arr X
    arr[1] = 7;
    arr[2] = 12;
    arr[3] = 4;
    //Arr Y
    arr[4] = 6;
    arr[5] = 10;
    arr[6] = 5;
    print("Array Created");
    
    x=1;
    while(x<=6)
    {
        print(arr[x]);
        x=x+1;
    }

    y=10;
    // Find de Array
    print("Find");
    x=1;
    while(x<=6)
    {
        if(arr[x]==y)
        {
            print("Found in position");
            print (x);
        }
        x = x + 1;
    }
        
    print("Sort");
    result = arr.sort();
    x=1;
    while(x<=6)
    {
        print(arr[x]);
        x=x+1;
    }
    
    print("Multiply x2 if less than 10");
    x=1;
    while(x<=6)
    {
        if(arr[x]<10)
        {
            arr[x] = arr[x] * 2;
        }
        x = x + 1;
    }
    x=1;
    while(x<=6)
    {
        print(arr[x]);
        x=x+1;
    }
    
    print("Create Array Acumulutivo");
    x=1;
    while(x<=5)
    {
        arr[x] = arr[x] + arr[x+1];
        x = x + 1;
    }
    x=1;
    while(x<=6)
    {
        print(arr[x]);
        x=x+1;
    }
    

    print("Max");
    result = arr.max();
    print(result);

    print("Min");
    print(arr.min());

    print("Range");
    print(arr.range());

    print("Median");
    print(arr.median());

    print("Average");
    print(arr.average());

    print("Standard Deviation");
    print(arr.stdev());

    print("Variance");
    print(arr.variance());
    
    print("Draw Linear Regression");
    result = arr.draw();

    //result = arr.max() + arr.average();
    //print(result);
}


'''

result = parser.parse(s)

if(result is not None):
    print(result)
else:
    print("Exito!")
