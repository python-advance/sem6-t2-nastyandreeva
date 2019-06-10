# 2.1 Разработать функцию, возвращающую элементы ряда Фибоначчи по данному максимальному значению.

value = int(input("Введите максимальное целое положительное число \t" ))

def fib(n):
  if n > 1:
    return fib(n-1) + fib(n-2)
  return n
for i in range(value):
  print(i, "=", fib(i))
