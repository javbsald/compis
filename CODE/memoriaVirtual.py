# Mapa de Memoria

# Memoria Global
global_int_start = 1000
global_float_start = 5000
global_char_start = 7000
global_bool_start = 9000

# Memoria local
memoriaLocal = dict()
local_int_start = 10000
local_int_counter = local_int_start
local_float_start = 15000
local_float_counter = local_float_start
local_char_start = 17000
local_char_counter = local_char_start
local_bool_start = 19000
local_bool_counter = local_bool_start

# Memoria temporal
temp_int_start = 20000
temp_float_start = 22000
temp_char_start = 23000
temp_bool_start = 24000

# Memoria Constante
memoriaConstante = dict()
memoriaConstanteDir = dict()
constant_int_start = 25000
constant_float_start = 27000
constant_char_start = 28000
constant_bool_start = 29000

def getGlobalDir(dir_type):
    if dir_type == "int":
        global global_int_start
        global_int_start += 1
        return global_int_start
    elif dir_type == "float":
        global global_float_start
        global_float_start += 1
        return global_float_start
    elif dir_type == "char":
        global global_char_start
        global_char_start += 1
        return global_char_start
    elif dir_type == "bool":
        global global_bool_start
        global_bool_start += 1
        return global_bool_start

def getLocalDir(dir_type):
    if dir_type == "int":
        global local_int_counter
        local_int_counter += 1
        return local_int_counter
    elif dir_type == "float":
        global local_float_counter
        local_int_counter += 1
        return local_int_counter
    elif dir_type == "char":
        global local_char_counter
        local_char_counter += 1
        return local_char_counter
    elif dir_type == "bool":
        global local_bool_counter
        local_bool_counter += 1
        return local_bool_counter

def getTempDir(dir_type):
    if dir_type == "int":
        global temp_int_start
        temp_int_start += 1
        return temp_int_start
    elif dir_type == "float":
        global temp_float_start
        temp_float_start += 1
        return temp_float_start
    elif dir_type == "char":
        global temp_char_start
        temp_char_start += 1
        return temp_char_start
    elif dir_type == "bool":
        global temp_bool_start
        temp_bool_start += 1
        return temp_bool_start

def getConstantDir(dir_type):
    if dir_type == "int":
        global constant_int_start
        constant_int_start += 1
        return constant_int_start
    elif dir_type == "float":
        global constant_float_start
        constant_float_start += 1
        return constant_float_start
    elif dir_type == "char":
        global constant_char_start
        constant_char_start += 1
        return constant_char_start
    elif dir_type == "bool":
        global constant_bool_start
        constant_bool_start += 1
        return constant_bool_start

def resetLocal():
    global local_int_counter
    global local_int_start
    local_int_counter = local_int_start-1
    global local_float_counter
    global local_float_start
    local_float_counter = local_float_start-1
    global local_char_counter
    global local_char_start
    local_char_counter = local_char_start-1
    global local_bool_counter
    global local_bool_start
    local_bool_counter = local_bool_start-1
