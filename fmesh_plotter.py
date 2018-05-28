import numpy as np
import matplotlib.pyplot as plt


###############################################################################
# User Defined Parameters
height_index = 8

###############################################################################
# Problem Defined Parameters
filename = 'meshtal'
xints = 120
yints = 120
zints = 40
###############################################################################


# load in data
data = np.loadtxt(filename, skiprows=15)

# unpack data
data = data.T
x = data[1]
y = data[2]
z = data[3]
d = data[7]

xpoints = np.sort(np.array(list(set(x))))

max_dose = max(d)

data_vert = np.array([x, y, z, d])
data_vert = data_vert.T
data = data_vert.reshape(xints, yints, zints, -1)

cross = data[:, :, height_index, -1]

# linear plot
fig = plt.figure(1)
ax = fig.add_subplot(111)
dose_x = cross[int(xints/2)]
ax.plot(xpoints, dose_x, 'k')
ax.set_yscale('log')
ax.set_xlabel('Position (cm)')
ax.set_ylabel('Dose (mr/hr)')
ax.set_title('Dose {} cm from floor'.format(z[height_index] + 70))
