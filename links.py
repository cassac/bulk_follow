import csv
from config import filename
from url_helper import url_checker

github_urls = []
linkedin_urls = []

with open(filename, 'r') as f:
    reader = csv.reader(f)
    # The first two rows are headers and are skipped.
    # Can be added by copying and pasting or deleted
    # as needed
    next(reader) # skip first row header
    next(reader) # skip second row header
    for row in reader:
        # Github URL is located in 3rd column. Your 
        # .csv file may be be different. 
        github_url = row[2] # Adjust column if needed 
        if (len(github_url)):
          github_url = url_checker(github_url)
          github_urls.append(github_url)
        else:
          print('# ' + row[0] + ' ' + row[1] + "'s github is blank")
        # Linkedin URL is located in 4th column. Your 
        # .csv file may be be different. 
        linkedin_url = row[3] # Adjust column if needed 
        if (len(linkedin_url)):
            linkedin_url = url_checker(linkedin_url)
            linkedin_urls.append(linkedin_url)
        else:
            print('# ' + row[0] + ' ' + row[1] + "'s linkedin is blank")