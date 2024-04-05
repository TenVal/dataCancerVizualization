import numpy as np
import matplotlib.pyplot as plt

vT = [0,
      0.11,
      0.22,
      0.33,
      0.44,
      0.55,
      0.66,
      0.77,
      0.88,
      0.99,
      1.10]

vV = [1e-06,
      1e-06,
      1.10019e-06,
      1.23794e-06,
      3.98768e-04,
      2.14332e-03,
      4.14332e-02,
      8.56348e-01,
      1.32562e+0,
      2.21064e+0,
      2.22064e+0, ]


def y1Func(x):
    return 3.8251 * x * x - 2.0856 * x + 0.1324


def y2Func(x):
    return 0.5723 * x * x * x + 2.8809 * x * x - 1.6896 * x + 0.1049


x1 = []
y1 = []
x2 = []
y2 = []
x3 = []
y3 = []


def frange(start, stop, step):
    i = start
    while i < stop:
        yield i
        i += step


for i in frange(0, 2, 0.1):
    x1.append(i)
    y1.append(y1Func(i))
    x2.append(i)
    y2.append(y1Func(i))

plt.plot(x1, y1)
plt.plot(x2, y2)
plt.xlim(-1, 4)
plt.ylim (-1, 10)
plt.xlabel("u1")
plt.ylabel("u2")
plt.title("bd")
plt.grid(True)
plt.axis('equal')
plt.show()