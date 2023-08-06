import setuptools

setuptools.setup(name='olive',
                 version='0.2.5',
                 description='a python wrapper for an AIS Database API',
                 install_requires=[
                     'requests',
                     'requests_aws4auth',
                     'boto3',
                     'botocore'
                 ],
                 url='https://github.com/GeoBigData/AISDatabase',
                 author='Elizabeth Golden, Rachel Wegener, Melissa Dozier',
                 author_email='elizabeth.golden@digitalglobe.com',
                 license='',
                 packages=setuptools.find_packages(),
                 python_requires='>=3')


# up the version
# python3 setup.py sdist bdist_wheel
# delete old dist files
# python3 -m twine upload dist/*
# @pypi
# conda info --envs
# conda remove --name olive --all
# conda create -n olive python=3.5
# conda activate olive
# pip install olive