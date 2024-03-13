import math
from Calculator import Caalculator as Calc

def eventer(event, values)->list:
    line = {"a": "", "b": "", "f": "", "r": ""}
    line = Calc.readline(Calc, values["-IN-"])
    
    if line["f"] == "+":
        line["r"] = Calc.add(Calc, line["a"], line["b"])

    if line["f"] == "-":
        line["r"] = Calc.subtract(Calc, line["a"], line["b"])

    if line["f"] == "*":
        line["r"] = Calc.multiply(Calc, line["a"], line["b"])

    if line["f"] == "/":
        line["r"] = Calc.divide(Calc, line["a"], line["b"])

    return line
