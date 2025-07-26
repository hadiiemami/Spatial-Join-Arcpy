import arcpy

# Set workspace environment
arcpy.env.workspace = "E:/Projects/Babayi/FinalSHP"
arcpy.env.overwriteOutput = True

# 1. Load the shapefiles
riser_shapefile = "Riser.shp"
parcel_shapefile = "Parcel.shp"

# 2. Ensure CRS is the same (reproject if necessary)
# Here, assuming both files are already in the same CRS. If not, you need to use arcpy.Project_management() to reproject.

# 3. Perform spatial join to associate each Riser with the parcels within it
spatial_join_output = "Riser_Parcel_SpatialJoin.shp"
arcpy.analysis.SpatialJoin(riser_shapefile, parcel_shapefile, spatial_join_output)

# 4. Find the minimum Address_Code for each Riser
# Create a feature layer from the spatial join result
arcpy.MakeFeatureLayer_management(spatial_join_output, "spatial_join_lyr")

# Verify field names in the spatial join result
fields = [f.name for f in arcpy.ListFields("spatial_join_lyr")]
print("Fields in spatial join result:", fields)

# Adjust column names based on actual names
riser_code_field = "Riser_Asse"  # Adjusted based on the output
address_code_field = "Address_Co"  # Adjusted based on the output

# Use SearchCursor to get minimum address codes for each Riser
address_min_results = []
with arcpy.da.SearchCursor("spatial_join_lyr", [riser_code_field, address_code_field]) as cursor:
    for row in cursor:
        address_min_results.append((row[0], row[1]))

# Remove duplicates (keep only one row per Riser)
address_min_dict = {}
for riser_code, address_code in address_min_results:
    if riser_code not in address_min_dict:
        address_min_dict[riser_code] = address_code
    else:
        if address_code < address_min_dict[riser_code]:
            address_min_dict[riser_code] = address_code

# Create a new table for minimum address codes
min_address_table = "MinAddrTbl.dbf"  # Shortened name
arcpy.management.CreateTable(arcpy.env.workspace, min_address_table)
arcpy.management.AddField(min_address_table, "R_Code", "TEXT")  # Shortened name
arcpy.management.AddField(min_address_table, "MinAddr", "TEXT")  # Shortened name

# Insert minimum address codes into the new table
with arcpy.da.InsertCursor(min_address_table, ["R_Code", "MinAddr"]) as cursor:
    for riser_code, min_address_code in address_min_dict.items():
        cursor.insertRow((riser_code, min_address_code))

# 6. Join the minimum address codes back to the original Riser shapefile
join_output = "Riser_With_MinAddr.shp"  # Shortened name
arcpy.management.JoinField(riser_shapefile, "Riser_Code", min_address_table, "R_Code", ["MinAddr"])

# 7. Save the result to a new shapefile
arcpy.management.CopyFeatures(riser_shapefile, "Riser_Final_Output.shp")

print("Process completed successfully.")
