import matplotlib.pyplot as plt
import numpy as np

t=np.arange(0,5,0.2)
x=np.linspace(0,2*np.pi, 100)
y=np.sin(x)
plt.plot(x, y, 'r--', x, (x**2)/100, 'bs')
plt.show()
