# Create Area of Interest

It is possible to simply pass a geometry GeoJSON file to save this to your My area space and once created it returns an ID which can then be used as either/or to generate stats or download data. While the atlas allows you to use the same name multiple times and is non unique, to avoid any confusion, the tool checks if a area of interest (aoi) exists with the same name and if yes then suggests you to change the name. This allows you to keep names distinct.

![pycoral_aoi-create](https://user-images.githubusercontent.com/6677629/118433354-69bdc880-b6a0-11eb-94d8-312a725fa29e.gif)

```
pycoral aoi-create -h
usage: pycoral aoi-create [-h] --name NAME --geometry GEOMETRY

optional arguments:
  -h, --help           show this help message and exit

Required named arguments.:
  --name NAME          AOI name
  --geometry GEOMETRY  Full path to geometry.geojson file
```
