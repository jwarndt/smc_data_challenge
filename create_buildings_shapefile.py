import csv

from osgeo import ogr
import osgeo.osr as osr
import numpy as np

def buildings_csv_to_shapefile(input_filename, output_filename):
    """
    Parameters:
    ------------
    input_filename: string
        the input csv that contains coordinates and attributes for
        the buildings
    output_filename: string
        the output name of the shapefile (e.g. "C:/Users/Jacob/buildings.shp")
        
    Returns:
    ---------
    None
    """
    # set up the shapefile driver
    driver = ogr.GetDriverByName("ESRI Shapefile")
    # create the data source
    data_source = driver.CreateDataSource(output_filename)
    # create the spatial reference, WGS84
    srs = osr.SpatialReference()
    srs.ImportFromEPSG(4326)
    # create the layer
    layer = data_source.CreateLayer("buildings", srs, ogr.wkbPolygon)
    
    with open(input_filename, "r") as f:
        reader = csv.DictReader(f)
        
        # define the field names for the shapfile
        layer.CreateField(ogr.FieldDefn("ID", ogr.OFTInteger))
        desc = ogr.FieldDefn("Description", ogr.OFTString)
        desc.SetWidth(50)
        layer.CreateField(desc)
        layer.CreateField(ogr.FieldDefn("YearBuilt", ogr.OFTInteger))
        layer.CreateField(ogr.FieldDefn("NumPeople", ogr.OFTInteger))
        layer.CreateField(ogr.FieldDefn("Area", ogr.OFTReal))
        layer.CreateField(ogr.FieldDefn("Height", ogr.OFTReal))
        layer.CreateField(ogr.FieldDefn("NumFloors", ogr.OFTInteger))
        layer.CreateField(ogr.FieldDefn("MonthlyElectricity", ogr.OFTReal))
        for row in reader:
            # create the feature
            feature = ogr.Feature(layer.GetLayerDefn())
            
            # Set the attributes using the values from the delimited text file
            feature.SetField("ID", row['ID'])
            feature.SetField("Description", row['Description'])
            feature.SetField("YearBuilt", row['YearBuilt'])
            feature.SetField("NumPeople", row['NumPeople'])
            feature.SetField("Area", row['Area'])
            feature.SetField("Height", row['Height'])
            feature.SetField("Area", row['Area'])
            feature.SetField("NumFloors", row['NumFloors'])
            feature.SetField("MonthlyElectricity", row['MonthlyElectricity'])
            
            polygon = parse_building_footprint(row["Footprint2D"])
            
            # Set the feature geometry using the polygon
            feature.SetGeometry(polygon)
            
            # Create the feature in the layer (shapefile)
            layer.CreateFeature(feature)
            
            # Dereference the feature
            feature = None
            
        # Save and close the data source
        data_source = None
        
def parse_building_footprint(input_string):
    """
    Parameters:
    -----------
    input_string: string
        a string of coordinates that makes up the 2D building footprint
    
    Returns:
    ---------
    poly: an ogr polygon feature
        a wkb representation of the 2D building footprint
    """
    # Create polygon
    ring = ogr.Geometry(ogr.wkbLinearRing)
    coord_list = input_string.split("_")
    for pair in coord_list:
        yx = pair.split("/")
        y = float(yx[0])
        x = float(yx[1])
        # add points to the polygon
        ring.AddPoint(x, y)
    closing_point = coord_list[0].split("/")
    ring.AddPoint(float(closing_point[1]), float(closing_point[0]))
    poly = ogr.Geometry(ogr.wkbPolygon)
    poly.AddGeometry(ring)
    return poly

buildings_csv_to_shapefile("D:/ornl/urban_challenge_dataset/chicago_loop_buildings.csv", "D:/ornl/urban_challenge_dataset/buildings.shp")