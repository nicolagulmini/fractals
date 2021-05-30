import numpy as np
import matplotlib.pyplot as plt
import math

# rotation matrix
def rotationMatrix(theta): 
    return np.array([[np.cos(theta), -np.sin(theta)], [np.sin(theta), np.cos(theta)]])

# return a vector that starts from (0,0) and arrives in B-A
def to_origin(a, b): 
    return np.array([b[0]-a[0], b[1]-a[1]])

def to_a(c, a):
    return np.array([c[0]+a[0], c[1]+a[1]])

# convex combination: lambda must be between 0 and 1
def convex_comb(a, b, lamb):
    return np.array([lamb*a[0]+(1-lamb)*b[0], lamb*a[1]+(1-lamb)*b[1]])

# rotate the segment ab of theta radiants
def change_dir(a, b, theta):
    return to_a(np.inner(rotationMatrix(theta), to_origin(a, b)), a)
    
def polyline(a, b, lambdas, thetas):
    n = len(lambdas)
    x_ax = []
    y_ax = []
    for i in range(n):
        c = change_dir(a, convex_comb(a, b, lambdas[i]), thetas[i])
        x_ax.append(c[0])
        y_ax.append(c[1])
    return [x_ax, y_ax] # returns only the internal points

def to_plot_polyline(a, b, p): 
    x_ax = [a[0]]
    y_ax = [a[1]]
    p_x = p[0]
    p_y = p[1]
    for i in range(len(p_x)):
        x_ax.append(p_x[i])
        y_ax.append(p_y[i])
    x_ax.append(b[0])
    y_ax.append(b[1])
    return [x_ax, y_ax]
    
def k_frac(a, b, lambdas, thetas, k):
    p = polyline(a, b, lambdas, thetas)
    if k == 1:
        return p
    px = p[0]
    py = p[1]
    first = [px[0], py[0]]
    q = k_frac(a, first, lambdas, thetas, k-1)
    x_ax = q[0]
    y_ax = q[1]
    for i in range(len(px)-1):
        x_ax.append(px[i])
        y_ax.append(py[i])
        c_i = [px[i], py[i]]
        c_i1 = [px[i+1], py[i+1]]
        q = k_frac(c_i, c_i1, lambdas, thetas, k-1)
        x_ax = x_ax + q[0]
        y_ax = y_ax + q[1]
    x_ax.append(px[len(px)-1])
    y_ax.append(py[len(px)-1])
    last = [px[len(px)-1], py[len(py)-1]]
    q = k_frac(last, b, lambdas, thetas, k-1)
    x_ax = x_ax + q[0]
    y_ax = y_ax + q[1]
    return [x_ax, y_ax]
    

'''
k = 5

a = [0, 0]
b = [6, 0]
lambdas = [2/3, 1-math.sqrt(2)/3, 1-math.sqrt(5)/3, 1/3]
thetas = [0, np.pi/4, 0.463647609, 0]
p = k_frac(a, b, lambdas, thetas, k)
q = to_plot_polyline(a, b, p)

plt.plot(q[0], q[1], linewidth=.5)
plt.savefig('first.png', dpi=300)
plt.show()


a = [0, 0]
b = [6, 0]
lambdas = [2/3, 1-math.sqrt(2)/2, 1/3]
thetas = [0, np.pi/4, 0]
p = k_frac(a, b, lambdas, thetas, 8)
q = to_plot_polyline(a, b, p)

plt.plot(q[0], q[1], linewidth=.5)
plt.savefig('second.png', dpi=300)
plt.show()
'''

a = [0, 0]
b = [6, 0]
lambdas = [2/3, 1-math.sqrt(2)/2, 1/3]
thetas = [0, 0.9*np.pi/4, 0]
p = k_frac(a, b, lambdas, thetas, 6)
q = to_plot_polyline(a, b, p)

plt.plot(q[0], q[1], linewidth=.5)
plt.show()