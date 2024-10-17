# main.py

from validador import (Validador, ReglaValidacionGanimedes, ReglaValidacionCalisto)
from errores import ( NoCumpleLongitudMinimaError, NoTieneLetraMayusculaError, NoTieneLetraMinusculaError,NoTieneNumeroError, NoTieneCaracterEspecialError, NoTienePalabraSecretaError)

def main():
    validador_ganimedes = Validador(ReglaValidacionGanimedes)
    validador_calisto = Validador(ReglaValidacionCalisto)

    clave = input("Introduce una clave para validar: ")
