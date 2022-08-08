import math
from tabulate import tabulate

def f(x):
    return x - math.cos(x)**2

def derivative(x):
    return 1 + 2*math.cos(x)*math.sin(x)

INITIAL_X = 0.5

rows = []
x_s = []
for k in range(1, 5):
    if k == 1:
        x = INITIAL_X
        x_s.append(x)
        rows.append([k, x, f(x), derivative(x), "--"])
    else:
        x = x - (f(x) / derivative(x))
        x_s.append(x)
        rows.append([k, x, f(x), derivative(x), (x_s[k-2] - x_s[k-1])/x_s[k-1]])

print(tabulate(rows, headers=['k', 'x', 'f(x)', "f'(x)", "e"]))


