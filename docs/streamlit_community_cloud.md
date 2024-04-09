# Streamlit Community Cloud

Our dashboards are hosted using Streamlit Community Cloud.

## Forked branch

The dashboard is hosted from a forked branch of the repository to ensure a stable release.

This has less risk of breaking as opposed to working in a development branch of a repository with the dashboard hosted from the main branch, wherein you could more easily accidentally make changes to main before you are ready for a full new release. Moreover, if you do not clone the forked repository to your local machine, this further minimises likelihood of accidentally working on the current release (rather than on a development version). 

The data is also stored in seperate dev and stable clusters on TIDB Cloud.

## Managing the application on community cloud

The app should be built based on the main branch in the GitHub repository. To push changes to the app from 'main':
* Go to [https://share.streamlit.io/](https://share.streamlit.io/).
* Login using your GitHub account and then - assumiung you have the appropriate access permissions - will be able to see the applications hosted as part of the kailo-beewell organisation.
* Go on the settings for a dashboard (three dots) and select 'Reboot' to recreate the app based on the latest version of your main branch.

You'll need to make sure that the secrets stored for that app are up-to-date, matching the `secrets.toml` you have in your local directory.

## Packages.txt

The app is built using the `requirements.txt` (dependencies as in virtual environment) and `packages.txt` files provided in its GItHub repository.

`Packages.txt` is used to manage any external dependencies. Streamlit Community Cloud runs on Linux, so these would be the same as the Linux dependencies that you would install with `apt-get` outside the Python environment. For this project, `libpangocairo-1.0-0` is included in `packages.txt`.