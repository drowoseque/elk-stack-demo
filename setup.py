from setuptools import setup, find_packages

setup(
    name='elk_stack_demo',
    version='1.0',
    packages=find_packages(),
    url='',
    license='',
    author='slavoshevskiy-me',
    author_email='slavoshevskii.mihail@phystech.edu',
    description='',
    install_requires=[
        'click==6.7',
        'tornado==5.0.2',
        'python-logstash==0.4.6'
    ]
)
