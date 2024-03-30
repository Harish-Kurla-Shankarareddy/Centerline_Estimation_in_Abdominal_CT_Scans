# -*- coding: utf-8 -*-
"""
Created on Thu Sep 21 17:32:36 2023

@author: HARISH
"""
import numpy as np
import matplotlib.pyplot as plt
import nibabel as nb
from skimage.morphology import skeletonize_3d
import sknw
import networkx as nx
from scipy import interpolate
import time
from scipy import ndimage
import rdp as rdp
from mpl_toolkits.mplot3d import Axes3D  # Import Axes3D for 3D projection
import open3d as od
from scipy.signal import savgol_filter
import pandas as pd


colon_image =  r'/Users/HARISH/Desktop/Internship/Newdata/airway.nii'
img = nb.load(colon_image)
data = img.get_fdata()
shape = data.shape
skel = skeletonize_3d(data)



graph = sknw.build_sknw(skel,multi=False, iso=False, ring=False, full=True)
allways = []
for i,j in graph.edges():
    edge_path = graph[i][j]['pts']
    # Get the starting and ending nodes of the edge
    start_node = np.array([graph.nodes[i]['o']])
    end_node = np.array([graph.nodes[j]['o']])
    combined_path = np.vstack((start_node, edge_path, end_node))
    
    allways.append(combined_path)
    
    
fig = plt.figure()
ax = fig.add_subplot(111)
for i in range(len(allways)):
    ax.plot(allways[i][:, 0], allways[i][:, 1])



skelindices = np.where(skel==255)
fig = plt.figure()
ax = fig.add_subplot(111,projection='3d')

lines = []
labels = []
smoothed_paths = []
for i in range(len(allways)):
    
    if np.shape(allways[i])[0]<=10:
        window_length = np.shape(allways[i])[0]
    else:
        window_length = 10
    print(window_length)
    line1, = ax.plot(allways[i][:, 0], allways[i][:, 1], allways[i][:, 2], linewidth=3, color='tab:blue')
    
    smooth_path = savgol_filter(allways[i], window_length=window_length, polyorder=2, axis=0)
    print(smooth_path)
    # Append the smoothed path to the list
    smoothed_paths.append(np.array(smooth_path))
    line2, = ax.plot(smooth_path[:,0], smooth_path[:, 1], smooth_path[:, 2], linewidth=1, color='red')

print(smooth_path)


