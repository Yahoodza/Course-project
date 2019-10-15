'''
Вспомогательный модуль основной программы.

Название: Methods_DE.

Разработал: Королёв Петр Олегович, группа ТМП-61.

Дата и номер версии: 02.04.2019 v4.0.

Язык: Python.

Используемые в модуле функции:
Euler() - функция, вычисляющая ДУ методом Эйлера;
ImprovedEuler() - функция, вычисляющая ДУ усовершенствованным методом Эйлера.
'''

from prettytable import PrettyTable as pt
from time import sleep
from Input import *
from math import cos, sin, tan, log, pi, e, acos, asin, atan

'''
Euler() - функция, вычисляющая ДУ методом Эйлера.

Локальные переменные:
TbE - результирующая таблица;
TbE.field_names - название столбцов результирующей таблицы;
Form - вводимое уравнение;
x - значение х[0];
y - значение y[0];
h - значение шага итерации;
k - количество итераций;
i - счетчик для цикла;
fxy - значение y';
dy - значение дельта y.
'''

def Euler ():

	TbE = pt()
	TbE.field_names = ["№", "x", "y", "y'=f(x,y)", "Delta(y)=y'h"]

	gotoxy(40, 2)
	SetColor(5, 15)
	print ('Задача: решить данное ДУ методом Эйлера')
	SetColor(0, 15)
	Form = Formula()
	x, y = CheckErrorFormula (Form)
	gotoxy(2, 7)
	print ('Введите шаг итерации h:')
	h = Enter_float (0, 2, '', 26, 7)
	gotoxy(2, 8)
	print ('Введите количество итераций:')
	k = Enter_int (1, 10, '', 31, 8)
	gotoxy(2, 9)
	SetColor(5, 15)
	print ('Решение будет производится на интервале [',x,', ',h*k+x,']')
	gotoxy(2, 10)
	print ('y(',h*k+x,') = ?\n')
	SetColor(0, 15)
	
	for i in range (k+1):						#Цикл вычисления ДУ методом Эйлера
		fxy = eval (Form)
		dy = fxy*h
		TbE.add_row ([i, "%.2f" %x, "%.2f" %y, "%.5f" %fxy, "%.5f" %dy])
		y += dy
		x += h

	print (TbE)

'''
ImprovedEuler() - функция, вычисляющая ДУ усовершенствованным методом Эйлера.

Локальные переменные:
TbImE - результирующая таблица;
TbImE.field_names - название столбцов результирующей таблицы;
Form - вводимое уравнение;
x - значение х[0];
y - значение y[0];
h - значение шага итерации;
t - количество знаков шага итерации после запятой;
Flag - флаг для выхода из цикла;
k - конечное значение х;
sizecicle - количество итераций на отрезке [x, k];
i - счетчик для цикла;
chx - переменная, хранящая значение переменной x;
chy - переменная, хранящая значение переменной y;
fxy - значение y';
xh - переменная, хранящая значение переменной x=x+h/2;
yh - переменная, хранящая значение переменной y=y+h/2*f(x,y);
fxhyh - значение y' при x=x+h/2 и y=y+h/2*f(x,y);
dy - значение дельта y при x=x+h/2 и y=y+h/2*f(x,y).
'''

def ImprovedEuler ():

	TbImE = pt()
	TbImE.field_names = ["№", "x", "y", "f(x,y)", "x+h/2", "y+h/2*f(x,y)", "f(x+h/2, y+h/2*f(x,y))", "Delta(y)=f(x+h/2, y+h/2*f(x,y))*h"]

	gotoxy(35, 2)
	SetColor(5, 15)
	print ('Задача: решить данное ДУ усовершенствованным методом Эйлера')
	SetColor(0, 15)
	Form = Formula()
	x, y = CheckErrorFormula (Form)
	gotoxy(2, 7)
	print ('Введите шаг итерации h:')
	h = Enter_float (0, 2, '', 26, 7)
	t = len(str(h)) - str(h).index('.') - 1
	Flag = False
	gotoxy(2, 8)
	print ('Введите X конечное:')
	while Flag == False:							#Цикл проверки правильности вода x конечного
		ShowCursor(True)							#и расчёта количества итераций
		k = Enter_float (x+h-0.0001, 20, '', 22, 8)
		sizecicle = (k - x) / h
		if round(k - h * round(sizecicle), t) == x:	#Условие проверки правильности вода x конечного
			Flag = True
		else:
			ShowCursor(False)
			gotoxy(22, 8)
			print ('\t\t\t\t\t\t\t\t\t\t\t\t\t\t')
			gotoxy(33, 20)
			SetColor(4, 15)
			print ('Ошибка!!! Введите X конечное, соответствующее шагу итерации!')
			sleep(4)
			SetColor(0, 15)
			gotoxy(33, 20)
			print ('\t\t\t\t\t\t\t\t\t')
	gotoxy(2, 9)
	SetColor(5, 15)
	print ('Решение будет производится на интервале [',x,',',k,']')
	gotoxy(2, 10)
	print ('y(',k,') = ?\n')
	SetColor(0, 15)

	for i in range (round(sizecicle)+1):			#Цикл вычисления ДУ усовершенствованным
		chx = x										#методом Эйлера
		chy = y
		fxy = eval (Form)
		x = x+h*0.5
		y = y+h*0.5*fxy
		xh = x
		yh = y
		fxhyh = eval (Form)
		x = chx
		y = chy
		dy = fxhyh*h
		TbImE.add_row ([i,  round(x, t), round(y, t),"%.5f" %fxy, "%.5f" %xh, "%.5f" %yh, "%.5f" %fxhyh, "%.5f" %dy])
		y += dy
		x += h

	print (TbImE)