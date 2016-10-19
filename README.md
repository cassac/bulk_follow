# Bulk follow Github and LinkedIn users

The Github script `follow_gh.py` will follow users. The LinkedIn script `follow_li.py` will send a invitation for each user or if the user has already sent you an invitation the script will automatically accept their invitation.

1) Download spreadsheet file as `.csv` and place in this repo's root directory

2) Change `config.example.py` to `config.py` and fill in Github username and password along with .csv filename

3) Install `pip`: Mac OS: `sudo easy_install pip`. Linux: `sudo apt-get install python-pip`. 

4) Install Python dependencies: Navigate to root directory of repo and in terminal type `pip install -r requirements.txt`

5) Install `chromedriver`. Mac OS: `brew install chromedriver`. Linux: http://stackoverflow.com/a/24364290

6) Execute scripts: 

**Github** 
  * In the terminal type `python follow_gh.py` or `python3 follow_gh.py`

**LinkedIn** 
  * In the terminal type `python follow_li.py` or `python3 follow_li.py`

**Troubleshooting**
  * Mac users: When running the scripts if there is an error message pertaining to Chrome driver not found then your Chrome brower may not be installed in the location. Reinstall `google-chrome` using this command `brew cask install google-chrome`.

_Some people's Github and/or LinkedIn handles may be missing, contain typos or have already been followed. Feedback will be provided in the terminal when running the script._

_These scripts DO NOT save your account information/credentials anywhere. Author is not responsible for misuse of these scripts. Use at your own risk._