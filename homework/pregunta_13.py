"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en los archivos `tbl0.tsv`, `tbl1.tsv` y 
`tbl2.tsv`. En este laboratorio solo puede utilizar las funciones y 
librerias de pandas para resolver las preguntas.
"""
import pandas as pd

def pregunta_13():
    archivo1 = pd.read_csv("files/input/tbl0.tsv", sep="\t")
    archivo2 = pd.read_csv("files/input/tbl2.tsv", sep="\t")
    union = pd.merge(archivo1, archivo2, on="c0") #se unen los dos archivos
    resultado = union.groupby("c1")["c5b"].sum() #se hace la suma

    return resultado
    """
    Si la columna `c0` es la clave en los archivos `tbl0.tsv` y `tbl2.tsv`,
    compute la suma de `tbl2.c5b` por cada valor en `tbl0.c1`.

    Rta/
    c1
    A    146
    B    134
    C     81
    D    112
    E    275
    Name: c5b, dtype: int64
    """
