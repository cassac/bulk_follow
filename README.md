# Bulk follow Github users

1) Download spreadsheet file as '.csv' and place in this repo's root directory

2) Change `config.example.py` to `config.py` and fill in Github username and password along with .csv filename

3) Install `pip`: Mac OS: `sudo easy_install pip`. Linux: `sudo apt-get install python-pip`. 

4) Install Python dependencies: Navigate to root directory of repo and in terminal type `pip install -r requirements.txt`

5) Install `chromedriver`. Mac OS: `brew install chromedriver`. Linux: http://stackoverflow.com/a/24364290

5) Execute script. In the terminal type `python follow.py` or `python3 follow.py`

*Some people's Github handles may have typos or have already been followed. Feedback will be provided in the terminal when running the script