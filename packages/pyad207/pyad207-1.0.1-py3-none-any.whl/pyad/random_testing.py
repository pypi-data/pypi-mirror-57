import reverse_mode as rev
import numpy as np
import matplotlib.pyplot as plt

x = rev.Tensor(0.5)
y = rev.Tensor(4.2)
z = rev.Tensor(3)
f = x * y**3 + rev.sin(x) - rev.logistic(z)

#set df seed
f.backward()

rev_g = rev.rev_graph()
plot = rev_g.plot_graph([x,y,z])

plt.show()