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
 'controlled_vocabulary': ['static/admin/css/*',
                           'static/admin/js/*',
                           'templates/controlled_vocabulary/*']}

setup_kwargs = {
    'name': 'django-controlled-vocabulary',
    'version': '0.1.4',
    'description': 'Link your data to authority lists or your own controlled lists',
    'long_description': "# Django Controlled Vocabulary\n\nFacilitates linkage to remote standard vocabularies (e.g. language codes, wikidata)\nwithin the Django Admin to increase the consistency and understandability of your project data.\n\nDevelopment Status: **Alpha** (only partly functional, work in progress)\n\n# Features\n\n* Lets you create your own controlled lists of terms (i.e. **local** lists)\n* look up terms from **remote** vocabularies (i.e. authority lists)\n* **plug-in architecture** for lookups into particular vocabularies\n* Built-in vocabulary plug-ins, such as ISO 639-2 (Language codes), DCMI Type (Dublin Core resource types)\n* **stores** used terms from remote vocabularies into the database:\n  * space efficient (don't clutter the database with unused terms)\n  * self-contained (i.e. can still works offline & DB always 'semantically' complete)\n* [TODO] possibility to store additional **metadata** (e.g. geographic coordinates)\n* [TODO] simple **rest API** to publish your own terms\n* New Django model field with **autocomplete** widget\n\n# Data Model & Software Design\n\n## Django models\n\n* ControlledVocabulary\n  * prefix: the vocabulary standard prefix, see http://prefix.cc/wikidata\n  * label: the short name of the vocabulary\n  * base_url: the url used as a base for all terms in the vocabulary\n  * concept: the type of terms this vocabulary contains\n  * description: a longer description\n\n* ControlledTerm\n  * termid: a unique code for the term within a vocabulary\n  * label: standard name for the term\n  * vocabulary: the vocabulary this term belongs to\n\n## Vocabulary plug-ins / managers\n\nA Vocabulary **plug-in** / **manager** is a python class that provides services for a vocabulary:\n* autocomplete terms from local or remote datasets (see ControlledTermField)\n* supplies metadata for the vocabulary (see ControlledVocabulary)\n\nManagers can provide terms from a CSV file downloaded from an authoritative source.\n\nSome vocabularies can contain thousands of terms or more. A plugin will\nonly insert the terms used by your application. The rest will be accessed on\ndemand from a file on disk or in a third-party server. This approach saves\ndatabase space and keeps your application data self-contained.\n\nThis project comes with built-in plugins for the following vocabularies:\nISO 639-2, DCMI Type, Wikidata, FAST Topics, MIME, Schema.org\n\nThose plugins are **enabled** by default; see below how to selectively enable them.\n\nThis architecture allows third-party plugins to be supplied via separate\npython packages.\n\n# Limitations\n* **controlled list** rather than fully fledged vocabularies, (i.e. just a bag of terms with unique IDs/URIs, no support for taxonomic relationships among terms like broader, narrower, synonyms, ...)\n* no notion of granularity (e.g. geonames country, region, city, street are all treated as part of the same vocabulary)\n\n# Setup\n\n## Installation\n\nInstall into your environment:\n\n```\npip install django-controlled-vocabulary\n```\n\nAdd the app to the INSTALLED_APPS list in your Django settings file:\n\n```\nINSTALLED_APPS = [\n    # other apps\n    'controlled_vocabulary',\n]\n```\n\nRun the migrations:\n\n```\n./manage.py migrate\n```\n\nDownload vocabulary data and add metadata to the database:\n\n```\n./manage.py vocab init\n```\n\n## Configuration\n\n### Enabling vocabulary plug-ins\n\nAdd the following code in your settings.py to enable specific vocabularies based on the import path of their classes.\n\n```\n# List of import paths to vocabularies lookup classes\nCONTROLLED_VOCABULARY_VOCABULARIES = [\n    'controlled_vocabulary.vocabularies.iso639_2',\n    'controlled_vocabulary.vocabularies.dcmitype',\n]\n```\n\n### ControlledTermField\n\nTo define a field with an autocomplete to controlled terms in your Django Model, use the following field:\n\n```\nfrom controlled_vocabulary.models import ControlledTermField\n```\n\n```\n    language_code = ControlledTermField(\n        'iso639-2',\n        null=True, blank=True\n    )\n```\n\nWhere 'iso639-2' is the prefix of a controlled vocabulary in your database.\n\n# vocab (command line tool)\n\nvocab is a django command line tool that lets you manipulate the vocabularies\nand the plugins. To find out more use the help:\n\n```\n./manage vocab help\n```\n\n",
    'author': 'geoffroy-noel-ddh',
    'author_email': 'geoffroy.noel@kcl.ac.uk',
    'url': 'https://github.com/kingsdigitallab/django-controlled-vocabulary',
    'packages': packages,
    'package_data': package_data,
    'python_requires': '>=3.5,<4.0',
}


setup(**setup_kwargs)
