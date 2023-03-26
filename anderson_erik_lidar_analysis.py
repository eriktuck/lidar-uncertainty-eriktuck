#!/usr/bin/env python
# coding: utf-8

# LiDAR vs Insitu Tree Height Comparison
# This notebook compares tree height measurements for two NEON sites: the SJER and SOAP sites.

import os
import pathlib

import earthpy as et
import lidar_functions as lf

# Download data from the Earth Py library
et.data.get_data('spatial-vector-lidar')

# Set working directory
home_dir = os.path.join(
    pathlib.Path.home(),
    'earth-analytics',
    'data',
    'spatial-vector-lidar'
)

os.chdir(home_dir)

# Define paths to data
# SJER site
sjer_base_dir = os.path.join(
    'california',
    'neon-sjer-site'
)

sjer_insitu_path = os.path.join(
    sjer_base_dir,
    '2013',
    'insitu',
    'veg_structure',
    'D17_2013_SJER_vegStr.csv'
)

sjer_plots_path = os.path.join(
    sjer_base_dir,
    'vector_data',
    'SJER_plot_centroids.shp'
)

sjer_chm_path = os.path.join(
    sjer_base_dir,
    '2013',
    'lidar',
    'SJER_lidarCHM.tif'
)

sjer_plots_path = os.path.join(
    sjer_base_dir,
    'vector_data',
    'SJER_plot_centroids.shp'
)

# Soap site
soap_base_dir = os.path.join(
    'california',
    'neon-soap-site'
)

soap_insitu_path = os.path.join(
    soap_base_dir,
    '2013',
    'insitu',
    'veg-structure',
    'D17_2013_SOAP_vegStr.csv'
)

soap_plots_path = os.path.join(
    soap_base_dir,
    'vector_data',
    'SOAP_centroids.shp'
)

soap_chm_path = os.path.join(
    soap_base_dir,
    '2013',
    'lidar',
    'SOAP_lidarCHM.tif'
)

soap_plots_path = os.path.join(
    soap_base_dir,
    'vector_data',
    'SOAP_centroids.shp'
)

# Calculate and plot SOAP site
soap_df = lf.calc_height_stats(soap_plots_path, soap_chm_path, soap_insitu_path,
                  id_col="ID", prepend_string="SOAP")
lf.plot_comparison(soap_df)

# Calculate and plot SJER site
sjer_df = lf.calc_height_stats(sjer_plots_path, sjer_chm_path, sjer_insitu_path)
lf.plot_comparison(sjer_df)
