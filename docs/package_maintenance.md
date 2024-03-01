# Package maintenance

## Testing

Whilst working on the dashboards, you can use a live version of the package to test new features. To do this, set up your virtual environment with requirements.txt file containing `-e ../kailo_beewell_dashboard_package`.

This will import a live version of your local package, assuming that your dashboard folder is sister directories with the package folder.

When running your streamlit site with `streamlit run Home.py`, it will use the package version at the point you ran that command, so you will need to re-run that to get any updates from the package.

## Publishing a new version

When you are ready to publish a new version of this package to PyPI, these are the recommended steps you should go through.

1. Update version number using [Semantic Versioning](https://semver.org/spec/v2.0.0.html) in:
    * `__init__.py`
    * `CITATION.cff` 
    * `README.md` PyPI package badge
2. Update `CHANGELOG.md` with new version, detailing:
    * Upload date
    * Contributors
    * Short section (one or two sentences) summarising changes
    * Detailed section with changes, with formatting based on [Keep a Changelog](https://keepachangelog.com/en/1.1.0/) - i.e. possible titles of 'added', 'changed', 'deprecated', 'removed', 'fixed', or 'security'

To sort:
* PyPI
* GitHub release
* Update documentation... `make clean` and `make html`
* Tests for each of the dashboards
* Updating the requirements file in each of the dashboards to use latest version of package and rebuilding site on community cloud