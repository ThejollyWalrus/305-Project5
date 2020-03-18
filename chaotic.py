#Mason Hamilton & Dylan Nasser
#CST-305-3:20
#Professor Ricardo Citro
#3/17/2020
#Chaotic ODE


#Import libraries used below
import numpy as np
import matplotlib.pyplot as plt
# This import registers the 3D projection, but is otherwise unused.
from mpl_toolkits.mplot3d import Axes3D  # noqa: F401 unused import



#Main defination used to create chaotic model
def Chaotic(x, y, z, t =100, r=28, b=2.33):
    '''
    Given:
       x, y, z: a point of interest in three dimensional space
       t, r, b: parameters defining the lorenz attractor
    Returns:
       x_dot, y_dot, z_dot: values of the lorenz attractor's partial
           derivatives at the point x, y, z
    '''
    Xdot = t * (y- x)
    Ydot = r * x + y - x * z
    Zdot = x * y - b * z
    return Xdot, Ydot, Zdot


dt = 0.01
count = 10000

# Need one more for the initial values

xs = np.empty(count + 1)
ys = np.empty(count + 1)
zs = np.empty(count + 1)

# Set initial values
xs[0], ys[0], zs[0] = (0., 1., 1.05)

# Step through "time", calculating the partial derivatives at the current point
# and using them to estimate the next point
for i in range(count):
    Xdot, Ydot, Zdot = Chaotic(xs[i], ys[i], zs[i])
    xs[i + 1] = xs[i] + (Xdot * dt)
    ys[i + 1] = ys[i] + (Ydot * dt)
    zs[i + 1] = zs[i] + (Zdot * dt)

# Plot
fig = plt.figure()
np = fig.gca(projection='3d')
np.plot(xs, ys, zs, lw=0.4)
np.set_xlabel("X-Axis")
np.set_ylabel("Y-Axis")
np.set_zlabel("Z-Axis")
np.set_title("Chaotic Model")

plt.show()

