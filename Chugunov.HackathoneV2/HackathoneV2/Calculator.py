import re

class Caalculator():
    def __init__(self) -> None:
        
        pass

    def add(self, x1, x2) -> float:
        """
        Функционал сложения полученных чисел.
        """
        # Принты для проверки получения цифр
        print("Ваше первое число:", x1)
        print("Ваше второе число:", x2)
        # Вычесление результата чтобы return было удобнее читать
        result = (x1+x2)
        # Переменные для вычесления кол-ва цифр
        lengt1 = len(str(x1))
        lengt2 = len(str(x2))
        # Проверка количества цифр чтобы по данному кол-ву обрезать лишнее
        if lengt2 >= lengt1:
            index = int(lengt2)
        else:
            index = int(lengt1)
        return round((result), index)
    
    def subtract(self, x1, x2) -> float:
        """
        Функционал вычитания полученных чисел.
        """
        # Принты для проверки получения цифр
        print("Ваше первое число:", x1)
        print("Ваше второе число:", x2)
        # Вычесление результата чтобы return было удобнее читать
        result = (x1-x2)
        # Переменные для вычесления кол-ва цифр
        lengt1 = len(str(x1))
        lengt2 = len(str(x2))
        # Проверка количества цифр чтобы по данному кол-ву обрезать лишнее
        if lengt2 >= lengt1:
            index = int(lengt2)
        else:
            index = int(lengt1)
        return round((result), index)
    
    def multiply(self, x1, x2) -> float:
        """
        Функционал умножения полученных чисел.
        """
        # Принты для проверки получения цифр
        print("Ваше первое число:", x1)
        print("Ваше второе число:", x2)
        # Вычесление результата чтобы return было удобнее читать
        result = (x1*x2)
        # Переменные для вычесления кол-ва цифр
        lengt1 = len(str(x1))
        lengt2 = len(str(x2))
        # Проверка количества цифр чтобы по данному кол-ву обрезать лишнее
        if lengt2 >= lengt1:
            index = int(lengt2*2)
        else:
            index = int(lengt1*2)
        # Возвращаем наш результат используя round() для отсеивания нулей
        # Используем все через переменные чтобы возвращение было читаемым
        return round((result), index)

    def divide(self, x1, x2) -> float:
        """
        Функционал деления полученных чисел.
        """
        # Принты для проверки получения цифр
        print("Ваше первое число:", x1)
        print("Ваше второе число:", x2)
        # Переменные для вычесления кол-ва цифр
        lengt1 = len(str(x1))
        lengt2 = len(str(x2))
        # Проверка количества цифр чтобы по данному кол-ву обрезать лишнее
        if lengt2 >= lengt1:
            index = int(lengt2)
        else:
            index = int(lengt1)
        # Обезательно делаем проверку на ноль, так как на ноль делить нельзя
        # Вычисляем результат прямо в result так как если вызвать вычесление
        # В переменной то все сломается 
        return (round((x1/x2), index) if x2!=0 else "Делить на ноль нельзя!")
    

    def readline(self, line) -> list:
        print("===Reading line started...===")
        splited_line = {"a": "???", "b": "???", "f": "???", "r": "???"}
        # Удаляем лишние пробелы чтобы код работал
        line = line.replace(' ','')
        # pattern для разделения целый чисел и чисел с плавающей точкой
        # у нас ^ для начала а $ для конца чтобы лишнего не добавлялось
        pattern = r"^(\d+(\.\d+)?)([\+\-\*/])(\d+(\.\d+)?)$"
        # Ищем совпадения с pattern
        match = re.search(pattern, str(line))
        # try и except для отлавливания ошибок
        if match:
            try:
                # Извлекаем числа и знак операции
                a = float(match.group(1))
                f = match.group(3)
                b = float(match.group(4))
                
                # Обновляем значения в словаре
                splited_line["a"] = a
                splited_line["b"] = b
                splited_line["f"] = f
            except:
                print("Введите корректные числа!")
        else:
            print("Неверный формат строки!")
            
        print("===Reading line finished...===")
        print(splited_line["a"], " ", splited_line["f"], " ", splited_line["b"], " = ", splited_line["r"])
        return splited_line

        
