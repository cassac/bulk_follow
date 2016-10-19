import csv
from config import filename

github_urls = []

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
        url = row[2] # Adjust column if needed 
        if (len(url)):
          github_urls.append(url)
        else:
          print('# ' + row[0] + ' ' + row[1] + "'s github is blank")