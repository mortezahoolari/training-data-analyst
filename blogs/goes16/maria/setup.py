import setuptools
setuptools.setup(
    name='maria',
    version='0.1',
    install_requires='pyresample netcdf4 matplotlib python-tk pillow google-cloud-storage'.split(),
    packages=setuptools.find_packages(),
 )
