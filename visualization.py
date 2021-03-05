#!/usr/bin/env python
# -*- coding: utf-8 -*-

import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.axes_grid1 import make_axes_locatable

def main(args):
    # Get the arguments from the parse
    gt_filename = './Results/S2P/truthGrid.npy'
    s2p_filename = './Results/S2P/solutionPostImg.npy'
    mccnn_filename = './Results/S2P-MCCNN-LAF/solutionPostImg.npy'
    
    # Load the data
    gt_dem = np.load(gt_filename)
    s2p_dem = np.load(s2p_filename)
    mccnn_dem = np.load(mccnn_filename)
    
    dem_max = np.max(gt_dem)
    dem_min = np.min(gt_dem)
    
    # Plot the image
    fig = plt.figure(figsize=(16, 12))
    ax1 = fig.add_subplot(131)
    im1 = ax1.imshow(gt_dem, cmap='jet', interpolation='None',vmax=dem_max,vmin=dem_min)
    plt.title('Groundtruth')
    divider = make_axes_locatable(ax1)
    cax = divider.append_axes('right', size='5%', pad=0.05)
    fig.colorbar(im1, cax=cax, orientation='vertical')
    ax2 = fig.add_subplot(132,sharex=ax1,sharey=ax1)
    im2 = ax2.imshow(s2p_dem, cmap='jet', interpolation='None',vmax=dem_max,vmin=dem_min)
    plt.title('S2P')
    divider = make_axes_locatable(ax2)
    cax = divider.append_axes('right', size='5%', pad=0.05)
    fig.colorbar(im2, cax=cax, orientation='vertical')
    ax3 = fig.add_subplot(133,sharex=ax1,sharey=ax1)
    im3 = ax3.imshow(mccnn_dem, cmap='jet', interpolation='None',vmax=dem_max,vmin=dem_min)
    plt.title('S2P-MCCNN-Filt-LAFNet')
    divider = make_axes_locatable(ax3)
    cax = divider.append_axes('right', size='5%', pad=0.05)
    fig.colorbar(im3, cax=cax, orientation='vertical')
     
    plt.show()
    
    return 0
if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))
