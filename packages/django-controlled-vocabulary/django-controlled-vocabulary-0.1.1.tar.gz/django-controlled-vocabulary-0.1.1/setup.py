# -*- coding: utf-8 -*-
from distutils.core import setup

packages = \
['controlled_vocabulary',
 'controlled_vocabulary.management',
 'controlled_vocabulary.management.commands',
 'controlled_vocabulary.migrations',
 'controlled_vocabulary.vocabularies']

package_data = \
{'': ['*'],
 'controlled_vocabulary': ['static/admin/css/*', 'static/admin/js/*']}

setup_kwargs = {
    'name': 'django-controlled-vocabulary',
    'version': '0.1.1',
    'description': 'Link your data to authority lists or your own controlled lists',
    'long_description': "# Django Controlled Vocabulary\n\nFacilitates linkage to remote standard vocabularies (e.g. language codes, geonames) within the Django Admin to increase the consistency and understandability of your project data.\n\n# Features\n\n* Lets you create your own controlled lists of terms (i.e. **local** lists)\n* [TODO] look up terms from **remote** vocabularies (i.e. authority lists)\n* **plug-in architecture** for lookups into particular vocabularies:\n  * Hard-coded lists: DCMI types\n  * CSV\n  * Python libraries\n  * [TODO] Sparql: TGN\n  * [TODO] Rest API\n* Built-in vocabulary plug-ins:\n  * ISO 639-2 (Language codes)\n  * DCMI Type (Dublin Core resource types)\n* **stores** used terms from remote vocabularies:\n  * space efficient (don't clutter the database with unused terms)\n  * self-contained (i.e. can still works offline & DB always 'semantically' complete)\n* [TODO] possibility to store additional **metadata** (e.g. geonames coordinates)\n* simple **rest API** to publish your own terms\n* **autocomplete** input widget for django admin\n  * [TODO] vocabulary selector\n\n# Data Models\n* ControlledVocabulary\n  * label, prefix, base_url, description\n* ControlledTerm:\n  * label, termid, vocabulary (-> ControlledVocabulary)\n\n# Limitations\n* **controlled list** rather than fully fledged vocabularies, (i.e. just a bag of terms with unique IDs/URIs, no support for taxonomic relationships among terms like broader, narrower, synonyms, ...)\n* no notion of granularity (e.g. geonames country, region, city, street are all treated as part of the same vocabulary)\n\n# Setup\n\n## Installation\n\nTODO\n\nAdd the app to the INSTALLED_APPS list in your Django settings file:\n\n```\nINSTALLED_APPS = [\n    # other apps\n    'controlled_vocabulary',\n]\n```\n\nRun the migrations:\n\n```\n./manage.py migrate\n```\n\n## Configuration\n\n### Enabling vocabulary plug-ins\n\nA Vocabulary plug-in / manager is a python class that provide services for a vocabulary: \n* implement the search() method used to dynamically look up terms in the admin interface\n* supplies metadata for the vocabulary\n\nAdd the following code in your settings.py to enable vocabularies based on the import path of their classes.\n\n```\n# List of import paths to vocabularies lookup classes\n# you can overwrite this in your django settings.py\nCONTROLLED_VOCABULARY_VOCABULARIES = [\n    'controlled_vocabulary.vocabularies.iso639_2',\n    'controlled_vocabulary.vocabularies.dcmitype',\n]\n```\n\nAfter enabling new vocabularies you'll need to run the following django command create or update records in the database for all enabled vocabulary plug-ins.\n\n```\n./manage.py vocab update\n```\n\nNote that this command only adds or update but never removes vocabularies from the database or changes terms.\n\n## Usage\n\nTo define a controlled term in your Django Model, use the following field:\n\n```\nfrom controlled_vocabulary.models import ControlledTermField\n```\n\n```\n    language_code = ControlledTermField(\n        'iso639-2', \n        null=True, blank=True\n    )\n```\n\nWhere 'iso639-2' is the prefix of a controlled vocabulary in your database.\n\n\n",
    'author': 'geoffroy-noel-ddh',
    'author_email': 'geoffroy.noel@kcl.ac.uk',
    'url': 'https://github.com/kingsdigitallab/django-controlled-vocabulary',
    'packages': packages,
    'package_data': package_data,
    'python_requires': '>=3.5,<4.0',
}


setup(**setup_kwargs)
