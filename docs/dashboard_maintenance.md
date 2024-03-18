# Dashboard maintenance

## Working on dev version of dashboard and package

Whilst working on the dashboards, you can use a live version of the package to test new features. To do this, set up your virtual environment with requirements.txt file containing `-e ../kailo_beewell_dashboard_package`. However, note that this should never be pushed to main, as the dashboard hosted on streamlit community cloud relies of released versions of the package and cannot operate from your live, local, unreleased version of the package.

This will import a live version of your local package, assuming that your dashboard folder is sister directories with the package folder.

When running your streamlit site with `streamlit run Home.py` on your local machine, it will use the package version at the point you ran that command, so you will need to re-run that to get any updates from the package.

It is important to constantly test and update code between the dashboard repositories if you make changes to the package code that would impact functioning - for example, changing a function or input names, requiring a new input in a function you're already using. I would recommend that you update it between the repositories immediately after you've finished making those changes (and not wait to update at the end, at which point you'll have made lots of changes and may not easily recall them all).

## Updating dashboards to use the new package version

Note: You may need to select "reboot" for you app on [https://share.streamlit.io/](https://share.streamlit.io/) to force it to update the app to the latest changes on your GitHub repository.

1. Push all changes to **main** - ensuring that you push the correct **version** of the kailo-beewell-dashboard package in requirements.txt (and not the live reference to the package)
2. Make sure **changelog** is up-to-date with all changes made, and set the version number and date
    * Note: Versioning of your dashboard is seperate to versioning of the package - they don't need to match!
3. **Switch the secrets** of dev-version of the dashboard on community cloud to temporarily use the secrets of the stable version (so we can test that the dashboard will work with the stable version of TIDB Cloud)
4. **Test the dashboard**, checking all functionality on the interactive dashboard and downloadable report
5. **Sync the fork** which contains the stable release of your dashboard
6. **Test again** briefly, to double-check all is operating alright
7. **Produce GitHub release** in the forked repository, copying the information from your changelog
    * Note: Forked repositories don't inherit releases, hence why we create the releases on the forked stable version of the repository, rather than in the active/development repository
8. **Return secrets** of the dev-version of the dashboard on community cloud to the secrets of the dev version of the TIDB Cloud clusters

**Note:** You should never be making changes to your stable release fork directly - the only actions you should do are to sync it with your dev repository, and to produce releases.

## New contributors

If new contributors join the project, substantially contributing to the package, then you should update the citations accordingly in:
* `README.md` ORCID badges