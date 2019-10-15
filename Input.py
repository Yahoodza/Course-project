'''
Вспомогательный модуль основной программы.

Название: Input.

Разработал: Королёв Петр Олегович, группа ТМП-61.

Дата и номер версии: 01.04.2019 v3.0.

Язык: Python.

Используемые в модуле функции:
catan() - функция котангенса;
acatan() - функция арккотангенса;
Enter_float() - функция ввода вещественных значений;
Enter_int() - функция ввода целочисленных значений;
Formula() - функция ввода ДУ;
CheckErrorFormula() - функция проверки начальных значений x[0] и y[0]
на возможность участия в введенном уравнении.
'''

from time import sleep
from ctypes import *
from math import cos, sin, tan, log, pi, e, acos, asin, atan

class COORD(Structure):
	#pass
    _fields_ = [("X", c_short), ("Y", c_short)]
#COORD._fields_ = [("X", c_short), ("Y", c_short)]

class CONSOLE_CURSOR_INFO(Structure):
	#pass
	_fields_ = [('dwSize', c_int), ('bVisible', c_bool)]
#CONSOLE_CURSOR_INFO._fields_ = [('dwSize', c_int), ('bVisible', c_byte)]

def gotoxy(c, r):
    h = windll.kernel32.GetStdHandle(-11)	#STD_OUTPUT_HANDLE = -11
    windll.kernel32.SetConsoleCursorPosition(h, COORD(c, r))

def SetColor(text, background):
	h = windll.kernel32.GetStdHandle(-11)	#STD_OUTPUT_HANDLE = -11
	windll.kernel32.SetConsoleTextAttribute(h, ((background << 4) | text))

def ShowCursor(Visible):
	h = windll.kernel32.GetStdHandle(-11)	#STD_OUTPUT_HANDLE = -11
	CursorInfo = CONSOLE_CURSOR_INFO()
	CursorInfo.dwSize = 1
	CursorInfo.bVisible = Visible
	windll.kernel32.SetConsoleCursorInfo(h, byref(CursorInfo))

'''
catan() - функция котангенса.

Формальный параметр:
ax - переменная, передающая значение аргумента функции (x).
'''

def catan (ax):
	return 1/tan(ax)

'''
acatan() - функция арккотангенса.

Формальный параметр:
ax - переменная, передающая значение аргумента функции (x).

Локальная переменная:
arcctg - пересенная для вычисления арккотангенса.
'''

def acatan (ax):
	if ax == 0:										#Условие проверки при
		arcctg = 0									#делении на 0
	else:
		arcctg = atan(1/ax)
	return arcctg

'''
Enter_float() - функция ввода вещественных значений.

Формальные параметры:
m - левая граница промежутка;
n - правая граница промежутка;
c - переменная для форматированного вывода;
x - переменная для вывода по оси Ox;
y - переменная для вывода по оси Oy.

Локальная переменная:
size - введённое значение.
'''

def Enter_float (m, n, c, x, y):
	while True:										#Цикл проверки правильности
		try:										#ввода вещественных значений
			ShowCursor(True)
			gotoxy(x, y)
			size = float (input("%s" %c))
		except ValueError:
			ShowCursor(False)
			gotoxy(x-1, y)
			print ('\t\t\t\t\t\t\t\t\t\t\t\t\t\t')
			gotoxy(43, 20)
			SetColor(4, 15)
			print ('Ошибка!!! Введите корректное значение!')
			sleep(4)
			SetColor(0, 15)
			gotoxy(43, 20)
			print ('\t\t\t\t\t\t\t\t\t')
		else:
			if m < size <= n:
				return size
			else:
				ShowCursor(False)
				gotoxy(x-1, y)
				print ('\t\t\t\t\t\t\t\t\t\t\t\t\t\t')
				gotoxy(45, 20)
				SetColor(4, 15)
				print ('Ошибка!!! Введите число от %d до %d!' %(m, n))
				sleep(4)
				SetColor(0, 15)
				gotoxy(45, 20)
				print ('\t\t\t\t\t\t\t\t\t')

'''
Enter_int() - функция ввода целочисленных значений.

Формальные параметры:
m - левая граница промежутка;
n - правая граница промежутка;
c - переменная для форматированного вывода;
x - переменная для вывода по оси Ox;
y - переменная для вывода по оси Oy.

Локальная переменная:
size - введённое значение.
'''

def Enter_int (m, n, c, x, y):
	while True:										#Цикл проверки правильности
		try:										#ввода целочисленных значений
			ShowCursor(True)
			gotoxy(x, y)
			size = int (input("%s" %c))
		except ValueError:
			ShowCursor(False)
			gotoxy(x-1, y)
			print ('\t\t\t\t\t\t\t\t\t\t\t\t\t')
			gotoxy(43, 20)
			SetColor(4, 15)
			print ('Ошибка!!! Введите корректное значение!')
			sleep(4)
			SetColor(0, 15)
			gotoxy(43, 20)
			print ('\t\t\t\t\t\t\t\t\t')
		else:
			if m <= size <= n:
				return size
			else:
				ShowCursor(False)
				gotoxy(x-1, y)
				print ('\t\t\t\t\t\t\t\t\t\t\t\t\t')
				gotoxy(45, 20)
				SetColor(4, 15)
				print ('Ошибка!!! Введите число от %d до %d!' %(m, n))
				sleep(4)
				SetColor(0, 15)
				gotoxy(45, 20)
				print ('\t\t\t\t\t\t\t\t\t')

'''
Formula() - функция ввода ДУ.

Локальные переменные:
x - переменная для проверка на правильность введенного
уравнения;
y - переменная для проверка на правильность введенного
уравнения;
f - введённое уравнение.
'''

def Formula ():
	x = 1
	y = 1
	while True:										#Цикл проверки правильности
		try:										#ввода ДУ
			ShowCursor(True)
			gotoxy(2, 4)
			SetColor(5, 15)
			print ("Введите уравнение: y' = ")
			SetColor(0, 15)
			gotoxy(26, 4)
			f = input()
			f = f.lower()
			eval (f)
		except (NameError, SyntaxError, ValueError, ZeroDivisionError):
			ShowCursor(False)
			gotoxy(25, 4)
			print ('\t\t\t\t\t\t\t\t\t\t\t\t\t')
			gotoxy(44, 20)
			SetColor(4, 15)
			print ('Ошибка!!! Введите корректное уравнение!')
			sleep(4)
			SetColor(0, 15)
			gotoxy(44, 20)
			print ('\t\t\t\t\t\t\t\t\t')
		else:
			if ('%' in f or '&' in f or '=' in f or '<' in f or '>' in f or '^' in f or '>=' in f or '<=' in f or '~' in f):
				ShowCursor(False)
				gotoxy(25, 4)
				print ('\t\t\t\t\t\t\t\t\t\t\t\t\t')
				gotoxy(44, 20)
				SetColor(4, 15)
				print ('Ошибка!!! Введите корректное уравнение!')
				sleep(4)
				SetColor(0, 15)
				gotoxy(44, 20)
				print ('\t\t\t\t\t\t\t\t\t')
			else:
				if 'x' in f and 'y' in f:
					return f
				else:
					ShowCursor(False)
					gotoxy(25, 4)
					print ('\t\t\t\t\t\t\t\t\t\t\t\t\t')
					gotoxy(44, 20)
					SetColor(4, 15)
					print ('Ошибка!!! Введите корректное уравнение!')
					sleep(4)
					SetColor(0, 15)
					gotoxy(44, 20)
					print ('\t\t\t\t\t\t\t\t\t')

'''
CheckErrorFormula() - функция проверки начальных значений x[0] и y[0]
на возможность участия в введенном уравнении.

Формальный параметр:
f - введённое уравнение.

Локальные переменные:
x - значение x[0];
y - значение y[0].
'''

def CheckErrorFormula (f):
	while True:										#Цикл проверки корректности
		try:										#ввода значений x[0] и y[0]
			ShowCursor(True)
			gotoxy(2, 5)
			print ('Введите x[0]:')
			x = Enter_float (-11, 10, '', 16, 5)
			gotoxy(2, 6)
			print ('Введите y[0]:')
			y = Enter_float (-11, 10, '', 16, 6)
			eval(f)
		except (ZeroDivisionError, ValueError):
			ShowCursor(False)
			gotoxy(16, 5)
			print ('\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t')
			gotoxy(16, 6)
			print ('\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t')
			gotoxy(43, 20)
			SetColor(4, 15)
			print ('Ошибка!!! Введите корректные данные!')
			sleep(4)
			SetColor(0, 15)
			gotoxy(43, 20)
			print ('\t\t\t\t\t\t\t\t\t')
		else:
			return x, y