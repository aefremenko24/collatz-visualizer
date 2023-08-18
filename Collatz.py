import time
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from matplotlib import style

def run():
  open('data.txt', 'w').close()
  ani = animation.FuncAnimation(fig, animate, interval=20)
  plt.show()

def animate(i):
  graph_data = open('data.txt', 'r').read()

  global iteration, n, current

  lines = graph_data.split('\n')
  xs = []
  ys = []
  for line in lines:
    if len(line) > 1:
      x, y = line.split(',')
      xs.append(float(x))
      ys.append(float(y))
  ax1.clear()
  ax1.plot(xs, ys, 'o-')
  ax1.set_facecolor("#4D4C5C")
  ax1.grid(color='#3F3E4A', linestyle='-', linewidth=2)
  ax1.set_title('Current number: {}'.format(current))
  ax1.set_xlim(0, max(iteration, 5))
  ax1.set_xlabel('Iteration')
  ax1.set_ylabel('Value')

  if n != 1:
    with open('data.txt', 'a') as f:
      f.write('\n' + '{},{}'.format(iteration, n))
    iteration += 1
    n = next_num(n)

  else:
    time.sleep(1)
    iteration = 0
    current += 1
    ax1.clear()
    n = current
    with open('data.txt', 'w') as f:
      f.write('{},{}'.format(0, current))

def next_num(n):
  if n % 2 == 0:
    return n / 2
  else:
    return 3 * n + 1

current = 26
iteration = 0
n = current

style.use('dark_background')
fig = plt.figure(facecolor='#4D4C5C')
ax1 = fig.add_subplot(1,1,1)

run()