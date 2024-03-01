# Streamlit Community Cloud

Our dashboards are hosted using Streamlit Community Cloud.

The app should be built based on the main branch in the GitHub repository. To push changes to the app from 'main':
* Go to [https://share.streamlit.io/](https://share.streamlit.io/).
* Login using your GitHub account and then - assumiung you have the appropriate access permissions - will be able to see the applications hosted as part of the kailo-beewell organisation.
* Go on the settings for a dashboard (three dots) and select 'Reboot' to recreate the app based on the latest version of your main branch.

You'll need to make sure that the secrets stored for that app are up-to-date, matching the `secrets.toml` you have in your local directory.