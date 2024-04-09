import setuptools
from kailo_beewell_dashboard import __version__

# Read in the requirements.txt file
with open('requirements.txt') as f:
    requirements = []
    for library in f.read().splitlines():
        requirements.append(library)

# Read in the README.md file
with open('README.md', 'r') as fh:
    long_description = fh.read()

# Provide information for setup, which governs package installation
setuptools.setup(
    name='kailo-beewell-dashboard',
    version=__version__,
    author='Amy Heather',
    author_email='a.heather2@exeter.ac.uk',
    license='The MIT License (MIT)',
    license_files=('LICENSE', ),
    description=(
        'Tools to support creation of #BeeWell survey dashboards for Kailo'),
    long_description=long_description,
    long_description_content_type='text/markdown',
    url='https://github.com/kailo-beewell/kailo_beewell_dashboard_package',
    packages=setuptools.find_packages(),
    classifiers=[
        'Programming Language :: Python :: 3.10',
        'License :: OSI Approved :: MIT License',
        'Operating System :: POSIX :: Linux',
    ],
    install_requires=requirements,
    include_package_data=True
)
