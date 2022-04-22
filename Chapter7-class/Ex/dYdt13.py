from Ex.Derivative13 import Derivative
from Ex.Y13 import Y

v0 = 1
g = 9.81
t = [0, v0/(2*g), v0/g]
y = Y(v0)
dy = Derivative(y)
dYdt_exact = []
dYdt_computed = []

dYdt_exact.append(v0)
dYdt_exact.append(v0/2)
dYdt_exact.append(0)

dYdt_computed.append(dy(t[0]))
dYdt_computed.append(dy(t[1]))
dYdt_computed.append(dy(t[2]))

for i in range(3):
    print("Difference between exact and computed derivatives is " +
          f"{abs(dYdt_computed[i]-dYdt_exact[i])} at t={t[i]}.")
