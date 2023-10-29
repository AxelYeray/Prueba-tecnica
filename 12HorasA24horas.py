#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'timeConversion' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING s as parameter.
#

def timeConversion(s):
    # Separa la hora, los minutos y los segundos de la cadena de entrada
    time_components = s.split(":")
    
    # Extrae la parte de AM o PM y la hora
    am_pm = time_components[2][-2:]
    hour = int(time_components[0])
    
    # Realiza la conversión a formato de 24 horas
    if am_pm == "AM":
        # Si es AM y la hora es 12, cambia a 0
        if hour == 12:
            hour = 0
    else:
        # Si es PM y la hora no es 12, suma 12
        if hour != 12:
            hour += 12
    
    # Formatea la hora en formato de 24 horas
    result = f"{hour:02d}:{time_components[1]}:{time_components[2][:2]}"
    
    return result
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = timeConversion(s)

    fptr.write(result + '\n')

    fptr.close()
