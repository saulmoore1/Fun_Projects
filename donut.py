#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Tutorial -- Donut Screensaver

@author: sm5911
@date: 24/04/2023

"""

#%% Imports


import numpy as np
# from scipy.spatial import

#%% Globals

theta_spacing = 0.07
phi_spacing = 0.02
R1 = 1
R2 = 2
K2 = 5
K1 = screen_width * K2 * 3 / (8 * (R1 + R2))


#%% Functions

def render_frame(A, B):
    assert type(A) == float and type(B) == float
    
    cosA, sinA = np.cos(A), np.sin(A)
    cosB, sinB = np.cos(B), np.sin(B)
    
    return

def main():
    
    render_frame(A, B)
    
    return

#%% Main

if __name__ == '__main__':
    main()