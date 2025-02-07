from setuptools import setup, find_packages

setup(
    name="geolocation",
    version="0.4",
    packages=find_packages(),
    entry_points= {
        #'group_1': 'run = geolocation.geolocation_api_call:main',
        'console_scripts': ['geo_entry_point = geolocation.geolocation_api_call:main']
    },
)
