import csv
from config import filename

github_urls = []

with open(filename, 'rb') as f:
    reader = csv.reader(f)
    next(reader) # skip first header
    next(reader) # skip second header
    for row in reader:
        url = row[2] # Github URL is located in 2nd row
        if (len(url)):
          github_urls.append(url)
        else:
          print '# ' + row[0] + ' ' + row[1] + "'s github is blank"