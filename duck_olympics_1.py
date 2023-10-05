def suma(a,b):
  x = a + b
  return x

def resta(a,b):
  x = a - b
  return x

print("Dame el primer numero:")
a = int(input())
print("Dame el segundo numero")
b = int(input())
print("La suma da", suma(a,b), "y la resta da", resta(a,b))


###

def multiplicacion(a,b):
  x = a * b
  return x

def division(a,b):
  x = a/b
  return x

print("Dame el primer numero:")
a = int(input())
print("Dame el segundo numero:")
b = int(input())
print("La multiplicacion da", multiplicacion(a,b), "y la divicion da", division(a,b))

###

def conversion(k):
  x = k * 1000
  return x

print("How many kilometers have passed?")
k = int(input())
print("It passed", conversion(k), "meters")

###

def triangle(b,a):
  x = (b*a)/2
  return x

print("What is the base of the triangle?")
b = int(input())
print("What is the height of the triangle?")
a = int(input())
print("The area of the triangle is:", triangle(b,a))
