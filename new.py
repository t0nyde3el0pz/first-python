import random

def a():
  c=random.randint(300,400)
  return c

def b():
  plus=int(input("Write a number: "))
  print(a() + plus)

b()