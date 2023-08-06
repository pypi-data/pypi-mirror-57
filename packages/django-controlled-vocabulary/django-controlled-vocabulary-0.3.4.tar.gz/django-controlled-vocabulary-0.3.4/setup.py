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

install_requires = \
['django>=2.2,<3.0', 'urllib3>=1.25,<2.0']

setup_kwargs = {
    'name': 'django-controlled-vocabulary',
    'version': '0.3.4',
    'description': 'Link your data to authority lists or your own controlled lists',
    'long_description': '[![PyPI version](https://badge.fury.io/py/django-controlled-vocabulary.svg)](https://badge.fury.io/py/django-controlled-vocabulary)\n\n# Django Controlled Vocabulary\n\nThis app provides models and admin interface to link your data to standard vocabularies (e.g. ISO language codes, Wikidata). Benefits: increases the consistency and understandability of your project data.\n\nDevelopment Status: **Alpha** (mostly functional, work in progress)\n\n<img src="docs/img/controlled-term-widget.png" />\n\n_A ControlledTerm field in the Django admin interface. The user selects the vocabulary (here: Wikidata), then starts typing a term in the text box. Suggestions are brought from Wikidata. When the user saves the changes, information about the selected term is copied into the database (url, identifier, label)._\n\n# Features\n\n* create your own controlled lists of terms (i.e. **local** lists)\n* look up terms from **remote** vocabularies (i.e. authority files)\n* extensible **plug-in architecture** for lookups into particular vocabularies:\n  * built-in vocabulary plug-ins, such as ISO 639-2 (Language codes), DCMI Type (Dublin Core resource types)\n  * see below for full list\n* **stores** used terms from remote vocabularies into your database:\n  * space efficient (doesn\'t clutter the database with unused terms)\n  * self-contained (i.e. can still works offline & DB always \'semantically\' complete)\n* **autocomplete** widget for Django admin; reusable ControlledTermField for your models\n* **command line tool** to download vocabulary files from authoritative sources\n* [TODO] possibility to store additional **metadata** (e.g. geographic coordinates)\n* [TODO] simple **rest API** to publish your own terms\n\n# Data Model & Software Design\n\n## Django models\n\n| Vocabularies | Terms |\n| ------------- | ------------- |\n| <img src="docs/img/controlled-vocabulary-list.png" width="400" />  | <img src="docs/img/controlled-term-list.png" width="400" />  |\n\n* **ControlledVocabulary**\n  * prefix: the vocabulary standard prefix, see http://prefix.cc/wikidata\n  * label: the short name of the vocabulary\n  * base_url: the url used as a base for all terms in the vocabulary\n  * concept: the type of terms this vocabulary contains\n  * description: a longer description\n\n* **ControlledTerm**\n  * termid: a unique code for the term within a vocabulary\n  * label: standard name for the term\n  * vocabulary: the vocabulary this term belongs to\n\n## Vocabulary plug-ins / managers\n\nA Vocabulary **plug-in** / **manager** is a python class that provides services for a vocabulary:\n* autocomplete terms from local or remote datasets (see ControlledTermField)\n* supplies metadata for the vocabulary (see ControlledVocabulary)\n\nManagers can provide terms from a CSV file downloaded from an authoritative source.\n\nSome vocabularies can contain thousands of terms or more. A plugin will\nonly insert the terms used by your application. The rest will be accessed on\ndemand from a file on disk or in a third-party server. This approach saves\ndatabase space and keeps your application data self-contained.\n\nThis project comes with built-in plugins for the following vocabularies:\n\n**ISO 639-2, DCMI Type, Wikidata, FAST Topics, MIME, Schema.org, VIAF, FAST Forms and Genres**\n\nThose plugins are **enabled** by default; see below how to selectively enable them.\n\nThis architecture allows third-party plugins to be supplied via separate\npython packages.\n\n# Limitations\n* **controlled list** rather than fully fledged vocabularies, (i.e. just a bag of terms with unique IDs/URIs, no support for taxonomic relationships among terms like broader, narrower, synonyms, ...)\n* no notion of granularity (e.g. geonames country, region, city, street are all treated as part of the same vocabulary)\n\n# Setup\n\n## Installation\n\nInstall into your environment:\n\n```\npip install django-controlled-vocabulary\n```\n\nAdd the app to the INSTALLED_APPS list in your Django settings file:\n\n```\nINSTALLED_APPS = [\n    ...\n    \'controlled_vocabulary\',\n    ...\n]\n```\n\nAdd the following path to your project urls.py:\n\n```\nfrom django.urls import path, include\n...\n\nurlpatterns = [\n    ...\n    path(\'vocabularies/\', include(\'controlled_vocabulary.urls\')),\n    ...\n]\n```\n\nRun the migrations:\n\n```\n./manage.py migrate\n```\n\nDownload vocabulary data and add metadata to the database:\n\n```\n./manage.py vocab init\n```\n\n## Configuration\n\n### Enabling vocabulary plug-ins\n\nAdd the following code in your settings.py to enable specific vocabularies based on the import path of their classes.\n\n```\n# List of import paths to vocabularies lookup classes\nCONTROLLED_VOCABULARY_VOCABULARIES = [\n    \'controlled_vocabulary.vocabularies.iso639_2\',\n    \'controlled_vocabulary.vocabularies.dcmitype\',\n]\n```\n\n### ControlledTermField\n\nTo define a field with an autocomplete to controlled terms in your Django Model, use the following field:\n\n```\nfrom controlled_vocabulary.models import ControlledTermField\n\n...\n\nclass MyModel(models.Model):\n\n    ...\n    language_code = ControlledTermField(\n        \'iso639-2\',\n        null=True, blank=True\n    )\n```\n\nWhere \'iso639-2\' is the prefix of a controlled vocabulary in your database.\n\n# vocab (command line tool)\n\nvocab is a django command line tool that lets you manipulate the vocabularies\nand the plugins. To find out more use the help:\n\n```\n./manage vocab help\n```\n\n',
    'author': 'geoffroy-noel-ddh',
    'author_email': 'geoffroy.noel@kcl.ac.uk',
    'url': 'https://github.com/kingsdigitallab/django-controlled-vocabulary',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.5,<4.0',
}


setup(**setup_kwargs)
