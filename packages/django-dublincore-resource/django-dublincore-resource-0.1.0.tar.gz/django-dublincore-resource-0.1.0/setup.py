# -*- coding: utf-8 -*-
from distutils.core import setup

packages = \
['dublincore_resource', 'dublincore_resource.migrations']

package_data = \
{'': ['*']}

setup_kwargs = {
    'name': 'django-dublincore-resource',
    'version': '0.1.0',
    'description': 'Describe your resources with a Dublin Core schema',
    'long_description': '# Django Dublin Core Resource\n\nA Django model and admin interface to manage metadata about your resources using Dublin Core (DC) standard.\n\nThe approach taken by this app is to centralise all your resource metadata into a single table.\n\nMost DC elements accepts only a single value to keep things simple.\n\n# Data Models\n\n* DublinCoreResource\n  * each DC element is represented by a field\n* DublinCoreAgent\n  * represents a person or organisation\n* DublinCoreRights\n  * represents Rights statements that can be shared among your resources\n\n# Features\n\n* One centralised table for all your resource\n* Standard Dublin Core elements/fields\n* Easy lookup into authority lists / controlled vocabularies\n* [TODO] smart bulk import/update from CSV\n* [TODO] advanced input validations\n* [TODO] customisable model\n* [TODO] API / export into various standard formats\n* [TODO] support for file attachment\n* [TODO] support for geonames\n* [TODO] support for bibliographic citation parsin\n* [TODO] support for EDTF dates\n\n# Set up\n\n## Installation\n\nTODO\n\n## Configuration\n\nTODO\n',
    'author': 'geoffroy-noel-ddh',
    'author_email': 'geoffroy.noel@kcl.ac.uk',
    'url': 'https://github.com/kingsdigitallab/django-dublincore-resource',
    'packages': packages,
    'package_data': package_data,
    'python_requires': '>=3.5,<4.0',
}


setup(**setup_kwargs)
