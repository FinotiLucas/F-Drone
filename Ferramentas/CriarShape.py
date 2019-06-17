path='/home/rikl/Dokumente/Python/shapefile/customer_points.shp'
import osgeo.ogr, osgeo.osr #we will need some packages
from osgeo import ogr #and one more for the creation of a new field

spatialReference = osgeo.osr.SpatialReference() #will create a spatial reference locally to tell the system what the reference will be
spatialReference.ImportFromProj4('+proj=utm +zone=48N +ellps=WGS84 +datum=WGS84 +units=m') #here we define this reference to be utm Zone 48N with wgs84...

driver = osgeo.ogr.GetDriverByName('ESRI Shapefile') # will select the driver foir our shp-file creation.
shapeData = driver.CreateDataSource(path) #so there we will store our data
layer = shapeData.CreateLayer('customs', spatialReference, osgeo.ogr.wkbPoint) #this will create a corresponding layer for our data with given spatial information.
layer_defn = layer.GetLayerDefn() # gets parameters of the current shapefile
point = osgeo.ogr.Geometry(osgeo.ogr.wkbPoint)
point.AddPoint(474695, 5429281) #create a new point at given ccordinates
featureIndex = 0 #this will be the first point in our dataset

##now lets write this into our layer/shape file:
feature = osgeo.ogr.Feature(layer_defn)
feature.SetGeometry(point)
feature.SetFID(featureIndex)
layer.CreateFeature(feature)

## lets add now a second point with different coordinates:
point.AddPoint(474598, 5429281)
featureIndex = 1
feature = osgeo.ogr.Feature(layer_defn)
feature.SetGeometry(point)
feature.SetFID(featureIndex)
layer.CreateFeature(feature)
shapeData.Destroy() #lets close the shapefile

shapeData = ogr.Open(path, 1)
layer = shapeData.GetLayer() #get possible layers.
layer_defn = layer.GetLayerDefn() #get definitions of the layer

field_names = [layer_defn.GetFieldDefn(i).GetName() for i in range(layer_defn.GetFieldCount())] #store the field names as a list of strings
print (len(field_names))# so there should be just one at the moment called "FID"
field_names #will show you the current field names

field_names = [layer_defn.GetFieldDefn(i).GetName() for i in range(layer_defn.GetFieldCount())] #store the field names as a list of strings
print (len(field_names))# so there should be just one at the moment called "FID"
field_names #will show you the current field names

new_field = ogr.FieldDefn('HOMETOWN', ogr.OFTString) #we will create a new field called Hometown as String
layer.CreateField(new_field) #self explaining
new_field = ogr.FieldDefn('VISITS', ogr.OFTInteger) #and a second field 'VISITS' stored as integer
layer.CreateField(new_field) #self explaining
field_names = [layer_defn.GetFieldDefn(i).GetName() for i in range(layer_defn.GetFieldCount())]
field_names #WOOHAA!

feature = layer.GetFeature(0) #lets get the first feature (FID=='0')
i = feature.GetFieldIndex("HOMETOWN") #so iterate along the field-names and store it in iIndex
feature.SetField(i, 'Chicago') #exactly at this position I would like to write 'Chicago'
layer.SetFeature(feature) #now make the change permanent
feature = layer.GetFeature(1)
i = feature.GetFieldIndex("HOMETOWN")
feature.SetField(i, 'Berlin')
layer.SetFeature(feature)
shapeData = None #lets close the shape file again.