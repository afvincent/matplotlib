"""
Demo of bar plot on a polar axis.

NB: the geometry is copied from the matplotlib logo example
available at http://matplotlib.org/examples/api/logo2.html
"""
import numpy as np
import matplotlib.pyplot as plt


N = 7
theta = np.linspace(0.0, 2 * np.pi, N, endpoint=False)
radii = 10 * np.array([0.2, 0.6, 0.8, 0.7, 0.4, 0.5, 0.8])
width = np.pi / 4 * np.array([0.4, 0.4, 0.6, 0.8, 0.2, 0.5, 0.3])

ax = plt.subplot(111, projection='polar')
bars = ax.bar(theta, radii, width=width, bottom=0.0)

# Use custom colors and opacity
for r, bar in zip(radii, bars):
    bar.set_facecolor(plt.cm.viridis(r / 10.))  # the real logo uses `jet`
    bar.set_alpha(0.5)

ax.set_rmax(radii.max() + 1)  # adjust maximal `r` to not touch the outer edge

plt.show()
