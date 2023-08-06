# -*- coding: utf-8 -*-
from distutils.core import setup

packages = \
['airflow_ecr_plugin']

package_data = \
{'': ['*'], 'airflow_ecr_plugin': ['tests/*']}

install_requires = \
['boto3>=1.10,<2.0']

extras_require = \
{u'airflow': ['apache-airflow>=1.10,<2.0']}

setup_kwargs = {
    'name': 'airflow-ecr-plugin',
    'version': '0.1.1',
    'description': 'Airflow ECR plugin',
    'long_description': '',
    'author': 'Sandeep Aggarwal',
    'author_email': 'asandeep.me@gmail.com',
    'url': 'https://github.com/asandeep/airflow-ecr-plugin',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'extras_require': extras_require,
    'python_requires': '>=2.7,<4.0',
}


setup(**setup_kwargs)
