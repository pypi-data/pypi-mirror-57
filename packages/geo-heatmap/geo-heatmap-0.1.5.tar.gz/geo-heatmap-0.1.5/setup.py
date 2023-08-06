# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['geo_heatmap']

package_data = \
{'': ['*']}

install_requires = \
['argparse>=1.4.0,<2.0.0',
 'beautifulsoup4>=4.8.1,<5.0.0',
 'folium>=0.10.1,<0.11.0',
 'ijson>=2.5.1,<3.0.0',
 'progressbar2>=3.47.0,<4.0.0']

entry_points = \
{'console_scripts': ['geo-heatmap = geo_heatmap.console:run']}

setup_kwargs = {
    'name': 'geo-heatmap',
    'version': '0.1.5',
    'description': 'Generate an interactive geo-heatmap from your Google location data',
    'long_description': '# Geo Heatmap\n\n![screenshot](https://user-images.githubusercontent.com/45404400/63515170-7a9cd280-c4ea-11e9-8875-e693622ac26e.png)\n\nThis is a script that generates an interactive geo heatmap from your Google location history data using Python, Folium and OpenStreetMap.\n\n## Getting Started\n\n### 1. Install Python 3+\n\nIf you don\'t already have Python 3+ installed, grab it from <https://www.python.org/downloads/>. You\'ll want to download install the latest version of **Python 3.x**. As of 2019-11-22, that is Version 3.8.\n\nFor ease of python version handling, I\'d recommend installing it through [pyenv](https://github.com/pyenv/pyenv#installation).\n\n### 2. Get Your Location Data\n\nHere you can find out how to download your Google data: <https://support.google.com/accounts/answer/3024190?hl=en></br>\nHere you can download all of the data that Google has stored on you: <https://takeout.google.com/>\n\nTo use this script, you only need to select and download your "Location History", which Google will provide to you as a JSON file by default. KML is also an output option and is accepted for this program.\n\n### 3. Install the script\n\nIn a [command prompt or Terminal window](https://tutorial.djangogirls.org/en/intro_to_command_line/#what-is-the-command-line), [navigate to the directory](https://tutorial.djangogirls.org/en/intro_to_command_line/#change-current-directory) containing the location data files. Then, type the following, and press enter:\n\n```shell\npip install geo-heatmap\n```\n\n### 4. Run the Script\n\nIn the same command prompt or Terminal window, type the following, and press enter:\n\n```shell\ngeo-heatmap <file> [<file> ...]\n```\n\nReplace the string `<file>` from above with the path to any of the following files:\n\n1. The `Location History.json` JSON file from Google Takeout\n2. The `Location History.kml` KML file from Google Takeout\n3. The `takeout-*.zip` raw download from Google Takeout that contains either of the above files\n\n#### Examples:\n\nSingle file:\n\n```shell\ngeo-heatmap C:\\Users\\Testuser\\Desktop\\locations.json\n```\n\n```shell\ngeo-heatmap "C:\\Users\\Testuser\\Desktop\\Location History.json"\n```\n\n```shell\ngeo-heatmap locations.json\n```\n\nMultiple files:\n\n```shell\ngeo-heatmap locations.json locations.kml takeout.zip\n```\n\nUsing the stream option (for users with Memory Errors):\n\n```shell\ngeo-heatmap -s locations.json\n```\n\nSet a date range:\n\n```shell\ngeo-heatmap --min-date 2017-01-02 --max-date 2018-12-30 locations.json\n```\n\n#### Usage:\n\n```\nusage: geo-heatmap [-h] [-o] [--min-date YYYY-MM-DD]\n                      [--max-date YYYY-MM-DD] [-s] [--map MAP]\n                      file [file ...]\n\npositional arguments:\n  file                  Any of the following files:\n                        1. Your location history JSON file from Google Takeout\n                        2. Your location history KML file from Google Takeout\n                        3. The takeout-*.zip raw download from Google Takeout\n                        that contains either of the above files\n\noptional arguments:\n  -h, --help            show this help message and exit\n  -o , --output         Path of heatmap HTML output file.\n  --min-date YYYY-MM-DD\n                        The earliest date from which you want to see data in the heatmap.\n  --max-date YYYY-MM-DD\n                        The latest date from which you want to see data in the heatmap.\n  -s, --stream          Option to iteratively load data.\n  --map MAP, -m MAP     The name of the map tiles you want to use.\n                        (e.g. \'OpenStreetMap\', \'StamenTerrain\', \'StamenToner\', \'StamenWatercolor\')\n```\n\n### 6. Review the Results\n\nThe script will generate a HTML file named `heatmap.html`. This file will automatically open in your browser once the script completes. Enjoy!\n\n## FAQ\n\n### I\'m getting an "Out of Memory" error or `MemoryError` when I try to run the script. What\'s going on?\n\nYour `LocationHistory.json` file is probably huge, and Python is running out of memory when the script tries to parse that file.\n\nTo fix this, download and install the 64-bit version of Python. To do this:\n\n1. Go to [python.org](https://www.python.org/downloads/).\n2. Click the link corresponding to your OS next to "Looking for Python with a different OS?"\n3. Click the "Latest Python 3 Release" link.\n4. Scroll down to "Files".\n5. Click to download the x64 release. For example, on Windows, that\'s the "Windows x86-64 executable installer" link.\n6. Install!\n\nIf this does not fix the issue you can use the stream option:\n\n```shell\ngeo-heatmap -s <file>\n```\n\nThis will be slower but will use much less memory to load your location data.\n\n### I\'m getting a `SyntaxError` when running `pip install -r requirements.txt` or `python geo_heatmap.py <file>`. What am I doing wrong?\n\nYou are probably using the python interpreter to run these commands. Try to run them in cmd.exe or Windows PowerShell (Windows) or the Terminal (Linux, MacOS).\n\n### I\'m getting the error message `TypeError: __init__() got an unexpected keyword argument \'max_value\'`. What can I do to fix this?\n\nTry to run:\n\n```shell\npip uninstall progressbar\npip install progressbar2\n```\n\nYou probably have progressbar installed, which uses `maxval` as an argument for `__init__`. Progressbar2 uses `max_value`.\n\n## Development\n\nThis project is using [Poetry](https://python-poetry.org/) to manage dependencies. You can install it by following their guide.\n\nIf you would like to develop on this further, after cloning this repository and navigating into it you can get up and running with the following:\n\n```shell\npoetry install\npoetry run geo-heatmap\n```\n',
    'author': 'Luka Steinbach',
    'author_email': 'luka.steinbach@gmx.de',
    'maintainer': None,
    'maintainer_email': None,
    'url': 'https://github.com/jamesjarvis/geo-heatmap',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'entry_points': entry_points,
    'python_requires': '>=3.7,<4.0',
}


setup(**setup_kwargs)
