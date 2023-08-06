import reverse_mode as rev
import matplotlib.pyplot as plt

x = rev.Tensor(3)
y = rev.Tensor(2)

f = x * y**3 + x / 3

f.backward()

graph_obj = rev.rev_graph()
plot = graph_obj.plot_graph([x, y])

plt.show()