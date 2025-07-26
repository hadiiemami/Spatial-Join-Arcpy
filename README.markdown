# RiserAddressMapper

A Python script utilizing ArcPy to automate spatial analysis and attribute mapping for GIS data. This project processes shapefiles to associate risers with parcels and assign the minimum address code to each riser, streamlining geospatial workflows in urban planning and infrastructure management.

## Overview
The RiserAddressMapper project provides a robust solution for geospatial analysts working with ArcGIS. It leverages ArcPy to perform spatial joins between riser and parcel shapefiles, extract the minimum address code for each riser, and update the riser dataset with these values. This automation enhances efficiency in tasks requiring spatial relationships and attribute aggregation, such as address mapping for utility networks or land management systems.

## Table of Contents
- [Purpose](#purpose)
- [Functionality](#functionality)
- [Prerequisites](#prerequisites)
- [Installation](#installation)
- [Usage](#usage)
- [Input and Output](#input-and-output)
- [Contributing](#contributing)
- [License](#license)

## Purpose
This project aims to simplify the process of linking geospatial features (risers and parcels) and aggregating attribute data (address codes) in ArcGIS. By automating spatial joins and attribute calculations, it reduces manual effort and ensures accuracy in mapping minimum address codes to risers, making it valuable for GIS professionals in urban development, infrastructure planning, or similar fields.

## Functionality
The script (`riser_address_mapper.py`) performs the following tasks:
- Configures the ArcGIS workspace to manage input and output files.
- Loads two shapefiles: one for risers and one for parcels.
- Executes a spatial join to identify parcels within each riser.
- Calculates the minimum address code for each riser using a cursor-based approach.
- Creates a new table to store riser codes and their corresponding minimum address codes.
- Joins the minimum address codes back to the original riser shapefile.
- Saves the updated riser dataset as a new shapefile for further analysis or visualization.

## Prerequisites
- ArcGIS Pro or ArcMap with a valid license and ArcPy module.
- Python environment compatible with ArcGIS (e.g., Python 3.x for ArcGIS Pro or Python 2.7 for ArcMap).
- Input shapefiles:
  - Riser shapefile with a unique identifier field (e.g., `Riser_Code`).
  - Parcel shapefile with an address code field (e.g., `Address_Code`).
- A workspace directory with read/write permissions for storing input and output files.

## Installation
1. Ensure ArcGIS Pro or ArcMap is installed and ArcPy is accessible in your Python environment.
2. Clone the repository to your local machine:
   ```bash
   git clone https://github.com/your-username/RiserAddressMapper.git
   ```
3. Place the required shapefiles in your workspace directory (e.g., `E:/Projects/Babayi/FinalSHP`).
4. Verify that both shapefiles share the same Coordinate Reference System (CRS) to ensure accurate spatial analysis.

## Usage
1. Navigate to the repository folder:
   ```bash
   cd RiserAddressMapper
   ```
2. Modify the workspace path in `riser_address_mapper.py` to match your directory:
   ```python
   arcpy.env.workspace = "E:/Your/Path/To/FinalSHP"
   ```
3. Execute the script in an ArcGIS-compatible Python environment (e.g., ArcGIS Pro Python Console or ArcMap Python Window):
   ```bash
   python riser_address_mapper.py
   ```
4. Review the output files generated in the workspace directory for analysis or visualization in ArcGIS.

## Input and Output
- **Input Files**:
  - Riser shapefile: Contains riser features with a unique identifier (e.g., `Riser_Code`).
  - Parcel shapefile: Contains parcel features with an address code (e.g., `Address_Code`).
- **Output Files**:
  - `Riser_Parcel_SpatialJoin.shp`: Intermediate shapefile from the spatial join.
  - `MinAddrTbl.dbf`: Table storing riser codes and their minimum address codes.
  - `Riser_Final_Output.shp`: Final shapefile with risers updated to include minimum address codes.
- **Note**: Ensure field names in the shapefiles match those specified in the script. Adjust field names (e.g., `Riser_Asse`, `Address_Co`) if necessary.

## Contributing
Contributions are encouraged to enhance the script or add new features. To contribute:
1. Fork the repository.
2. Create a new branch (`git checkout -b feature-branch`).
3. Implement changes with clear documentation and comments.
4. Submit a pull request describing the updates.

## License
MIT License