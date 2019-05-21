import matplotlib.pyplot as plt
import numpy as np

x=np.array(range(30))
y=np.array(range(30))

y=np.sin(x/30*np.pi*2)

plt.plot(x,y,'r')
plt.show()
