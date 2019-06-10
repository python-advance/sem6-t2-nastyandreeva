# 2.2 Создание программы, возвращающей список чисел Фибоначчи с помощью итератора.

a = int(raw_input('Введите число: '))

def fib(n):
    a, b = 0, 1
    for i in range(n):
        yield a
        a, b = b, a + b

print list(fib(a))

value = int(input("Введите максимальное число: \t" ))


def fib(value):
  lst = [0, 1, ]
  it = iter(list(range(2, value)))
  while True:
    try:
      elem = next(it)
    except StopIteration:
      break
    n = lst[elem - 1] + lst[elem - 2]
    lst.append(n)
  return lst

res = fib(value)
print(res)
