import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D


###############################################################################
# User Defined Parameters
filename = 'senior_design_mesh.imsht'
xints = 60
yints = 60
zints = 20
###############################################################################


# load in data
data = np.loadtxt(filename, skiprows=15)

# unpack data
data = data.T
x = data[1]
y = data[2]
z = data[3]
d = data[7]

max_dose = max(d)

data_vert = np.array([x, y, z, d])
data_vert = data_vert.T
data = data_vert.reshape(xints, yints, zints, -1)
























###############################################################################
# 3d plotting

if False:
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')
    for point in data_vert[:2000]:
        xp, yp, zp, dp = point
        print('>> Plotting {}, {}, {}'.format(xp, yp, zp), end='\r', flush=True)
        ax.scatter(xp, yp, zp, color='k', depthshade=False, alpha=dp/max_dose)
    plt.show()
