#!/usr/bin/python
# -*- coding: utf-8 -*-

__copyright__ = """

MIT License

Copyright (c) 2021 Samapriya Roy

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.


"""
__license__ = "MIT License"

import argparse
import base64
import getpass
import json
import os
import sys
import time
import webbrowser
from os.path import expanduser

import geojson
import pkg_resources
import progressbar
import requests
from area import area
from bs4 import BeautifulSoup


class Solution:
    def compareVersion(self, version1, version2):
        versions1 = [int(v) for v in version1.split(".")]
        versions2 = [int(v) for v in version2.split(".")]
        for i in range(max(len(versions1), len(versions2))):
            v1 = versions1[i] if i < len(versions1) else 0
            v2 = versions2[i] if i < len(versions2) else 0
            if v1 > v2:
                return 1
            elif v1 < v2:
                return -1
        return 0


ob1 = Solution()

# Get package version


def pycoral_version():
    url = "https://pypi.org/project/pycoral/"
    source = requests.get(url)
    html_content = source.text
    soup = BeautifulSoup(html_content, "html.parser")
    company = soup.find("h1")
    vcheck = ob1.compareVersion(
        company.string.strip().split(" ")[-1],
        pkg_resources.get_distribution("pycoral").version,
    )
    if vcheck == 1:
        print(
            "\n"
            + "========================================================================="
        )
        print(
            "Current version of pycoral is {} upgrade to lastest version: {}".format(
                pkg_resources.get_distribution("pycoral").version,
                company.string.strip().split(" ")[-1],
            )
        )
        print(
            "========================================================================="
        )
    elif vcheck == -1:
        print(
            "\n"
            + "========================================================================="
        )
        print(
            "Possibly running staging code {} compared to pypi release {}".format(
                pkg_resources.get_distribution("pycoral").version,
                company.string.strip().split(" ")[-1],
            )
        )
        print(
            "========================================================================="
        )


pycoral_version()

# Go to the readMe


def readme():
    try:
        a = webbrowser.open("https://pycoral.openoceans.xyz", new=2)
        if a == False:
            print("Your setup does not have a monitor to display the webpage")
            print(" Go to {}".format("https://pycoral.openoceans.xyz"))
    except Exception as e:
        print(e)


def read_from_parser(args):
    readme()


# set credentials
def auth():
    home = expanduser("~/coral.json")
    usr = input("Enter email: ")
    pwd = getpass.getpass("Enter password: ")
    data = {"email": usr, "password": pwd}
    with open(home, "w") as outfile:
        json.dump(data, outfile)


# auth()
def auth_from_parser(args):
    auth()


def tokenize():
    try:
        home = expanduser("~/coral.json")
        with open(home) as json_file:
            data = json.load(json_file)
            if not data.get("email"):
                email = input("Enter username: ")
            else:
                email = data.get("email")
            if not data.get("password"):
                password = getpass.getpass("Enter password: ")
            else:
                password = data.get("password")
    except Exception as e:
        print(e)
    headers = {
        "authority": "allencoralatlas.org",
        "sec-ch-ua": '" Not A;Brand";v="99", "Chromium";v="90", "Google Chrome";v="90"',
        "sec-ch-ua-mobile": "?0",
        "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.93 Safari/537.36",
        "content-type": "application/x-www-form-urlencoded",
        "accept": "*/*",
        "origin": "https://allencoralatlas.org",
        "sec-fetch-site": "same-origin",
        "sec-fetch-mode": "cors",
        "sec-fetch-dest": "empty",
        "accept-language": "en-US,en;q=0.9",
    }

    response = requests.post(
        "https://allencoralatlas.org/auth/login", headers=headers, data=json.dumps(data)
    )
    if response.status_code == 200:
        return response.json()["access_token"]
    else:
        print(
            "Authentication failed with response code {}".format(
                response.status_code)
        )


# List or find system polygons and user polygons
def poly_list(name):
    bearer = tokenize()
    mapped_area_list = []
    my_area_list = []
    headers = {
        "authority": "allencoralatlas.org",
        "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.45 Safari/537.36",
        "authorization": "Bearer {}".format(bearer),
    }
    response = requests.get(
        "https://allencoralatlas.org/mapping/aois?geometries=false", headers=headers
    )
    if response.status_code == 200:
        for things in response.json()["data"]:
            if name is None:
                if not things["owner"] is None and things["is_group"] == False:
                    my_area_list.append([things["name"], things["id"]])
                elif things["is_group"] == False:
                    mapped_area_list.append([things["name"], things["id"]])
            elif name is not None:
                if things["name"].strip().lower() == name.strip().lower():
                    print(f"Matching ID : {things['name']}: {things['id']}")
                    print("")
                    return things["id"]
        if mapped_area_list:
            print("\n" + "================MAPPED AREA LIST================")
            print(
                "\n".join(
                    [
                        " : ".join([str(cell) for cell in row])
                        for row in mapped_area_list
                    ]
                )
            )
        if my_area_list:
            print("\n" + "================MY AREA LIST================")
            print(
                "\n".join(
                    [" : ".join([str(cell) for cell in row])
                     for row in my_area_list]
                )
            )
    else:
        print(
            f"Failed to fetch default or user areas with response : {response.status_code}"
        )


def poly_list_from_parser(args):
    poly_list(name=args.name)


def getarea(geom):
    obj = {"type": "Polygon", "coordinates": []}
    obj["coordinates"] = geom
    poly_area = area(obj)
    return poly_area / 1000000


def poly_create(filepath, name):
    if name is not None:
        if name.isdigit():
            id = str(name)
        else:
            id = poly_list(name=str(name))
    else:
        sys.exit("Pass valid geometry name or ID")
    if id is None:
        print(f"Polygon name does not exist: Creating {name}")
    else:
        sys.exit(
            f"Existing polygon name {name} found: Try a different name or delete")
    bearer = tokenize()
    headers = {
        "authority": "allencoralatlas.org",
        "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.45 Safari/537.36",
        "authorization": "Bearer {}".format(bearer),
    }
    with open(filepath) as f:
        gj = geojson.load(f)
    features = gj["features"][0]
    area_value = getarea(features["geometry"]["coordinates"])
    print(f"Total area in sqkm {round(area_value,2)}")
    data = {
        "name": name,
        "unsaved": False,
        "owner": "local",
        "local": True,
        "geom": {"type": "Polygon", "coordinates": []},
    }
    data["geom"]["coordinates"] = features["geometry"]["coordinates"]
    response = requests.post(
        "https://allencoralatlas.org/mapping/aois",
        headers=headers,
        data=json.dumps(data),
    )
    if response.status_code == 201:
        print(
            f"Created {response.json()['data']['name']} with ID: {response.json()['data']['id']}"
        )
        return response.json()["data"]["id"]
    else:
        print(
            f"Create failed with response {response.status_code} and error message {response.string}"
        )


def poly_create_from_parser(args):
    poly_create(name=args.name, filepath=args.geometry)


def poly_delete(id):
    if id is not None:
        if id.isdigit():
            id = str(id)
        else:
            id = poly_list(name=str(id))
    else:
        sys.exit("Pass valid geometry name or ID")
    bearer = tokenize()
    headers = {
        "authority": "allencoralatlas.org",
        "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.45 Safari/537.36",
        "authorization": "Bearer {}".format(bearer),
    }
    response = requests.delete(
        f"https://allencoralatlas.org/mapping/aois/{id}", headers=headers
    )
    if response.status_code == 200:
        print(f"Deleted {id} successfully")
    else:
        print(
            f"No results for name or id {id}: returned {response.status_code}")


def poly_delete_from_parser(args):
    poly_delete(id=args.aoi)


def poly_stat(id, filepath):
    bearer = tokenize()
    headers = {
        "authority": "allencoralatlas.org",
        "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.45 Safari/537.36",
        "authorization": "Bearer {}".format(bearer),
    }
    if id is not None:
        if id.isdigit():
            id = str(id)
        else:
            id = poly_list(name=str(id))
        response = requests.get(
            f"https://allencoralatlas.org/mapping/aois/{id}/stats", headers=headers
        )
    elif id is None and filepath is not None:
        with open(filepath) as f:
            gj = geojson.load(f)
        features = gj["features"][0]
        area_value = getarea(features["geometry"]["coordinates"])
        if int(area_value) < 100:
            data = {"geom": {"type": "Polygon", "coordinates": []}}
            data["geom"]["coordinates"] = features["geometry"]["coordinates"]
            response = requests.post(
                "https://allencoralatlas.org/mapping/aois/stats",
                headers=headers,
                data=json.dumps(data),
            )
        else:
            print("AOI area exceeds 100 sqkm: Creating Polygon to run stats")
            current_timestamp = str(time.time())
            message_bytes = current_timestamp.encode("ascii")
            base64_bytes = base64.b64encode(message_bytes)
            name = base64_bytes.decode("ascii")
            id = poly_create(filepath, name)
            response = requests.get(
                f"https://allencoralatlas.org/mapping/aois/{id}/stats", headers=headers
            )
            while response.status_code != 200:
                time.sleep(5)
                response = requests.get(
                    f"https://allencoralatlas.org/mapping/aois/{id}/stats",
                    headers=headers,
                )
    else:
        sys.exit("Pass valid geometry, name or ID")
    if response.status_code == 200:
        if float(response.json()["data"]["stats"]["mapped_sqkm"]) > 0.0:
            print(json.dumps(response.json()["data"], indent=2))
        else:
            print("No mapped area for the AOI")
    else:
        print(
            f"No results for name or id {id}: returned {response.status_code}")


def poly_stat_from_parser(args):
    poly_stat(id=args.aoi, filepath=args.geometry)


def downloader(url, local_path):
    response = requests.request("HEAD", url)
    filename = url.split("/")[-1]
    local_path = os.path.join(local_path, filename)
    print("Waiting for zip file to complete ...")
    try:
        while response.status_code != 200:
            bar = progressbar.ProgressBar()
            for _ in bar(range(120)):
                time.sleep(1)
            response = requests.request("HEAD", url)
        if not os.path.exists(local_path) and response.status_code == 200:
            print(f"Downloading to :{local_path}")
            response = requests.get(url)
            f = open(local_path, "wb")
            for chunk in response.iter_content(chunk_size=512 * 1024):
                if chunk:
                    f.write(chunk)
            f.close()
        elif response.status_code == 429:
            raise Exception("rate limit error")
        else:
            if int(response.status_code) != 200:
                print(
                    f"Encountered error with code: {response.status_code} for {os.path.split(local_path)[-1]}"
                )
            elif int(response.status_code) == 200:
                print(
                    f"File already exists SKIPPING: {os.path.split(local_path)[-1]}")
    except Exception as e:
        print(e)
    except KeyboardInterrupt:
        sys.exit("\n" + "Exited by user")


def poly_download(id, local_path, format):
    if id is not None:
        if id.isdigit():
            id = str(id)
        else:
            id = poly_list(name=str(id))
    else:
        sys.exit("Pass valid geometry name or ID")
    bearer = tokenize()
    headers = {
        "authority": "allencoralatlas.org",
        "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.45 Safari/537.36",
        "authorization": "Bearer {}".format(bearer),
    }
    aoi_check = requests.get(
        f"https://allencoralatlas.org/mapping/aois/{id}", headers=headers
    )
    if aoi_check.status_code == 200 and aoi_check.json()["data"]["owner"] is None:
        print(
            f"This is a system polygon checking for a user copy of {aoi_check.json()['data']['name']}"
        )
        user_poly = f"{aoi_check.json()['data']['name'].lower().replace(' ', '_')}_user"
        id = poly_list(name=str(user_poly))
        print(
            """
            User copies of system polygon can take a long time to prepare for download
            Once order is placed use Ctrl+C to terminate and wait for the download email to be sent
            """
        )
        if id is not None:
            print(f"Existing polygon name {user_poly} found")
        else:
            print(f"Polygon name does not exist: Creating {user_poly}")
            data = {
                "name": user_poly,
                "unsaved": False,
                "owner": "local",
                "local": True,
                "geom": {
                    "type": "MultiPolygon",
                    "coordinates": aoi_check.json()["data"]["geom"]["coordinates"],
                },
            }
            response = requests.post(
                "https://allencoralatlas.org/mapping/aois",
                headers=headers,
                data=json.dumps(data),
            )
            if response.status_code == 201:
                print(
                    f"Created {response.json()['data']['name']} with ID: {response.json()['data']['id']}"
                )
                id = response.json()["data"]["id"]
            else:
                print(
                    f"Create failed with response {response.status_code} and error message {response.text}"
                )
        # print(id)
    data = {"datasets": "empty"}
    product_dict = {}
    response = requests.get(
        f"https://allencoralatlas.org/mapping/aois/{id}/products", headers=headers
    )
    for products in response.json()["data"]:
        if products["allow_downloads"] == True:
            if format in products["options"]["valid_formats"]:
                product_dict[products["uuid"]] = format
            else:
                product_dict[products["uuid"]
                             ] = products["options"]["default_format"]
    data["datasets"] = product_dict
    response = requests.post(
        f"https://allencoralatlas.org/download/aois/{id}",
        headers=headers,
        data=json.dumps(data),
    )

    if response.status_code == 200:
        print(f'Submited {response.json()["data"]["name"]} for download')
        downloader(response.json()["data"]["url"], local_path)
    elif response.status_code == 202:
        print(f'Submited {response.json()["data"]["name"]} for download')
        downloader(response.json()["data"]["url"], local_path)
    else:
        print(
            f"No results for name or id {id}: returned {response.status_code}")


def poly_download_from_parser(args):
    poly_download(id=args.aoi, local_path=args.local, format=args.format)


def main(args=None):
    parser = argparse.ArgumentParser(
        description="Simple CLI for Allen Coral Atlas")
    subparsers = parser.add_subparsers()

    parser_read = subparsers.add_parser(
        "readme", help="Go to the web based pycoral readme page"
    )
    parser_read.set_defaults(func=read_from_parser)

    parser_auth = subparsers.add_parser(
        "auth", help="Saves your username and password")
    parser_auth.set_defaults(func=auth_from_parser)

    parser_poly_list = subparsers.add_parser(
        "aoi-find", help="Find AOI name and ID or list all"
    )
    optional_named = parser_poly_list.add_argument_group(
        "Optional named arguments")
    optional_named.add_argument("--name", help="Pass area name", default=None)
    parser_poly_list.set_defaults(func=poly_list_from_parser)

    parser_poly_create = subparsers.add_parser(
        "aoi-create", help="Use a GeoJSON geometry file to create My Area AOI"
    )
    required_named = parser_poly_create.add_argument_group(
        "Required named arguments.")
    required_named.add_argument("--name", help="AOI name", required=True)
    required_named.add_argument(
        "--geometry", help="Full path to geometry.geojson file", required=True
    )
    parser_poly_create.set_defaults(func=poly_create_from_parser)

    parser_poly_stat = subparsers.add_parser(
        "aoi-stat",
        help="Print summary statistics for AOI using geoemtry file, name or ID",
    )
    optional_named = parser_poly_stat.add_argument_group(
        "Optional named arguments")
    optional_named.add_argument("--aoi", help="AOI name or ID", default=None)
    optional_named.add_argument(
        "--geometry", help="Full path to geometry.geojson file", default=None
    )
    parser_poly_stat.set_defaults(func=poly_stat_from_parser)

    parser_poly_delete = subparsers.add_parser(
        "aoi-delete", help="Delete AOI from My Areas list"
    )
    required_named = parser_poly_delete.add_argument_group(
        "Required named arguments.")
    required_named.add_argument("--aoi", help="AOI name or ID", required=True)
    parser_poly_delete.set_defaults(func=poly_delete_from_parser)

    parser_poly_download = subparsers.add_parser(
        "aoi-download", help="Download files using name or ID"
    )
    required_named = parser_poly_download.add_argument_group(
        "Required named arguments."
    )
    required_named.add_argument("--aoi", help="AOI name or ID", required=True)
    required_named.add_argument(
        "--local", help="Full path to folder to download files", required=True
    )
    optional_named = parser_poly_download.add_argument_group(
        "Optional named arguments")
    optional_named.add_argument(
        "--format", help="Format types 'geojson', 'kml', 'shp', 'gpkg'", default=None
    )
    parser_poly_download.set_defaults(func=poly_download_from_parser)

    args = parser.parse_args()

    try:
        func = args.func
    except AttributeError:
        parser.error("too few arguments")
    func(args)


if __name__ == "__main__":
    main()
