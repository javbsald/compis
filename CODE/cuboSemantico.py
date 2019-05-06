# Cubo Semantico
# [operacion][tipo1][tipo2]

# 0 -   void          void          &&
# 1 -   int           int           ||
# 2 -   float         float         <
# 3 -   bool          bool          >
# 4 -   char          char          <=
# 5 -   pieChart      pieChart      >=
# 6 -   barGraph      barGraph      ==
# 7 -   plotLine      plotLine      !=
# 8 -                               +
# 9 -                               -
# 10 -                              *
# 11 -                              /
# 12 -                              =
# 13 -                              !

import pprint

def convertSemCubeParam(tipo):
    if tipo == "void" or tipo == "&&":
        return 0
    elif tipo == "int" or tipo == "||":
        return 1
    elif tipo == "float" or tipo == "<":
        return 2
    elif tipo == "bool" or tipo == ">":
        return 3
    elif tipo == "char"  or tipo == "<=":
        return 4
    elif tipo == "pieChart" or tipo == ">=":
        return 5
    elif tipo == "barGraph" or tipo == "==":
        return 6
    elif tipo == "plotLine" or tipo == "!=":
        return 7
    elif tipo == "+":
        return 8
    elif tipo == "-":
        return 9
    elif tipo == "*":
        return 10
    elif tipo == "/":
        return 11
    elif tipo == "=":
        return 12
    elif tipo == "!":
        return 13
    elif tipo == 1:
        return "int"
    elif tipo == 2:
        return "float"
    elif tipo == 3:
        return "bool"
    elif tipo == 4:
        return "char"
    else:
        return "Error"

cube_operacion = 14
cube_tipo1 = 8
cube_tipo2 = 8

semCube = [[["Error" for k in range(cube_tipo1)] for j in range(cube_tipo2)] for i in range(cube_operacion)]

# 0 - &&
semCube[0][3][3] = 3        # bool && bool = bool

# 1 - ||
semCube[1][3][3] = 3        # bool || bool = bool

# 2 - <
semCube[2][1][1] = 3        # int < int = bool
semCube[2][1][2] = 3        # int < float = bool
semCube[2][2][1] = 3        # float < int = bool
semCube[2][2][2] = 3        # float < float = bool

# 3 - >
semCube[3][1][1] = 3        # int > int = bool
semCube[3][1][2] = 3        # int > float = bool
semCube[3][2][1] = 3        # float > int = bool
semCube[3][2][2] = 3        # float > float = bool

# 4 - <=
semCube[4][1][1] = 3        # int <= int = bool
semCube[4][1][2] = 3        # int <= float = bool
semCube[4][2][1] = 3        # float <= int = bool
semCube[4][2][2] = 3        # float <= float = bool

# 5 - >=
semCube[5][1][1] = 3        # int >= int = bool
semCube[5][1][2] = 3        # int >= float = bool
semCube[5][2][1] = 3        # float >= int = bool
semCube[5][2][2] = 3        # float >= float = bool

# 6 - ==
semCube[6][1][1] = 3        # int == int = bool
semCube[6][1][2] = 3        # int == float = bool
semCube[6][2][1] = 3        # float == int = bool
semCube[6][2][2] = 3        # float == float = bool
semCube[6][3][3] = 3        # bool == bool = bool
semCube[6][4][4] = 3        # char == char = bool

# 7 - !=
semCube[7][1][1] = 3        # int != int = bool
semCube[7][1][2] = 3        # int != float = bool
semCube[7][2][1] = 3        # float != int = bool
semCube[7][2][2] = 3        # float != float = bool
semCube[7][3][3] = 3        # bool != bool = bool
semCube[7][4][4] = 3        # char != char = bool

# 8 - +
semCube[8][1][1] = 1        # int + int = int
semCube[8][1][2] = 2        # int + float = float
semCube[8][2][1] = 2        # float + int = float
semCube[8][2][2] = 2        # float + float = float

# 9 - -
semCube[9][1][1] = 1        # int - int = int
semCube[9][1][2] = 2        # int - float = float
semCube[9][2][1] = 2        # float - int = float
semCube[9][2][2] = 2        # float - float = float

# 10 - *
semCube[10][1][1] = 1        # int * int = int
semCube[10][1][2] = 2        # int * float = float
semCube[10][2][1] = 2        # float * int = float
semCube[10][2][2] = 2        # float * float = float

# 11 - /
semCube[11][1][1] = 2        # int / int = float
semCube[11][1][2] = 2        # int / float = float
semCube[11][2][1] = 2        # float / int = float
semCube[11][2][2] = 2        # float / float = float

# 12 - =
semCube[12][1][1] = 1        # int = int = int
semCube[12][1][2] = 1        # int = float = int
semCube[12][2][1] = 2        # float = int = float
semCube[12][2][2] = 2        # float = float = float
semCube[12][3][3] = 3        # bool = bool = bool
semCube[12][4][4] = 4        # char = char = char

# 13 - !
# como el NOT es un operador unario,toda la columna del tipo2 (bool), va a regresar bool, sin importar el lado izquierdo
semCube[13][0][3] = 3        # void ! bool = bool
semCube[13][1][3] = 3        # int ! bool = bool
semCube[13][2][3] = 3        # float ! bool = bool
semCube[13][3][3] = 3        # bool ! bool = bool
semCube[13][4][3] = 3        # char ! bool = bool
semCube[13][5][3] = 3        # pieChart ! bool = char
semCube[13][6][3] = 3        # barGraph ! bool = char
semCube[13][7][3] = 3        # plotLine ! bool = char

#pprint.pprint(semCube)
