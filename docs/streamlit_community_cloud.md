# Streamlit Community Cloud

Our dashboards are hosted using Streamlit Community Cloud.

The app should be built based on the main branch in the GitHub repository. To push changes to the app from 'main':
* Go to [https://share.streamlit.io/](https://share.streamlit.io/).
* Login using your GitHub account and then - assumiung you have the appropriate access permissions - will be able to see the applications hosted as part of the kailo-beewell organisation.
* Go on the settings for a dashboard (three dots) and select 'Reboot' to recreate the app based on the latest version of your main branch.

You'll need to make sure that the secrets stored for that app are up-to-date, matching the `secrets.toml` you have in your local directory.

## Packages.txt

The app is built using the `requirements.txt` (dependencies as in virtual environment) and `packages.txt` files provided in its GItHub repository.

`Packages.txt` is used to manage any external dependencies. Streamlit Community Cloud runs on Linux, so these would be the same as the Linux dependencies that you would install with `apt-get` outside the Python environment. For this project, `libpangocairo-1.0-0` is included in `packages.txt`.