# Package maintenance

## Publishing a new version of the package

When you are ready to publish a new version of this package to PyPI, these are the recommended steps you should go through.

You should always be creating a **new version** when you push to main - or, in other words, the code in main should not include work-in-progress changes to the package. This likewise applies to your dashboard repositories - that you should only push to main with everything up to date (as community cloud builds based on main, and based on the kailo-beewell-dashboard package version last provided).

1. **Test all dashboards** using the latest version of the package functions, by importing live version of package (`-e ../kailo_beewell_dashboard_package`) before proceeding
2. **Update version number** using [Semantic Versioning](https://semver.org/spec/v2.0.0.html) in:
    * `__init__.py`
    * `CITATION.cff` - this is 'version' (not cff-version) - and also, change the date here too on 'date-released'
    * `README.md` PyPI package badge - change in both the hyperlinks that produce the badge
    * `README.md` Harvard citation
    * `README.md` Latex citation - and add the new date for the latest version
3. **Update changelog** (`CHANGELOG.md`) with new version, detailing:
    * Upload date
    * Contributors
    * Short section (one or two sentences) summarising changes
    * Detailed section with changes, with formatting based on [Keep a Changelog](https://keepachangelog.com/en/1.1.0/) - i.e. possible titles of 'added', 'changed', 'deprecated', 'removed', 'fixed', or 'security'. Can be helpful to compare changes between main and your dev branch before you merge, as that will show you everything you have modified since your last version. To do so on the GitHub site, go to your dev branch (which should have a message like 'This branch is n commits ahead of main.'). Click on the hyperlink in that message, and then on the 'Files changed' tab.
4. **Push those files** that you just modified through to your development branch
5. **Push everything to main** on GitHub, and switch to the main branch on VS Code
6. **Upload to PyPI** for which you need to:
    * a) Delete the existing `dist/` folder
    * b) Run `python setup.py sdist bdist_wheel`
    * c) Run `twine upload --skip-existing --repository-url https://upload.pypi.org/legacy/ dist/*`. You'll be asked to enter your API token, and then new version will be uploaded.
7. **Create GitHub release** as follows:
    * a) Go to GitHub repository > Releases > Draft a new release
    * b) Set the tag and the release title to the latest version (i.e. 'vX.X.X')
    * c) For the description, copy from the changelog.
    * d) Upload the .whl and .tar.gz files form dist/. The GitHub release will be linked to your latest commit (which should match the commit that creates those files on PyPI).

The documentation is hosted with Read the Docs. If any changes were made to the package documentation, this should be automatically updated from your latest GitHub push.

## Updating data on TiDB Cloud

If you have made changes to the processing steps that produce the aggregated data, you'll need to make sure that the **updated csv files are uploaded to TiDB Cloud**, replacing the previous data frames.

If you make any changes to where the data are stored on TiDB Cloud (e.g. different cluster), make sure you provided Streamlit Community Cloud with the updated contents of `secrets.toml`.

## Updating dashboards to use the new package version

See page on **dashboard maintenance**.

## Documentation

If you create any new functions - or modify existing functions - you should create or modify the docstrings accordingly. Docstrings for this package and the accompanying dashboard repositories are formatted based on the [numpy docstring style guide](https://numpydoc.readthedocs.io/en/latest/format.html).

Package documentation is created using Sphinx and hosted on Read the Docs (**which automatically updates with GitHub pushes**). We use readthedocs community, and you can be add as maintainers to the project, https://readthedocs.org/projects/kailo-beewell-dashboard/.

You can preview updated documentation locally by running the following **from the `docs` folder**:
1. `make clean`
2. `make html`

You can then view the local documentation by opening the file `docs/_build/html/index.html` in your browser.

## Linting

Whilst coding, you should be linting your .py and .ipynb files.
* Use the `Flake8` VS Code extension to lint your .py files
* Lint .ipynb files from the terminal by running `nbqa flake8 notebook.ipynb`

## New contributors

If new contributors join the project, substantially contributing to the package, then you should update the citations accordingly in:
* `README.md` ORCID badges
* `README.md` citation
* `CITATION.cff` file