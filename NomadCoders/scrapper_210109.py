def p_plus(a,b):
  print(a+b)

def r_plus(a,b):
  return a+b

p_result = p_plus(2,3)
r_result = r_plus(2,3)

print(p_result, r_result)

##############################

def say_hello(name, age):
  return f"Hello {name} you are {age} years old"

hello = say_hello("nico", "12")
print(hello)

##############################

#code challenge!#

def sum(a,b):
  if type(a) == int and type(b) == int:
    return a + b
  elif type(a) != int or type(b) != int:
    print("숫자를 입력하여 주세요")

def difference(a,b):
  if type(a) == int and type(b) == int:
    return a - b
  elif type(a) != int or type(b) != int:
    print("숫자를 입력하여 주세요")

def product(a,b):
  if type(a) == int and type(b) == int:
    return a * b
  elif type(a) != int or type(b) != int:
    print("숫자를 입력하여 주세요")

def quotient(a,b):
  if type(a) == int and type(b) == int:
    return a / b
  elif type(a) != int or type(b) != int:
    print("숫자를 입력하여 주세요")

def reminder(a,b):
  if type(a) == int and type(b) == int:
    return a % b
  elif type(a) != int or type(b) != int:
    print("숫자를 입력하여 주세요")

def power(a,b):
  if type(a) == int and type(b) == int:
    return a ** b
  elif type(a) != int or type(b) != int:
    print("숫자를 입력하여 주세요")

sum(3,"야호")
print(sum(5,2))
print(difference(5,2))
print(product(5,2))
print(quotient(5,2))
print(reminder(5,2))
print(power(5,2))
