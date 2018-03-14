# -*- coding: utf-8 -*-
"""
Created on Wed Mar 14 10:23:43 2018

@author: Administrator
"""

import numpy as np
import matplotlib.pyplot as plt
X = np.linspace(-np.pi, np.pi, 256,endpoint=True)
C,S = np.cos(X), np.sin(X)
plot(X,C)
plot(X,S)
show()