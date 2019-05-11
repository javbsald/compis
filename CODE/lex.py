import ply.lex as lex
import sys

# Reserved Words
reserved = {
    'program' : 'PROGRAM',
    'var' : 'VAR',
    'as' : 'AS',
    'int' : 'INT',
    'float' : 'FLOAT',
    'bool' : 'BOOL',
    'char' : 'CHAR',
    'pieChart' : 'PIECHART',
    'barGraph' : 'BARGRAPH',
    'plotLine' : 'PLOTLINE',
    'func' : 'FUNC',
    'void' : 'VOID',
    'main' : 'MAIN',
    'if' : 'IF',
    'else' : 'ELSE',
    'do' : 'DO',
    'while' : 'WHILE',
    'print' : 'PRINT',
    'input' : 'INPUT',
    'call' : 'CALL',
    'return' : 'RETURN',
    'max' : 'MAX',
    'min' : 'MIN',
    'range' : 'RANGE',
    'iqrange' : 'IQRANGE',
    'median' : 'MEDIAN',
    'average' : 'AVERAGE',
    'stdev' : 'STDEV',
    'variance' : 'VARIANCE',
    'modify' : 'MODIFY',
    'draw' : 'DRAW',
    'sort' : 'SORT'
 }

# Tokens
tokens = [
    'ID',
    'CTE_INT',
    'CTE_FLOAT',
    'CTE_BOOL',
    'CTE_CHAR',
    'CTE_STRING',
    'SEMICOLON',
    'COMMA',
    'PUNTO',
    'LPAREN',
    'RPAREN',
    'LBLOQUE',
    'RBLOQUE',
    'LBRACKET',
    'RBRACKET',
    'EQUALS',
    'PLUS',
    'MINUS',
    'TIMES',
    'DIVIDE',
    'LESSTHAN',
    'GREATERTHAN',
    'LESSTHANEQUAL',
    'GREATERTHANEQUAL',
    'EQUALEQUAL',
    'NOTEQUAL',
    'AND',
    'OR',
    'NOT'
    #'COMMENT'
 ] + list(reserved.values())

# Regular epression rules for simple tokens
t_SEMICOLON             = r'\;'
t_COMMA                 = r'\,'
t_PUNTO                 = r'\.'
t_LPAREN                = r'\('
t_RPAREN                = r'\)'
t_LBLOQUE               = r'\{'
t_RBLOQUE               = r'\}'
t_LBRACKET              = r'\['
t_RBRACKET              = r'\]'
t_EQUALS                = r'\='
t_PLUS                  = r'\+'
t_MINUS                 = r'\-'
t_TIMES                 = r'\*'
t_DIVIDE                = r'\/'
t_LESSTHAN              = r'\<'
t_GREATERTHAN           = r'\>'
t_LESSTHANEQUAL         = r'\<='
t_GREATERTHANEQUAL      = r'\>='
t_EQUALEQUAL            = r'\=='
t_NOTEQUAL              = r'\!='
t_AND                   = r'\&&'
t_OR                    = r'\|\|'
t_NOT                   = r'\!'
#t_COMMENT               = r'\//'

# A regular expression rule with some action code

def t_CTE_BOOL(t):
    r'true|false'
    t.type = reserved.get(t.value, 'CTE_BOOL')
    return t

def t_CTE_STRING(t):
    r'\"[a-zA-Z_0-9 ]*\"'
    t.type = reserved.get(t.value, 'CTE_STRING')
    return t

def t_ID(t):
    r'[a-z][a-zA-Z_0-9]*'
    t.type = reserved.get(t.value, 'ID')
    return t

def t_CTE_CHAR(t):
    r'\'[a-zA-Z]\''
    t.type = reserved.get(t.value, 'CTE_CHAR')
    return t

def t_CTE_FLOAT(t):
    r'\d+\.\d+'
    t.value = float(t.value)
    return t

def t_CTE_INT(t):
    r'\d+'
    t.value = int(t.value)
    return t

# Define a rule so we can track line numbers
def t_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)

# A string containing ignored characters (spaces and tabs)
t_ignore  = ' \t'
t_ignore_comment = r'\/\/.*'

# Error handling rule
def t_error(t):
    print("Illegal character '%s'" % t.value[0])
    t.lexer.skip(1)

lexer = lex.lex()

# Test it out
#data = '''
#program patito;
#func int suma1(int x)
#{
#    x = x+1;
#    return x;
#}
#func void printSmile()
#{
#    print("happy face");
#}
#void main()
#{
#    var counter as int[10];
#    var pi as float;
#    var x as int;
#    if(counter[5]>10)
#    {
#        counter[5] = input();
#    }
#    else
#    {
#        print(counter.size());
#    }
#    pi = 3.14;
#    // two decimals
#    x = call.suma1(int x);
#    boolID = true;
#    chad = 'A';
#    call.printSmile();
#}
#'''
#lexer.input(data)

#while True:
#    tok = lexer.token()
#    if not tok:
#        break      # No more input
#    print(tok)
