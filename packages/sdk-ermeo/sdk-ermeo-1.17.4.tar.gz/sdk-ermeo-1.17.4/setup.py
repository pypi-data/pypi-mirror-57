from setuptools import setup

setup(
    name='sdk-ermeo',
    version='1.17.4',
    description='Ermeo SDK for interacting with the API',
    url='https://github.com/ermeo/sdk-python',
    author='Ermeo',
    author_email='developer@ermeo.com',
    license='MIT',
    packages=['ermeo', 'ermeo.common', 'ermeo.schema', 'tests'],
    zip_safe=False,
    python_requires='>=3.6',
    install_requires=[
        'requests', 'marshmallow', 'tox'
    ],
)
