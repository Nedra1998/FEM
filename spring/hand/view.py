#!/usr/bin/env python3

import matplotlib.pyplot as plt
import numpy as np

c1 = np.loadtxt("CASE_1.txt")
c2 = np.loadtxt("CASE_2.txt")
plt.imsave("CASE_1.png", c1, vmin=0, vmax=4.5, origin='lower', cmap='jet')
plt.imsave("CASE_1b.png", c1, vmin=0, origin='lower', cmap='jet')
plt.imsave("CASE_2.png", c2, vmin=0, vmax=4.5, origin='lower', cmap='jet')
plt.imsave("CASE_2b.png", np.rot90(np.rot90(c2)), vmin=0, origin='lower', cmap='jet_r')
