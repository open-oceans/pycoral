# Download data

The download tool can only be utilized for area of interest that have been saved to my areas. As such this tool utilizes either the AOI name or ID. This submits the request and then waits for zipping to complete to then download a single zip files with all sources.

![pycoral_aoi-download](https://user-images.githubusercontent.com/6677629/118433385-7e9a5c00-b6a0-11eb-87cd-d84b81960757.gif)


You can also specify a format now since v0.0.7

![aoi_download_format](https://user-images.githubusercontent.com/6677629/119296374-6b4a3c00-bc1e-11eb-85d9-df5f476dbbf7.gif)

```
pycoral aoi-download -h
usage: pycoral aoi-download [-h] --aoi AOI --local LOCAL [--format FORMAT]

optional arguments:
  -h, --help       show this help message and exit

Required named arguments.:
  --aoi AOI        AOI name or ID
  --local LOCAL    Full path to folder to download files

Optional named arguments:
  --format FORMAT  Format types 'geojson', 'kml', 'shp', 'gpkg'
```
