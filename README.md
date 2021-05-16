# pycoral: Simple CLI for Allen Coral Atlas

[![CI pycoral](https://github.com/samapriya/pycoral/actions/workflows/package_ci.yml/badge.svg)](https://github.com/samapriya/pycoral/actions/workflows/package_ci.yml)

The Allen Coral Atlas was conceived and funded by the late Paul Allen’s Vulcan Inc. and is managed by the Arizona State University Center for Global Discovery and Conservation Science. Along with partners from Planet, the University of Queensland, and the National Geographic Society, the Atlas utilizes high-resolution satellite imagery and advanced analytics to map and monitor the world’s coral reefs in unprecedented detail. These products support coral reef science, management, conservation, and policy across the planet.

**Disclaimer: This is an unofficial tool. Is not licensed or endorsed by Allen Coral Atlas. It is created and maintained by Samapriya Roy.**

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
                  {auth,aoi-find,aoi-create,aoi-stat,aoi-delete,aoi-download}
                  ...

Simple CLI for Allen Coral Atlas

positional arguments:
  {auth,aoi-find,aoi-create,aoi-stat,aoi-delete,aoi-download}
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

### aoi-find

### aoi-create

### aoi-stat

### aoi-delete

### aoi-download
