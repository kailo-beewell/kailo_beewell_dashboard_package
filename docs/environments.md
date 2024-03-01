# Environments

This package and the accompanying dashboard repositories use virtual environments. This page contains tips and advice relating to these, in case they are unfamiliar to you.

## Virtual environment wrapper

I recommend using virtualenvwrapper to manage your python virtual environments. This is because:
* It stores all your environments in one place (so you can easily see a list of your environments)
* The syntax for deleting an environment prevents you from accidentally deleting folders, as it has a specify command, rather than a general delete command that could apply to an environment or a folder with the same name

To do so, you'll need to have `pip`, `python`, `virtualenv` and `virtualenvwrapper` installed on your machine.

Commands:
* Create environment - `mkvirtualenv env_kailo_dashboards`
* Enter environment -  `workon env_kailo_dashboards`
* Install requirements into environment - `pip install -r requirements.txt`
* See list of all available environments - `workon`
* List contents of active environment - `pip list`
* Delete environment - `rmvirtualenv env_kailo_dashboards`

## Streamlit Community Cloud

Streamlit Community Cloud only appears to work with virtual environment - states compatability with environment.yml but failed when I and my colleague attempted it.

Therefore, we us a virtual environment with the requirements.txt file provided and python version 3.9.12 (with community cloud set up on python 3.9).