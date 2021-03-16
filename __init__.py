# coding: utf-8
"""
Base para desarrollo de modulos externos.
Para obtener el modulo/Funcion que se esta llamando:
     GetParams("module")

Para obtener las variables enviadas desde formulario/comando Rocketbot:
    var = GetParams(variable)
    Las "variable" se define en forms del archivo package.json

Para modificar la variable de Rocketbot:
    SetVar(Variable_Rocketbot, "dato")

Para obtener una variable de Rocketbot:
    var = GetVar(Variable_Rocketbot)

Para obtener la Opcion seleccionada:
    opcion = GetParams("option")


Para instalar librerias se debe ingresar por terminal a la carpeta "libs"

    pip install <package> -t .

"""

import difflib

"""
    Obtengo el modulo que fueron invocados
"""
module = GetParams("module")

if module == "diff_ratio":
    str_1 = GetParams("str1")
    str_2 = GetParams("str2")
    result = GetParams("result")
   

    try:
       ratio = difflib.SequenceMatcher(None, str_1, str_2).ratio()
       SetVar(result, ratio)
    except Exception as e:
        PrintException()
        raise e

if module == "replace":
    old_str = GetParams("old")
    new_str = GetParams("new")
    var = GetParams("var")
    result = GetParams("result")

    try:
        new_var = var.replace(old_str, new_str)
        SetVar(result, new_var)
    except Exception as e:
        PrintException()
        raise e

if module == "split":
    var = GetParams("var")
    delimiter = GetParams("delimiter")
    result = GetParams("result")

    try:
        new_var = var.split(delimiter)
        SetVar(result, new_var)
    except Exception as e:
        PrintException()
        raise e


if module == "find":
    var = GetParams("var")
    data = GetParams("data")
    result = GetParams("result")

    try:
        new_var = var.find(data)
        SetVar(result, new_var)
    except Exception as e:
        PrintException()
        raise e

if module == "reverse":
    string = GetParams("string")
    result = GetParams("result")

    reverse_string = string[::-1]
    if result:
        SetVar(result, reverse_string)

