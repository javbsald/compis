
# parsetab.py
# This file is automatically generated. Do not edit.
# pylint: disable=W,C,R
_tabversion = '3.10'

_lr_method = 'LALR'

_lr_signature = 'AND AS AVERAGE BARGRAPH BOOL CALL CHAR COMMA CTE_BOOL CTE_CHAR CTE_FLOAT CTE_INT CTE_STRING DIVIDE DO DRAW ELSE EQUALEQUAL EQUALS FLOAT FUNC GREATERTHAN GREATERTHANEQUAL ID IF INPUT INT IQRANGE LBLOQUE LBRACKET LESSTHAN LESSTHANEQUAL LPAREN MAIN MAX MEDIAN MIN MINUS MODIFY NOT NOTEQUAL OR PIECHART PLOTLINE PLUS PRINT PROGRAM PUNTO RANGE RBLOQUE RBRACKET RETURN RPAREN SEMICOLON STDEV TIMES VAR VARIANCE VOID WHILEprograma : PROGRAM ID puntoCreateProgram SEMICOLON puntoCreateVarTable puntoCreateVarTableState programa1 programa2 puntoChangeStateLocal puntoCreateVarTableState puntoFillMainQuad main puntoPrintFinal\n    programa1 : vars programa1\n    | empty\n    \n    programa2 : funciones programa2\n    | empty\n    puntoFillMainQuad : puntoCreateProgram : puntoChangeStateLocal : puntoPrintFinal : vars : VAR ID puntoCreateVar vars1 AS vars2 vars3 puntoCreateDimension SEMICOLON\n    vars1 : COMMA ID puntoCreateVar vars1\n    | empty\n    \n    vars2 : tipo puntoCreateVarType\n    | tipo_graph\n    \n    vars3 : LBRACKET CTE_INT puntoChangeDimension RBRACKET\n    | empty\n    puntoChangeDimension : puntoCreateVarTable : puntoCreateVarTableState : puntoCreateVar : puntoCreateVarType : puntoCreateDimension : \n    tipo : INT puntoCurrentType\n    | FLOAT puntoCurrentType\n    | BOOL puntoCurrentType\n    | CHAR puntoCurrentType\n    puntoCurrentType : \n    tipo_cte : CTE_INT puntoPushInt\n    | CTE_FLOAT puntoPushFloat\n    | CTE_BOOL puntoPushBool\n    | CTE_CHAR puntoPushChar\n    | ID puntoPushID tipo_cte1\n    | llamada\n    \n    tipo_cte1 : LBRACKET CTE_INT RBRACKET\n    | funciones_arr\n    | empty\n    puntoPushInt : puntoPushFloat : puntoPushBool : puntoPushChar : puntoPushID : \n    tipo_graph : PIECHART\n    | BARGRAPH\n    | PLOTLINE\n    funciones : FUNC funciones1 ID puntoChangeStateFuncion puntoCreateVarTableState LPAREN puntoCreateParamTable funciones2 RPAREN puntoCreateParamCount bloque_modular puntoFinalFuncQuad\n    funciones1 : VOID\n    | tipo puntoReturnType\n    \n    funciones2 : tipo ID puntoCreateVar puntoCreateVarType puntoPushParam funciones3\n    | empty\n    \n    funciones3 : COMMA tipo ID puntoCreateVar puntoCreateVarType puntoPushParam funciones3\n    | empty\n    puntoReturnType : puntoChangeStateFuncion : puntoCreateParamTable : puntoPushParam : puntoCreateParamCount : puntoFinalFuncQuad : main : VOID MAIN LPAREN RPAREN bloque_modularbloque_modular : LBLOQUE bloque_modular1 bloque_modular2 RBLOQUE\n    bloque_modular1 : vars bloque_modular1\n    | empty\n    \n    bloque_modular2 : estatuto bloque_modular2\n    | empty\n    bloque : LBLOQUE bloque1 RBLOQUE\n    bloque1 : estatuto bloque1\n    | empty\n    \n    estatuto : asignacion\n    | condicion\n    | escritura\n    | return\n    | while\n    | do_while\n    | llamada SEMICOLON\n    asignacion : ID puntoSaveIDAsignacion asignacion1 EQUALS asignacion2 SEMICOLON\n    asignacion1 : LBRACKET expresion RBRACKET\n    | empty\n    \n    asignacion2 : expresion puntoCreateAsignacionQuad\n    | leida\n    puntoSaveIDAsignacion :puntoCreateAsignacionQuad : leida : INPUT LPAREN RPARENcondicion : IF LPAREN expresion RPAREN puntoCreateIfQuad bloque condicion1 puntoFillIfQuad\n    condicion1 : ELSE puntoCreateElseQuad bloque\n    | empty\n    puntoCreateIfQuad : puntoFillIfQuad : puntoCreateElseQuad : escritura : PRINT LPAREN escritura1 RPAREN SEMICOLON\n    escritura1 : expresion puntoCreatePrintQuad\n    | CTE_STRING puntoCreatePrintConstantQuad\n    puntoCreatePrintQuad : puntoCreatePrintConstantQuad : llamada : CALL PUNTO puntoPushFondoFalso ID puntoVerifyLlamada LPAREN llamada1 RPAREN puntoPopFondoFalso puntoCreateGoSubQuad\n    llamada1 : expresion puntoVerifyArgumento llamada2\n    | empty\n    \n    llamada2 : COMMA expresion puntoVerifyArgumento llamada2\n    | empty\n    puntoVerifyLlamada : puntoVerifyArgumento : puntoCreateGoSubQuad : return : RETURN expresion puntoReturnQuad SEMICOLONpuntoReturnQuad : while : WHILE puntoPushSaltoWhile LPAREN expresion RPAREN puntoCreateWhileQuad bloque puntoEndWhileQuadpuntoPushSaltoWhile : puntoCreateWhileQuad : puntoEndWhileQuad : do_while : DO puntoPushSaltoDoWhile bloque WHILE LPAREN expresion RPAREN puntoCreateDoWhileQuadpuntoPushSaltoDoWhile : puntoCreateDoWhileQuad : expresion : compare expresion2\n    expresion2 : AND compare\n    | OR compare\n    | empty\n    compare : exp compare1\n    compare1 : GREATERTHAN puntoPushOperador exp puntoOperacionRelacional\n    | LESSTHAN puntoPushOperador exp puntoOperacionRelacional\n    | GREATERTHANEQUAL puntoPushOperador exp puntoOperacionRelacional\n    | LESSTHANEQUAL puntoPushOperador exp puntoOperacionRelacional\n    | EQUALEQUAL puntoPushOperador exp puntoOperacionRelacional\n    | NOTEQUAL puntoPushOperador exp puntoOperacionRelacional\n    | empty\n    puntoOperacionRelacional : exp : termino puntoSumaResta exp1\n    exp1 : PLUS puntoPushOperador termino puntoSumaResta exp1\n    | MINUS puntoPushOperador termino puntoSumaResta exp1\n    | empty\n    puntoSumaResta : termino : factor puntoMultDivide termino1\n    termino1 : TIMES puntoPushOperador factor puntoMultDivide termino1\n    | DIVIDE puntoPushOperador factor puntoMultDivide termino1\n    | empty\n    puntoMultDivide : puntoPushOperador : \n    factor : LPAREN puntoPushFondoFalso expresion RPAREN puntoPopFondoFalso\n    | tipo_cte\n    | MINUS tipo_cte\n    | NOT tipo_cte\n    puntoPushFondoFalso : puntoPopFondoFalso : funciones_arr : PUNTO funciones_arr1 LPAREN RPAREN\n    funciones_arr1 : MAX\n    | MIN\n    | RANGE\n    | MEDIAN\n    | AVERAGE\n    | IQRANGE\n    | STDEV\n    | VARIANCE\n    | MODIFY\n    | DRAW\n    empty : '
    
_lr_action_items = {'PROGRAM':([0,],[2,]),'$end':([1,42,52,70,100,],[0,-9,-1,-58,-59,]),'ID':([2,11,20,21,22,23,24,25,26,30,31,32,33,34,36,66,68,71,75,76,77,81,83,84,85,86,87,88,93,97,102,104,105,111,113,114,123,127,135,136,139,140,141,142,143,144,148,156,158,159,163,169,172,173,174,175,176,177,179,180,183,184,195,198,205,212,213,214,215,230,231,235,238,254,257,259,265,266,271,277,278,282,285,],[3,17,29,-46,-52,-27,-27,-27,-27,-47,-23,-24,-25,-26,41,73,-10,-151,90,-151,-61,90,-67,-68,-69,-70,-71,-72,119,-60,-73,119,119,-138,119,119,-138,119,119,119,-133,-133,-133,-133,-133,-133,119,119,90,197,119,-101,119,119,119,119,119,119,-133,-133,-133,-133,90,234,-88,119,119,119,119,119,-64,-74,-151,119,-86,-84,-106,-109,-82,-103,-107,-83,119,]),'SEMICOLON':([3,4,23,24,25,26,31,32,33,34,45,46,47,48,49,50,55,57,58,62,74,89,106,107,108,109,110,112,115,116,117,118,119,120,133,134,137,138,145,146,147,149,150,151,152,153,154,155,166,170,171,178,181,182,185,187,189,190,199,200,201,206,207,208,209,210,211,216,236,239,240,241,242,243,244,245,246,247,248,249,250,256,260,261,262,263,264,273,274,275,276,279,283,288,],[-7,5,-27,-27,-27,-27,-23,-24,-25,-26,-151,-21,-14,-42,-43,-44,-22,-16,-13,68,-15,102,-102,-151,-151,-127,-132,-135,-37,-38,-39,-40,-41,-33,169,-110,-113,-114,-121,-151,-151,-136,-137,-28,-29,-30,-31,-151,205,-111,-112,-123,-126,-128,-131,-32,-35,-36,235,-80,-78,-122,-122,-122,-122,-122,-122,-139,-77,-115,-116,-117,-118,-119,-120,-127,-127,-132,-132,-134,-34,-81,-151,-151,-151,-151,-140,-124,-125,-129,-130,-139,-100,-93,]),'VAR':([5,6,7,9,68,71,76,],[-18,-19,11,11,-10,11,11,]),'FUNC':([5,6,7,8,9,10,13,16,68,98,100,124,],[-18,-19,-151,15,-151,-3,15,-2,-10,-57,-59,-45,]),'VOID':([5,6,7,8,9,10,12,13,14,15,16,18,19,28,38,68,98,100,124,],[-18,-19,-151,-151,-151,-3,-8,-151,-5,21,-2,-19,-4,-6,43,-10,-57,-59,-45,]),'INT':([15,40,54,61,161,],[23,23,-54,23,23,]),'FLOAT':([15,40,54,61,161,],[24,24,-54,24,24,]),'BOOL':([15,40,54,61,161,],[25,25,-54,25,25,]),'CHAR':([15,40,54,61,161,],[26,26,-54,26,26,]),'COMMA':([17,27,41,51,73,79,99,107,108,109,110,112,115,116,117,118,119,120,125,134,137,138,145,146,147,149,150,151,152,153,154,155,170,171,178,181,182,185,187,189,190,206,207,208,209,210,211,216,234,239,240,241,242,243,244,245,246,247,248,249,250,255,260,261,262,263,264,268,270,273,274,275,276,279,280,281,283,288,289,290,],[-20,36,-20,36,-20,-21,-55,-151,-151,-127,-132,-135,-37,-38,-39,-40,-41,-33,161,-110,-113,-114,-121,-151,-151,-136,-137,-28,-29,-30,-31,-151,-111,-112,-123,-126,-128,-131,-32,-35,-36,-122,-122,-122,-122,-122,-122,-139,-20,-115,-116,-117,-118,-119,-120,-127,-127,-132,-132,-134,-34,-21,-151,-151,-151,-151,-140,-99,-55,-124,-125,-129,-130,-139,285,161,-100,-93,-99,285,]),'AS':([17,27,35,37,41,51,59,],[-20,-151,40,-12,-20,-151,-11,]),'LBRACKET':([23,24,25,26,31,32,33,34,45,46,47,48,49,50,58,90,103,119,155,],[-27,-27,-27,-27,-23,-24,-25,-26,56,-21,-14,-42,-43,-44,-13,-79,127,-41,188,]),'LPAREN':([29,39,44,53,91,92,93,94,104,105,111,121,127,135,136,139,140,141,142,143,144,148,156,163,172,173,174,175,176,177,179,180,183,184,193,197,202,212,213,214,215,218,219,220,221,222,223,224,225,226,227,228,230,233,254,285,],[-53,-19,54,60,104,105,111,-104,111,111,-138,156,111,111,111,-133,-133,-133,-133,-133,-133,111,111,111,111,111,111,111,111,111,-133,-133,-133,-133,230,-98,237,111,111,111,111,251,-141,-142,-143,-144,-145,-146,-147,-148,-149,-150,111,254,111,111,]),'PIECHART':([40,],[48,]),'BARGRAPH':([40,],[49,]),'PLOTLINE':([40,],[50,]),'MAIN':([43,],[53,]),'RPAREN':([54,60,61,65,67,73,79,99,107,108,109,110,112,115,116,117,118,119,120,125,129,130,131,132,134,137,138,145,146,147,149,150,151,152,153,154,155,160,162,167,168,170,171,178,181,182,185,186,187,189,190,192,206,207,208,209,210,211,216,234,237,239,240,241,242,243,244,245,246,247,248,249,250,251,253,254,255,260,261,262,263,264,267,268,269,270,273,274,275,276,279,280,281,283,284,286,287,288,289,290,291,],[-54,64,-151,72,-49,-20,-21,-55,-151,-151,-127,-132,-135,-37,-38,-39,-40,-41,-33,-151,165,166,-91,-92,-110,-113,-114,-121,-151,-151,-136,-137,-28,-29,-30,-31,-151,-48,-51,-89,-90,-111,-112,-123,-126,-128,-131,216,-32,-35,-36,229,-122,-122,-122,-122,-122,-122,-139,-20,256,-115,-116,-117,-118,-119,-120,-127,-127,-132,-132,-134,-34,264,266,-151,-21,-151,-151,-151,-151,-140,279,-99,-95,-55,-124,-125,-129,-130,-139,-151,-151,-100,-94,-97,-50,-93,-99,-151,-96,]),'CTE_INT':([56,93,104,105,111,113,114,127,135,136,139,140,141,142,143,144,148,156,163,172,173,174,175,176,177,179,180,183,184,188,212,213,214,215,230,254,285,],[63,115,115,115,-138,115,115,115,115,115,-133,-133,-133,-133,-133,-133,115,115,115,115,115,115,115,115,115,-133,-133,-133,-133,217,115,115,115,115,115,115,115,]),'RBRACKET':([63,69,107,108,109,110,112,115,116,117,118,119,120,134,137,138,145,146,147,149,150,151,152,153,154,155,164,170,171,178,181,182,185,187,189,190,206,207,208,209,210,211,216,217,239,240,241,242,243,244,245,246,247,248,249,250,260,261,262,263,264,273,274,275,276,279,283,288,],[-17,74,-151,-151,-127,-132,-135,-37,-38,-39,-40,-41,-33,-110,-113,-114,-121,-151,-151,-136,-137,-28,-29,-30,-31,-151,203,-111,-112,-123,-126,-128,-131,-32,-35,-36,-122,-122,-122,-122,-122,-122,-139,250,-115,-116,-117,-118,-119,-120,-127,-127,-132,-132,-134,-34,-151,-151,-151,-151,-140,-124,-125,-129,-130,-139,-100,-93,]),'LBLOQUE':([64,72,78,95,122,165,204,229,252,258,272,],[71,-56,71,-108,158,-85,158,-105,158,-87,158,]),'IF':([68,71,75,76,77,81,83,84,85,86,87,88,97,102,158,169,195,205,231,235,238,257,259,265,266,271,277,278,282,],[-10,-151,91,-151,-61,91,-67,-68,-69,-70,-71,-72,-60,-73,91,-101,91,-88,-64,-74,-151,-86,-84,-106,-109,-82,-103,-107,-83,]),'PRINT':([68,71,75,76,77,81,83,84,85,86,87,88,97,102,158,169,195,205,231,235,238,257,259,265,266,271,277,278,282,],[-10,-151,92,-151,-61,92,-67,-68,-69,-70,-71,-72,-60,-73,92,-101,92,-88,-64,-74,-151,-86,-84,-106,-109,-82,-103,-107,-83,]),'RETURN':([68,71,75,76,77,81,83,84,85,86,87,88,97,102,158,169,195,205,231,235,238,257,259,265,266,271,277,278,282,],[-10,-151,93,-151,-61,93,-67,-68,-69,-70,-71,-72,-60,-73,93,-101,93,-88,-64,-74,-151,-86,-84,-106,-109,-82,-103,-107,-83,]),'WHILE':([68,71,75,76,77,81,83,84,85,86,87,88,97,102,157,158,169,195,205,231,235,238,257,259,265,266,271,277,278,282,],[-10,-151,94,-151,-61,94,-67,-68,-69,-70,-71,-72,-60,-73,193,94,-101,94,-88,-64,-74,-151,-86,-84,-106,-109,-82,-103,-107,-83,]),'DO':([68,71,75,76,77,81,83,84,85,86,87,88,97,102,158,169,195,205,231,235,238,257,259,265,266,271,277,278,282,],[-10,-151,95,-151,-61,95,-67,-68,-69,-70,-71,-72,-60,-73,95,-101,95,-88,-64,-74,-151,-86,-84,-106,-109,-82,-103,-107,-83,]),'CALL':([68,71,75,76,77,81,83,84,85,86,87,88,93,97,102,104,105,111,113,114,127,135,136,139,140,141,142,143,144,148,156,158,163,169,172,173,174,175,176,177,179,180,183,184,195,205,212,213,214,215,230,231,235,238,254,257,259,265,266,271,277,278,282,285,],[-10,-151,96,-151,-61,96,-67,-68,-69,-70,-71,-72,96,-60,-73,96,96,-138,96,96,96,96,96,-133,-133,-133,-133,-133,-133,96,96,96,96,-101,96,96,96,96,96,96,-133,-133,-133,-133,96,-88,96,96,96,96,96,-64,-74,-151,96,-86,-84,-106,-109,-82,-103,-107,-83,96,]),'RBLOQUE':([68,71,75,76,77,80,81,82,83,84,85,86,87,88,97,101,102,158,169,194,195,196,205,231,232,235,238,257,259,265,266,271,277,278,282,],[-10,-151,-151,-151,-61,100,-151,-63,-67,-68,-69,-70,-71,-72,-60,-62,-73,-151,-101,231,-151,-66,-88,-64,-65,-74,-151,-86,-84,-106,-109,-82,-103,-107,-83,]),'EQUALS':([90,103,126,128,203,],[-79,-151,163,-76,-75,]),'MINUS':([93,104,105,109,110,111,112,115,116,117,118,119,120,127,135,136,139,140,141,142,143,144,146,147,148,149,150,151,152,153,154,155,156,163,172,173,174,175,176,177,179,180,182,183,184,185,187,189,190,212,213,214,215,216,230,245,246,247,248,249,250,254,260,261,262,263,264,275,276,279,283,285,288,],[113,113,113,-127,-132,-138,-135,-37,-38,-39,-40,-41,-33,113,113,113,-133,-133,-133,-133,-133,-133,180,-151,113,-136,-137,-28,-29,-30,-31,-151,113,113,113,113,113,113,113,113,-133,-133,-128,-133,-133,-131,-32,-35,-36,113,113,113,113,-139,113,-127,-127,-132,-132,-134,-34,113,180,180,-151,-151,-140,-129,-130,-139,-100,113,-93,]),'NOT':([93,104,105,111,127,135,136,139,140,141,142,143,144,148,156,163,172,173,174,175,176,177,179,180,183,184,212,213,214,215,230,254,285,],[114,114,114,-138,114,114,114,-133,-133,-133,-133,-133,-133,114,114,114,114,114,114,114,114,114,-133,-133,-133,-133,114,114,114,114,114,114,114,]),'CTE_FLOAT':([93,104,105,111,113,114,127,135,136,139,140,141,142,143,144,148,156,163,172,173,174,175,176,177,179,180,183,184,212,213,214,215,230,254,285,],[116,116,116,-138,116,116,116,116,116,-133,-133,-133,-133,-133,-133,116,116,116,116,116,116,116,116,116,-133,-133,-133,-133,116,116,116,116,116,116,116,]),'CTE_BOOL':([93,104,105,111,113,114,127,135,136,139,140,141,142,143,144,148,156,163,172,173,174,175,176,177,179,180,183,184,212,213,214,215,230,254,285,],[117,117,117,-138,117,117,117,117,117,-133,-133,-133,-133,-133,-133,117,117,117,117,117,117,117,117,117,-133,-133,-133,-133,117,117,117,117,117,117,117,]),'CTE_CHAR':([93,104,105,111,113,114,127,135,136,139,140,141,142,143,144,148,156,163,172,173,174,175,176,177,179,180,183,184,212,213,214,215,230,254,285,],[118,118,118,-138,118,118,118,118,118,-133,-133,-133,-133,-133,-133,118,118,118,118,118,118,118,118,118,-133,-133,-133,-133,118,118,118,118,118,118,118,]),'PUNTO':([96,119,155,],[123,-41,191,]),'CTE_STRING':([105,],[132,]),'AND':([107,108,109,110,112,115,116,117,118,119,120,138,145,146,147,149,150,151,152,153,154,155,178,181,182,185,187,189,190,206,207,208,209,210,211,216,239,240,241,242,243,244,245,246,247,248,249,250,260,261,262,263,264,273,274,275,276,279,283,288,],[135,-151,-127,-132,-135,-37,-38,-39,-40,-41,-33,-114,-121,-151,-151,-136,-137,-28,-29,-30,-31,-151,-123,-126,-128,-131,-32,-35,-36,-122,-122,-122,-122,-122,-122,-139,-115,-116,-117,-118,-119,-120,-127,-127,-132,-132,-134,-34,-151,-151,-151,-151,-140,-124,-125,-129,-130,-139,-100,-93,]),'OR':([107,108,109,110,112,115,116,117,118,119,120,138,145,146,147,149,150,151,152,153,154,155,178,181,182,185,187,189,190,206,207,208,209,210,211,216,239,240,241,242,243,244,245,246,247,248,249,250,260,261,262,263,264,273,274,275,276,279,283,288,],[136,-151,-127,-132,-135,-37,-38,-39,-40,-41,-33,-114,-121,-151,-151,-136,-137,-28,-29,-30,-31,-151,-123,-126,-128,-131,-32,-35,-36,-122,-122,-122,-122,-122,-122,-139,-115,-116,-117,-118,-119,-120,-127,-127,-132,-132,-134,-34,-151,-151,-151,-151,-140,-124,-125,-129,-130,-139,-100,-93,]),'GREATERTHAN':([108,109,110,112,115,116,117,118,119,120,146,147,149,150,151,152,153,154,155,178,181,182,185,187,189,190,216,245,246,247,248,249,250,260,261,262,263,264,273,274,275,276,279,283,288,],[139,-127,-132,-135,-37,-38,-39,-40,-41,-33,-151,-151,-136,-137,-28,-29,-30,-31,-151,-123,-126,-128,-131,-32,-35,-36,-139,-127,-127,-132,-132,-134,-34,-151,-151,-151,-151,-140,-124,-125,-129,-130,-139,-100,-93,]),'LESSTHAN':([108,109,110,112,115,116,117,118,119,120,146,147,149,150,151,152,153,154,155,178,181,182,185,187,189,190,216,245,246,247,248,249,250,260,261,262,263,264,273,274,275,276,279,283,288,],[140,-127,-132,-135,-37,-38,-39,-40,-41,-33,-151,-151,-136,-137,-28,-29,-30,-31,-151,-123,-126,-128,-131,-32,-35,-36,-139,-127,-127,-132,-132,-134,-34,-151,-151,-151,-151,-140,-124,-125,-129,-130,-139,-100,-93,]),'GREATERTHANEQUAL':([108,109,110,112,115,116,117,118,119,120,146,147,149,150,151,152,153,154,155,178,181,182,185,187,189,190,216,245,246,247,248,249,250,260,261,262,263,264,273,274,275,276,279,283,288,],[141,-127,-132,-135,-37,-38,-39,-40,-41,-33,-151,-151,-136,-137,-28,-29,-30,-31,-151,-123,-126,-128,-131,-32,-35,-36,-139,-127,-127,-132,-132,-134,-34,-151,-151,-151,-151,-140,-124,-125,-129,-130,-139,-100,-93,]),'LESSTHANEQUAL':([108,109,110,112,115,116,117,118,119,120,146,147,149,150,151,152,153,154,155,178,181,182,185,187,189,190,216,245,246,247,248,249,250,260,261,262,263,264,273,274,275,276,279,283,288,],[142,-127,-132,-135,-37,-38,-39,-40,-41,-33,-151,-151,-136,-137,-28,-29,-30,-31,-151,-123,-126,-128,-131,-32,-35,-36,-139,-127,-127,-132,-132,-134,-34,-151,-151,-151,-151,-140,-124,-125,-129,-130,-139,-100,-93,]),'EQUALEQUAL':([108,109,110,112,115,116,117,118,119,120,146,147,149,150,151,152,153,154,155,178,181,182,185,187,189,190,216,245,246,247,248,249,250,260,261,262,263,264,273,274,275,276,279,283,288,],[143,-127,-132,-135,-37,-38,-39,-40,-41,-33,-151,-151,-136,-137,-28,-29,-30,-31,-151,-123,-126,-128,-131,-32,-35,-36,-139,-127,-127,-132,-132,-134,-34,-151,-151,-151,-151,-140,-124,-125,-129,-130,-139,-100,-93,]),'NOTEQUAL':([108,109,110,112,115,116,117,118,119,120,146,147,149,150,151,152,153,154,155,178,181,182,185,187,189,190,216,245,246,247,248,249,250,260,261,262,263,264,273,274,275,276,279,283,288,],[144,-127,-132,-135,-37,-38,-39,-40,-41,-33,-151,-151,-136,-137,-28,-29,-30,-31,-151,-123,-126,-128,-131,-32,-35,-36,-139,-127,-127,-132,-132,-134,-34,-151,-151,-151,-151,-140,-124,-125,-129,-130,-139,-100,-93,]),'PLUS':([109,110,112,115,116,117,118,119,120,146,147,149,150,151,152,153,154,155,182,185,187,189,190,216,245,246,247,248,249,250,260,261,262,263,264,275,276,279,283,288,],[-127,-132,-135,-37,-38,-39,-40,-41,-33,179,-151,-136,-137,-28,-29,-30,-31,-151,-128,-131,-32,-35,-36,-139,-127,-127,-132,-132,-134,-34,179,179,-151,-151,-140,-129,-130,-139,-100,-93,]),'TIMES':([110,112,115,116,117,118,119,120,147,149,150,151,152,153,154,155,187,189,190,216,247,248,249,250,262,263,264,279,283,288,],[-132,-135,-37,-38,-39,-40,-41,-33,183,-136,-137,-28,-29,-30,-31,-151,-32,-35,-36,-139,-132,-132,-134,-34,183,183,-140,-139,-100,-93,]),'DIVIDE':([110,112,115,116,117,118,119,120,147,149,150,151,152,153,154,155,187,189,190,216,247,248,249,250,262,263,264,279,283,288,],[-132,-135,-37,-38,-39,-40,-41,-33,184,-136,-137,-28,-29,-30,-31,-151,-32,-35,-36,-139,-132,-132,-134,-34,184,184,-140,-139,-100,-93,]),'INPUT':([163,],[202,]),'MAX':([191,],[219,]),'MIN':([191,],[220,]),'RANGE':([191,],[221,]),'MEDIAN':([191,],[222,]),'AVERAGE':([191,],[223,]),'IQRANGE':([191,],[224,]),'STDEV':([191,],[225,]),'VARIANCE':([191,],[226,]),'MODIFY':([191,],[227,]),'DRAW':([191,],[228,]),'ELSE':([231,238,],[-64,258,]),}

_lr_action = {}
for _k, _v in _lr_action_items.items():
   for _x,_y in zip(_v[0],_v[1]):
      if not _x in _lr_action:  _lr_action[_x] = {}
      _lr_action[_x][_k] = _y
del _lr_action_items

_lr_goto_items = {'programa':([0,],[1,]),'puntoCreateProgram':([3,],[4,]),'puntoCreateVarTable':([5,],[6,]),'puntoCreateVarTableState':([6,18,39,],[7,28,44,]),'programa1':([7,9,],[8,16,]),'vars':([7,9,71,76,],[9,9,76,76,]),'empty':([7,8,9,13,27,45,51,61,71,75,76,81,103,107,108,125,146,147,155,158,195,238,254,260,261,262,263,280,281,290,],[10,14,10,14,37,57,37,67,77,82,77,82,128,137,145,162,181,185,190,196,196,259,269,181,181,185,185,286,162,286,]),'programa2':([8,13,],[12,19,]),'funciones':([8,13,],[13,13,]),'puntoChangeStateLocal':([12,],[18,]),'funciones1':([15,],[20,]),'tipo':([15,40,61,161,],[22,46,66,198,]),'puntoCreateVar':([17,41,73,234,],[27,51,79,255,]),'puntoReturnType':([22,],[30,]),'puntoCurrentType':([23,24,25,26,],[31,32,33,34,]),'vars1':([27,51,],[35,59,]),'puntoFillMainQuad':([28,],[38,]),'puntoChangeStateFuncion':([29,],[39,]),'main':([38,],[42,]),'vars2':([40,],[45,]),'tipo_graph':([40,],[47,]),'puntoPrintFinal':([42,],[52,]),'vars3':([45,],[55,]),'puntoCreateVarType':([46,79,255,],[58,99,270,]),'puntoCreateParamTable':([54,],[61,]),'puntoCreateDimension':([55,],[62,]),'funciones2':([61,],[65,]),'puntoChangeDimension':([63,],[69,]),'bloque_modular':([64,78,],[70,98,]),'bloque_modular1':([71,76,],[75,97,]),'puntoCreateParamCount':([72,],[78,]),'bloque_modular2':([75,81,],[80,101,]),'estatuto':([75,81,158,195,],[81,81,195,195,]),'asignacion':([75,81,158,195,],[83,83,83,83,]),'condicion':([75,81,158,195,],[84,84,84,84,]),'escritura':([75,81,158,195,],[85,85,85,85,]),'return':([75,81,158,195,],[86,86,86,86,]),'while':([75,81,158,195,],[87,87,87,87,]),'do_while':([75,81,158,195,],[88,88,88,88,]),'llamada':([75,81,93,104,105,113,114,127,135,136,148,156,158,163,172,173,174,175,176,177,195,212,213,214,215,230,254,285,],[89,89,120,120,120,120,120,120,120,120,120,120,89,120,120,120,120,120,120,120,89,120,120,120,120,120,120,120,]),'puntoSaveIDAsignacion':([90,],[103,]),'expresion':([93,104,105,127,148,156,163,230,254,285,],[106,129,131,164,186,192,200,253,268,289,]),'compare':([93,104,105,127,135,136,148,156,163,230,254,285,],[107,107,107,107,170,171,107,107,107,107,107,107,]),'exp':([93,104,105,127,135,136,148,156,163,172,173,174,175,176,177,230,254,285,],[108,108,108,108,108,108,108,108,108,206,207,208,209,210,211,108,108,108,]),'termino':([93,104,105,127,135,136,148,156,163,172,173,174,175,176,177,212,213,230,254,285,],[109,109,109,109,109,109,109,109,109,109,109,109,109,109,109,245,246,109,109,109,]),'factor':([93,104,105,127,135,136,148,156,163,172,173,174,175,176,177,212,213,214,215,230,254,285,],[110,110,110,110,110,110,110,110,110,110,110,110,110,110,110,110,110,247,248,110,110,110,]),'tipo_cte':([93,104,105,113,114,127,135,136,148,156,163,172,173,174,175,176,177,212,213,214,215,230,254,285,],[112,112,112,149,150,112,112,112,112,112,112,112,112,112,112,112,112,112,112,112,112,112,112,112,]),'puntoPushSaltoWhile':([94,],[121,]),'puntoPushSaltoDoWhile':([95,],[122,]),'puntoFinalFuncQuad':([98,],[124,]),'puntoPushParam':([99,270,],[125,281,]),'asignacion1':([103,],[126,]),'escritura1':([105,],[130,]),'puntoReturnQuad':([106,],[133,]),'expresion2':([107,],[134,]),'compare1':([108,],[138,]),'puntoSumaResta':([109,245,246,],[146,260,261,]),'puntoMultDivide':([110,247,248,],[147,262,263,]),'puntoPushFondoFalso':([111,123,],[148,159,]),'puntoPushInt':([115,],[151,]),'puntoPushFloat':([116,],[152,]),'puntoPushBool':([117,],[153,]),'puntoPushChar':([118,],[154,]),'puntoPushID':([119,],[155,]),'bloque':([122,204,252,272,],[157,238,265,282,]),'funciones3':([125,281,],[160,287,]),'puntoCreatePrintQuad':([131,],[167,]),'puntoCreatePrintConstantQuad':([132,],[168,]),'puntoPushOperador':([139,140,141,142,143,144,179,180,183,184,],[172,173,174,175,176,177,212,213,214,215,]),'exp1':([146,260,261,],[178,273,274,]),'termino1':([147,262,263,],[182,275,276,]),'tipo_cte1':([155,],[187,]),'funciones_arr':([155,],[189,]),'bloque1':([158,195,],[194,232,]),'asignacion2':([163,],[199,]),'leida':([163,],[201,]),'puntoCreateIfQuad':([165,],[204,]),'funciones_arr1':([191,],[218,]),'puntoVerifyLlamada':([197,],[233,]),'puntoCreateAsignacionQuad':([200,],[236,]),'puntoOperacionRelacional':([206,207,208,209,210,211,],[239,240,241,242,243,244,]),'puntoPopFondoFalso':([216,279,],[249,283,]),'puntoCreateWhileQuad':([229,],[252,]),'condicion1':([238,],[257,]),'llamada1':([254,],[267,]),'puntoFillIfQuad':([257,],[271,]),'puntoCreateElseQuad':([258,],[272,]),'puntoEndWhileQuad':([265,],[277,]),'puntoCreateDoWhileQuad':([266,],[278,]),'puntoVerifyArgumento':([268,289,],[280,290,]),'llamada2':([280,290,],[284,291,]),'puntoCreateGoSubQuad':([283,],[288,]),}

_lr_goto = {}
for _k, _v in _lr_goto_items.items():
   for _x, _y in zip(_v[0], _v[1]):
       if not _x in _lr_goto: _lr_goto[_x] = {}
       _lr_goto[_x][_k] = _y
del _lr_goto_items
_lr_productions = [
  ("S' -> programa","S'",1,None,None,None),
  ('programa -> PROGRAM ID puntoCreateProgram SEMICOLON puntoCreateVarTable puntoCreateVarTableState programa1 programa2 puntoChangeStateLocal puntoCreateVarTableState puntoFillMainQuad main puntoPrintFinal','programa',13,'p_programa','yacc.py',39),
  ('programa1 -> vars programa1','programa1',2,'p_programa1','yacc.py',42),
  ('programa1 -> empty','programa1',1,'p_programa1','yacc.py',43),
  ('programa2 -> funciones programa2','programa2',2,'p_programa2','yacc.py',47),
  ('programa2 -> empty','programa2',1,'p_programa2','yacc.py',48),
  ('puntoFillMainQuad -> <empty>','puntoFillMainQuad',0,'p_puntoFillMainQuad','yacc.py',51),
  ('puntoCreateProgram -> <empty>','puntoCreateProgram',0,'p_puntoCreateProgram','yacc.py',56),
  ('puntoChangeStateLocal -> <empty>','puntoChangeStateLocal',0,'p_puntoChangeStateLocal','yacc.py',64),
  ('puntoPrintFinal -> <empty>','puntoPrintFinal',0,'p_puntoPrintFinal','yacc.py',69),
  ('vars -> VAR ID puntoCreateVar vars1 AS vars2 vars3 puntoCreateDimension SEMICOLON','vars',9,'p_vars','yacc.py',74),
  ('vars1 -> COMMA ID puntoCreateVar vars1','vars1',4,'p_vars1','yacc.py',77),
  ('vars1 -> empty','vars1',1,'p_vars1','yacc.py',78),
  ('vars2 -> tipo puntoCreateVarType','vars2',2,'p_vars2','yacc.py',82),
  ('vars2 -> tipo_graph','vars2',1,'p_vars2','yacc.py',83),
  ('vars3 -> LBRACKET CTE_INT puntoChangeDimension RBRACKET','vars3',4,'p_vars3','yacc.py',87),
  ('vars3 -> empty','vars3',1,'p_vars3','yacc.py',88),
  ('puntoChangeDimension -> <empty>','puntoChangeDimension',0,'p_puntoChangeDimension','yacc.py',92),
  ('puntoCreateVarTable -> <empty>','puntoCreateVarTable',0,'p_puntoCreateVarTable','yacc.py',98),
  ('puntoCreateVarTableState -> <empty>','puntoCreateVarTableState',0,'p_puntoCreateVarTableState','yacc.py',103),
  ('puntoCreateVar -> <empty>','puntoCreateVar',0,'p_puntoCreateVar','yacc.py',109),
  ('puntoCreateVarType -> <empty>','puntoCreateVarType',0,'p_puntoCreateVarType','yacc.py',118),
  ('puntoCreateDimension -> <empty>','puntoCreateDimension',0,'p_puntoCreateDimension','yacc.py',130),
  ('tipo -> INT puntoCurrentType','tipo',2,'p_tipo','yacc.py',139),
  ('tipo -> FLOAT puntoCurrentType','tipo',2,'p_tipo','yacc.py',140),
  ('tipo -> BOOL puntoCurrentType','tipo',2,'p_tipo','yacc.py',141),
  ('tipo -> CHAR puntoCurrentType','tipo',2,'p_tipo','yacc.py',142),
  ('puntoCurrentType -> <empty>','puntoCurrentType',0,'p_puntoCurrentType','yacc.py',145),
  ('tipo_cte -> CTE_INT puntoPushInt','tipo_cte',2,'p_tipo_cte','yacc.py',151),
  ('tipo_cte -> CTE_FLOAT puntoPushFloat','tipo_cte',2,'p_tipo_cte','yacc.py',152),
  ('tipo_cte -> CTE_BOOL puntoPushBool','tipo_cte',2,'p_tipo_cte','yacc.py',153),
  ('tipo_cte -> CTE_CHAR puntoPushChar','tipo_cte',2,'p_tipo_cte','yacc.py',154),
  ('tipo_cte -> ID puntoPushID tipo_cte1','tipo_cte',3,'p_tipo_cte','yacc.py',155),
  ('tipo_cte -> llamada','tipo_cte',1,'p_tipo_cte','yacc.py',156),
  ('tipo_cte1 -> LBRACKET CTE_INT RBRACKET','tipo_cte1',3,'p_tipo_cte1','yacc.py',160),
  ('tipo_cte1 -> funciones_arr','tipo_cte1',1,'p_tipo_cte1','yacc.py',161),
  ('tipo_cte1 -> empty','tipo_cte1',1,'p_tipo_cte1','yacc.py',162),
  ('puntoPushInt -> <empty>','puntoPushInt',0,'p_puntoPushInt','yacc.py',165),
  ('puntoPushFloat -> <empty>','puntoPushFloat',0,'p_puntoPushFloat','yacc.py',177),
  ('puntoPushBool -> <empty>','puntoPushBool',0,'p_puntoPushBool','yacc.py',189),
  ('puntoPushChar -> <empty>','puntoPushChar',0,'p_puntoPushChar','yacc.py',201),
  ('puntoPushID -> <empty>','puntoPushID',0,'p_puntoPushID','yacc.py',213),
  ('tipo_graph -> PIECHART','tipo_graph',1,'p_tipo_graph','yacc.py',231),
  ('tipo_graph -> BARGRAPH','tipo_graph',1,'p_tipo_graph','yacc.py',232),
  ('tipo_graph -> PLOTLINE','tipo_graph',1,'p_tipo_graph','yacc.py',233),
  ('funciones -> FUNC funciones1 ID puntoChangeStateFuncion puntoCreateVarTableState LPAREN puntoCreateParamTable funciones2 RPAREN puntoCreateParamCount bloque_modular puntoFinalFuncQuad','funciones',12,'p_funciones','yacc.py',245),
  ('funciones1 -> VOID','funciones1',1,'p_funciones1','yacc.py',248),
  ('funciones1 -> tipo puntoReturnType','funciones1',2,'p_funciones1','yacc.py',249),
  ('funciones2 -> tipo ID puntoCreateVar puntoCreateVarType puntoPushParam funciones3','funciones2',6,'p_funciones2','yacc.py',253),
  ('funciones2 -> empty','funciones2',1,'p_funciones2','yacc.py',254),
  ('funciones3 -> COMMA tipo ID puntoCreateVar puntoCreateVarType puntoPushParam funciones3','funciones3',7,'p_funciones3','yacc.py',258),
  ('funciones3 -> empty','funciones3',1,'p_funciones3','yacc.py',259),
  ('puntoReturnType -> <empty>','puntoReturnType',0,'p_puntoReturnType','yacc.py',262),
  ('puntoChangeStateFuncion -> <empty>','puntoChangeStateFuncion',0,'p_puntoChangeStateFuncion','yacc.py',266),
  ('puntoCreateParamTable -> <empty>','puntoCreateParamTable',0,'p_puntoCreateParamTable','yacc.py',272),
  ('puntoPushParam -> <empty>','puntoPushParam',0,'p_puntoPushParam','yacc.py',286),
  ('puntoCreateParamCount -> <empty>','puntoCreateParamCount',0,'p_puntoCreateParamCount','yacc.py',289),
  ('puntoFinalFuncQuad -> <empty>','puntoFinalFuncQuad',0,'p_puntoFinalFuncQuad','yacc.py',303),
  ('main -> VOID MAIN LPAREN RPAREN bloque_modular','main',5,'p_main','yacc.py',308),
  ('bloque_modular -> LBLOQUE bloque_modular1 bloque_modular2 RBLOQUE','bloque_modular',4,'p_bloque_modular','yacc.py',311),
  ('bloque_modular1 -> vars bloque_modular1','bloque_modular1',2,'p_bloque_modular1','yacc.py',314),
  ('bloque_modular1 -> empty','bloque_modular1',1,'p_bloque_modular1','yacc.py',315),
  ('bloque_modular2 -> estatuto bloque_modular2','bloque_modular2',2,'p_bloque_modular2','yacc.py',319),
  ('bloque_modular2 -> empty','bloque_modular2',1,'p_bloque_modular2','yacc.py',320),
  ('bloque -> LBLOQUE bloque1 RBLOQUE','bloque',3,'p_bloque','yacc.py',324),
  ('bloque1 -> estatuto bloque1','bloque1',2,'p_bloque1','yacc.py',327),
  ('bloque1 -> empty','bloque1',1,'p_bloque1','yacc.py',328),
  ('estatuto -> asignacion','estatuto',1,'p_estatuto','yacc.py',333),
  ('estatuto -> condicion','estatuto',1,'p_estatuto','yacc.py',334),
  ('estatuto -> escritura','estatuto',1,'p_estatuto','yacc.py',335),
  ('estatuto -> return','estatuto',1,'p_estatuto','yacc.py',336),
  ('estatuto -> while','estatuto',1,'p_estatuto','yacc.py',337),
  ('estatuto -> do_while','estatuto',1,'p_estatuto','yacc.py',338),
  ('estatuto -> llamada SEMICOLON','estatuto',2,'p_estatuto','yacc.py',339),
  ('asignacion -> ID puntoSaveIDAsignacion asignacion1 EQUALS asignacion2 SEMICOLON','asignacion',6,'p_asignacion','yacc.py',343),
  ('asignacion1 -> LBRACKET expresion RBRACKET','asignacion1',3,'p_asignacion1','yacc.py',346),
  ('asignacion1 -> empty','asignacion1',1,'p_asignacion1','yacc.py',347),
  ('asignacion2 -> expresion puntoCreateAsignacionQuad','asignacion2',2,'p_asignacion2','yacc.py',351),
  ('asignacion2 -> leida','asignacion2',1,'p_asignacion2','yacc.py',352),
  ('puntoSaveIDAsignacion -> <empty>','puntoSaveIDAsignacion',0,'p_puntoSaveIDAsignacion','yacc.py',355),
  ('puntoCreateAsignacionQuad -> <empty>','puntoCreateAsignacionQuad',0,'p_puntoCreateAsignacionQuad','yacc.py',369),
  ('leida -> INPUT LPAREN RPAREN','leida',3,'p_leida','yacc.py',376),
  ('condicion -> IF LPAREN expresion RPAREN puntoCreateIfQuad bloque condicion1 puntoFillIfQuad','condicion',8,'p_condicion','yacc.py',379),
  ('condicion1 -> ELSE puntoCreateElseQuad bloque','condicion1',3,'p_condicion1','yacc.py',382),
  ('condicion1 -> empty','condicion1',1,'p_condicion1','yacc.py',383),
  ('puntoCreateIfQuad -> <empty>','puntoCreateIfQuad',0,'p_puntoCreateIfQuad','yacc.py',386),
  ('puntoFillIfQuad -> <empty>','puntoFillIfQuad',0,'p_puntoFillIfQuad','yacc.py',396),
  ('puntoCreateElseQuad -> <empty>','puntoCreateElseQuad',0,'p_puntoCreateElseQuad','yacc.py',400),
  ('escritura -> PRINT LPAREN escritura1 RPAREN SEMICOLON','escritura',5,'p_escritura','yacc.py',413),
  ('escritura1 -> expresion puntoCreatePrintQuad','escritura1',2,'p_escritura1','yacc.py',416),
  ('escritura1 -> CTE_STRING puntoCreatePrintConstantQuad','escritura1',2,'p_escritura1','yacc.py',417),
  ('puntoCreatePrintQuad -> <empty>','puntoCreatePrintQuad',0,'p_puntoCreatePrintQuad','yacc.py',420),
  ('puntoCreatePrintConstantQuad -> <empty>','puntoCreatePrintConstantQuad',0,'p_puntoCreatePrintConstantQuad','yacc.py',426),
  ('llamada -> CALL PUNTO puntoPushFondoFalso ID puntoVerifyLlamada LPAREN llamada1 RPAREN puntoPopFondoFalso puntoCreateGoSubQuad','llamada',10,'p_llamada','yacc.py',432),
  ('llamada1 -> expresion puntoVerifyArgumento llamada2','llamada1',3,'p_llamada1','yacc.py',435),
  ('llamada1 -> empty','llamada1',1,'p_llamada1','yacc.py',436),
  ('llamada2 -> COMMA expresion puntoVerifyArgumento llamada2','llamada2',4,'p_llamada2','yacc.py',440),
  ('llamada2 -> empty','llamada2',1,'p_llamada2','yacc.py',441),
  ('puntoVerifyLlamada -> <empty>','puntoVerifyLlamada',0,'p_puntoVerifyLlamada','yacc.py',444),
  ('puntoVerifyArgumento -> <empty>','puntoVerifyArgumento',0,'p_puntoVerifyArgumento','yacc.py',460),
  ('puntoCreateGoSubQuad -> <empty>','puntoCreateGoSubQuad',0,'p_puntoCreateGoSubQuad','yacc.py',473),
  ('return -> RETURN expresion puntoReturnQuad SEMICOLON','return',4,'p_return','yacc.py',487),
  ('puntoReturnQuad -> <empty>','puntoReturnQuad',0,'p_puntoReturnQuad','yacc.py',489),
  ('while -> WHILE puntoPushSaltoWhile LPAREN expresion RPAREN puntoCreateWhileQuad bloque puntoEndWhileQuad','while',8,'p_while','yacc.py',496),
  ('puntoPushSaltoWhile -> <empty>','puntoPushSaltoWhile',0,'p_puntoPushSaltoWhile','yacc.py',498),
  ('puntoCreateWhileQuad -> <empty>','puntoCreateWhileQuad',0,'p_puntoCreateWhileQuad','yacc.py',501),
  ('puntoEndWhileQuad -> <empty>','puntoEndWhileQuad',0,'p_puntoEndWhileQuad','yacc.py',511),
  ('do_while -> DO puntoPushSaltoDoWhile bloque WHILE LPAREN expresion RPAREN puntoCreateDoWhileQuad','do_while',8,'p_do_while','yacc.py',519),
  ('puntoPushSaltoDoWhile -> <empty>','puntoPushSaltoDoWhile',0,'p_puntoPushSaltoDoWhile','yacc.py',521),
  ('puntoCreateDoWhileQuad -> <empty>','puntoCreateDoWhileQuad',0,'p_puntoCreateDoWhileQuad','yacc.py',524),
  ('expresion -> compare expresion2','expresion',2,'p_expresion','yacc.py',535),
  ('expresion2 -> AND compare','expresion2',2,'p_expresion2','yacc.py',538),
  ('expresion2 -> OR compare','expresion2',2,'p_expresion2','yacc.py',539),
  ('expresion2 -> empty','expresion2',1,'p_expresion2','yacc.py',540),
  ('compare -> exp compare1','compare',2,'p_compare','yacc.py',544),
  ('compare1 -> GREATERTHAN puntoPushOperador exp puntoOperacionRelacional','compare1',4,'p_compare1','yacc.py',547),
  ('compare1 -> LESSTHAN puntoPushOperador exp puntoOperacionRelacional','compare1',4,'p_compare1','yacc.py',548),
  ('compare1 -> GREATERTHANEQUAL puntoPushOperador exp puntoOperacionRelacional','compare1',4,'p_compare1','yacc.py',549),
  ('compare1 -> LESSTHANEQUAL puntoPushOperador exp puntoOperacionRelacional','compare1',4,'p_compare1','yacc.py',550),
  ('compare1 -> EQUALEQUAL puntoPushOperador exp puntoOperacionRelacional','compare1',4,'p_compare1','yacc.py',551),
  ('compare1 -> NOTEQUAL puntoPushOperador exp puntoOperacionRelacional','compare1',4,'p_compare1','yacc.py',552),
  ('compare1 -> empty','compare1',1,'p_compare1','yacc.py',553),
  ('puntoOperacionRelacional -> <empty>','puntoOperacionRelacional',0,'p_puntoOperacionRelacional','yacc.py',556),
  ('exp -> termino puntoSumaResta exp1','exp',3,'p_exp','yacc.py',573),
  ('exp1 -> PLUS puntoPushOperador termino puntoSumaResta exp1','exp1',5,'p_exp1','yacc.py',576),
  ('exp1 -> MINUS puntoPushOperador termino puntoSumaResta exp1','exp1',5,'p_exp1','yacc.py',577),
  ('exp1 -> empty','exp1',1,'p_exp1','yacc.py',578),
  ('puntoSumaResta -> <empty>','puntoSumaResta',0,'p_puntoSumaResta','yacc.py',582),
  ('termino -> factor puntoMultDivide termino1','termino',3,'p_termino','yacc.py',617),
  ('termino1 -> TIMES puntoPushOperador factor puntoMultDivide termino1','termino1',5,'p_termino1','yacc.py',620),
  ('termino1 -> DIVIDE puntoPushOperador factor puntoMultDivide termino1','termino1',5,'p_termino1','yacc.py',621),
  ('termino1 -> empty','termino1',1,'p_termino1','yacc.py',622),
  ('puntoMultDivide -> <empty>','puntoMultDivide',0,'p_puntoMultDivide','yacc.py',626),
  ('puntoPushOperador -> <empty>','puntoPushOperador',0,'p_puntoPushOperador','yacc.py',635),
  ('factor -> LPAREN puntoPushFondoFalso expresion RPAREN puntoPopFondoFalso','factor',5,'p_factor','yacc.py',641),
  ('factor -> tipo_cte','factor',1,'p_factor','yacc.py',642),
  ('factor -> MINUS tipo_cte','factor',2,'p_factor','yacc.py',643),
  ('factor -> NOT tipo_cte','factor',2,'p_factor','yacc.py',644),
  ('puntoPushFondoFalso -> <empty>','puntoPushFondoFalso',0,'p_puntoPushFondoFalso','yacc.py',647),
  ('puntoPopFondoFalso -> <empty>','puntoPopFondoFalso',0,'p_puntoPopFondoFalso','yacc.py',651),
  ('funciones_arr -> PUNTO funciones_arr1 LPAREN RPAREN','funciones_arr',4,'p_funciones_arr','yacc.py',655),
  ('funciones_arr1 -> MAX','funciones_arr1',1,'p_funciones_arr1','yacc.py',658),
  ('funciones_arr1 -> MIN','funciones_arr1',1,'p_funciones_arr1','yacc.py',659),
  ('funciones_arr1 -> RANGE','funciones_arr1',1,'p_funciones_arr1','yacc.py',660),
  ('funciones_arr1 -> MEDIAN','funciones_arr1',1,'p_funciones_arr1','yacc.py',661),
  ('funciones_arr1 -> AVERAGE','funciones_arr1',1,'p_funciones_arr1','yacc.py',662),
  ('funciones_arr1 -> IQRANGE','funciones_arr1',1,'p_funciones_arr1','yacc.py',663),
  ('funciones_arr1 -> STDEV','funciones_arr1',1,'p_funciones_arr1','yacc.py',664),
  ('funciones_arr1 -> VARIANCE','funciones_arr1',1,'p_funciones_arr1','yacc.py',665),
  ('funciones_arr1 -> MODIFY','funciones_arr1',1,'p_funciones_arr1','yacc.py',666),
  ('funciones_arr1 -> DRAW','funciones_arr1',1,'p_funciones_arr1','yacc.py',667),
  ('empty -> <empty>','empty',0,'p_empty','yacc.py',671),
]
