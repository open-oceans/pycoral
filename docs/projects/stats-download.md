# Download stats

The download stats tool can only be utilized to download Benthic and Geomorphic stats and is designed to be able to use a list of CSV latitude and longitude table along with a buffer area to search or you can also pass an existing AOI name or ID or a shapefile or GeoJSON file.

#### Key features
* Can handle multi geometry and single geometry features
* Can handle CSVs with multiple rows
* Can save geometry for large areas before trying to fetch stats

The table must have at least two columns

|"latitude" |"longitude|

![pycoral_stats_download](https://github.com/open-oceans/pycoral/assets/6677629/ea29e469-af84-466b-83e5-185fa45c4627)


```
pycoral stats-download -h
usage: pycoral stats-download [-h] --local LOCAL [--geometry GEOMETRY] [--aoi AOI]
                              [--buffer BUFFER]

options:
  -h, --help           show this help message and exit

Required named arguments.:
  --local LOCAL        Full path to folder to download stats files

Optional named arguments:
  --geometry GEOMETRY  Full path to geometry .csv/.geojson/.shp file
  --aoi AOI            AOI name or ID
  --buffer BUFFER      Buffer length for square buffer in meters
```
