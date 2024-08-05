import os
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
from shapely.geometry import mapping
import geopandas as gpd
import rasterio as rio
from rasterio.plot import plotting_extent
from rasterio.mask import mask
import earthpy as et
import earthpy.spatial as es
import earthpy.plot as ep
import geojson, gdal, subprocess 
with open('D:/qqq.geojson', 'w') as f:
    geojson.dump(data, f)

args = ['ogr2ogr', '-f', 'ESRI Shapefile', 'qqq.shp', 'qqq.geojson']
subprocess.Popen(args)
# Prettier plotting with seaborn
sns.set(font_scale=1.5)