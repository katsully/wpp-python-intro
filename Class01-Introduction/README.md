# Setting up your Environment

### Python

First, we need to make sure Python has been installed. (This is only for Window users, Python comes standard in Mac). Open the Command Prompt and type Python and press enter. If it says Python 3.x.xx ...., you're all set! If not, please download [Python](https://www.python.org/downloads/windows). Under 'Stable Releases' search for the Windows installer (64-bit). Open the installer and **make sure the "Add Python 3.x to PATH" is selected**. Click Install Now. You'll need to close and reopen Command Prompt after installation.

Be sure Python is installed before moving on the next steps!

### Pip

If all went according to plan, you should have pip installed as well. In the command prompt type

```
pip --version
```

and hit enter. It should give a version number and at the end you should see Python 3.x that corresponds to whichever Python you have installed. If you're here - great! If not, reinstall Python and be sure that you include pip in your installation!

Next install Jupyter by typing the following into the command line

```
pip install jupyter
```

and hit enter. The installation will take a few minutes - don't worry! If it seems like it has stalled, just wait a little bit. To start the notebook server type

```
jupyter notebook
```

and hit enter. This should open the notebook in your browser. Note your location in the command prompt determines where the notebook is opened - be mindful of this! To close the notebook hit Ctrl+C in the command prompt.