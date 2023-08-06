# -*- coding: utf-8 -*-
from distutils.core import setup

packages = \
['matrix_saml_strip_hostname']

package_data = \
{'': ['*']}

setup_kwargs = {
    'name': 'matrix-saml-strip-hostname',
    'version': '0.1.0',
    'description': 'SAML mapping provider to strip hostnames from mxids',
    'long_description': None,
    'author': 'Sylvain Fankhauser',
    'author_email': 'sephi@fhtagn.top',
    'url': None,
    'packages': packages,
    'package_data': package_data,
    'python_requires': '>=3.5',
}


setup(**setup_kwargs)
