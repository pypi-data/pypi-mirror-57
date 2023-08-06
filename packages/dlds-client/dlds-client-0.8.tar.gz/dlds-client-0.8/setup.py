#  Copyright (c) 2019 Data Spree UG (haftungsbeschraenkt) - All Rights Reserved
#  Unauthorized copying of this file, via any medium is strictly prohibited.
#  Proprietary and confidential.

from setuptools import setup

setup(
    name='dlds-client',
    version='0.8',
    py_modules=['dlds', 'dlds_cli', 'http_token_authentication'],
    install_requires=[
        'Click',
        'joblib',
        'numpy',
        'Pillow',
        'requests',
        'tqdm',
    ],
    entry_points='''
        [console_scripts]
        dlds=dlds_cli:cli
    ''',
)