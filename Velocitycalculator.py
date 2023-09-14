
Velocity calculator:

def f(x):
  f_g = int(x)
  return f_x

print("The first time it took to advance 2 meter")
x = input()
h1 = int(x)
g1 = 2/int(x)


print("The second time it took to advance 2 meter")
x = input()
h2 = int(x)
g2 = 2/int(x)

print("The third time it took to advance 2 meter")
x = input()
h3 = int(x)
g3 = 2/int(x)

print("The 3 velocities are:",g1,"mt/s,",g2,"mt/s,",g3,"mt/s")

g4 = (g1+g2+g3)/int(3)
print("The average velocity was:",g4)

h4 = (h1+h2+h3)/int(3)
print("The average time was:",h4)
t1 = g4/h4
print("the average acceleration was:",t1)
print("The 3 velocities were:",g1,g2,g3,"and the rate of change in velocity was:",g4)
