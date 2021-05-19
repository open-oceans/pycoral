# Changelog

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
