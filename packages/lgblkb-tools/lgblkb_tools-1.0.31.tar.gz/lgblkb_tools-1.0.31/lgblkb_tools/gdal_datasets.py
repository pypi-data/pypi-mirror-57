import logging
import os
import uuid

import matplotlib.pyplot as plt
import numpy as np
from osgeo import gdal,gdal_array,ogr,osr

from . import logger
from . import pathify

gdal.UseExceptions()

def ds_to_array(ds,band_index=1):
	if isinstance(ds,str): ds=gdal.Open(ds)
	return ds.GetRasterBand(band_index).ReadAsArray(0,0,ds.RasterXSize,ds.RasterYSize)

geom_from_ds=lambda ds:np.abs(np.array(ds.GetGeoTransform()).reshape(2,-1))
resol_from_ds=lambda ds:geom_from_ds(ds)[:,1:].sum(axis=0)
ul_from_ds=lambda ds:geom_from_ds(ds)[:,0]

get_epsg_from=lambda ds:int(
	gdal.Info(ds,format='json')['coordinateSystem']['wkt'].rsplit('"EPSG","',1)[-1].split('"')[0])

def plot_ds(ds,show=False):
	array=ds_to_array(ds)
	plt.imshow(array)
	if show: plt.show()

code_lut={v:k for k,v in gdal_array.codes.items()}

def array_to_ds(array,parent_info):
	try:
		arr_ds=gdal_array.OpenNumPyArray(array,True)
	except:
		arr_ds=gdal_array.OpenNumPyArray(array)
	if isinstance(parent_info,DataSet): parent_info=parent_info.ds
	if isinstance(parent_info,gdal.Dataset):
		transform=parent_info.GetGeoTransform()
		projection=parent_info.GetProjection()
	else:
		transform,projection=parent_info
	arr_ds.SetGeoTransform(transform)
	arr_ds.SetProjection(projection)
	return arr_ds

def get_datasource(driver_name,fpath,field_name,field_type):
	dest_datasource=ogr.GetDriverByName(driver_name).CreateDataSource(fpath)
	dest_layer=dest_datasource.CreateLayer('',srs=None)
	dest_layer.CreateField(ogr.FieldDefn(field_name,field_type))
	return dest_datasource,dest_layer

@logger.trace()
def polygonize(ds,driver_name,fpath,field_name='DN',field_type=ogr.OFTInteger):
	dest_datasource,dest_layer=get_datasource(driver_name,fpath,field_name,field_type)
	if field_type is ogr.OFTReal: polygonizer=gdal.FPolygonize
	else: polygonizer=gdal.Polygonize
	polygonizer(ds.GetRasterBand(1),None,dest_layer,0,['8connected=8'],callback=None)
	return dest_datasource,dest_layer

def contour_generate(ds,val_ranges,driver_name,fpath,field_name,field_type):
	contour_dsrc,contour_layer=get_datasource(driver_name,fpath,field_name,field_type)
	gdal.ContourGenerate(ds.GetRasterBand(1),0,0,val_ranges,0,0,contour_layer,0,0)
	return contour_dsrc,contour_layer

#todo:Cropping dataset
class DataSet:

	def __init__(self,ds,array=None,name=''):
		if isinstance(ds,str):
			name=name or '_'.join(pathify.get_splitted(os.path.splitext(ds)[0])[-2:])
			ds=gdal.Open(ds)
		self.ds=ds
		geom=geom_from_ds(self.ds)
		self.resol=geom[:,1:].sum(axis=0)
		self.ul=geom[:,0]
		self.__array=array
		self.projection=self.ds.GetProjection()
		self.transform=self.ds.GetGeoTransform()
		self.name=name

	@logger.trace(level=logging.DEBUG,skimpy=True)
	def generate_array(self):
		self.__array=ds_to_array(self.ds)
		return self

	@property
	def array(self):
		if self.__array is None:
			self.generate_array()
		return self.__array

	@property
	def epsg(self):
		return get_epsg_from(self.ds)

	def plot(self,show=False):
		return plot_ds(self.ds,show=show)

	@logger.trace()
	def reproject(self,to_epsg):
		"""
		A sample function to reproject and resample a GDAL dataset from within
		Python. The idea here is to reproject from one system to another, as well
		as to change the pixel size. The procedure is slightly long-winded, but
		goes like this:

		1. Set up the two Spatial Reference systems.
		2. Open the original dataset, and get the geotransform
		3. Calculate bounds of new geotransform by projecting the UL corners
		4. Calculate the number of pixels with the new projection & spacing
		5. Create an in-memory raster dataset
		6. Perform the projection
		"""
		# Define the UK OSNG, see <http://spatialreference.org/ref/epsg/27700/>
		osng=osr.SpatialReference()
		osng.ImportFromEPSG(to_epsg)
		wgs84=osr.SpatialReference()
		wgs84.ImportFromEPSG(get_epsg_from(self.ds))
		tx=osr.CoordinateTransformation(wgs84,osng)
		# Up to here, all  the projection have been defined, as well as a
		# transformation from the from to the  to :)
		# We now open the dataset
		# Get the Geotransform vector
		geo_t=self.ds.GetGeoTransform()
		x_size,y_size=self.raster_sizes
		# Work out the boundaries of the new dataset in the target projection
		(ulx,uly,ulz)=tx.TransformPoint(geo_t[0],geo_t[3])
		(lrx,lry,lrz)=tx.TransformPoint(geo_t[0]+geo_t[1]*x_size,geo_t[3]+geo_t[5]*y_size)
		# See how using 27700 and WGS84 introduces a z-value!
		# Now, we create an in-memory raster
		mem_drv=gdal.GetDriverByName('MEM')
		# The size of the raster is given the new projection and pixel spacing
		# Using the values we calculated above. Also, setting it to store one band
		# and to use Float32 data type.
		#dest=mem_drv.Create('',int((lrx-ulx)/x_size),int((uly-lry)/y_size),1,gdal.GDT_Float32)
		dtype=np.typeDict[str(self.array.dtype)]
		dest=mem_drv.Create('',x_size,y_size,1,code_lut[dtype])
		#dest=mem_drv.Create('',pixel_x_size,pixel_y_size,1,gdal.GDT_Float32)
		# Calculate the new geotransform
		resol=self.resol
		new_geo=(ulx,resol[0],geo_t[2],uly,geo_t[4],-resol[1])
		# Perform the projection/resampling
		# Set the geotransform
		dest.SetGeoTransform(new_geo)
		dest.SetProjection(osng.ExportToWkt())
		gdal.ReprojectImage(self.ds,dest,wgs84.ExportToWkt(),osng.ExportToWkt(),gdal.GRA_Bilinear)
		#gdal.ReprojectImage(self.ds,dest,wgs84.ExportToWkt(),osng.ExportToWkt())
		return DataSet(dest)

	@logger.trace(level=logging.DEBUG,skimpy=True)
	def do_warp(self,cutline_json=None,destroy_after=True,out_epsg=4326,**kwargs):
		temp_filepath=f"/vsimem/{uuid.uuid4()}"

		gdal.Warp(temp_filepath,self.ds,
		          cropToCutline=not cutline_json is None,srcSRS=f'EPSG:{self.epsg}',dstSRS=f'EPSG:{out_epsg}',
		          cutlineDSName=cutline_json,**dict(dict(),**kwargs))
		ds=DataSet(temp_filepath)
		# cropped_ds=gdal.Warp('',self.ds,format='VRT',cropToCutline=cropToCutline,cutlineDSName=cutline_json,**kwargs)
		if destroy_after: self.ds=None
		return ds

	@property
	def geo_info(self):
		return self.transform,self.projection

	@property
	def raster_sizes(self):
		return self.ds.RasterXSize,self.ds.RasterYSize

	@classmethod
	def from_array(cls,array,geo_info):
		if isinstance(geo_info,str): geo_info=DataSet(geo_info)
		return DataSet(array_to_ds(array,geo_info),array)

	@logger.trace()
	def polygonize(self,driver_name,fpath,destroy_after=True,**kwargs):
		datasource,ds_layer=polygonize(self.ds,driver_name,fpath,**kwargs)
		if not 'mem' in driver_name.lower():
			ds_layer=None
			datasource=None
		if destroy_after: self.ds=None
		return datasource,ds_layer

	@logger.trace()
	def generate_contours(self,val_ranges,driver_name,fpath,field_name='DN',
	                      field_type=ogr.OFTReal,destroy_after=True):
		datasource,ds_layer=contour_generate(ds=self.ds,val_ranges=val_ranges,
		                                     driver_name=driver_name,fpath=fpath,
		                                     field_name=field_name,field_type=field_type)
		if not 'mem' in driver_name.lower():
			ds_layer=None
			datasource=None
		if destroy_after: self.ds=None
		return datasource,ds_layer

	@logger.trace()
	def to_geotiff(self,filepath,no_data_value=-9999,dtype=gdal.GDT_Float32):
		band=self.ds.GetRasterBand(1)
		arr=band.ReadAsArray()
		[cols,rows]=arr.shape
		driver=gdal.GetDriverByName("GTiff")
		outdata=driver.Create(filepath,rows,cols,1,dtype)
		outdata.SetGeoTransform(self.transform)  ##sets same geotransform as input
		outdata.SetProjection(self.projection)  ##sets same projection as input
		outdata.GetRasterBand(1).WriteArray(np.where(np.isnan(arr),no_data_value,arr))
		if no_data_value is not False:
			outdata.GetRasterBand(1).SetNoDataValue(no_data_value)  ##if you want these values transparent
		outdata.FlushCache()  ##saves to disk!!
		outdata=None
		band=None
		ds=None

	def scale_array(self,scaler):
		scaled=scaler.fit_transform(self.array.reshape(-1,1))
		scaled_band=scaled.reshape(self.array.shape)
		out=self.from_array(scaled_band,self.geo_info)
		self.ds=None
		return out

@logger.trace(level=logging.DEBUG)
def translate_tiff(input_tiff,output_tiff,translate_opts: gdal.TranslateOptions) -> str:
	ds=gdal.Open(input_tiff)
	ds=gdal.Translate(output_tiff,ds,options=translate_opts)
	ds=None
	return output_tiff

@logger.trace(level=logging.DEBUG)
def rgb_to_geotiff(tiff_path,*band_paths,no_data_value=-9999,dtype=gdal.GDT_Float32,**warp_opts):
	# logsup.logger.info('no_data_value: %s',no_data_value)
	band_dss=[DataSet(path).do_warp(**warp_opts).generate_array() for path in band_paths]
	band_arrays=[band_ds.array for band_ds in band_dss]
	# for path in band_paths:
	# 	step1=DataSet(path).do_warp(out_epsg=3857,srcNodata=-2000)  #
	# 	step3=step1.scale_array(RobustScaler()).scale_array(MinMaxScaler((0,255))).array
	# 	band_arrays.append(step3)
	# band_arrays=[_get_image_prepared_array(path,warp_opts=dict(out_epsg=3857),scaler=MinMaxScaler((0,255))) for path in band_paths]
	# band_arrays=gsup.ParallelTasker(_get_image_prepared_array,scaler=MinMaxScaler((0,255))).set_run_params(ds=band_paths).run(sleep_time=1e-1)
	# band_arrays=gsup.ParallelTasker(ds_to_array).set_run_params(ds=band_paths).run(sleep_time=1e-1)
	[cols,rows]=band_arrays[0].shape
	driver=gdal.GetDriverByName("GTiff")
	if len(band_paths)==3:
		options=['PHOTOMETRIC=RGB','PROFILE=GeoTIFF',]
	else:
		options=None
	# elif len(band_paths)==4:
	# 	options=['PHOTOMETRIC=RGBA','PROFILE=GeoTIFF',]
	# else:
	# 	raise NotImplementedError(f'Invalid number of input files - {len(band_paths)}.',dict(count=len(band_paths)))

	outdata=driver.Create(tiff_path,rows,cols,len(band_paths),dtype,options=options)
	outdata.SetGeoTransform(band_dss[0].transform)  ##sets same geotransform as input
	outdata.SetProjection(band_dss[0].projection)  ##sets same projection as input
	for i,(array,band_interpretation) in\
			enumerate(zip(band_arrays,[gdal.GCI_RedBand,gdal.GCI_GreenBand,gdal.GCI_BlueBand])):
		raster_band=outdata.GetRasterBand(i+1)
		raster_band.SetColorInterpretation(band_interpretation)
		raster_band.WriteArray(np.where(array==0,no_data_value,array))
		if no_data_value is not False:
			raster_band.SetNoDataValue(no_data_value)  ##if you want these values transparent

	outdata.FlushCache()  ##saves to disk!!
	outdata=None
	band=None
	ds=None
	pass

def get_mean_std_scale_params(stack: np.array,std_num=2):
	mean=np.nanmean(stack)
	std=np.nanstd(stack)
	return [mean-std_num*std,mean+std_num*std]
