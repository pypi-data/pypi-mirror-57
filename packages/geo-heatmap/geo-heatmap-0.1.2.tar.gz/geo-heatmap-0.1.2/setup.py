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
    'version': '0.1.2',
    'description': 'Generate an interactive geo-heatmap from your Google location data',
    'long_description': None,
    'author': 'James Jarvis',
    'author_email': 'git@jamesjarvis.io',
    'maintainer': None,
    'maintainer_email': None,
    'url': None,
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'entry_points': entry_points,
    'python_requires': '>=3.7,<4.0',
}


setup(**setup_kwargs)
