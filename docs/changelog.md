# Changelog

#### v0.2.0
- Improved area and file format parsing
- Better logging support and error reporting
- Added support for GeoJSON, shapefile and CSV imports
- Added new aoi statistics support tool for stats export
- Major overall improvements and updates

#### v0.1.0
- Better site parsing
- Better error handling for Download
- Increase wait time for download to 2 minutes

#### v0.0.9
- Better error handling and now users user agent.
- Download tool for system polygon now creates a user copy to allow for all file types.

#### v0.0.8
- Better handles stats request.
- Prints info if AOI exceeds 100 sqkm.

#### v0.0.7
- Uses requests head to estimate zip completion for download.
- Added option to download data in specific format kml,geojson,shp or gpkg.
- Improved notification for download tool

#### v0.0.6
- Added auto version check to the tool.
- Added a web based readme site for the tool for ease of use.

#### v0.0.5
- Captures products available for download for parsing product type.
- For now chooses default product type only.
- Product download is more graceful since it checks product UUID and type before download per AOI.

#### v0.0.4
- Added aoi-delete capability along with create using GeoJSON and unique name check.
- Added local timestamp based unique name generator to AOI stats tool and checks to see if mapped area.
- Stability test across python3.6 to 3.9 and for all OS types built into CI
- Updated docs and code cleanup.
