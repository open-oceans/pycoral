# General Installation
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

*I recommend installation within a virtual environment. Find more information on [creating virtual environments here](https://docs.python.org/3/library/venv.html).*


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
