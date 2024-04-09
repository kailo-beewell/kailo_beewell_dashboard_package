# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.1.0/) (with possible titles of 'added', 'changed', 'deprecated', 'removed', 'fixed', or 'security'),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

This should align with:
* Releases on [PyPI](https://pypi.org/project/kailo-beewell-dashboard/#history)
* Releases on [GitHub](https://github.com/kailo-beewell/kailo_beewell_dashboard_package/releases) (which are like a non-portable changelog only displayed to users within GitHub)

## 0.3.0

**Release date:** 9th April 2024

**Contributors:** Amy Heather

Modified package so it can be used to produce the **synthetic public** #BeeWell survey dashboard, as well as the standard and symbol survey dashboards.

### Added

* An introduction to and glossary for CSS to the package documentation
* Step-by-step on dashboard maintenace (updating to use new package version) in package documentation
* CSS stylesheets and image files
* `about_page.py` - to produce the About pages for each dashboard - with loads more text used in this added to to `reuse_text.py`
* Add `choose_topic()` to `explore_results.py` (although produced errors when used on public dashboard as the selectbox wouldn't update correctly between two pages that both used this function, so ended up producing those manually in script rather than using this function, which is now just used in processing)
* `map.py` - to produce map for public dashboard with results for standard survey by MSOA
* Add function for `get_image_path()`
* `topic_labels.py` - names and descriptions used for the standard survey topics

### Changed

* Modified and added to some of the documentation pages (package maintenance, streamlit community cloud)
* Use CSS and image files stored within package rather than within dashboard directory (modifications throughout package), and import them with package in `setup.py`
* Renamed `convert_image.py` to `images.py`
* Seperated `create_and_aggregate_data.py` into four seperate scripts, with modifications and additions throughout that enable it to be used for creation and processing of data for the public dashboard -
    * `synthesise_aggregate.py`
    * `synthesise_demographic.py`
    * `synthesise_responses.py`
    * `synthesise_scores.py`
* Modified text of `write_response_section_intro()` and `caution_comparing()` so can be used for public dashboard
* Standard survey school dashboard no longer imports standard_school_aggregate_scores (and just the version with RAG added)
* In `extract_nested_results()`, made addition of group optional
* Changed how the RAG boxes are created in `summary_rag.py`
* Adapted `who_took_part.py` to work with public dashboard
* Modified environment in `requirements.txt`

## 0.2.0

**Release date:** 1st March 2024

**Contributors:** Amy Heather

Modified package so it can be used to produce the **synthetic symbol** #BeeWell survey dashboard, as well as the standard survey dashboard.

### Added

* Created `CHANGELOG.md` (with backdated entry for 0.1.0)
* Created `CITATION.cff`
* Created package documentation using Sphinx and readthedocs - `docs/` and `.readthedocs.yaml`
* `create_group_list()` in `bar_charts.py` which creates a correctly formatted list of strings depending on number of inputs (e.g. 'a', 'a and b', 'a, b and c')
* `grammar.py` - contains `lower_first()` which converts first letter of string to lower case, unless all other letters are upper case
* Add `aggregate_demographic()` to `create_and_aggregate_data.py`
* Add new alternative inputs, outputs and process to existing functions that were developed for standard survey, so they can be used to output equivalent content for symbol survey. This includes
    * `authentication.py` - custom login screen text
    * `create_and_aggregate_data.py` - two possible sets of groups to aggregate by
    * `explore_results.py` - custom page text, and providing survey type to functions like `filter_by_group()`
    * `import_data.py` - add names of data for symbol survey as for session_state and as in TiDB Cloud, and simplified import function
    * `page_setup.py` - to use name 'symbol' survey in the page menu
    * `reshape_data.py` - for differences with symbol (e.g. exc SEN)
    * `response_labels.py` - new function `create_symbol_response_label_dict()`
    * `static_report.py` - converting some of the processes into standalone functions, so they can be imported to old function making static standard report and new function making static symbol report
    * `who_took_part.py` - modifications for symbol like different headers and no descriptive text

### Changed

* Moved all About page text to `reuse_text.py`
* In `requirements.txt`, upgraded pip to 24.0 and streamlit to 1.31.1, and add packages used to produce documentation (sphinx, sphinx-rtd-theme, myst-parser, sphinx-autoapi)

### Removed

* Removed option to compare data import from TiDB to imported CSVs from the project directory (as function wasn't being used) in `import_data.py`

### Fixed

* Hide responses (and non-response) on 'who took part' if n<10 for a given response option (more strict than elsewhere on dashboard, which just requires n>=10 for the entire question). For this, modified `survey_responses()` in `bar_charts.py`

## 0.1.0

**Release date:** 21st February 2024

**Contributors:** [Amy Heather](https://github.com/amyheather)

First release of kailo-beewell-dashboard package on PyPi. Contains functions for production of **synthetic standard** #BeeWell survey dashboard (including static PDF version, which can be produced using the dashboard).

### Added

Functions used to generate and process data, and to produce the dashboard:
* `authentication.py` - for user authentication using Django
* `bar_charts.py` - to create bar charts of proportions of each survey responses, or ordered bar charts comparing scores
* `bar_charts_text.py` - dictionary with descriptions to go above bar charts on the 'explore results' page
* `convert_image.py` - converts a plotly figure to HTML string
* `create_and_aggregate_data.py` - functions used to create and process the pupil-level data
* `explore_results.py` - functions used for the 'explore results' page
* `import_data.py` - connects to TiDB Cloud and imports data to session state
* `page_setup.py` - page configuration, styling, formatting
* `reshape_data.py` - to reshape data or extract a certain element, with functions often used across multiple different pages
* `response_labels.py` - dictionary of labels to each of the question response options
* `reuse_text.py` - two sections of text that were reused on different pages of the dashboard vs PDF report
* `score_descriptions.py` - simple descriptions used on the 'explore results' page to support score interpretation
* `static_report.py` - uses same functions as on the dashboard, to produce a static HTML report (containing same information as in dashboard)
* `stylable_container.py` - produces stylised containers for streamlit
* `summary_rag.py` - produces the red-amber-green boxes and 'summary' page introduction and table
* `switch_page.py` - function to switch page programmatically
* `who_took_part.py` - functions used for the 'who took part' page