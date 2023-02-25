Python 3.11.2 (tags/v3.11.2:878ead1, Feb  7 2023, 16:38:35) [MSC v.1934 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> 
... while True:
...     s = input("Знак (+,-,*,/): ")
...     if s == '0':
...         break
...     if s in ('+', '-', '*', '/'):
...         x = float(input("x="))
...         y = float(input("y="))
...         if s == '+':
...             print("%.2f" % (x+y))
...         elif s == '-':
...             print("%.2f" % (x-y))
...         elif s == '*':
...             print("%.2f" % (x*y))
...         elif s == '/':
...             if y != 0:
...                 print("%.2f" % (x/y))
...             else:
...                 print("Деление на ноль!")
...     else:
