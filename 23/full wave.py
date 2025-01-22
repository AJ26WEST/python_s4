import numpy as np
import matplotlib.pyplot as plt
t=np.linspace(0,2*np.pi,50)
x=np.sin(t)
y=np.abs(x)
plt.plot(t,x)
plt.plot(t,y)
plt.xlabel("TIme")
plt.ylabel("Amplitude")
plt.grid()
plt.title("FULL wave rectifier")
plt.show()
