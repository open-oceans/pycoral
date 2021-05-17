# Print stats

This tool allows you to get to the stats for an area of interest. The area of interest can be passed as ether a name, an ID , or as a geometry GeoJSON file. Depending on the size of the geometry it might take time to run the analysis. Since the atlas needs you to save your area of interest if the area is larger than 100 sqkm, this checks for area constraints and if the area is larger then it creates a temporary AOI.

To avoid asking the user for a AOI name, it uses the current local timestamp and encodes it into a unique string and returns to you the ID for the AOI along with the stats after a while.

![pycoral_aoi-stat](https://user-images.githubusercontent.com/6677629/118433364-6fb3a980-b6a0-11eb-9387-2495ae185b45.gif)

```
pycoral aoi-stat -h
usage: pycoral aoi-stat [-h] [--aoi AOI] [--geometry GEOMETRY]

optional arguments:
  -h, --help           show this help message and exit

Optional named arguments:
  --aoi AOI            AOI name or ID
  --geometry GEOMETRY  Full path to geometry.geojson file
```
