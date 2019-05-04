import ply.yacc as yacc
from lex import tokens

# Libreria pretty print
import pprint

# Import cubo semantico
from cuboSemantico import *

# Import memoria Virtual
from memoriaVirtual import *

# Variables globales para crear la var table
globalProgram = dict()
varList = []
programID = None
currentState = "global"
currentType = None
currentDimension = 0

# Varibles globales para Cuadruplos
vectorPolaco = []
pilaOper = []
pilaTipos = []
pilaQuads = []
currentIDAsignacion = None # Para guardar el ID al que se le va a asignar

def p_programa(p):
    'programa : PROGRAM ID puntoCreateProgram SEMICOLON puntoCreateVarTable puntoCreateVarTableState programa1 programa2 puntoChangeStateLocal puntoCreateVarTableState main puntoPrintFinal'
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

def p_puntoCreateProgram(p):
    'puntoCreateProgram : '
    global programID
    programID = p[-1]

def p_puntoChangeStateLocal(p):
    'puntoChangeStateLocal : '
    global currentState
    currentState = "main"

def p_puntoPrintFinal(p):
    'puntoPrintFinal : '
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

def p_puntoCreateVarType(p):
    'puntoCreateVarType : '
    for x in varList:
        globalProgram[programID][currentState]['varTable'][x]["Type"] = currentType
        if(currentState=="global"):
            currentDireccion = getGlobalDir(currentType)
        else:
            currentDireccion = getLocalDir(currentType)
        globalProgram[programID][currentState]['varTable'][x]["Direccion"] = currentDireccion
        #varList.pop(0)
    #pprint.pprint(globalProgram)

def p_puntoCreateDimension(p):
    'puntoCreateDimension : '
    global currentDimension
    while (len(varList) > 0):
        globalProgram[programID][currentState]['varTable'][varList[0]]["Dimension"] = currentDimension
        varList.pop(0)
    currentDimension = 0

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
    tipo_cte1 : LBRACKET CTE_INT RBRACKET
    | funciones_arr
    | empty
    '''
def p_puntoPushInt(p):
    'puntoPushInt : '
    vectorPolaco.append(p[-1])
    pilaTipos.append("int")

def p_puntoPushFloat(p):
    'puntoPushFloat : '
    vectorPolaco.append(p[-1])
    pilaTipos.append("float")

def p_puntoPushBool(p):
    'puntoPushBool : '
    vectorPolaco.append(p[-1])
    pilaTipos.append("bool")

def p_puntoPushChar(p):
    'puntoPushChar : '
    vectorPolaco.append(p[-1])
    pilaTipos.append("char")

def p_puntoPushID(p):
    'puntoPushID : '
    currentID = p[-1]
    vectorPolaco.append(currentID)
    #print(currentID)
    if currentID in globalProgram[programID][currentState]['varTable']:
        pilaTipos.append(globalProgram[programID][currentState]['varTable'][currentID]['Type'])
    elif currentID in globalProgram[programID]['global']['varTable']:
        pilaTipos.append(globalProgram[programID]['global']['varTable'][currentID]['Type'])
    else:
        print("not found in varTable, does not exist o es constante")
        #print(globalProgram[programID][currentState]['varTable'][currentID])

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
    'funciones : FUNC funciones1 ID puntoChangeStateFuncion puntoCreateVarTableState LPAREN funciones2 RPAREN bloque_modular'
def p_funciones1(p):
    '''
    funciones1 : VOID
    | tipo
    '''
def p_funciones2(p):
    '''
    funciones2 : tipo ID funciones3
    | empty
    '''
def p_funciones3(p):
    '''
    funciones3 : COMMA tipo ID funciones3
    | empty
    '''
def p_puntoChangeStateFuncion(p):
    'puntoChangeStateFuncion : '
    global currentState
    currentState = p[-1]

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
    asignacion1 : LBRACKET expresion RBRACKET
    | empty
    '''
def p_asignacion2(p):
    '''
    asignacion2 : expresion puntoCreateAsignacionQuad
    | leida
    '''
def p_puntoSaveIDAsignacion(p):
    'puntoSaveIDAsignacion :'
    global currentIDAsignacion
    currentIDAsignacion = p[-1]
def p_puntoCreateAsignacionQuad(p):
    'puntoCreateAsignacionQuad : '
    global currentIDAsignacion
    assignTo = vectorPolaco.pop()
    quad = ("=", currentIDAsignacion, None, assignTo)
    pilaQuads.append(quad)
    currentIDAsignacion = None

def p_leida(p):
    'leida : INPUT LPAREN RPAREN'

def p_condicion(p):
    'condicion : IF LPAREN expresion RPAREN bloque condicion1'
def p_condicion1(p):
    '''
    condicion1 : ELSE bloque
    | empty
    '''

def p_escritura(p):
    'escritura : PRINT LPAREN escritura1 RPAREN puntoCreatePrintQuad SEMICOLON'
def p_escritura1(p):
    '''
    escritura1 : expresion
    | CTE_STRING
    '''
def p_puntoCreatePrintQuad(p):
    'puntoCreatePrintQuad : '
    toPrint = vectorPolaco.pop()
    quad = ("write", None, None, toPrint)
    # print(quad)
    pilaQuads.append(quad);

def p_llamada(p):
    'llamada : CALL PUNTO ID LPAREN llamada1 RPAREN'
def p_llamada1(p):
    '''
    llamada1 : expresion llamada2
    | empty
    '''
def p_llamada2(p):
    '''
    llamada2 : COMMA tipo ID llamada2
    | empty
    '''

def p_return(p):
    'return : RETURN expresion SEMICOLON'

def p_while(p):
    'while : WHILE LPAREN expresion RPAREN bloque'

def p_do_while(p):
    'do_while : DO bloque WHILE LPAREN expresion RPAREN'

def p_expresion(p):
    'expresion : compare expresion2'
def p_expresion2(p):
    '''
    expresion2 : AND compare
    | OR compare
    | empty
    '''

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
        print("Error: Type mismatch")

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
    funciones_arr1 : MAX
    | MIN
    | RANGE
    | MEDIAN
    | AVERAGE
    | IQRANGE
    | STDEV
    | VARIANCE
    | MODIFY
    | DRAW
    '''

def p_empty(p):
    'empty : '

def p_error(p):
    if p:
        print("Syntax error at token", p.type)
        print(p.lexer.lineno)
    else:
        print("Syntax error at EOF")

# Build the parser
parser = yacc.yacc()

s = '''
program simple;
var globalCounter, sum as int;
void main()
{
    var a, b, c as int;

    a=1;
    b=2;
    c=3;
    c = b + a;
    print(a+b*c);
    if(b<a){
        print(b+1);
    }
    else{
        print(a+1);
    }
}
'''


result = parser.parse(s)

if(result is not None):
    print(result)
else:
    print("Exito!")
