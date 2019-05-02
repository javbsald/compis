import ply.yacc as yacc
import pprint
from lex import tokens

# Variables globales para crear la var table
globalProgram = dict()
varList = []
programID = None
currentState = "global"
currentType = None
currentDimension = 0

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
    tipo_cte : CTE_INT
    | CTE_FLOAT
    | CTE_BOOL
    | CTE_CHAR
    | ID tipo_cte1
    | llamada
    '''
def p_tipo_cte1(p):
    '''
    tipo_cte1 : LBRACKET CTE_INT RBRACKET
    | funciones_arr
    | empty
    '''

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
    'asignacion : ID asignacion1 EQUALS asignacion2 SEMICOLON'
def p_asignacion1(p):
    '''
    asignacion1 : LBRACKET expresion RBRACKET
    | empty
    '''
def p_asignacion2(p):
    '''
    asignacion2 : expresion
    | leida
    '''

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
    'escritura : PRINT LPAREN escritura1 RPAREN SEMICOLON'
def p_escritura1(p):
    '''
    escritura1 : expresion
    | CTE_STRING
    '''

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
    compare1 : GREATERTHAN exp
    | LESSTHAN exp
    | GREATERTHANEQUAL exp
    | LESSTHANEQUAL exp
    | EQUALEQUAL exp
    | NOTEQUAL exp
    | empty
    '''

def p_exp(p):
    'exp : termino exp1'
def p_exp1(p):
    '''
    exp1 : PLUS termino exp1
    | MINUS termino exp1
    | empty
    '''

def p_termino(p):
    'termino : factor termino1'
def p_termino1(p):
    '''
    termino1 : TIMES factor termino1
    | DIVIDE factor termino1
    | empty
    '''

def p_factor(p):
    '''
    factor : LPAREN expresion RPAREN
    | tipo_cte
    | MINUS tipo_cte
    | NOT tipo_cte
    '''

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
program patito2k19;
var globalCounter, sum as int;
// globalCounter = 100;
func int suma1(int x)
{
    var y as int;
    var pog as char[100];
    y = x/2;
    x = y+1;
    print(10);
    return x;
}
func void printSmile()
{
    print("happy face");
}
void main()
{
    var counter, secondArr as int[10];
    var pi as float;
    var x as int;
    if(counter[5]>10)
    {
        counter[5] = input();
    }
    else
    {
        print(counter.average());
    }
    print(30);
    pi = 3.14;
    // two decimals
    x = call.suma1(x);
    boolID = true;
    chad = 'A';
    call.printSmile();
    x = call.factorial(4) + call.factorial(5);
    print("end");
}
'''


result = parser.parse(s)

if(result is not None):
    print(result)
else:
    print("Exito!")
