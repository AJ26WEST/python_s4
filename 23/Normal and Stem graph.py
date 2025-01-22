import numpy as np
import matplotlib.pyplot as plt
x=np.arange(0,11)
y=x**2
plt.subplot(1,2,1)
plt.plot(x,y)
plt.xlabel("X")
plt.ylabel("Y")
plt.title("NORMAL")

plt.subplot(1,2,2)
plt.stem(x,y)
plt.xlabel("X")
plt.ylabel("Y")
plt.title("STEM")
plt.show()
