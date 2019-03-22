import logging
log = logging.getLogger(__name__)

#GDAL
try:
	from osgeo import gdal
except:
	HAS_GDAL = False
else:
	HAS_GDAL = True


#PyProj
try:
	import pyproj
except:
	HAS_PYPROJ = False
else:
	HAS_PYPROJ = True


#PIL/Pillow
try:
	from PIL import Image
except:
	HAS_PIL = False
else:
	HAS_PIL = True


#Imageio freeimage plugin
try:
	from .lib import imageio
	imageio.plugins._freeimage.get_freeimage_lib() #try to download freeimage lib
except Exception as e:
	log.error("Cannot install ImageIO's Freeimage plugin", exc_info=True)
	HAS_IMGIO = False
else:
	HAS_IMGIO = True
