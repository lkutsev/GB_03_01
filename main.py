from collections import deque
class parser:
    instr = ""
    def __init__(self):
        self.instr = "0 + 0"
    def instr_by_input(self):
        self.instr = input("Введи формулу:")
    def set_instr(self, p_instr):
        self.instr = p_instr
    def get_instr(self):
        return self.instr
    def out_instr(self):
        print(self.instr)
    def check_str(self):#здесь надо строку проверить на корректность, привести к нужному виду
        return self.instr
class calc:
    stackIn = deque()
    stackOps = deque()
    stackOut = deque()
    def polsk_zap(self, stroka):
        # цикл по исходному выражению
        inList = stroka.split(' ')
        # заполняем очередь исходным выражением
        for i in inList:
            try:
                self.stackIn.append(i)
            except:
                pass
        while 1 == 1:
            try:
                i = self.stackIn.popleft()
                #        print("i=",i,", stackOps:",stackOps, ", stackIn:",stackIn,", stackOut:",stackOut)
                # Число - добавляем в строку вывода.
                if i.isdigit():
                    self.stackOut.append(i)
                # Функция или открывающая скобка - помещаем в стек.
                if i in ("("):
                    self.stackOps.append(i)
                # Оператор (O1):
                # Пока присутствует на вершине стека лексема-оператор (O2) чей приоритет выше или равен приоритету O1, либо равенство приоритетов является левоассоциативным:
                # Перекладываем O2 из стека в выходную очередь.
                # Помещаем O1 в стек.
                if i in ("+", "-"):
                    try:
                        while 1 == 1:
                            try:
                                sym = self.stackOps.pop()
                            except Exception:
                                sym = ''
                            if sym in ("*", "/", "+", "-"):
                                self.stackOut.append(sym)
                            else:
                                self.stackOps.append(sym)
                                break
                        self.stackOps.append(i)
                    except Exception as e:
                        print("except50:", e)
                if i in ("*", "/"):
                    try:
                        while 1 == 1:
                            try:
                                sym = self.stackOps.pop()
                            except Exception:
                                sym = ''
                            if sym in ("*", "/"):
                                self.stackOut.append(sym)
                            else:
                                self.stackOps.append(sym)
                                break
                        self.stackOps.append(i)
                    except Exception:
                        print("exc 65: i = ", i)
                # Закрывающая скобка:
                # Пока лексема на вершине стека не станет открывающей скобкой, перекладываем лексемы-операторы из стека в выходную очередь.
                # Удаляем из стека открывающую скобку.
                # Если лексема на вершине стека — функция, перекладываем её в выходную очередь.
                # Если стек закончился до того, как была встречена открывающая скобка - в выражении содержится ошибка.
                if i in (")"):
                    try:
                        while 1 == 1:
                            sym = self.stackOps.pop()
                            if sym not in ("(") and sym in ("*", "/", "+", "-"):
                                self.stackOut.append(sym)
                            else:
                                break
                    except Exception:
                        print("exc11")
            except Exception:
                break
                # Если во входной строке больше не осталось лексем:
                # Пока есть операторы в стеке:
                # Если на вершине стека скобка - в выражении допущена ошибка.
                # Перекладываем оператор из стека в выходную очередь.
        try:
            while 1 == 1:
                try:
                    sym = self.stackOps.pop()
                except Exception:
                    break
                if sym in ("(", ")"):
                    print("ERROR: the stackops contains extra parentheses")
                if sym in (""):
                    break
                else:
                    self.stackOut.append(sym)
        except Exception as e:
            pass
        return self.stackOut
    def calculate(self):
        # Алгоритм вычисления выражения, записанного в ОПЗ
        # Для реализации этого алгоритма используется стек для чисел (или для переменных,
        # если они встречаются в исходном выражении). Алгоритм очень прост. В качестве входной
        # строки мы теперь рассматриваем выражение, записанное в ОПЗ:
        # 1. Если очередной символ входной строки - число, то кладем его в стек.
        # 2. Если очередной символ - знак операции, то извлекаем из стека два верхних числа,
        # используем их в качестве операндов для этой операции, затем кладем результат обратно в стек.
        # Когда вся входная строка будет разобрана в стеке должно остаться одно число,
        # которое и будет результатом данного выражения.
        self.stackIn.clear()
        while 1 == 1:
            try:
                sym1 = self.stackOut.popleft()
            except Exception:
                break
            if sym1.isdigit():
                self.stackIn.append(sym1)
            else:
                try:
                    b = int(self.stackIn.pop())
                    a = int(self.stackIn.pop())
                    if sym1 == "+":
                        c = a + b
                    elif sym1 == "-":
                        c = a - b
                    elif sym1 == "*":
                        c = a * b
                    elif sym1 == "/":
                        c = a / b
                    self.stackIn.append(c)
                except Exception:
                    pass
        return self.stackIn.pop()
#inTxt = '( 8 + 2 * 5 ) / ( 1 + 3 * 2 - 4 )' #825*+132*+4-/
#inTxt = '( 1 + 2 ) * 4 + 3'
ins = parser()
#ins.instr_by_input()
ins.set_instr('( 1 + 2 ) * 4 + 3')
ins.out_instr()
clc = calc()
opz = str(clc.polsk_zap(ins.get_instr()))
res = clc.calculate()
print("Обратная польская запись:",opz)
print ("Результат:",res)




