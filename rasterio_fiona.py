import fiona
import rasterio
import rasterio.mask


with fiona.open("D:/county.shp", "r") as shapefile:
    shapes = [feature["geometry"] for feature in shapefile]
with rasterio.open("D:/KM003320MI_010_MUL_L1T.tif") as src:
    out_image, out_transform = rasterio.mask.mask(src, shapes, crop=True)
    out_meta = src.meta
out_meta.update({"driver": "GTiff",
                 "height": out_image.shape[1],
                 "width": out_image.shape[2],
                 "transform": out_transform})

with rasterio.open("test.tif", "w", **out_meta) as dest:
    dest.write(out_image)