# pycoral: Simple CLI for Allen Coral Atlas

[![Twitter URL](https://img.shields.io/twitter/follow/samapriyaroy?style=social)](https://twitter.com/intent/follow?screen_name=samapriyaroy)
![](https://tokei.rs/b1/github/samapriya/pycoral?category=code)
![](https://tokei.rs/b1/github/samapriya/pycoral?category=files)
![PyPI - License](https://img.shields.io/pypi/l/pycoral)
[![Downloads](https://pepy.tech/badge/pycoral)](https://pepy.tech/project/pycoral)
[![CI pycoral](https://github.com/samapriya/pycoral/actions/workflows/package_ci.yml/badge.svg)](https://github.com/samapriya/pycoral/actions/workflows/package_ci.yml)
[![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.5497093.svg)](https://doi.org/10.5281/zenodo.5497093)
![PyPI](https://img.shields.io/pypi/v/pycoral)

The Allen Coral Atlas was conceived and funded by the late Paul Allen’s Vulcan Inc. and is managed by the Arizona State University Center for Global Discovery and Conservation Science. Along with partners from Planet, the University of Queensland, and the National Geographic Society, the Atlas utilizes high-resolution satellite imagery and advanced analytics to map and monitor the world’s coral reefs in unprecedented detail. These products support coral reef science, management, conservation, and policy across the planet. This tool is designed to help interact programmatically with the Allen Coral Atlas and is not based on any official API so expect features to break once in a while.

**Disclaimer: This is an unofficial tool. Is not licensed or endorsed by Allen Coral Atlas. It is created and maintained by Samapriya Roy.**

#### Citation

```
Samapriya Roy. (2021). samapriya/pycoral: Simple CLI for Allen Coral Atlas (0.0.8).
Zenodo. https://doi.org/10.5281/zenodo.5497093
```

Readme Docs [available online](https://samapriya.github.io/pycoral)

## Table of contents
* [Getting started](#getting-started)
    * [auth](#auth)
    * [aoi-find](#aoi-find)
    * [aoi-create](#aoi-create)
    * [aoi-stat](#aoi-stat)
    * [aoi-delete](#aoi-delete)
    * [aoi-download](#aoi-download)

## Getting started
The tool is a simple standalone tool and the requirements for the setup are included in the requirements.txt file. Depending on the OS and the python version you should be able to simply run

```pip install -r requirements.txt```

To install pycoral: Simple CLI for Allen Coral Atlas you can install using two methods.

```
pip install pycoral
```

or you can also try

```
git clone https://github.com/samapriya/pycoral.git
cd pycoral
python setup.py install
```

## Main screen

```
usage: pycoral [-h]
               {readme,auth,aoi-find,aoi-create,aoi-stat,aoi-delete,aoi-download}
               ...

Simple CLI for Allen Coral Atlas

positional arguments:
  {readme,auth,aoi-find,aoi-create,aoi-stat,aoi-delete,aoi-download}
    readme              Go to the web based pycoral readme page
    auth                Saves your username and password
    aoi-find            Find AOI name and ID or list all
    aoi-create          Use a GeoJSON geometry file to create My Area AOI
    aoi-stat            Print summary statistics for AOI using geoemtry file,
                        name or ID
    aoi-delete          Delete AOI from My Areas list
    aoi-download        Download files using name or ID

optional arguments:
  -h, --help            show this help message and exit
```

### auth
The auth or authentication tool allows the user to use their name and password used for logging into Allen Coral Atlas. This is stored locally and a bearer token is generated everytime the tool is being used from the saved credentials.

![pycoral_auth](https://user-images.githubusercontent.com/6677629/118433326-5d397000-b6a0-11eb-9078-905064bcd244.gif)

### aoi-find
The aoi-find tool can be handy if you are looking for a specific aoi-name and is mostly useful to list all allowed polygons including those that are default or stored by the atlas vs your own areas of interest.

![pycoral_aoi-find](https://user-images.githubusercontent.com/6677629/118433340-6296ba80-b6a0-11eb-83f3-e2376f4fa5a6.gif)

### aoi-create
It is possible to simply pass a geometry GeoJSON file to save this to your My area space and once created it returns an ID which can then be used as either/or to generate stats or download data. While the atlas allows you to use the same name multiple times and is non unique, to avoid any confusion, the tool checks if a area of interest (aoi) exists with the same name and if yes then suggests you to change the name. This allows you to keep names distinct.

![pycoral_aoi-create](https://user-images.githubusercontent.com/6677629/118433354-69bdc880-b6a0-11eb-94d8-312a725fa29e.gif)

### aoi-stat
This tool allows you to get to the stats for an area of interest. The area of interest can be passed as ether a name, an ID , or as a geometry GeoJSON file. Depending on the size of the geometry it might take time to run the analysis. Since the atlas needs you to save your area of interest if the area is larger than 100 sqkm, this checks for area constraints and if the area is larger then it creates a temporary AOI.

To avoid asking the user for a AOI name, it uses the current local timestamp and encodes it into a unique string and returns to you the ID for the AOI along with the stats after a while.

![pycoral_aoi-stat](https://user-images.githubusercontent.com/6677629/118433364-6fb3a980-b6a0-11eb-9387-2495ae185b45.gif)

### aoi-delete
This tool allows the user to delete any AOI from the my areas space based on either a name or the AOI id. The AOI name or ID must exist in your my areas list.

![pycoral_aoi-delete](https://user-images.githubusercontent.com/6677629/118433379-780be480-b6a0-11eb-8420-33708e4bac6a.gif)

### aoi-download
The download tool can only be utilized for area of interest that have been saved to my areas. As such this tool utilizes either the AOI name or ID. This submits the request and then waits for zipping to complete to then download a single zip files with all sources.

![pycoral_aoi-download](https://user-images.githubusercontent.com/6677629/118433385-7e9a5c00-b6a0-11eb-87cd-d84b81960757.gif)

You can also specify a format now since v0.0.7

![aoi_download_format](https://user-images.githubusercontent.com/6677629/119296374-6b4a3c00-bc1e-11eb-85d9-df5f476dbbf7.gif)


## Changelog

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
